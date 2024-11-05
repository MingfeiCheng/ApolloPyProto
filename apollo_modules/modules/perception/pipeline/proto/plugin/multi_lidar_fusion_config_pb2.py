# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/plugin/multi_lidar_fusion_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHmodules/perception/pipeline/proto/plugin/multi_lidar_fusion_config.proto\x12\x17\x61pollo.perception.lidar\"\xc5\x02\n\x11MlfDistanceWeight\x12\x1a\n\x10sensor_name_pair\x18\x01 \x01(\t:\x00\x12\x1f\n\x14location_dist_weight\x18\x02 \x01(\x02:\x01\x30\x12 \n\x15\x64irection_dist_weight\x18\x03 \x01(\x02:\x01\x30\x12 \n\x15\x62\x62ox_size_dist_weight\x18\x04 \x01(\x02:\x01\x30\x12 \n\x15point_num_dist_weight\x18\x05 \x01(\x02:\x01\x30\x12 \n\x15histogram_dist_weight\x18\x06 \x01(\x02:\x01\x30\x12%\n\x1a\x63\x65ntroid_shift_dist_weight\x18\x07 \x01(\x02:\x01\x30\x12\x1f\n\x14\x62\x62ox_iou_dist_weight\x18\x08 \x01(\x02:\x01\x30\x12#\n\x18semantic_map_dist_weight\x18\t \x01(\x02:\x01\x30\"\xa3\x01\n\x11MlfDistanceConfig\x12\x46\n\x12\x66oreground_weights\x18\x01 \x03(\x0b\x32*.apollo.perception.lidar.MlfDistanceWeight\x12\x46\n\x12\x62\x61\x63kground_weights\x18\x02 \x03(\x0b\x32*.apollo.perception.lidar.MlfDistanceWeight\"\xd4\x01\n\x1bMlfTrackObjectMatcherConfig\x12?\n\x19\x66oreground_mathcer_method\x18\x01 \x01(\t:\x1cMultiHmBipartiteGraphMatcher\x12;\n\x19\x62\x61\x63kground_matcher_method\x18\x02 \x01(\t:\x18GnnBipartiteGraphMatcher\x12\x18\n\x0b\x62ound_value\x18\x03 \x01(\x02:\x03\x31\x30\x30\x12\x1d\n\x12max_match_distance\x18\x04 \x01(\x02:\x01\x34\"\'\n\x10MlfTrackerConfig\x12\x13\n\x0b\x66ilter_name\x18\x01 \x03(\t\"\xd2\x03\n\x15MlfMotionFilterConfig\x12\x1a\n\x0cuse_adaptive\x18\x01 \x01(\x08:\x04true\x12\x1b\n\ruse_breakdown\x18\x02 \x01(\x08:\x04true\x12%\n\x17use_convergence_boostup\x18\x03 \x01(\x08:\x04true\x12!\n\x16init_velocity_variance\x18\x04 \x01(\x01:\x01\x35\x12&\n\x1ainit_acceleration_variance\x18\x05 \x01(\x01:\x02\x31\x30\x12\'\n\x1ameasured_velocity_variance\x18\x06 \x01(\x01:\x03\x30.4\x12\'\n\x1bpredict_variance_per_sqrsec\x18\x07 \x01(\x01:\x02\x31\x30\x12\'\n\x1c\x62oostup_history_size_minimum\x18\x08 \x01(\r:\x01\x33\x12\'\n\x1c\x62oostup_history_size_maximum\x18\t \x01(\r:\x01\x36\x12)\n\x1c\x63onverged_confidence_minimum\x18\n \x01(\x01:\x03\x30.5\x12\x1a\n\rnoise_maximum\x18\x0c \x01(\x01:\x03\x30.1\x12#\n\x17trust_orientation_range\x18\r \x01(\x01:\x02\x34\x30\"h\n\x16MlfMotionRefinerConfig\x12*\n\x1e\x63laping_acceleration_threshold\x18\x01 \x01(\x01:\x02\x31\x30\x12\"\n\x17\x63laping_speed_threshold\x18\x02 \x01(\x01:\x01\x31\"m\n\x14MlfShapeFilterConfig\x12+\n\x1e\x62ottom_points_ignore_threshold\x18\x01 \x01(\x01:\x03\x30.1\x12(\n\x1btop_points_ignore_threshold\x18\x02 \x01(\x01:\x03\x31.6')



