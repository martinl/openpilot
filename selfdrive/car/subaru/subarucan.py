import copy
from cereal import car

VisualAlert = car.CarControl.HUDControl.VisualAlert

def create_steering_control(packer, apply_steer, frame, steer_step):

  # counts from 0 to 15 then back to 0 + 16 for enable bit
  idx = ((frame // steer_step) % 16)

  values = {
    "Counter": idx,
    "LKAS_Output": apply_steer,
    "LKAS_Request": 1 if apply_steer != 0 else 0,
    "SET_1": 1
  }

  return packer.make_can_msg("ES_LKAS", 0, values)

def create_steering_status(packer, apply_steer, frame, steer_step):
  return packer.make_can_msg("ES_LKAS_State", 0, {})

def create_es_distance(packer, es_distance_msg, enabled, pcm_cancel_cmd, brake_cmd, cruise_throttle):

  values = copy.copy(es_distance_msg)
  if enabled:
    values["Cruise_Throttle"] = cruise_throttle
  if pcm_cancel_cmd:
    values["Cruise_Cancel"] = 1
  if brake_cmd:
    values["Cruise_Throttle"] = 808
    values["Cruise_Brake_Active"] = 1

  return packer.make_can_msg("ES_Distance", 0, values)

def create_es_dashstatus(packer, es_dashstatus_msg, enabled, lead_visible):

  values = copy.copy(es_dashstatus_msg)
  if enabled:
    values["Cruise_State"] = 0
    values["Cruise_Activated"] = 1
    values["Cruise_Disengaged"] = 0
    values["Car_Follow"] = int(lead_visible)

  return packer.make_can_msg("ES_DashStatus", 0, values)

def create_es_lkas_state(packer, es_lkas_msg, visual_alert, left_line, right_line, left_ldw, right_ldw, lkas_signal):

  values = copy.copy(es_lkas_msg)
  if visual_alert == VisualAlert.steerRequired:
    values["Keep_Hands_On_Wheel"] = 1

  values["LKAS_Left_Line_Visible"] = int(left_line)
  values["LKAS_Right_Line_Visible"] = int(right_line)

  if left_ldw:
    values["LKAS_Alert"] = 7 # 11?
  if right_ldw:
    values["LKAS_Alert"] = 12

  values["LKAS_Alert"] = lkas_signal

  return packer.make_can_msg("ES_LKAS_State", 0, values)

def create_es_brake(packer, es_brake_msg, enabled, brake_cmd, brake_value):

  values = copy.copy(es_brake_msg)
  if enabled:
    values["Cruise_Activated"] = 1
  if brake_cmd:
    values["Brake_Pressure"] = brake_value
    values["Cruise_Brake_Active"] = 1
    values["Cruise_Brake_Lights"] = 1 if brake_value >= 70 else 0

  return packer.make_can_msg("ES_Brake", 0, values)

def create_es_status(packer, es_status_msg, enabled, brake_cmd, cruise_rpm):

  values = copy.copy(es_status_msg)
  if enabled:
    values["Cruise_Activated"] = 1
    values["Cruise_RPM"] = cruise_rpm
  if brake_cmd:
    values["Cruise_RPM"] = 600

  return packer.make_can_msg("ES_Status", 0, values)

# disable cruise_activated feedback to eyesight to keep ready state
def create_cruise_control(packer, cruise_control_msg):

  values = copy.copy(cruise_control_msg)
  values["Cruise_Activated"] = 0

  return packer.make_can_msg("CruiseControl", 2, values)

# disable es_brake feedback to eyesight, except PCB
def create_brake_status(packer, brake_status_msg, es_brake_active):

  values = copy.copy(brake_status_msg)
  if not es_brake_active:
    values["ES_Brake"] = 0

  return packer.make_can_msg("Brake_Status", 2, values)
