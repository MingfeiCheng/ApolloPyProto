# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/perception_msgs/perception_lane.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.perception_msgs import perception_camera_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_perception__camera__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/common_msgs/perception_msgs/perception_lane.proto\x12\x11\x61pollo.perception\x1a+modules/common_msgs/basic_msgs/header.proto\x1a;modules/common_msgs/perception_msgs/perception_camera.proto\"\xa3\x02\n\x0fPerceptionLanes\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x14\n\x0csource_topic\x18\x02 \x01(\t\x12I\n\nerror_code\x18\x03 \x01(\x0e\x32).apollo.perception.camera.CameraErrorCode:\nERROR_NONE\x12\x45\n\x11\x63\x61mera_calibrator\x18\x04 \x01(\x0b\x32*.apollo.perception.camera.CameraCalibrator\x12\x41\n\x0f\x63\x61mera_laneline\x18\x05 \x03(\x0b\x32(.apollo.perception.camera.CameraLaneLine')



_PERCEPTIONLANES = DESCRIPTOR.message_types_by_name['PerceptionLanes']
PerceptionLanes = _reflection.GeneratedProtocolMessageType('PerceptionLanes', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONLANES,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_lane_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.PerceptionLanes)
  })
_sym_db.RegisterMessage(PerceptionLanes)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERCEPTIONLANES._serialized_start=187
  _PERCEPTIONLANES._serialized_end=478
# @@protoc_insertion_point(module_scope)