_MLFDISTANCEWEIGHT = DESCRIPTOR.message_types_by_name['MlfDistanceWeight']
_MLFDISTANCECONFIG = DESCRIPTOR.message_types_by_name['MlfDistanceConfig']
_MLFTRACKOBJECTMATCHERCONFIG = DESCRIPTOR.message_types_by_name['MlfTrackObjectMatcherConfig']
_MLFTRACKERCONFIG = DESCRIPTOR.message_types_by_name['MlfTrackerConfig']
_MLFMOTIONFILTERCONFIG = DESCRIPTOR.message_types_by_name['MlfMotionFilterConfig']
_MLFMOTIONREFINERCONFIG = DESCRIPTOR.message_types_by_name['MlfMotionRefinerConfig']
_MLFSHAPEFILTERCONFIG = DESCRIPTOR.message_types_by_name['MlfShapeFilterConfig']
MlfDistanceWeight = _reflection.GeneratedProtocolMessageType('MlfDistanceWeight', (_message.Message,), {
  'DESCRIPTOR' : _MLFDISTANCEWEIGHT,
  '__module__' : 'modules.perception.pipeline.proto.plugin.multi_lidar_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.MlfDistanceWeight)
  })
_sym_db.RegisterMessage(MlfDistanceWeight)

MlfDistanceConfig = _reflection.GeneratedProtocolMessageType('MlfDistanceConfig', (_message.Message,), {
  'DESCRIPTOR' : _MLFDISTANCECONFIG,
  '__module__' : 'modules.perception.pipeline.proto.plugin.multi_lidar_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.MlfDistanceConfig)
  })
_sym_db.RegisterMessage(MlfDistanceConfig)

MlfTrackObjectMatcherConfig = _reflection.GeneratedProtocolMessageType('MlfTrackObjectMatcherConfig', (_message.Message,), {
  'DESCRIPTOR' : _MLFTRACKOBJECTMATCHERCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.plugin.multi_lidar_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.MlfTrackObjectMatcherConfig)
  })
_sym_db.RegisterMessage(MlfTrackObjectMatcherConfig)

MlfTrackerConfig = _reflection.GeneratedProtocolMessageType('MlfTrackerConfig', (_message.Message,), {
  'DESCRIPTOR' : _MLFTRACKERCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.plugin.multi_lidar_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.MlfTrackerConfig)
  })
_sym_db.RegisterMessage(MlfTrackerConfig)

MlfMotionFilterConfig = _reflection.GeneratedProtocolMessageType('MlfMotionFilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _MLFMOTIONFILTERCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.plugin.multi_lidar_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.MlfMotionFilterConfig)
  })
_sym_db.RegisterMessage(MlfMotionFilterConfig)

MlfMotionRefinerConfig = _reflection.GeneratedProtocolMessageType('MlfMotionRefinerConfig', (_message.Message,), {
  'DESCRIPTOR' : _MLFMOTIONREFINERCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.plugin.multi_lidar_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.MlfMotionRefinerConfig)
  })
_sym_db.RegisterMessage(MlfMotionRefinerConfig)

MlfShapeFilterConfig = _reflection.GeneratedProtocolMessageType('MlfShapeFilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _MLFSHAPEFILTERCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.plugin.multi_lidar_fusion_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.MlfShapeFilterConfig)
  })
_sym_db.RegisterMessage(MlfShapeFilterConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MLFDISTANCEWEIGHT._serialized_start=102
  _MLFDISTANCEWEIGHT._serialized_end=427
  _MLFDISTANCECONFIG._serialized_start=430
  _MLFDISTANCECONFIG._serialized_end=593
  _MLFTRACKOBJECTMATCHERCONFIG._serialized_start=596
  _MLFTRACKOBJECTMATCHERCONFIG._serialized_end=808
  _MLFTRACKERCONFIG._serialized_start=810
  _MLFTRACKERCONFIG._serialized_end=849
  _MLFMOTIONFILTERCONFIG._serialized_start=852
  _MLFMOTIONFILTERCONFIG._serialized_end=1318
  _MLFMOTIONREFINERCONFIG._serialized_start=1320
  _MLFMOTIONREFINERCONFIG._serialized_end=1424
  _MLFSHAPEFILTERCONFIG._serialized_start=1426
  _MLFSHAPEFILTERCONFIG._serialized_end=1535
# @@protoc_insertion_point(module_scope)
