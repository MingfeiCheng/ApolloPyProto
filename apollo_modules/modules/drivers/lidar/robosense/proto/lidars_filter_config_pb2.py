# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/lidar/robosense/proto/lidars_filter_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/drivers/lidar/robosense/proto/lidars_filter_config.proto\x12\x15\x61pollo.drivers.suteng\"9\n\x05Lidar\x12\x10\n\x08\x66rame_id\x18\x01 \x02(\t\x12\x0f\n\x07grading\x18\x02 \x02(\x05\x12\r\n\x05point\x18\x03 \x03(\t\";\n\x0cLidarsFilter\x12+\n\x05lidar\x18\x01 \x03(\x0b\x32\x1c.apollo.drivers.suteng.Lidar')



_LIDAR = DESCRIPTOR.message_types_by_name['Lidar']
_LIDARSFILTER = DESCRIPTOR.message_types_by_name['LidarsFilter']
Lidar = _reflection.GeneratedProtocolMessageType('Lidar', (_message.Message,), {
  'DESCRIPTOR' : _LIDAR,
  '__module__' : 'modules.drivers.lidar.robosense.proto.lidars_filter_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.suteng.Lidar)
  })
_sym_db.RegisterMessage(Lidar)

LidarsFilter = _reflection.GeneratedProtocolMessageType('LidarsFilter', (_message.Message,), {
  'DESCRIPTOR' : _LIDARSFILTER,
  '__module__' : 'modules.drivers.lidar.robosense.proto.lidars_filter_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.suteng.LidarsFilter)
  })
_sym_db.RegisterMessage(LidarsFilter)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIDAR._serialized_start=91
  _LIDAR._serialized_end=148
  _LIDARSFILTER._serialized_start=150
  _LIDARSFILTER._serialized_end=209
# @@protoc_insertion_point(module_scope)