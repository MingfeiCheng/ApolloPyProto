# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lane_detection/proto/perception.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import plugin_param_pb2 as modules_dot_perception_dot_common_dot_proto_dot_plugin__param__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/perception/lane_detection/proto/perception.proto\x12\x1c\x61pollo.perception.camera.app\x1a\x32modules/perception/common/proto/plugin_param.proto\"Z\n\rDetectorParam\x12\x34\n\x0cplugin_param\x18\x01 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x13\n\x0b\x63\x61mera_name\x18\x02 \x01(\t\"\xd0\x01\n\nDebugParam\x12\x19\n\x11\x64\x65tection_out_dir\x18\x01 \x01(\t\x12!\n\x19tracked_detection_out_dir\x18\x02 \x01(\t\x12\x16\n\x0etrack_out_file\x18\x03 \x01(\t\x12\x1a\n\x12\x64\x65tect_feature_dir\x18\x04 \x01(\t\x12\x14\n\x0clane_out_dir\x18\x05 \x01(\t\x12\x1d\n\x15\x63\x61mera2world_out_file\x18\x06 \x01(\t\x12\x1b\n\x13\x63\x61libration_out_dir\x18\x07 \x01(\t\"\xed\x01\n\x13LanePerceptionParam\x12H\n\x13lane_detector_param\x18\x01 \x01(\x0b\x32+.apollo.perception.camera.app.DetectorParam\x12@\n\x18lane_postprocessor_param\x18\x02 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12:\n\x12lane_tracker_param\x18\x03 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\x12\x0e\n\x06gpu_id\x18\x04 \x01(\x05\"j\n\x17\x43\x61librationServiceParam\x12\x19\n\x11\x63\x61librator_method\x18\x02 \x01(\t\x12\x34\n\x0cplugin_param\x18\x03 \x01(\x0b\x32\x1e.apollo.perception.PluginParam\"\x81\x02\n\x0fPerceptionParam\x12\x0e\n\x06gpu_id\x18\x01 \x01(\x05\x12\x45\n\nlane_param\x18\x02 \x03(\x0b\x32\x31.apollo.perception.camera.app.LanePerceptionParam\x12X\n\x19\x63\x61libration_service_param\x18\x03 \x01(\x0b\x32\x35.apollo.perception.camera.app.CalibrationServiceParam\x12=\n\x0b\x64\x65\x62ug_param\x18\x04 \x01(\x0b\x32(.apollo.perception.camera.app.DebugParam')



_DETECTORPARAM = DESCRIPTOR.message_types_by_name['DetectorParam']
_DEBUGPARAM = DESCRIPTOR.message_types_by_name['DebugParam']
_LANEPERCEPTIONPARAM = DESCRIPTOR.message_types_by_name['LanePerceptionParam']
_CALIBRATIONSERVICEPARAM = DESCRIPTOR.message_types_by_name['CalibrationServiceParam']
_PERCEPTIONPARAM = DESCRIPTOR.message_types_by_name['PerceptionParam']
DetectorParam = _reflection.GeneratedProtocolMessageType('DetectorParam', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.perception_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.app.DetectorParam)
  })
_sym_db.RegisterMessage(DetectorParam)

DebugParam = _reflection.GeneratedProtocolMessageType('DebugParam', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.perception_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.app.DebugParam)
  })
_sym_db.RegisterMessage(DebugParam)

LanePerceptionParam = _reflection.GeneratedProtocolMessageType('LanePerceptionParam', (_message.Message,), {
  'DESCRIPTOR' : _LANEPERCEPTIONPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.perception_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.app.LanePerceptionParam)
  })
_sym_db.RegisterMessage(LanePerceptionParam)

CalibrationServiceParam = _reflection.GeneratedProtocolMessageType('CalibrationServiceParam', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATIONSERVICEPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.perception_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.app.CalibrationServiceParam)
  })
_sym_db.RegisterMessage(CalibrationServiceParam)

PerceptionParam = _reflection.GeneratedProtocolMessageType('PerceptionParam', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.perception_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.app.PerceptionParam)
  })
_sym_db.RegisterMessage(PerceptionParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DETECTORPARAM._serialized_start=142
  _DETECTORPARAM._serialized_end=232
  _DEBUGPARAM._serialized_start=235
  _DEBUGPARAM._serialized_end=443
  _LANEPERCEPTIONPARAM._serialized_start=446
  _LANEPERCEPTIONPARAM._serialized_end=683
  _CALIBRATIONSERVICEPARAM._serialized_start=685
  _CALIBRATIONSERVICEPARAM._serialized_end=791
  _PERCEPTIONPARAM._serialized_start=794
  _PERCEPTIONPARAM._serialized_end=1051
# @@protoc_insertion_point(module_scope)
