# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/sensor_msgs/ins.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/common_msgs/sensor_msgs/ins.proto\x12\x13\x61pollo.drivers.gnss\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto\"V\n\x07InsStat\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x12\n\nins_status\x18\x02 \x01(\r\x12\x10\n\x08pos_type\x18\x03 \x01(\r\"\xd6\x04\n\x03Ins\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12+\n\x04type\x18\x03 \x01(\x0e\x32\x1d.apollo.drivers.gnss.Ins.Type\x12)\n\x08position\x18\x04 \x01(\x0b\x32\x17.apollo.common.PointLLH\x12,\n\x0c\x65uler_angles\x18\x05 \x01(\x0b\x32\x16.apollo.common.Point3D\x12/\n\x0flinear_velocity\x18\x06 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x30\n\x10\x61ngular_velocity\x18\x07 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x33\n\x13linear_acceleration\x18\x08 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x1f\n\x13position_covariance\x18\t \x03(\x02\x42\x02\x10\x01\x12#\n\x17\x65uler_angles_covariance\x18\n \x03(\x02\x42\x02\x10\x01\x12&\n\x1alinear_velocity_covariance\x18\x0b \x03(\x02\x42\x02\x10\x01\x12\'\n\x1b\x61ngular_velocity_covariance\x18\x0c \x03(\x02\x42\x02\x10\x01\x12*\n\x1elinear_acceleration_covariance\x18\r \x03(\x02\x42\x02\x10\x01\"-\n\x04Type\x12\x0b\n\x07INVALID\x10\x00\x12\x0e\n\nCONVERGING\x10\x01\x12\x08\n\x04GOOD\x10\x02')



_INSSTAT = DESCRIPTOR.message_types_by_name['InsStat']
_INS = DESCRIPTOR.message_types_by_name['Ins']
_INS_TYPE = _INS.enum_types_by_name['Type']
InsStat = _reflection.GeneratedProtocolMessageType('InsStat', (_message.Message,), {
  'DESCRIPTOR' : _INSSTAT,
  '__module__' : 'modules.common_msgs.sensor_msgs.ins_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.InsStat)
  })
_sym_db.RegisterMessage(InsStat)

Ins = _reflection.GeneratedProtocolMessageType('Ins', (_message.Message,), {
  'DESCRIPTOR' : _INS,
  '__module__' : 'modules.common_msgs.sensor_msgs.ins_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.Ins)
  })
_sym_db.RegisterMessage(Ins)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INS.fields_by_name['position_covariance']._options = None
  _INS.fields_by_name['position_covariance']._serialized_options = b'\020\001'
  _INS.fields_by_name['euler_angles_covariance']._options = None
  _INS.fields_by_name['euler_angles_covariance']._serialized_options = b'\020\001'
  _INS.fields_by_name['linear_velocity_covariance']._options = None
  _INS.fields_by_name['linear_velocity_covariance']._serialized_options = b'\020\001'
  _INS.fields_by_name['angular_velocity_covariance']._options = None
  _INS.fields_by_name['angular_velocity_covariance']._serialized_options = b'\020\001'
  _INS.fields_by_name['linear_acceleration_covariance']._options = None
  _INS.fields_by_name['linear_acceleration_covariance']._serialized_options = b'\020\001'
  _INSSTAT._serialized_start=158
  _INSSTAT._serialized_end=244
  _INS._serialized_start=247
  _INS._serialized_end=845
  _INS_TYPE._serialized_start=800
  _INS_TYPE._serialized_end=845
# @@protoc_insertion_point(module_scope)
