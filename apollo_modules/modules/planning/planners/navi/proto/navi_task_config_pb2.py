# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/planners/navi/proto/navi_task_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;modules/planning/planners/navi/proto/navi_task_config.proto\x12\x0f\x61pollo.planning\"\x88\x03\n\x19NaviObstacleDeciderConfig\x12\x1f\n\x12min_nudge_distance\x18\x01 \x01(\x01:\x03\x30.2\x12\x1f\n\x12max_nudge_distance\x18\x02 \x01(\x01:\x03\x31.2\x12%\n\x15max_allow_nudge_speed\x18\x03 \x01(\x01:\x06\x31\x36.667\x12\x1a\n\rsafe_distance\x18\x04 \x01(\x01:\x03\x30.2\x12#\n\x15nudge_allow_tolerance\x18\x05 \x01(\x01:\x04\x30.05\x12\x18\n\rcycles_number\x18\x06 \x01(\r:\x01\x33\x12\x1a\n\x0fjudge_dis_coeff\x18\x07 \x01(\x01:\x01\x32\x12\x1b\n\x0f\x62\x61sis_dis_value\x18\x08 \x01(\x01:\x02\x33\x30\x12#\n\x16lateral_velocity_value\x18\t \x01(\x01:\x03\x30.5\x12%\n\x1aspeed_decider_detect_range\x18\n \x01(\x01:\x01\x31\x12\"\n\x15max_keep_nudge_cycles\x18\x0b \x01(\r:\x03\x31\x30\x30\"\xd5\x03\n\x15NaviPathDeciderConfig\x12\x1a\n\x0fmin_path_length\x18\x01 \x01(\x01:\x01\x35\x12 \n\x15min_look_forward_time\x18\x02 \x01(\r:\x01\x32\x12#\n\x16max_keep_lane_distance\x18\x03 \x01(\x01:\x03\x30.8\x12!\n\x15max_keep_lane_shift_y\x18\x04 \x01(\x01:\x02\x32\x30\x12 \n\x14min_keep_lane_offset\x18\x05 \x01(\x01:\x02\x31\x35\x12*\n\x1ckeep_lane_shift_compensation\x18\x06 \x01(\x01:\x04\x30.01\x12M\n\x1bmove_dest_lane_config_talbe\x18\x07 \x01(\x0b\x32(.apollo.planning.MoveDestLaneConfigTable\x12)\n\x1bmove_dest_lane_compensation\x18\x08 \x01(\x01:\x04\x30.35\x12\x1e\n\x13max_kappa_threshold\x18\t \x01(\x01:\x01\x30\x12,\n!kappa_move_dest_lane_compensation\x18\n \x01(\x01:\x01\x30\x12 \n\x15start_plan_point_from\x18\x0b \x01(\r:\x01\x30\"N\n\x17MoveDestLaneConfigTable\x12\x33\n\rlateral_shift\x18\x01 \x03(\x0b\x32\x1c.apollo.planning.ShiftConfig\"O\n\x0bShiftConfig\x12\x17\n\tmax_speed\x18\x01 \x01(\x01:\x04\x34.16\x12\'\n\x1amax_move_dest_lane_shift_y\x18\x03 \x01(\x01:\x03\x30.4\"\xd2\x04\n\x16NaviSpeedDeciderConfig\x12\x1a\n\x0fpreferred_accel\x18\x01 \x01(\x01:\x01\x32\x12\x1a\n\x0fpreferred_decel\x18\x02 \x01(\x01:\x01\x32\x12\x19\n\x0epreferred_jerk\x18\x03 \x01(\x01:\x01\x32\x12\x14\n\tmax_accel\x18\x04 \x01(\x01:\x01\x34\x12\x14\n\tmax_decel\x18\x05 \x01(\x01:\x01\x35\x12\x1c\n\x0fobstacle_buffer\x18\x06 \x01(\x01:\x03\x30.5\x12\x1d\n\x12safe_distance_base\x18\x07 \x01(\x01:\x01\x32\x12\x1e\n\x13safe_distance_ratio\x18\x08 \x01(\x01:\x01\x31\x12\"\n\x15\x66ollowing_accel_ratio\x18\t \x01(\x01:\x03\x30.5\x12%\n\x18soft_centric_accel_limit\x18\n \x01(\x01:\x03\x31.2\x12%\n\x18hard_centric_accel_limit\x18\x0b \x01(\x01:\x03\x31.5\x12\x1d\n\x10hard_speed_limit\x18\x0c \x01(\x01:\x03\x31\x30\x30\x12\x1c\n\x10hard_accel_limit\x18\r \x01(\x01:\x02\x31\x30\x12\x1e\n\x10\x65nable_safe_path\x18\x0e \x01(\x08:\x04true\x12)\n\x1b\x65nable_planning_start_point\x18\x0f \x01(\x08:\x04true\x12,\n\x1e\x65nable_accel_auto_compensation\x18\x10 \x01(\x08:\x04true\x12\x18\n\rkappa_preview\x18\x11 \x01(\x01:\x01\x30\x12\x1a\n\x0fkappa_threshold\x18\x12 \x01(\x01:\x01\x30*X\n\x0cNaviTaskType\x12\x19\n\x15NAVI_OBSTACLE_DECIDER\x10\x03\x12\x15\n\x11NAVI_PATH_DECIDER\x10\x04\x12\x16\n\x12NAVI_SPEED_DECIDER\x10\x05')

