# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/tasks/fallback_path/proto/fallback_path.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.planning.planning_base.proto import piecewise_jerk_path_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_piecewise__jerk__path__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/planning/tasks/fallback_path/proto/fallback_path.proto\x12\x0f\x61pollo.planning\x1a\x45modules/planning/planning_base/proto/piecewise_jerk_path_config.proto\"\xa2\x01\n\x12\x46\x61llbackPathConfig\x12,\n$is_extend_lane_bounds_to_include_adc\x18\x01 \x01(\x08\x12\x15\n\rextend_buffer\x18\x02 \x01(\x01\x12G\n\x15path_optimizer_config\x18\x03 \x01(\x0b\x32(.apollo.planning.PiecewiseJerkPathConfig')



_FALLBACKPATHCONFIG = DESCRIPTOR.message_types_by_name['FallbackPathConfig']
FallbackPathConfig = _reflection.GeneratedProtocolMessageType('FallbackPathConfig', (_message.Message,), {
  'DESCRIPTOR' : _FALLBACKPATHCONFIG,
  '__module__' : 'modules.planning.tasks.fallback_path.proto.fallback_path_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.FallbackPathConfig)
  })
_sym_db.RegisterMessage(FallbackPathConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FALLBACKPATHCONFIG._serialized_start=155
  _FALLBACKPATHCONFIG._serialized_end=317
# @@protoc_insertion_point(module_scope)