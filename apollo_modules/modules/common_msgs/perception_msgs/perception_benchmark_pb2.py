# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/perception_msgs/perception_benchmark.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import error_code_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.perception_msgs import perception_obstacle_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_perception__obstacle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/common_msgs/perception_msgs/perception_benchmark.proto\x12\x11\x61pollo.perception\x1a/modules/common_msgs/basic_msgs/error_code.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a=modules/common_msgs/perception_msgs/perception_obstacle.proto\"R\n\x0fSensorFrameInfo\x12\x11\n\tsensor_id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x19\n\x11sensor2world_pose\x18\x03 \x03(\x01\"\xf6\x01\n\x18PerceptionBenchmarkFrame\x12\x42\n\x13perception_obstacle\x18\x01 \x03(\x0b\x32%.apollo.perception.PerceptionObstacle\x12%\n\x06header\x18\x02 \x01(\x0b\x32\x15.apollo.common.Header\x12\x30\n\nerror_code\x18\x03 \x01(\x0e\x32\x18.apollo.common.ErrorCode:\x02OK\x12=\n\x11sensor_frame_info\x18\x04 \x01(\x0b\x32\".apollo.perception.SensorFrameInfo')



_SENSORFRAMEINFO = DESCRIPTOR.message_types_by_name['SensorFrameInfo']
_PERCEPTIONBENCHMARKFRAME = DESCRIPTOR.message_types_by_name['PerceptionBenchmarkFrame']
SensorFrameInfo = _reflection.GeneratedProtocolMessageType('SensorFrameInfo', (_message.Message,), {
  'DESCRIPTOR' : _SENSORFRAMEINFO,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_benchmark_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.SensorFrameInfo)
  })
_sym_db.RegisterMessage(SensorFrameInfo)

PerceptionBenchmarkFrame = _reflection.GeneratedProtocolMessageType('PerceptionBenchmarkFrame', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONBENCHMARKFRAME,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_benchmark_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.PerceptionBenchmarkFrame)
  })
_sym_db.RegisterMessage(PerceptionBenchmarkFrame)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SENSORFRAMEINFO._serialized_start=242
  _SENSORFRAMEINFO._serialized_end=324
  _PERCEPTIONBENCHMARKFRAME._serialized_start=327
  _PERCEPTIONBENCHMARKFRAME._serialized_end=573
# @@protoc_insertion_point(module_scope)