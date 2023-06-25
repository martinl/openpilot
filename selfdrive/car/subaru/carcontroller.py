from opendbc.can.packer import CANPacker
from selfdrive.car import apply_driver_steer_torque_limits
from selfdrive.car.subaru import subarucan
from selfdrive.car.subaru.values import DBC, GLOBAL_GEN2, PREGLOBAL_CARS, CarControllerParams, SubaruFlags, CAR, GLOBAL_CARS_SNG


class CarController:
  def __init__(self, dbc_name, CP, VM):
    self.CP = CP
    self.apply_steer_last = 0
    self.frame = 0

    self.cruise_button_prev = 0
    self.last_cancel_frame = 0
    self.throttle_cnt = -1
    self.brake_pedal_cnt = -1
    self.prev_close_distance = 0
    self.prev_standstill = False
    self.standstill_start = 0
    self.steer_rate_limited = False
    self.sng_acc_resume = False
    self.sng_acc_resume_cnt = -1
    self.manual_hold = False
    self.prev_cruise_state = 0

    self.p = CarControllerParams(CP)
    self.packer = CANPacker(DBC[CP.carFingerprint]['pt'])

  def update(self, CC, CS, now_nanos):
    actuators = CC.actuators
    hud_control = CC.hudControl
    pcm_cancel_cmd = CC.cruiseControl.cancel

    can_sends = []

    # *** steering ***
    if (self.frame % self.p.STEER_STEP) == 0:
      apply_steer = int(round(actuators.steer * self.p.STEER_MAX))

      # limits due to driver torque

      new_steer = int(round(apply_steer))
      apply_steer = apply_driver_steer_torque_limits(new_steer, self.apply_steer_last, CS.out.steeringTorque, self.p)

      if not CC.latActive:
        apply_steer = 0

      if self.CP.carFingerprint in PREGLOBAL_CARS:
        can_sends.append(subarucan.create_preglobal_steering_control(self.packer, apply_steer, self.frame, self.p.STEER_STEP))
      elif self.CP.carFingerprint == CAR.FORESTER_2022:
        can_sends.append(subarucan.create_preglobal_steering_control(self.packer, apply_steer, CC.latActive))
      else:
        can_sends.append(subarucan.create_steering_control(self.packer, apply_steer, CC.latActive))

      self.apply_steer_last = apply_steer

    # *** stop and go ***

    throttle_cmd = False
    speed_cmd = False

    if CS.CP.carFingerprint in PREGLOBAL_CARS:
      # Initiate the ACC resume sequence if conditions are met
      if (CC.enabled                                         # ACC active
          and CS.car_follow == 1                             # lead car
          and CS.out.standstill                              # must be standing still
          and CS.close_distance > self.p.ACC_MIN_DIST        # acc resume trigger low threshold
          and CS.close_distance < self.p.ACC_MAX_DIST        # acc resume trigger high threshold
          and CS.close_distance > self.prev_close_distance): # distance with lead car is increasing
        self.sng_acc_resume = True
      # Cancel ACC if stopped, brake pressed and no lead car
      if CC.enabled and CS.out.brakePressed and CS.car_follow == 0 and CS.out.standstill:
        pcm_cancel_cmd = True
    elif CS.CP.carFingerprint in GLOBAL_CARS_SNG:
      if CS.has_epb:
        # Record manual hold set while in standstill and no car in front
        if CS.out.standstill and self.prev_cruise_state == 1 and CS.cruise_state == 3 and CS.car_follow == 0:
          self.manual_hold = True
        # Cancel manual hold when car starts moving
        if not CS.out.standstill:
          self.manual_hold = False
        # Initiate the ACC resume sequence if conditions are met
        if (CC.enabled                                          # ACC active
            and not self.manual_hold
            and CS.car_follow == 1                             # lead car
            and CS.cruise_state == 3                           # ACC HOLD (only with EPB)
            and CS.close_distance > self.p.ACC_MIN_DIST        # acc resume trigger low threshold
            and CS.close_distance < self.p.ACC_MAX_DIST        # acc resume trigger high threshold
            and CS.close_distance > self.prev_close_distance): # distance with lead car is increasing
          self.sng_acc_resume = True
      else:
        # Send brake message with non-zero speed in standstill to avoid non-EPB ACC disengage
        if (CC.enabled                                         # ACC active
              and CS.car_follow == 1                           # lead car
              and CS.out.standstill
              and self.frame > self.standstill_start + 50):    # standstill for >0.5 second
          speed_cmd = True

      if CS.out.standstill and not self.prev_standstill:
        self.standstill_start = self.frame
      self.prev_standstill = CS.out.standstill
      self.prev_cruise_state = CS.cruise_state

    if self.sng_acc_resume:
      if self.sng_acc_resume_cnt < 5:
        throttle_cmd = True
        self.sng_acc_resume_cnt += 1
      else:
        self.sng_acc_resume = False
        self.sng_acc_resume_cnt = -1

    if CS.CP.carFingerprint != CAR.CROSSTREK_2020H:
      self.prev_close_distance = CS.close_distance

    # *** alerts and pcm cancel ***

    if self.CP.carFingerprint in PREGLOBAL_CARS:
      if self.frame % 5 == 0:
        # 1 = main, 2 = set shallow, 3 = set deep, 4 = resume shallow, 5 = resume deep
        # disengage ACC when OP is disengaged
        if pcm_cancel_cmd:
          cruise_button = 1
        # turn main on if off and past start-up state
        elif not CS.out.cruiseState.available and CS.ready:
          cruise_button = 1
        else:
          cruise_button = CS.cruise_button

        # unstick previous mocked button press
        if cruise_button == 1 and self.cruise_button_prev == 1:
          cruise_button = 0
        self.cruise_button_prev = cruise_button

        can_sends.append(subarucan.create_preglobal_es_distance(self.packer, cruise_button, CS.es_distance_msg))

      if self.throttle_cnt != CS.throttle_msg["COUNTER"]:
        can_sends.append(subarucan.create_preglobal_throttle(self.packer, CS.throttle_msg, throttle_cmd))
        self.throttle_cnt = CS.throttle_msg["COUNTER"]

    else:
      if CS.CP.carFingerprint != CAR.CROSSTREK_2020H:
        if pcm_cancel_cmd and (self.frame - self.last_cancel_frame) > 0.2:
          bus = 1 if self.CP.carFingerprint in GLOBAL_GEN2 else 0
          can_sends.append(subarucan.create_es_distance(self.packer, CS.es_distance_msg, bus, pcm_cancel_cmd))
          self.last_cancel_frame = self.frame

      if self.frame % 10 == 0:
        can_sends.append(subarucan.create_es_dashstatus(self.packer, CS.es_dashstatus_msg))

        can_sends.append(subarucan.create_es_lkas_state(self.packer, CS.es_lkas_state_msg, CC.enabled, hud_control.visualAlert,
                                                        hud_control.leftLaneVisible, hud_control.rightLaneVisible,
                                                        hud_control.leftLaneDepart, hud_control.rightLaneDepart))

        if self.CP.flags & SubaruFlags.SEND_INFOTAINMENT:
          can_sends.append(subarucan.create_infotainmentstatus(self.packer, CS.es_infotainmentstatus_msg, hud_control.visualAlert))

      if self.throttle_cnt != CS.throttle_msg["COUNTER"]:
        can_sends.append(subarucan.create_throttle(self.packer, CS.throttle_msg, throttle_cmd))
        self.throttle_cnt = CS.throttle_msg["COUNTER"]

      if self.brake_pedal_cnt != CS.brake_pedal_msg["COUNTER"]:
        can_sends.append(subarucan.create_brake_pedal(self.packer, CS.brake_pedal_msg, speed_cmd, pcm_cancel_cmd))
        self.brake_pedal_cnt = CS.brake_pedal_msg["COUNTER"]

    new_actuators = actuators.copy()
    new_actuators.steer = self.apply_steer_last / self.p.STEER_MAX
    new_actuators.steerOutputCan = self.apply_steer_last

    self.frame += 1
    return new_actuators, can_sends
