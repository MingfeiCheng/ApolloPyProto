# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/contrib/lgsvl_msgs/proto/detection3d.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_modules.modules.contrib.lgsvl_msgs.proto import detection2d_pb2 as modules_dot_contrib_dot_lgsvl__msgs_dot_proto_dot_detection2d__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/contrib/lgsvl_msgs/proto/detection3d.proto\x12\x19\x61pollo.contrib.lgsvl_msgs\x1a+modules/common_msgs/basic_msgs/header.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a\x32modules/contrib/lgsvl_msgs/proto/detection2d.proto\"`\n\x04Pose\x12(\n\x08position\x18\x01 \x01(\x0b\x32\x16.apollo.common.Point3D\x12.\n\x0borientation\x18\x02 \x01(\x0b\x32\x19.apollo.common.Quaternion\"t\n\rBoundingBox3D\x12\x31\n\x08position\x18\x01 \x01(\x0b\x32\x1f.apollo.contrib.lgsvl_msgs.Pose\x12\x30\n\x04size\x18\x02 \x01(\x0b\x32\".apollo.contrib.lgsvl_msgs.Vector3\"\xca\x01\n\x0b\x44\x65tection3D\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\n\n\x02id\x18\x02 \x01(\r\x12\r\n\x05label\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x01\x12\x36\n\x04\x62\x62ox\x18\x05 \x01(\x0b\x32(.apollo.contrib.lgsvl_msgs.BoundingBox3D\x12\x32\n\x08velocity\x18\x06 \x01(\x0b\x32 .apollo.contrib.lgsvl_msgs.Twistb\x06proto3')



_POSE = DESCRIPTOR.message_types_by_name['Pose']
_BOUNDINGBOX3D = DESCRIPTOR.message_types_by_name['BoundingBox3D']
_DETECTION3D = DESCRIPTOR.message_types_by_name['Detection3D']
Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'modules.contrib.lgsvl_msgs.proto.detection3d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Pose)
  })
_sym_db.RegisterMessage(Pose)

BoundingBox3D = _reflection.GeneratedProtocolMessageType('BoundingBox3D', (_message.Message,), {
  'DESCRIPTOR' : _BOUNDINGBOX3D,
  '__module__' : 'modules.contrib.lgsvl_msgs.proto.detection3d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.BoundingBox3D)
  })
_sym_db.RegisterMessage(BoundingBox3D)

Detection3D = _reflection.GeneratedProtocolMessageType('Detection3D', (_message.Message,), {
  'DESCRIPTOR' : _DETECTION3D,
  '__module__' : 'modules.contrib.lgsvl_msgs.proto.detection3d_pb2'
  # @@protoc_insertion_point(class_scope:apollo.contrib.lgsvl_msgs.Detection3D)
  })
_sym_db.RegisterMessage(Detection3D)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POSE._serialized_start=225
  _POSE._serialized_end=321
  _BOUNDINGBOX3D._serialized_start=323
  _BOUNDINGBOX3D._serialized_end=439
  _DETECTION3D._serialized_start=442
  _DETECTION3D._serialized_end=644
# @@protoc_insertion_point(module_scope)
