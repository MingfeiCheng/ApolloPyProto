# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/external_command_msgs/geometry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/common_msgs/external_command_msgs/geometry.proto\x12\x17\x61pollo.external_command\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\"-\n\x04Pose\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\";\n\nRoiPolygon\x12-\n\x05point\x18\x01 \x03(\x0b\x32\x1e.apollo.external_command.Point')



_POINT = DESCRIPTOR.message_types_by_name['Point']
_POSE = DESCRIPTOR.message_types_by_name['Pose']
_ROIPOLYGON = DESCRIPTOR.message_types_by_name['RoiPolygon']
Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'modules.common_msgs.external_command_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.external_command.Point)
  })
_sym_db.RegisterMessage(Point)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'modules.common_msgs.external_command_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.external_command.Pose)
  })
_sym_db.RegisterMessage(Pose)

RoiPolygon = _reflection.GeneratedProtocolMessageType('RoiPolygon', (_message.Message,), {
  'DESCRIPTOR' : _ROIPOLYGON,
  '__module__' : 'modules.common_msgs.external_command_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.external_command.RoiPolygon)
  })
_sym_db.RegisterMessage(RoiPolygon)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POINT._serialized_start=85
  _POINT._serialized_end=114
  _POSE._serialized_start=116
  _POSE._serialized_end=161
  _ROIPOLYGON._serialized_start=163
  _ROIPOLYGON._serialized_end=222
# @@protoc_insertion_point(module_scope)