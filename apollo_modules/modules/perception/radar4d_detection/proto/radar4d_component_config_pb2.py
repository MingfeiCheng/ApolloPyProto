# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/radar4d_detection/proto/radar4d_component_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nImodules/perception/radar4d_detection/proto/radar4d_component_config.proto\x12\x19\x61pollo.perception.radar4d\x1a\x32modules/perception/common/proto/plugin_param.proto\"\x99\x02\n\x16Radar4dDetectionConfig\x12\x12\n\nradar_name\x18\x01 \x01(\t\x12\x19\n\x11tf_child_frame_id\x18\x02 \x01(\t\x12\x1e\n\x16radar_forward_distance\x18\x03 \x01(\x01\x12:\n\x12preprocessor_param\x18\x04 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x38\n\x10perception_param\x18\x05 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x1d\n\x15odometry_channel_name\x18\x07 \x01(\t\x12\x1b\n\x13output_channel_name\x18\x08 \x01(\t')



_RADAR4DDETECTIONCONFIG = DESCRIPTOR.message_types_by_name['Radar4dDetectionConfig']
Radar4dDetectionConfig = _reflection.GeneratedProtocolMessageType('Radar4dDetectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RADAR4DDETECTIONCONFIG,
  '__module__' : 'modules.perception.radar4d_detection.proto.radar4d_component_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.Radar4dDetectionConfig)
  })
_sym_db.RegisterMessage(Radar4dDetectionConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RADAR4DDETECTIONCONFIG._serialized_start=157
  _RADAR4DDETECTIONCONFIG._serialized_end=438
# @@protoc_insertion_point(module_scope)
