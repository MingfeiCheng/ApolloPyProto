# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/stage/all_latest_fusion_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFmodules/perception/pipeline/proto/stage/all_latest_fusion_config.proto\x12\x18\x61pollo.perception.fusion\"x\n\x15\x41llLatestFusionConfig\x12\x13\n\x0bmain_sensor\x18\x01 \x01(\t\x12\x17\n\tuse_lidar\x18\x02 \x01(\x08:\x04true\x12\x17\n\tuse_radar\x18\x03 \x01(\x08:\x04true\x12\x18\n\nuse_camera\x18\x04 \x01(\x08:\x04true')



_ALLLATESTFUSIONCONFIG = DESCRIPTOR.message_types_by_name['AllLatestFusionConfig']
AllLatestFusionConfig = _reflection.GeneratedProtocolMessageType('AllLatestFusionConfig', (_message.Message,), {
  'DESCRIPTOR' : _ALLLATESTFUSIONCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.stage.all_latest_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.fusion.AllLatestFusionConfig)
  })
_sym_db.RegisterMessage(AllLatestFusionConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALLLATESTFUSIONCONFIG._serialized_start=100
  _ALLLATESTFUSIONCONFIG._serialized_end=220
# @@protoc_insertion_point(module_scope)
