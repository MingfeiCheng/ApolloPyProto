# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/external_command_msgs/command_status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/common_msgs/external_command_msgs/command_status.proto\x12\x17\x61pollo.external_command\x1a+modules/common_msgs/basic_msgs/header.proto\"U\n\x14\x43ommandStatusRequest\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x16\n\ncommand_id\x18\x02 \x01(\x03:\x02-1\"\x9b\x01\n\rCommandStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x16\n\ncommand_id\x18\x02 \x01(\x03:\x02-1\x12:\n\x06status\x18\x03 \x02(\x0e\x32*.apollo.external_command.CommandStatusType\x12\x0f\n\x07message\x18\x04 \x01(\t*F\n\x11\x43ommandStatusType\x12\x0b\n\x07RUNNING\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04')

_COMMANDSTATUSTYPE = DESCRIPTOR.enum_types_by_name['CommandStatusType']
CommandStatusType = enum_type_wrapper.EnumTypeWrapper(_COMMANDSTATUSTYPE)
RUNNING = 1
FINISHED = 2
ERROR = 3
UNKNOWN = 4


_COMMANDSTATUSREQUEST = DESCRIPTOR.message_types_by_name['CommandStatusRequest']
_COMMANDSTATUS = DESCRIPTOR.message_types_by_name['CommandStatus']
CommandStatusRequest = _reflection.GeneratedProtocolMessageType('CommandStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDSTATUSREQUEST,
  '__module__' : 'modules.common_msgs.external_command_msgs.command_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.external_command.CommandStatusRequest)
  })
_sym_db.RegisterMessage(CommandStatusRequest)

CommandStatus = _reflection.GeneratedProtocolMessageType('CommandStatus', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDSTATUS,
  '__module__' : 'modules.common_msgs.external_command_msgs.command_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.external_command.CommandStatus)
  })
_sym_db.RegisterMessage(CommandStatus)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMANDSTATUSTYPE._serialized_start=381
  _COMMANDSTATUSTYPE._serialized_end=451
  _COMMANDSTATUSREQUEST._serialized_start=136
  _COMMANDSTATUSREQUEST._serialized_end=221
  _COMMANDSTATUS._serialized_start=224
  _COMMANDSTATUS._serialized_end=379
# @@protoc_insertion_point(module_scope)
