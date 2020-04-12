#from common.numpy_fast import clip
from selfdrive.car import apply_std_steer_torque_limits
from selfdrive.car.subaru import subarucan
from selfdrive.car.subaru.values import DBC
from opendbc.can.packer import CANPacker


class CarControllerParams():
  def __init__(self):
    self.STEER_MAX = 2047              # max_steer 4095
    self.STEER_STEP = 2                # how often we update the steer cmd
    self.STEER_DELTA_UP = 50           # torque increase per refresh, 0.8s to max
    self.STEER_DELTA_DOWN = 70         # torque decrease per refresh
    self.STEER_DRIVER_ALLOWANCE = 60   # allowed driver torque before start limiting
    self.STEER_DRIVER_MULTIPLIER = 10  # weight driver torque heavily
    self.STEER_DRIVER_FACTOR = 1       # from dbc



class CarController():
  def __init__(self, dbc_name, CP, VM):
    self.lkas_active = False
    self.apply_steer_last = 0
    self.es_lkas_state_cnt = -1
    self.cruise_control_cnt = -1
    self.brake_status_cnt = -1
    self.es_distance_cnt = -1
    self.es_status_cnt = -1
    self.es_brake_cnt = -1
    self.steer_rate_limited = False

    # Setup detection helper. Routes commands to
    # an appropriate CAN bus number.
    self.params = CarControllerParams()
    self.packer = CANPacker(DBC[CP.carFingerprint]['pt'])

  def update(self, enabled, CS, frame, actuators, pcm_cancel_cmd, visual_alert, left_line, right_line):
    """ Controls thread """

    P = self.params

    # Send CAN commands.
    can_sends = []

    ### STEER ###

    if (frame % P.STEER_STEP) == 0:

      final_steer = actuators.steer if enabled else 0.
      apply_steer = int(round(final_steer * P.STEER_MAX))

      # limits due to driver torque

      new_steer = int(round(apply_steer))
      apply_steer = apply_std_steer_torque_limits(new_steer, self.apply_steer_last, CS.out.steeringTorque, P)
      self.steer_rate_limited = new_steer != apply_steer

      lkas_enabled = enabled

      if not lkas_enabled:
        apply_steer = 0

      can_sends.append(subarucan.create_steering_control(self.packer, apply_steer, frame, P.STEER_STEP))

      self.apply_steer_last = apply_steer

    ### LONG ###

    #accel_cmd = False
    #accel_value = 0

    brake_cmd = False
    brake_value = 0

    '''
    # Manual trigger using wipers signal
    if CS.wipers:
      actuators.brake = 0.5
      print("wipers set brake 0.5")
      brake_cmd = True
    '''

    if enabled and actuators.brake > 0:
      brake_value = int(actuators.brake * 400)
      print("brake_value: %s" % brake_value)

      print('actuators.brake: %s, es_brake_pressure: %s es_brake_state: %s es_status_brake: %s' % (actuators.brake, CS.es_brake_pressure, CS.es_brake_state, CS.es_status_brake))

    if enabled and actuators.gas > 0:
      accel_cmd = True
      accel_value = int(1810 + (actuators.gas * 1000))
      print("accel_value: %s" % accel_value)

      print('actuators.gas: %s throttle_cruise: %s es_throttle_cruise: %s' % (actuators.gas, CS.throttle_cruise, CS.es_cruise_throttle))
    else:
      accel_value = 808
      accel_cmd = True

    if self.es_distance_cnt != CS.es_distance_msg["Counter"]:
      can_sends.append(subarucan.create_es_distance(self.packer, CS.es_distance_msg, enabled, pcm_cancel_cmd, brake_cmd, accel_value))
      self.es_distance_cnt = CS.es_distance_msg["Counter"]

    if self.es_status_cnt != CS.es_status_msg["Counter"]:
      can_sends.append(subarucan.create_es_status(self.packer, CS.es_status_msg, enabled, brake_cmd, accel_value))
      self.es_status_cnt = CS.es_status_msg["Counter"]

    if self.es_lkas_state_cnt != CS.es_lkas_state_msg["Counter"]:
      can_sends.append(subarucan.create_es_lkas_state(self.packer, CS.es_lkas_state_msg, visual_alert, left_line, right_line))
      self.es_lkas_state_cnt = CS.es_lkas_state_msg["Counter"]

    if self.es_brake_cnt != CS.es_brake_msg["Counter"]:
      can_sends.append(subarucan.create_es_brake(self.packer, CS.es_brake_msg, enabled, brake_cmd, brake_value))
      self.es_brake_cnt = CS.es_brake_msg["Counter"]

    if self.cruise_control_cnt != CS.cruise_control_msg["Counter"]:
      can_sends.append(subarucan.create_cruise_control(self.packer, CS.cruise_control_msg))
      self.cruise_control_cnt = CS.cruise_control_msg["Counter"]

    if self.brake_status_cnt != CS.brake_status_msg["Counter"]:
      can_sends.append(subarucan.create_brake_status(self.packer, CS.brake_status_msg))
      self.brake_status_cnt = CS.brake_status_msg["Counter"]

    return can_sends
