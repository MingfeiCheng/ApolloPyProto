# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pointcloud_ground_detection/ground_detector/proto/ground_service_detector_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nimodules/perception/pointcloud_ground_detection/ground_detector/proto/ground_service_detector_config.proto\x12\x17\x61pollo.perception.lidar\"=\n\x1bGroundServiceDetectorConfig\x12\x1e\n\x10ground_threshold\x18\x01 \x01(\x01:\x04\x30.25')



_GROUNDSERVICEDETECTORCONFIG = DESCRIPTOR.message_types_by_name['GroundServiceDetectorConfig']
GroundServiceDetectorConfig = _reflection.GeneratedProtocolMessageType('GroundServiceDetectorConfig', (_message.Message,), {
  'DESCRIPTOR' : _GROUNDSERVICEDETECTORCONFIG,
  '__module__' : 'modules.perception.pointcloud_ground_detection.ground_detector.proto.ground_service_detector_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.GroundServiceDetectorConfig)
  })
_sym_db.RegisterMessage(GroundServiceDetectorConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GROUNDSERVICEDETECTORCONFIG._serialized_start=134
  _GROUNDSERVICEDETECTORCONFIG._serialized_end=195
# @@protoc_insertion_point(module_scope)
