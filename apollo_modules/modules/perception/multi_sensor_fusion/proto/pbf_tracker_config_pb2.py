# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/multi_sensor_fusion/proto/pbf_tracker_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEmodules/perception/multi_sensor_fusion/proto/pbf_tracker_config.proto\x12\x18\x61pollo.perception.fusion\x1a\x32modules/perception/common/proto/plugin_param.proto\"\x86\x02\n\x10PbfTrackerConfig\x12\x39\n\x11type_fusion_param\x18\x01 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12;\n\x13motion_fusion_param\x18\x02 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12:\n\x12shape_fusion_param\x18\x03 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12>\n\x16\x65xistence_fusion_param\x18\x04 \x01(\x0b\x32\x1e.apollo.perception.PluginParam')



_PBFTRACKERCONFIG = DESCRIPTOR.message_types_by_name['PbfTrackerConfig']
PbfTrackerConfig = _reflection.GeneratedProtocolMessageType('PbfTrackerConfig', (_message.Message,), {
  'DESCRIPTOR' : _PBFTRACKERCONFIG,
  '__module__' : 'modules.perception.multi_sensor_fusion.proto.pbf_tracker_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.fusion.PbfTrackerConfig)
  })
_sym_db.RegisterMessage(PbfTrackerConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PBFTRACKERCONFIG._serialized_start=152
  _PBFTRACKERCONFIG._serialized_end=414
# @@protoc_insertion_point(module_scope)