# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lane_detection/proto/darkSCNN_postprocessor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDmodules/perception/lane_detection/proto/darkSCNN_postprocessor.proto\x12\x1d\x61pollo.perception.camera.lane\"\x92\x02\n\x1e\x44\x61rkSCNNLanePostprocessorParam\x12\x1b\n\x0elane_map_width\x18\x01 \x01(\r:\x03\x36\x34\x30\x12\x1c\n\x0flane_map_height\x18\x02 \x01(\r:\x03\x34\x38\x30\x12\x17\n\nroi_height\x18\x03 \x01(\r:\x03\x37\x36\x38\x12\x16\n\troi_start\x18\x04 \x01(\r:\x03\x33\x31\x32\x12\x17\n\troi_width\x18\x05 \x01(\r:\x04\x31\x39\x32\x30\x12\x19\n\x0einput_offset_x\x18\x06 \x01(\r:\x01\x30\x12\x19\n\x0einput_offset_y\x18\x07 \x01(\r:\x01\x30\x12\x19\n\x0cresize_width\x18\x08 \x01(\r:\x03\x35\x31\x32\x12\x1a\n\rresize_height\x18\t \x01(\r:\x03\x35\x31\x32')



_DARKSCNNLANEPOSTPROCESSORPARAM = DESCRIPTOR.message_types_by_name['DarkSCNNLanePostprocessorParam']
DarkSCNNLanePostprocessorParam = _reflection.GeneratedProtocolMessageType('DarkSCNNLanePostprocessorParam', (_message.Message,), {
  'DESCRIPTOR' : _DARKSCNNLANEPOSTPROCESSORPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.darkSCNN_postprocessor_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.lane.DarkSCNNLanePostprocessorParam)
  })
_sym_db.RegisterMessage(DarkSCNNLanePostprocessorParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DARKSCNNLANEPOSTPROCESSORPARAM._serialized_start=104
  _DARKSCNNLANEPOSTPROCESSORPARAM._serialized_end=378
# @@protoc_insertion_point(module_scope)