_NAVITASKTYPE = DESCRIPTOR.enum_types_by_name['NaviTaskType']
NaviTaskType = enum_type_wrapper.EnumTypeWrapper(_NAVITASKTYPE)
NAVI_OBSTACLE_DECIDER = 3
NAVI_PATH_DECIDER = 4
NAVI_SPEED_DECIDER = 5


_NAVIOBSTACLEDECIDERCONFIG = DESCRIPTOR.message_types_by_name['NaviObstacleDeciderConfig']
_NAVIPATHDECIDERCONFIG = DESCRIPTOR.message_types_by_name['NaviPathDeciderConfig']
_MOVEDESTLANECONFIGTABLE = DESCRIPTOR.message_types_by_name['MoveDestLaneConfigTable']
_SHIFTCONFIG = DESCRIPTOR.message_types_by_name['ShiftConfig']
_NAVISPEEDDECIDERCONFIG = DESCRIPTOR.message_types_by_name['NaviSpeedDeciderConfig']
NaviObstacleDeciderConfig = _reflection.GeneratedProtocolMessageType('NaviObstacleDeciderConfig', (_message.Message,), {
  'DESCRIPTOR' : _NAVIOBSTACLEDECIDERCONFIG,
  '__module__' : 'modules.planning.planners.navi.proto.navi_task_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.NaviObstacleDeciderConfig)
  })
_sym_db.RegisterMessage(NaviObstacleDeciderConfig)

NaviPathDeciderConfig = _reflection.GeneratedProtocolMessageType('NaviPathDeciderConfig', (_message.Message,), {
  'DESCRIPTOR' : _NAVIPATHDECIDERCONFIG,
  '__module__' : 'modules.planning.planners.navi.proto.navi_task_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.NaviPathDeciderConfig)
  })
_sym_db.RegisterMessage(NaviPathDeciderConfig)

MoveDestLaneConfigTable = _reflection.GeneratedProtocolMessageType('MoveDestLaneConfigTable', (_message.Message,), {
  'DESCRIPTOR' : _MOVEDESTLANECONFIGTABLE,
  '__module__' : 'modules.planning.planners.navi.proto.navi_task_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MoveDestLaneConfigTable)
  })
_sym_db.RegisterMessage(MoveDestLaneConfigTable)

ShiftConfig = _reflection.GeneratedProtocolMessageType('ShiftConfig', (_message.Message,), {
  'DESCRIPTOR' : _SHIFTCONFIG,
  '__module__' : 'modules.planning.planners.navi.proto.navi_task_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ShiftConfig)
  })
_sym_db.RegisterMessage(ShiftConfig)

NaviSpeedDeciderConfig = _reflection.GeneratedProtocolMessageType('NaviSpeedDeciderConfig', (_message.Message,), {
  'DESCRIPTOR' : _NAVISPEEDDECIDERCONFIG,
  '__module__' : 'modules.planning.planners.navi.proto.navi_task_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.NaviSpeedDeciderConfig)
  })
_sym_db.RegisterMessage(NaviSpeedDeciderConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NAVITASKTYPE._serialized_start=1705
  _NAVITASKTYPE._serialized_end=1793
  _NAVIOBSTACLEDECIDERCONFIG._serialized_start=81
  _NAVIOBSTACLEDECIDERCONFIG._serialized_end=473
  _NAVIPATHDECIDERCONFIG._serialized_start=476
  _NAVIPATHDECIDERCONFIG._serialized_end=945
  _MOVEDESTLANECONFIGTABLE._serialized_start=947
  _MOVEDESTLANECONFIGTABLE._serialized_end=1025
  _SHIFTCONFIG._serialized_start=1027
  _SHIFTCONFIG._serialized_end=1106
  _NAVISPEEDDECIDERCONFIG._serialized_start=1109
  _NAVISPEEDDECIDERCONFIG._serialized_end=1703
# @@protoc_insertion_point(module_scope)
