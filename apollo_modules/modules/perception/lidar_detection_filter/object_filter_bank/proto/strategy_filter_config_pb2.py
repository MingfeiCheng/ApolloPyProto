# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar_detection_filter/object_filter_bank/proto/strategy_filter_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n_modules/perception/lidar_detection_filter/object_filter_bank/proto/strategy_filter_config.proto\x12\x17\x61pollo.perception.lidar\"w\n\x14StrategyFilterConfig\x12 \n\x12is_merge_inclusive\x18\x01 \x01(\x08:\x04true\x12\x1d\n\x10\x65xpand_bbox_dist\x18\x02 \x01(\x02:\x03\x30.2\x12\x1e\n\x10\x61llow_fore_merge\x18\x03 \x01(\x08:\x04true')



_STRATEGYFILTERCONFIG = DESCRIPTOR.message_types_by_name['StrategyFilterConfig']
StrategyFilterConfig = _reflection.GeneratedProtocolMessageType('StrategyFilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _STRATEGYFILTERCONFIG,
  '__module__' : 'modules.perception.lidar_detection_filter.object_filter_bank.proto.strategy_filter_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.StrategyFilterConfig)
  })
_sym_db.RegisterMessage(StrategyFilterConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STRATEGYFILTERCONFIG._serialized_start=124
  _STRATEGYFILTERCONFIG._serialized_end=243
# @@protoc_insertion_point(module_scope)
