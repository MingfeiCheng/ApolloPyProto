# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/localization/proto/sins_pva.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)modules/localization/proto/sins_pva.proto\x12\x13\x61pollo.localization\x1a+modules/common_msgs/basic_msgs/header.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\"\xe7\x01\n\x0cIntegSinsPva\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12)\n\x08position\x18\x02 \x01(\x0b\x32\x17.apollo.common.PointLLH\x12(\n\x08velocity\x18\x03 \x01(\x0b\x32\x16.apollo.common.Point3D\x12(\n\x08\x61ttitude\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x15\n\tpva_covar\x18\x05 \x03(\x01\x42\x02\x10\x01\x12\x1a\n\x12init_and_alignment\x18\x06 \x01(\x08')



_INTEGSINSPVA = DESCRIPTOR.message_types_by_name['IntegSinsPva']
IntegSinsPva = _reflection.GeneratedProtocolMessageType('IntegSinsPva', (_message.Message,), {
  'DESCRIPTOR' : _INTEGSINSPVA,
  '__module__' : 'modules.localization.proto.sins_pva_pb2'
  # @@protoc_insertion_point(class_scope:apollo.localization.IntegSinsPva)
  })
_sym_db.RegisterMessage(IntegSinsPva)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INTEGSINSPVA.fields_by_name['pva_covar']._options = None
  _INTEGSINSPVA.fields_by_name['pva_covar']._serialized_options = b'\020\001'
  _INTEGSINSPVA._serialized_start=159
  _INTEGSINSPVA._serialized_end=390
# @@protoc_insertion_point(module_scope)
