# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/map_msgs/map_yield_sign.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.map_msgs import map_geometry_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_id_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/common_msgs/map_msgs/map_yield_sign.proto\x12\x0c\x61pollo.hdmap\x1a/modules/common_msgs/map_msgs/map_geometry.proto\x1a)modules/common_msgs/map_msgs/map_id.proto\"w\n\tYieldSign\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.apollo.hdmap.Id\x12&\n\tstop_line\x18\x02 \x03(\x0b\x32\x13.apollo.hdmap.Curve\x12$\n\noverlap_id\x18\x03 \x03(\x0b\x32\x10.apollo.hdmap.Id')



_YIELDSIGN = DESCRIPTOR.message_types_by_name['YieldSign']
YieldSign = _reflection.GeneratedProtocolMessageType('YieldSign', (_message.Message,), {
  'DESCRIPTOR' : _YIELDSIGN,
  '__module__' : 'modules.common_msgs.map_msgs.map_yield_sign_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.YieldSign)
  })
_sym_db.RegisterMessage(YieldSign)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _YIELDSIGN._serialized_start=159
  _YIELDSIGN._serialized_end=278
# @@protoc_insertion_point(module_scope)
