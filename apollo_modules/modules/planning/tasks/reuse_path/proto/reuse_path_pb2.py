# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/tasks/reuse_path/proto/reuse_path.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.planning.planning_base.proto import piecewise_jerk_path_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_piecewise__jerk__path__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/planning/tasks/reuse_path/proto/reuse_path.proto\x12\x0f\x61pollo.planning\x1a\x45modules/planning/planning_base/proto/piecewise_jerk_path_config.proto\"]\n\x0fReusePathConfig\x12(\n enable_reuse_path_in_lane_follow\x18\x01 \x01(\x08\x12 \n\x14short_path_threshold\x18\x02 \x01(\r:\x02\x36\x30')



_REUSEPATHCONFIG = DESCRIPTOR.message_types_by_name['ReusePathConfig']
ReusePathConfig = _reflection.GeneratedProtocolMessageType('ReusePathConfig', (_message.Message,), {
  'DESCRIPTOR' : _REUSEPATHCONFIG,
  '__module__' : 'modules.planning.tasks.reuse_path.proto.reuse_path_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ReusePathConfig)
  })
_sym_db.RegisterMessage(ReusePathConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REUSEPATHCONFIG._serialized_start=148
  _REUSEPATHCONFIG._serialized_end=241
# @@protoc_insertion_point(module_scope)
