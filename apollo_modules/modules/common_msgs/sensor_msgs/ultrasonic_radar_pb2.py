# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/sensor_msgs/ultrasonic_radar.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/common_msgs/sensor_msgs/ultrasonic_radar.proto\x12\x0e\x61pollo.drivers\x1a+modules/common_msgs/basic_msgs/header.proto\"C\n\nUltrasonic\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x0e\n\x06ranges\x18\x02 \x03(\x02')



_ULTRASONIC = DESCRIPTOR.message_types_by_name['Ultrasonic']
Ultrasonic = _reflection.GeneratedProtocolMessageType('Ultrasonic', (_message.Message,), {
  'DESCRIPTOR' : _ULTRASONIC,
  '__module__' : 'modules.common_msgs.sensor_msgs.ultrasonic_radar_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.Ultrasonic)
  })
_sym_db.RegisterMessage(Ultrasonic)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ULTRASONIC._serialized_start=119
  _ULTRASONIC._serialized_end=186
# @@protoc_insertion_point(module_scope)