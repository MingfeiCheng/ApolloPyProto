# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/planning_interface_base/scenario_base/proto/scenario_pipeline.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.planning.planning_base.proto import plugin_declare_info_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_plugin__declare__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTmodules/planning/planning_interface_base/scenario_base/proto/scenario_pipeline.proto\x12\x0f\x61pollo.planning\x1a>modules/planning/planning_base/proto/plugin_declare_info.proto\"\xa9\x01\n\rStagePipeline\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x30\n\x04task\x18\x04 \x03(\x0b\x32\".apollo.planning.PluginDeclareInfo\x12\x39\n\rfallback_task\x18\x05 \x01(\x0b\x32\".apollo.planning.PluginDeclareInfo\"A\n\x10ScenarioPipeline\x12-\n\x05stage\x18\x01 \x03(\x0b\x32\x1e.apollo.planning.StagePipeline')



_STAGEPIPELINE = DESCRIPTOR.message_types_by_name['StagePipeline']
_SCENARIOPIPELINE = DESCRIPTOR.message_types_by_name['ScenarioPipeline']
StagePipeline = _reflection.GeneratedProtocolMessageType('StagePipeline', (_message.Message,), {
  'DESCRIPTOR' : _STAGEPIPELINE,
  '__module__' : 'modules.planning.planning_interface_base.scenario_base.proto.scenario_pipeline_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.StagePipeline)
  })
_sym_db.RegisterMessage(StagePipeline)

ScenarioPipeline = _reflection.GeneratedProtocolMessageType('ScenarioPipeline', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIOPIPELINE,
  '__module__' : 'modules.planning.planning_interface_base.scenario_base.proto.scenario_pipeline_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ScenarioPipeline)
  })
_sym_db.RegisterMessage(ScenarioPipeline)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STAGEPIPELINE._serialized_start=170
  _STAGEPIPELINE._serialized_end=339
  _SCENARIOPIPELINE._serialized_start=341
  _SCENARIOPIPELINE._serialized_end=406
# @@protoc_insertion_point(module_scope)