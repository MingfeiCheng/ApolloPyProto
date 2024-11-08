# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/radar4d_detection/lib/tracker/multi_radar_fusion/proto/mrf_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nZmodules/perception/radar4d_detection/lib/tracker/multi_radar_fusion/proto/mrf_config.proto\x12\x19\x61pollo.perception.radar4d\"\xc5\x02\n\x11MrfDistanceWeight\x12\x1a\n\x10sensor_name_pair\x18\x01 \x01(\t:\x00\x12\x1f\n\x14location_dist_weight\x18\x02 \x01(\x02:\x01\x30\x12 \n\x15\x64irection_dist_weight\x18\x03 \x01(\x02:\x01\x30\x12 \n\x15\x62\x62ox_size_dist_weight\x18\x04 \x01(\x02:\x01\x30\x12 \n\x15point_num_dist_weight\x18\x05 \x01(\x02:\x01\x30\x12 \n\x15histogram_dist_weight\x18\x06 \x01(\x02:\x01\x30\x12%\n\x1a\x63\x65ntroid_shift_dist_weight\x18\x07 \x01(\x02:\x01\x30\x12\x1f\n\x14\x62\x62ox_iou_dist_weight\x18\x08 \x01(\x02:\x01\x30\x12#\n\x18semantic_map_dist_weight\x18\t \x01(\x02:\x01\x30\"\xa7\x01\n\x11MrfDistanceConfig\x12H\n\x12\x66oreground_weights\x18\x01 \x03(\x0b\x32,.apollo.perception.radar4d.MrfDistanceWeight\x12H\n\x12\x62\x61\x63kground_weights\x18\x02 \x03(\x0b\x32,.apollo.perception.radar4d.MrfDistanceWeight\"\xd4\x01\n\x1bMrfTrackObjectMatcherConfig\x12?\n\x19\x66oreground_mathcer_method\x18\x01 \x01(\t:\x1cMultiHmBipartiteGraphMatcher\x12;\n\x19\x62\x61\x63kground_matcher_method\x18\x02 \x01(\t:\x18GnnBipartiteGraphMatcher\x12\x18\n\x0b\x62ound_value\x18\x03 \x01(\x02:\x03\x31\x30\x30\x12\x1d\n\x12max_match_distance\x18\x04 \x01(\x02:\x01\x34\"\'\n\x10MrfTrackerConfig\x12\x13\n\x0b\x66ilter_name\x18\x01 \x03(\t\"\xd2\x03\n\x15MrfMotionFilterConfig\x12\x1a\n\x0cuse_adaptive\x18\x01 \x01(\x08:\x04true\x12\x1b\n\ruse_breakdown\x18\x02 \x01(\x08:\x04true\x12%\n\x17use_convergence_boostup\x18\x03 \x01(\x08:\x04true\x12!\n\x16init_velocity_variance\x18\x04 \x01(\x01:\x01\x35\x12&\n\x1ainit_acceleration_variance\x18\x05 \x01(\x01:\x02\x31\x30\x12\'\n\x1ameasured_velocity_variance\x18\x06 \x01(\x01:\x03\x30.4\x12\'\n\x1bpredict_variance_per_sqrsec\x18\x07 \x01(\x01:\x02\x31\x30\x12\'\n\x1c\x62oostup_history_size_minimum\x18\x08 \x01(\r:\x01\x33\x12\'\n\x1c\x62oostup_history_size_maximum\x18\t \x01(\r:\x01\x36\x12)\n\x1c\x63onverged_confidence_minimum\x18\n \x01(\x01:\x03\x30.5\x12\x1a\n\rnoise_maximum\x18\x0c \x01(\x01:\x03\x30.1\x12#\n\x17trust_orientation_range\x18\r \x01(\x01:\x02\x34\x30\"h\n\x16MrfMotionRefinerConfig\x12*\n\x1e\x63laping_acceleration_threshold\x18\x01 \x01(\x01:\x02\x31\x30\x12\"\n\x17\x63laping_speed_threshold\x18\x02 \x01(\x01:\x01\x31\"m\n\x14MrfShapeFilterConfig\x12+\n\x1e\x62ottom_points_ignore_threshold\x18\x01 \x01(\x01:\x03\x30.1\x12(\n\x1btop_points_ignore_threshold\x18\x02 \x01(\x01:\x03\x31.6\"\xde\x01\n\x0fMrfEngineConfig\x12\x13\n\x0bmain_sensor\x18\x01 \x03(\t\x12%\n\x17use_histogram_for_match\x18\x02 \x01(\x08:\x04true\x12\x1e\n\x12histogram_bin_size\x18\x03 \x01(\r:\x02\x31\x30\x12%\n\x16output_predict_objects\x18\x04 \x01(\x08:\x05\x66\x61lse\x12$\n\x17reserved_invisible_time\x18\x05 \x01(\x01:\x03\x30.2\x12\"\n\x13use_frame_timestamp\x18\x06 \x01(\x08:\x05\x66\x61lse')



