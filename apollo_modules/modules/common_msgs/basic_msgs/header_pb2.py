# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/basic_msgs/header.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import error_code_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+modules/common_msgs/basic_msgs/header.proto\x12\rapollo.common\x1a/modules/common_msgs/basic_msgs/error_code.proto\"\xe5\x01\n\x06Header\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x12\x14\n\x0csequence_num\x18\x03 \x01(\r\x12\x17\n\x0flidar_timestamp\x18\x04 \x01(\x04\x12\x18\n\x10\x63\x61mera_timestamp\x18\x05 \x01(\x04\x12\x17\n\x0fradar_timestamp\x18\x06 \x01(\x04\x12\x12\n\x07version\x18\x07 \x01(\r:\x01\x31\x12\'\n\x06status\x18\x08 \x01(\x0b\x32\x17.apollo.common.StatusPb\x12\x10\n\x08\x66rame_id\x18\t \x01(\t')



_HEADER = DESCRIPTOR.message_types_by_name['Header']
Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'modules.common_msgs.basic_msgs.header_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.Header)
  })
_sym_db.RegisterMessage(Header)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEADER._serialized_start=112
  _HEADER._serialized_end=341
# @@protoc_insertion_point(module_scope)