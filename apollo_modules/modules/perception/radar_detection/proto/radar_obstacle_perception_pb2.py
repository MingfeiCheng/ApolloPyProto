# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/radar_detection/proto/radar_obstacle_perception.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHmodules/perception/radar_detection/proto/radar_obstacle_perception.proto\x12\x17\x61pollo.perception.radar\x1a\x32modules/perception/common/proto/plugin_param.proto\"\xc8\x01\n\x1dRadarObstaclePerceptionConfig\x12\x36\n\x0e\x64\x65tector_param\x18\x01 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x38\n\x10roi_filter_param\x18\x02 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x35\n\rtracker_param\x18\x03 \x01(\x0b\x32\x1e.apollo.perception.PluginParam')



_RADAROBSTACLEPERCEPTIONCONFIG = DESCRIPTOR.message_types_by_name['RadarObstaclePerceptionConfig']
RadarObstaclePerceptionConfig = _reflection.GeneratedProtocolMessageType('RadarObstaclePerceptionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RADAROBSTACLEPERCEPTIONCONFIG,
  '__module__' : 'modules.perception.radar_detection.proto.radar_obstacle_perception_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar.RadarObstaclePerceptionConfig)
  })
_sym_db.RegisterMessage(RadarObstaclePerceptionConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RADAROBSTACLEPERCEPTIONCONFIG._serialized_start=154
  _RADAROBSTACLEPERCEPTIONCONFIG._serialized_end=354
# @@protoc_insertion_point(module_scope)
