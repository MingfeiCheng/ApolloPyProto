# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/radar4d_detection/proto/radar_obstacle_perception_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nQmodules/perception/radar4d_detection/proto/radar_obstacle_perception_config.proto\x12\x19\x61pollo.perception.radar4d\x1a\x32modules/perception/common/proto/plugin_param.proto\"\xb8\x02\n\x1dRadarObstaclePerceptionConfig\x12\x36\n\x0e\x64\x65tector_param\x18\x01 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x38\n\x10roi_filter_param\x18\x02 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x42\n\x1amulti_target_tracker_param\x18\x03 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12?\n\x17\x66usion_classifier_param\x18\x04 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12 \n\x11\x65nable_roi_filter\x18\x05 \x01(\x08:\x05\x66\x61lse')



_RADAROBSTACLEPERCEPTIONCONFIG = DESCRIPTOR.message_types_by_name['RadarObstaclePerceptionConfig']
RadarObstaclePerceptionConfig = _reflection.GeneratedProtocolMessageType('RadarObstaclePerceptionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RADAROBSTACLEPERCEPTIONCONFIG,
  '__module__' : 'modules.perception.radar4d_detection.proto.radar_obstacle_perception_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.RadarObstaclePerceptionConfig)
  })
_sym_db.RegisterMessage(RadarObstaclePerceptionConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RADAROBSTACLEPERCEPTIONCONFIG._serialized_start=165
  _RADAROBSTACLEPERCEPTIONCONFIG._serialized_end=477
# @@protoc_insertion_point(module_scope)