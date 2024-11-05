# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lane_detection/proto/lane_perception_component.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGmodules/perception/lane_detection/proto/lane_perception_component.proto\x12\x19\x61pollo.perception.onboard\x1a\x32modules/perception/common/proto/plugin_param.proto\"\xcc\x06\n\rLaneDetection\x12*\n\x0c\x63\x61mera_names\x18\x01 \x01(\t:\x14\x66ront_6mm,front_12mm\x12p\n\x1ainput_camera_channel_names\x18\x02 \x01(\t:L/apollo/sensor/camera/front_6mm/image,/apollo/sensor/camera/front_12mm/image\x12\x1b\n\x10timestamp_offset\x18\x03 \x01(\x01:\x01\x30\x12\x37\n\x0f\x64\x65tection_param\x18\x04 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x1a\n\x0e\x66rame_capacity\x18\x05 \x01(\x05:\x02\x32\x30\x12\x1c\n\x11image_channel_num\x18\x06 \x01(\x05:\x01\x33\x12\"\n\x13\x65nable_undistortion\x18\x07 \x01(\x08:\x05\x66\x61lse\x12#\n\x14\x65nable_visualization\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x34\n\x19output_lanes_channel_name\x18\t \x01(\t:\x11/perception/lanes\x12\x1f\n\x14\x64\x65\x66\x61ult_camera_pitch\x18\n \x01(\x01:\x01\x30\x12\"\n\x15\x64\x65\x66\x61ult_camera_height\x18\x0b \x01(\x01:\x03\x31.5\x12\x37\n$lane_calibration_working_sensor_name\x18\x0c \x01(\t:\tfront_6mm\x12-\n\x11\x63\x61librator_method\x18\r \x01(\t:\x12LaneLineCalibrator\x12\x34\n\x12\x63\x61lib_service_name\x18\x0e \x01(\t:\x18OnlineCalibrationService\x12\x1f\n\x11run_calib_service\x18\x0f \x01(\x08:\x04true\x12\x14\n\x07ts_diff\x18\x10 \x01(\x01:\x03\x30.1\x12\x31\n\x13visual_debug_folder\x18\x11 \x01(\t:\x14/apollo/debug_output\x12 \n\rvisual_camera\x18\x12 \x01(\t:\tfront_6mm\x12\x1f\n\x10write_visual_img\x18\x13 \x01(\x08:\x05\x66\x61lse')



_LANEDETECTION = DESCRIPTOR.message_types_by_name['LaneDetection']
LaneDetection = _reflection.GeneratedProtocolMessageType('LaneDetection', (_message.Message,), {
  'DESCRIPTOR' : _LANEDETECTION,
  '__module__' : 'modules.perception.lane_detection.proto.lane_perception_component_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.onboard.LaneDetection)
  })
_sym_db.RegisterMessage(LaneDetection)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LANEDETECTION._serialized_start=155
  _LANEDETECTION._serialized_end=999
# @@protoc_insertion_point(module_scope)
