# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar_output/proto/lidar_output_component_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nImodules/perception/lidar_output/proto/lidar_output_component_config.proto\x12\x17\x61pollo.perception.lidar\"\x84\x01\n\x1aLidarOutputComponentConfig\x12\x1b\n\x13output_channel_name\x18\x01 \x01(\t\x12#\n\x14save_benchmark_frame\x18\x02 \x01(\x08:\x05\x66\x61lse\x12$\n\x1a\x62\x65nchmark_frame_output_dir\x18\x03 \x01(\t:\x00')



_LIDAROUTPUTCOMPONENTCONFIG = DESCRIPTOR.message_types_by_name['LidarOutputComponentConfig']
LidarOutputComponentConfig = _reflection.GeneratedProtocolMessageType('LidarOutputComponentConfig', (_message.Message,), {
  'DESCRIPTOR' : _LIDAROUTPUTCOMPONENTCONFIG,
  '__module__' : 'modules.perception.lidar_output.proto.lidar_output_component_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.LidarOutputComponentConfig)
  })
_sym_db.RegisterMessage(LidarOutputComponentConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIDAROUTPUTCOMPONENTCONFIG._serialized_start=103
  _LIDAROUTPUTCOMPONENTCONFIG._serialized_end=235
# @@protoc_insertion_point(module_scope)