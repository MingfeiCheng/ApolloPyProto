# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/guardian_msgs/guardian.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.control_msgs import control_cmd_pb2 as modules_dot_common__msgs_dot_control__msgs_dot_control__cmd__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/common_msgs/guardian_msgs/guardian.proto\x12\x0f\x61pollo.guardian\x1a+modules/common_msgs/basic_msgs/header.proto\x1a\x32modules/common_msgs/control_msgs/control_cmd.proto\"q\n\x0fGuardianCommand\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x37\n\x0f\x63ontrol_command\x18\x02 \x01(\x0b\x32\x1e.apollo.control.ControlCommand')



_GUARDIANCOMMAND = DESCRIPTOR.message_types_by_name['GuardianCommand']
GuardianCommand = _reflection.GeneratedProtocolMessageType('GuardianCommand', (_message.Message,), {
  'DESCRIPTOR' : _GUARDIANCOMMAND,
  '__module__' : 'modules.common_msgs.guardian_msgs.guardian_pb2'
  # @@protoc_insertion_point(class_scope:apollo.guardian.GuardianCommand)
  })
_sym_db.RegisterMessage(GuardianCommand)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GUARDIANCOMMAND._serialized_start=166
  _GUARDIANCOMMAND._serialized_end=279
# @@protoc_insertion_point(module_scope)
