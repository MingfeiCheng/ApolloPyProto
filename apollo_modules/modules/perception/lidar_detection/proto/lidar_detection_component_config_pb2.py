# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar_detection/proto/lidar_detection_component_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOmodules/perception/lidar_detection/proto/lidar_detection_component_config.proto\x12\x17\x61pollo.perception.lidar\x1a\x32modules/perception/common/proto/plugin_param.proto\"\xb5\x01\n\x1dLidarDetectionComponentConfig\x12\x1b\n\x13output_channel_name\x18\x01 \x01(\t\x12\x13\n\x0bsensor_name\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x03 \x01(\t\x12\x1a\n\x12use_object_builder\x18\x04 \x01(\x08\x12\x34\n\x0cplugin_param\x18\x05 \x01(\x0b\x32\x1e.apollo.perception.PluginParam')



_LIDARDETECTIONCOMPONENTCONFIG = DESCRIPTOR.message_types_by_name['LidarDetectionComponentConfig']
LidarDetectionComponentConfig = _reflection.GeneratedProtocolMessageType('LidarDetectionComponentConfig', (_message.Message,), {
  'DESCRIPTOR' : _LIDARDETECTIONCOMPONENTCONFIG,
  '__module__' : 'modules.perception.lidar_detection.proto.lidar_detection_component_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.LidarDetectionComponentConfig)
  })
_sym_db.RegisterMessage(LidarDetectionComponentConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIDARDETECTIONCOMPONENTCONFIG._serialized_start=161
  _LIDARDETECTIONCOMPONENTCONFIG._serialized_end=342
# @@protoc_insertion_point(module_scope)
