# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/external_command/command_processor/action_command_processor/proto/action_command_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nemodules/external_command/command_processor/action_command_processor/proto/action_command_config.proto\x12\x17\x61pollo.external_command\"r\n\x13\x41\x63tionCommandConfig\x12\x1f\n\x17pull_over_scenario_name\x18\x01 \x02(\t\x12\x1a\n\x12stop_scenario_name\x18\x02 \x02(\t\x12\x1e\n\x16minimun_non_zero_speed\x18\x03 \x02(\x01')



_ACTIONCOMMANDCONFIG = DESCRIPTOR.message_types_by_name['ActionCommandConfig']
ActionCommandConfig = _reflection.GeneratedProtocolMessageType('ActionCommandConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONCOMMANDCONFIG,
  '__module__' : 'modules.external_command.command_processor.action_command_processor.proto.action_command_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.external_command.ActionCommandConfig)
  })
_sym_db.RegisterMessage(ActionCommandConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ACTIONCOMMANDCONFIG._serialized_start=130
  _ACTIONCOMMANDCONFIG._serialized_end=244
# @@protoc_insertion_point(module_scope)