# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/dreamview/backend/common/teleop/proto/daemon_cmd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/dreamview/backend/common/teleop/proto/daemon_cmd.proto\x12\x15modules.teleop.daemon\x1a+modules/common_msgs/basic_msgs/header.proto\"Y\n\tDaemonCmd\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x11\n\x07service\x18\x02 \x01(\t:\x00\x12\x12\n\x03\x63md\x18\x03 \x01(\t:\x05start')



_DAEMONCMD = DESCRIPTOR.message_types_by_name['DaemonCmd']
DaemonCmd = _reflection.GeneratedProtocolMessageType('DaemonCmd', (_message.Message,), {
  'DESCRIPTOR' : _DAEMONCMD,
  '__module__' : 'modules.dreamview.backend.common.teleop.proto.daemon_cmd_pb2'
  # @@protoc_insertion_point(class_scope:modules.teleop.daemon.DaemonCmd)
  })
_sym_db.RegisterMessage(DaemonCmd)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DAEMONCMD._serialized_start=134
  _DAEMONCMD._serialized_end=223
# @@protoc_insertion_point(module_scope)
