# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/localization_msgs/localization.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_modules.modules.common_msgs.basic_msgs import pnc_point_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2
from apollo_modules.modules.common_msgs.localization_msgs import localization_status_pb2 as modules_dot_common__msgs_dot_localization__msgs_dot_localization__status__pb2
from apollo_modules.modules.common_msgs.localization_msgs import pose_pb2 as modules_dot_common__msgs_dot_localization__msgs_dot_pose__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/common_msgs/localization_msgs/localization.proto\x12\x13\x61pollo.localization\x1a+modules/common_msgs/basic_msgs/header.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a.modules/common_msgs/basic_msgs/pnc_point.proto\x1a?modules/common_msgs/localization_msgs/localization_status.proto\x1a\x30modules/common_msgs/localization_msgs/pose.proto\"\xa4\x02\n\x0bUncertainty\x12\x30\n\x10position_std_dev\x18\x01 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x33\n\x13orientation_std_dev\x18\x02 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x37\n\x17linear_velocity_std_dev\x18\x03 \x01(\x0b\x32\x16.apollo.common.Point3D\x12;\n\x1blinear_acceleration_std_dev\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x38\n\x18\x61ngular_velocity_std_dev\x18\x05 \x01(\x0b\x32\x16.apollo.common.Point3D\"\xe5\x02\n\x14LocalizationEstimate\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\'\n\x04pose\x18\x02 \x01(\x0b\x32\x19.apollo.localization.Pose\x12\x35\n\x0buncertainty\x18\x03 \x01(\x0b\x32 .apollo.localization.Uncertainty\x12\x18\n\x10measurement_time\x18\x04 \x01(\x01\x12\x38\n\x10trajectory_point\x18\x05 \x03(\x0b\x32\x1e.apollo.common.TrajectoryPoint\x12\x32\n\nmsf_status\x18\x06 \x01(\x0b\x32\x1e.apollo.localization.MsfStatus\x12>\n\rsensor_status\x18\x07 \x01(\x0b\x32\'.apollo.localization.MsfSensorMsgStatus\"\x9f\x02\n\x12LocalizationStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x38\n\rfusion_status\x18\x02 \x01(\x0e\x32!.apollo.localization.MeasureState\x12:\n\x0bgnss_status\x18\x03 \x01(\x0e\x32!.apollo.localization.MeasureStateB\x02\x18\x01\x12;\n\x0clidar_status\x18\x04 \x01(\x0e\x32!.apollo.localization.MeasureStateB\x02\x18\x01\x12\x18\n\x10measurement_time\x18\x05 \x01(\x01\x12\x15\n\rstate_message\x18\x06 \x01(\t*T\n\x0cMeasureState\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08WARNNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x12\n\x0e\x43RITICAL_ERROR\x10\x03\x12\x0f\n\x0b\x46\x41TAL_ERROR\x10\x04')

_MEASURESTATE = DESCRIPTOR.enum_types_by_name['MeasureState']
MeasureState = enum_type_wrapper.EnumTypeWrapper(_MEASURESTATE)
OK = 0
WARNNING = 1
ERROR = 2
CRITICAL_ERROR = 3
FATAL_ERROR = 4


_UNCERTAINTY = DESCRIPTOR.message_types_by_name['Uncertainty']
_LOCALIZATIONESTIMATE = DESCRIPTOR.message_types_by_name['LocalizationEstimate']
_LOCALIZATIONSTATUS = DESCRIPTOR.message_types_by_name['LocalizationStatus']
Uncertainty = _reflection.GeneratedProtocolMessageType('Uncertainty', (_message.Message,), {
  'DESCRIPTOR' : _UNCERTAINTY,
  '__module__' : 'modules.common_msgs.localization_msgs.localization_pb2'
  # @@protoc_insertion_point(class_scope:apollo.localization.Uncertainty)
  })
_sym_db.RegisterMessage(Uncertainty)

LocalizationEstimate = _reflection.GeneratedProtocolMessageType('LocalizationEstimate', (_message.Message,), {
  'DESCRIPTOR' : _LOCALIZATIONESTIMATE,
  '__module__' : 'modules.common_msgs.localization_msgs.localization_pb2'
  # @@protoc_insertion_point(class_scope:apollo.localization.LocalizationEstimate)
  })
_sym_db.RegisterMessage(LocalizationEstimate)

LocalizationStatus = _reflection.GeneratedProtocolMessageType('LocalizationStatus', (_message.Message,), {
  'DESCRIPTOR' : _LOCALIZATIONSTATUS,
  '__module__' : 'modules.common_msgs.localization_msgs.localization_pb2'
  # @@protoc_insertion_point(class_scope:apollo.localization.LocalizationStatus)
  })
_sym_db.RegisterMessage(LocalizationStatus)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCALIZATIONSTATUS.fields_by_name['gnss_status']._options = None
  _LOCALIZATIONSTATUS.fields_by_name['gnss_status']._serialized_options = b'\030\001'
  _LOCALIZATIONSTATUS.fields_by_name['lidar_status']._options = None
  _LOCALIZATIONSTATUS.fields_by_name['lidar_status']._serialized_options = b'\030\001'
  _MEASURESTATE._serialized_start=1281
  _MEASURESTATE._serialized_end=1365
  _UNCERTAINTY._serialized_start=337
  _UNCERTAINTY._serialized_end=629
  _LOCALIZATIONESTIMATE._serialized_start=632
  _LOCALIZATIONESTIMATE._serialized_end=989
  _LOCALIZATIONSTATUS._serialized_start=992
  _LOCALIZATIONSTATUS._serialized_end=1279
# @@protoc_insertion_point(module_scope)