_MRFDISTANCEWEIGHT = DESCRIPTOR.message_types_by_name['MrfDistanceWeight']
_MRFDISTANCECONFIG = DESCRIPTOR.message_types_by_name['MrfDistanceConfig']
_MRFTRACKOBJECTMATCHERCONFIG = DESCRIPTOR.message_types_by_name['MrfTrackObjectMatcherConfig']
_MRFTRACKERCONFIG = DESCRIPTOR.message_types_by_name['MrfTrackerConfig']
_MRFMOTIONFILTERCONFIG = DESCRIPTOR.message_types_by_name['MrfMotionFilterConfig']
_MRFMOTIONREFINERCONFIG = DESCRIPTOR.message_types_by_name['MrfMotionRefinerConfig']
_MRFSHAPEFILTERCONFIG = DESCRIPTOR.message_types_by_name['MrfShapeFilterConfig']
_MRFENGINECONFIG = DESCRIPTOR.message_types_by_name['MrfEngineConfig']
MrfDistanceWeight = _reflection.GeneratedProtocolMessageType('MrfDistanceWeight', (_message.Message,), {
  'DESCRIPTOR' : _MRFDISTANCEWEIGHT,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfDistanceWeight)
  })
_sym_db.RegisterMessage(MrfDistanceWeight)

MrfDistanceConfig = _reflection.GeneratedProtocolMessageType('MrfDistanceConfig', (_message.Message,), {
  'DESCRIPTOR' : _MRFDISTANCECONFIG,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfDistanceConfig)
  })
_sym_db.RegisterMessage(MrfDistanceConfig)

MrfTrackObjectMatcherConfig = _reflection.GeneratedProtocolMessageType('MrfTrackObjectMatcherConfig', (_message.Message,), {
  'DESCRIPTOR' : _MRFTRACKOBJECTMATCHERCONFIG,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfTrackObjectMatcherConfig)
  })
_sym_db.RegisterMessage(MrfTrackObjectMatcherConfig)

MrfTrackerConfig = _reflection.GeneratedProtocolMessageType('MrfTrackerConfig', (_message.Message,), {
  'DESCRIPTOR' : _MRFTRACKERCONFIG,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfTrackerConfig)
  })
_sym_db.RegisterMessage(MrfTrackerConfig)

MrfMotionFilterConfig = _reflection.GeneratedProtocolMessageType('MrfMotionFilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _MRFMOTIONFILTERCONFIG,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfMotionFilterConfig)
  })
_sym_db.RegisterMessage(MrfMotionFilterConfig)

MrfMotionRefinerConfig = _reflection.GeneratedProtocolMessageType('MrfMotionRefinerConfig', (_message.Message,), {
  'DESCRIPTOR' : _MRFMOTIONREFINERCONFIG,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfMotionRefinerConfig)
  })
_sym_db.RegisterMessage(MrfMotionRefinerConfig)

MrfShapeFilterConfig = _reflection.GeneratedProtocolMessageType('MrfShapeFilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _MRFSHAPEFILTERCONFIG,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfShapeFilterConfig)
  })
_sym_db.RegisterMessage(MrfShapeFilterConfig)

MrfEngineConfig = _reflection.GeneratedProtocolMessageType('MrfEngineConfig', (_message.Message,), {
  'DESCRIPTOR' : _MRFENGINECONFIG,
  '__module__' : 'modules.perception.radar4d_detection.lib.tracker.multi_radar_fusion.proto.mrf_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.MrfEngineConfig)
  })
_sym_db.RegisterMessage(MrfEngineConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MRFDISTANCEWEIGHT._serialized_start=122
  _MRFDISTANCEWEIGHT._serialized_end=447
  _MRFDISTANCECONFIG._serialized_start=450
  _MRFDISTANCECONFIG._serialized_end=617
  _MRFTRACKOBJECTMATCHERCONFIG._serialized_start=620
  _MRFTRACKOBJECTMATCHERCONFIG._serialized_end=832
  _MRFTRACKERCONFIG._serialized_start=834
  _MRFTRACKERCONFIG._serialized_end=873
  _MRFMOTIONFILTERCONFIG._serialized_start=876
  _MRFMOTIONFILTERCONFIG._serialized_end=1342
  _MRFMOTIONREFINERCONFIG._serialized_start=1344
  _MRFMOTIONREFINERCONFIG._serialized_end=1448
  _MRFSHAPEFILTERCONFIG._serialized_start=1450
  _MRFSHAPEFILTERCONFIG._serialized_end=1559
  _MRFENGINECONFIG._serialized_start=1562
  _MRFENGINECONFIG._serialized_end=1784
# @@protoc_insertion_point(module_scope)
