# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/common/proto/plugin_param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/perception/common/proto/plugin_param.proto\x12\x11\x61pollo.perception\"E\n\x0bPluginParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63onfig_path\x18\x02 \x01(\t\x12\x13\n\x0b\x63onfig_file\x18\x03 \x01(\t')



_PLUGINPARAM = DESCRIPTOR.message_types_by_name['PluginParam']
PluginParam = _reflection.GeneratedProtocolMessageType('PluginParam', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINPARAM,
  '__module__' : 'modules.perception.common.proto.plugin_param_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.PluginParam)
  })
_sym_db.RegisterMessage(PluginParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLUGINPARAM._serialized_start=73
  _PLUGINPARAM._serialized_end=142
# @@protoc_insertion_point(module_scope)
