# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/stage/ncut_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/perception/pipeline/proto/stage/ncut_config.proto\x12\x17\x61pollo.perception.lidar\"?\n\nNCutConfig\x12\x31\n\nparam_file\x18\x01 \x01(\t:\x1d./data/models/ncut/param.conf')



_NCUTCONFIG = DESCRIPTOR.message_types_by_name['NCutConfig']
NCutConfig = _reflection.GeneratedProtocolMessageType('NCutConfig', (_message.Message,), {
  'DESCRIPTOR' : _NCUTCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.stage.ncut_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.NCutConfig)
  })
_sym_db.RegisterMessage(NCutConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NCUTCONFIG._serialized_start=86
  _NCUTCONFIG._serialized_end=149
# @@protoc_insertion_point(module_scope)