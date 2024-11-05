# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/contrib/lgsvl_msgs/proto/detection2d.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/contrib/lgsvl_msgs/proto/detection2d.proto\x12\x19\x61pollo.contrib.lgsvl_msgs\x1a+modules/common_msgs/basic_msgs/header.proto\"D\n\rBoundingBox2D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"p\n\x05Twist\x12\x32\n\x06linear\x18\x01 \x01(\x0b\x32\".apollo.contrib.lgsvl_msgs.Vector3\x12\x33\n\x07\x61ngular\x18\x02 \x01(\x0b\x32\".apollo.contrib.lgsvl_msgs.Vector3\"\xca\x01\n\x0b\x44\x65tection2D\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\n\n\x02id\x18\x02 \x01(\r\x12\r\n\x05label\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x01\x12\x36\n\x04\x62\x62ox\x18\x05 \x01(\x0b\x32(.apollo.contrib.lgsvl_msgs.BoundingBox2D\x12\x32\n\x08velocity\x18\x06 \x01(\x0b\x32 .apollo.contrib.lgsvl_msgs.Twistb\x06proto3')



_BOUNDINGBOX2D = DESCRIPTOR.message_types_by_name['BoundingBox2D']
_VECTOR3 = DESCRIPTOR.message_types_by_name['Vector3']
_TWIST = DESCRIPTOR.message_types_by_name['Twist']
_DETECTION2D = DESCRIPTOR.message_types_by_name['Detection2D']
BoundingBox2D = _reflection.GeneratedProtocolMessageType('BoundingBox2D', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGBOX2D,
  '__module__' : 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.BoundingBox2D)
  })
_sym_db.RegisterMessage(BoundingBox2D)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR3,
  '__module__' : 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Vector3)
  })
_sym_db.RegisterMessage(Vector3)

Twist = _reflection.GeneratedProtocolMessageType('Twist', (_message.Message,), {
  'DESCRIPTOR' : _TWIST,
  '__module__' : 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Twist)
  })
_sym_db.RegisterMessage(Twist)

Detection2D = _reflection.GeneratedProtocolMessageType('Detection2D', (_message.Message,), {
  'DESCRIPTOR' : _DETECTION2D,
  '__module__' : 'modules.contrib.lgsvl_msgs.proto.detection2d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Detection2D)
  })
_sym_db.RegisterMessage(Detection2D)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOUNDINGBOX2D._serialized_start=126
  _BOUNDINGBOX2D._serialized_end=194
  _VECTOR3._serialized_start=196
  _VECTOR3._serialized_end=238
  _TWIST._serialized_start=240
  _TWIST._serialized_end=352
  _DETECTION2D._serialized_start=355
  _DETECTION2D._serialized_end=557
# @@protoc_insertion_point(module_scope)
