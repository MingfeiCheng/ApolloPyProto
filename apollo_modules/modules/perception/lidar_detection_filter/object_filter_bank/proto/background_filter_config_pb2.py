# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar_detection_filter/object_filter_bank/proto/background_filter_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\namodules/perception/lidar_detection_filter/object_filter_bank/proto/background_filter_config.proto\x12\x17\x61pollo.perception.lidar\"@\n\x16\x42\x61\x63kgroundFilterConfig\x12&\n\x1boutside_roi_filter_distance\x18\x01 \x01(\x01:\x01\x30')



_BACKGROUNDFILTERCONFIG = DESCRIPTOR.message_types_by_name['BackgroundFilterConfig']
BackgroundFilterConfig = _reflection.GeneratedProtocolMessageType('BackgroundFilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _BACKGROUNDFILTERCONFIG,
  '__module__' : 'modules.perception.lidar_detection_filter.object_filter_bank.proto.background_filter_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.BackgroundFilterConfig)
  })
_sym_db.RegisterMessage(BackgroundFilterConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BACKGROUNDFILTERCONFIG._serialized_start=126
  _BACKGROUNDFILTERCONFIG._serialized_end=190
# @@protoc_insertion_point(module_scope)
