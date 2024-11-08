# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/control/controllers/lon_based_pid_controller/proto/lon_based_pid_controller_conf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.control.control_component.proto import leadlag_conf_pb2 as modules_dot_control_dot_control__component_dot_proto_dot_leadlag__conf__pb2
from apollo_modules.modules.control.control_component.proto import pid_conf_pb2 as modules_dot_control_dot_control__component_dot_proto_dot_pid__conf__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n^modules/control/controllers/lon_based_pid_controller/proto/lon_based_pid_controller_conf.proto\x12\x0e\x61pollo.control\x1a:modules/control/control_component/proto/leadlag_conf.proto\x1a\x36modules/control/control_component/proto/pid_conf.proto\"!\n\nFilterConf\x12\x13\n\x0b\x63utoff_freq\x18\x01 \x01(\x05\"\x83\x0c\n\x19LonBasedPidControllerConf\x12\n\n\x02ts\x18\x01 \x01(\x01\x12\x1c\n\x14\x62rake_minimum_action\x18\x02 \x01(\x01\x12\x1f\n\x17throttle_minimum_action\x18\x03 \x01(\x01\x12$\n\x1cspeed_controller_input_limit\x18\x04 \x01(\x01\x12\x1b\n\x13station_error_limit\x18\x05 \x01(\x01\x12\x16\n\x0epreview_window\x18\x06 \x01(\x01\x12\x1f\n\x17standstill_acceleration\x18\x07 \x01(\x01\x12\x31\n\x10station_pid_conf\x18\x08 \x01(\x0b\x32\x17.apollo.control.PidConf\x12\x33\n\x12low_speed_pid_conf\x18\t \x01(\x0b\x32\x17.apollo.control.PidConf\x12\x34\n\x13high_speed_pid_conf\x18\n \x01(\x0b\x32\x17.apollo.control.PidConf\x12\x14\n\x0cswitch_speed\x18\x0b \x01(\x01\x12\x39\n\x18reverse_station_pid_conf\x18\x0c \x01(\x0b\x32\x17.apollo.control.PidConf\x12\x37\n\x16reverse_speed_pid_conf\x18\r \x01(\x0b\x32\x17.apollo.control.PidConf\x12;\n\x17pitch_angle_filter_conf\x18\x0e \x01(\x0b\x32\x1a.apollo.control.FilterConf\x12\x41\n\x1creverse_station_leadlag_conf\x18\x0f \x01(\x0b\x32\x1b.apollo.control.LeadlagConf\x12?\n\x1areverse_speed_leadlag_conf\x18\x10 \x01(\x0b\x32\x1b.apollo.control.LeadlagConf\x12\x32\n#enable_reverse_leadlag_compensation\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x13switch_speed_window\x18\x13 \x01(\x01:\x01\x30\x12+\n\x1c\x65nable_speed_station_preview\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x65nable_slope_offset\x18\x15 \x01(\x08:\x05\x66\x61lse\x12)\n\x1cmax_path_remain_when_stopped\x18\x16 \x01(\x01:\x03\x30.3\x12,\n\x1duse_acceleration_lookup_limit\x18\x17 \x01(\x08:\x05\x66\x61lse\x12*\n\x1buse_preview_reference_check\x18\x18 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x12steer_cmd_interval\x18\x19 \x01(\x01:\x01\x30\x12!\n\x12use_steering_check\x18\x1a \x01(\x08:\x05\x66\x61lse\x12 \n\x14pedestrian_stop_time\x18\x1b \x01(\x01:\x02\x31\x30\x12)\n\x1estandstill_narmal_acceleration\x18\x1c \x01(\x01:\x01\x30\x12\x1e\n\x13\x66ull_stop_long_time\x18\x1d \x01(\x01:\x01\x30\x12\x35\n\x14pit_station_pid_conf\x18\x1e \x01(\x0b\x32\x17.apollo.control.PidConf\x12\x33\n\x12pit_speed_pid_conf\x18\x1f \x01(\x0b\x32\x17.apollo.control.PidConf\x12!\n\x15pit_replan_check_time\x18  \x01(\x01:\x02\x31\x34\x12!\n\x16pit_replan_check_count\x18! \x01(\x05:\x01\x33\x12\x1b\n\x10\x65pb_change_count\x18\" \x01(\x05:\x01\x32\x12\x1e\n\x16stop_gain_acceleration\x18# \x01(\x01\x12\x1e\n\x0fuse_vehicle_epb\x18$ \x01(\x08:\x05\x66\x61lse\x12\"\n\x1a\x66ull_stop_path_remain_gain\x18% \x01(\x01\x12*\n\x1fuse_opposite_slope_compensation\x18& \x01(\x05:\x01\x31')



_FILTERCONF = DESCRIPTOR.message_types_by_name['FilterConf']
_LONBASEDPIDCONTROLLERCONF = DESCRIPTOR.message_types_by_name['LonBasedPidControllerConf']
FilterConf = _reflection.GeneratedProtocolMessageType('FilterConf', (_message.Message,), {
  'DESCRIPTOR' : _FILTERCONF,
  '__module__' : 'modules.control.controllers.lon_based_pid_controller.proto.lon_based_pid_controller_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.FilterConf)
  })
_sym_db.RegisterMessage(FilterConf)

LonBasedPidControllerConf = _reflection.GeneratedProtocolMessageType('LonBasedPidControllerConf', (_message.Message,), {
  'DESCRIPTOR' : _LONBASEDPIDCONTROLLERCONF,
  '__module__' : 'modules.control.controllers.lon_based_pid_controller.proto.lon_based_pid_controller_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.LonBasedPidControllerConf)
  })
_sym_db.RegisterMessage(LonBasedPidControllerConf)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILTERCONF._serialized_start=230
  _FILTERCONF._serialized_end=263
  _LONBASEDPIDCONTROLLERCONF._serialized_start=266
  _LONBASEDPIDCONTROLLERCONF._serialized_end=1805
# @@protoc_insertion_point(module_scope)
