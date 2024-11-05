# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/basic_msgs/geometry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-modules/common_msgs/basic_msgs/geometry.proto\x12\rapollo.common\"8\n\x08PointENU\x12\x0e\n\x01x\x18\x01 \x01(\x01:\x03nan\x12\x0e\n\x01y\x18\x02 \x01(\x01:\x03nan\x12\x0c\n\x01z\x18\x03 \x01(\x01:\x01\x30\"A\n\x08PointLLH\x12\x10\n\x03lon\x18\x01 \x01(\x01:\x03nan\x12\x10\n\x03lat\x18\x02 \x01(\x01:\x03nan\x12\x11\n\x06height\x18\x03 \x01(\x01:\x01\x30\")\n\x07Point2D\x12\x0e\n\x01x\x18\x01 \x01(\x01:\x03nan\x12\x0e\n\x01y\x18\x02 \x01(\x01:\x03nan\"9\n\x07Point3D\x12\x0e\n\x01x\x18\x01 \x01(\x01:\x03nan\x12\x0e\n\x01y\x18\x02 \x01(\x01:\x03nan\x12\x0e\n\x01z\x18\x03 \x01(\x01:\x03nan\"P\n\nQuaternion\x12\x0f\n\x02qx\x18\x01 \x01(\x01:\x03nan\x12\x0f\n\x02qy\x18\x02 \x01(\x01:\x03nan\x12\x0f\n\x02qz\x18\x03 \x01(\x01:\x03nan\x12\x0f\n\x02qw\x18\x04 \x01(\x01:\x03nan\"0\n\x07Polygon\x12%\n\x05point\x18\x01 \x03(\x0b\x32\x16.apollo.common.Point3D')



_POINTENU = DESCRIPTOR.message_types_by_name['PointENU']
_POINTLLH = DESCRIPTOR.message_types_by_name['PointLLH']
_POINT2D = DESCRIPTOR.message_types_by_name['Point2D']
_POINT3D = DESCRIPTOR.message_types_by_name['Point3D']
_QUATERNION = DESCRIPTOR.message_types_by_name['Quaternion']
_POLYGON = DESCRIPTOR.message_types_by_name['Polygon']
PointENU = _reflection.GeneratedProtocolMessageType('PointENU', (_message.Message,), {
  'DESCRIPTOR' : _POINTENU,
  '__module__' : 'modules.common_msgs.basic_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.PointENU)
  })
_sym_db.RegisterMessage(PointENU)

PointLLH = _reflection.GeneratedProtocolMessageType('PointLLH', (_message.Message,), {
  'DESCRIPTOR' : _POINTLLH,
  '__module__' : 'modules.common_msgs.basic_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.PointLLH)
  })
_sym_db.RegisterMessage(PointLLH)

Point2D = _reflection.GeneratedProtocolMessageType('Point2D', (_message.Message,), {
  'DESCRIPTOR' : _POINT2D,
  '__module__' : 'modules.common_msgs.basic_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.Point2D)
  })
_sym_db.RegisterMessage(Point2D)

Point3D = _reflection.GeneratedProtocolMessageType('Point3D', (_message.Message,), {
  'DESCRIPTOR' : _POINT3D,
  '__module__' : 'modules.common_msgs.basic_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.Point3D)
  })
_sym_db.RegisterMessage(Point3D)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), {
  'DESCRIPTOR' : _QUATERNION,
  '__module__' : 'modules.common_msgs.basic_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.Quaternion)
  })
_sym_db.RegisterMessage(Quaternion)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {
  'DESCRIPTOR' : _POLYGON,
  '__module__' : 'modules.common_msgs.basic_msgs.geometry_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.Polygon)
  })
_sym_db.RegisterMessage(Polygon)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POINTENU._serialized_start=64
  _POINTENU._serialized_end=120
  _POINTLLH._serialized_start=122
  _POINTLLH._serialized_end=187
  _POINT2D._serialized_start=189
  _POINT2D._serialized_end=230
  _POINT3D._serialized_start=232
  _POINT3D._serialized_end=289
  _QUATERNION._serialized_start=291
  _QUATERNION._serialized_end=371
  _POLYGON._serialized_start=373
  _POLYGON._serialized_end=421
# @@protoc_insertion_point(module_scope)
