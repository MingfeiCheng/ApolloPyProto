# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/camera_detection_bev/proto/camera_detection_bev.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHmodules/perception/camera_detection_bev/proto/camera_detection_bev.proto\x12\x18\x61pollo.perception.camera\x1a\x32modules/perception/common/proto/plugin_param.proto\"\x8a\x02\n\x12\x43\x61meraDetectionBEV\x12\x1e\n\x0b\x63\x61mera_name\x18\x01 \x01(\t:\tfront_6mm\x12\x1b\n\x10timestamp_offset\x18\x02 \x01(\x01:\x01\x30\x12\x34\n\x0cplugin_param\x18\x03 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\"\n\x13\x65nable_undistortion\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x0e\n\x06gpu_id\x18\x05 \x01(\x05\x12;\n\x07\x63hannel\x18\x06 \x01(\x0b\x32*.apollo.perception.camera.DetectionChannel\x12\x10\n\x08\x66rame_id\x18\x07 \x01(\t\"\\\n\x10\x44\x65tectionChannel\x12!\n\x19input_camera_channel_name\x18\x01 \x03(\t\x12%\n\x1doutput_obstacles_channel_name\x18\x02 \x01(\t\"0\n\x05\x44\x65\x62ug\x12\'\n\x1foutput_viz_message_channel_name\x18\x01 \x01(\t')



_CAMERADETECTIONBEV = DESCRIPTOR.message_types_by_name['CameraDetectionBEV']
_DETECTIONCHANNEL = DESCRIPTOR.message_types_by_name['DetectionChannel']
_DEBUG = DESCRIPTOR.message_types_by_name['Debug']
CameraDetectionBEV = _reflection.GeneratedProtocolMessageType('CameraDetectionBEV', (_message.Message,), {
  'DESCRIPTOR' : _CAMERADETECTIONBEV,
  '__module__' : 'modules.perception.camera_detection_bev.proto.camera_detection_bev_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.CameraDetectionBEV)
  })
_sym_db.RegisterMessage(CameraDetectionBEV)

DetectionChannel = _reflection.GeneratedProtocolMessageType('DetectionChannel', (_message.Message,), {
  'DESCRIPTOR' : _DETECTIONCHANNEL,
  '__module__' : 'modules.perception.camera_detection_bev.proto.camera_detection_bev_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.DetectionChannel)
  })
_sym_db.RegisterMessage(DetectionChannel)

Debug = _reflection.GeneratedProtocolMessageType('Debug', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG,
  '__module__' : 'modules.perception.camera_detection_bev.proto.camera_detection_bev_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.Debug)
  })
_sym_db.RegisterMessage(Debug)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CAMERADETECTIONBEV._serialized_start=155
  _CAMERADETECTIONBEV._serialized_end=421
  _DETECTIONCHANNEL._serialized_start=423
  _DETECTIONCHANNEL._serialized_end=515
  _DEBUG._serialized_start=517
  _DEBUG._serialized_end=565
# @@protoc_insertion_point(module_scope)
