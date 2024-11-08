# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/camera_tracking/proto/tracking_feature.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?modules/perception/camera_tracking/proto/tracking_feature.proto\x12)apollo.perception.camera.tracking_feature\"\xbb\x01\n\x0c\x46\x65\x61tureParam\x12\x17\n\x0b\x66\x65\x61t_stride\x18\x01 \x01(\x05:\x02\x33\x32\x12L\n\textractor\x18\x02 \x03(\x0b\x32\x39.apollo.perception.camera.tracking_feature.ExtractorParam\x12\x13\n\x0bremap_model\x18\x03 \x01(\t\x12\x16\n\x0e\x66\x65\x61t_blob_name\x18\x04 \x01(\t\x12\x17\n\x0f\x66\x65\x61t_blob_shape\x18\x05 \x03(\x05\"\xdb\x02\n\x0e\x45xtractorParam\x12\x11\n\tfeat_blob\x18\x01 \x01(\t\x12\x64\n\tfeat_type\x18\x02 \x01(\x0e\x32\x45.apollo.perception.camera.tracking_feature.ExtractorParam.FeatureType:\nROIPooling\x12U\n\x11roi_pooling_param\x18\x03 \x01(\x0b\x32:.apollo.perception.camera.tracking_feature.ROIPoolingParam\x12Z\n\x14ps_roi_pooling_param\x18\x04 \x01(\x0b\x32<.apollo.perception.camera.tracking_feature.PSROIPoolingParam\"\x1d\n\x0b\x46\x65\x61tureType\x12\x0e\n\nROIPooling\x10\x00\"U\n\x0fROIPoolingParam\x12\x13\n\x08pooled_h\x18\x01 \x01(\x05:\x01\x33\x12\x13\n\x08pooled_w\x18\x02 \x01(\x05:\x01\x33\x12\x18\n\tuse_floor\x18\x03 \x01(\x08:\x05\x66\x61lse\"\xc3\x01\n\x11PSROIPoolingParam\x12\x16\n\nheat_map_a\x18\x01 \x01(\x05:\x02\x31\x36\x12\x16\n\noutput_dim\x18\x02 \x01(\x05:\x02\x31\x30\x12\x17\n\x0cgroup_height\x18\x03 \x01(\x05:\x01\x37\x12\x16\n\x0bgroup_width\x18\x04 \x01(\x05:\x01\x37\x12\x18\n\rpooled_height\x18\x05 \x01(\x05:\x01\x37\x12\x17\n\x0cpooled_width\x18\x06 \x01(\x05:\x01\x37\x12\x1a\n\x0fsample_per_part\x18\x07 \x01(\x05:\x01\x34')



_FEATUREPARAM = DESCRIPTOR.message_types_by_name['FeatureParam']
_EXTRACTORPARAM = DESCRIPTOR.message_types_by_name['ExtractorParam']
_ROIPOOLINGPARAM = DESCRIPTOR.message_types_by_name['ROIPoolingParam']
_PSROIPOOLINGPARAM = DESCRIPTOR.message_types_by_name['PSROIPoolingParam']
_EXTRACTORPARAM_FEATURETYPE = _EXTRACTORPARAM.enum_types_by_name['FeatureType']
FeatureParam = _reflection.GeneratedProtocolMessageType('FeatureParam', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREPARAM,
  '__module__' : 'modules.perception.camera_tracking.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.tracking_feature.FeatureParam)
  })
_sym_db.RegisterMessage(FeatureParam)

ExtractorParam = _reflection.GeneratedProtocolMessageType('ExtractorParam', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTORPARAM,
  '__module__' : 'modules.perception.camera_tracking.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.tracking_feature.ExtractorParam)
  })
_sym_db.RegisterMessage(ExtractorParam)

ROIPoolingParam = _reflection.GeneratedProtocolMessageType('ROIPoolingParam', (_message.Message,), {
  'DESCRIPTOR' : _ROIPOOLINGPARAM,
  '__module__' : 'modules.perception.camera_tracking.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.tracking_feature.ROIPoolingParam)
  })
_sym_db.RegisterMessage(ROIPoolingParam)

PSROIPoolingParam = _reflection.GeneratedProtocolMessageType('PSROIPoolingParam', (_message.Message,), {
  'DESCRIPTOR' : _PSROIPOOLINGPARAM,
  '__module__' : 'modules.perception.camera_tracking.proto.tracking_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.tracking_feature.PSROIPoolingParam)
  })
_sym_db.RegisterMessage(PSROIPoolingParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FEATUREPARAM._serialized_start=111
  _FEATUREPARAM._serialized_end=298
  _EXTRACTORPARAM._serialized_start=301
  _EXTRACTORPARAM._serialized_end=648
  _EXTRACTORPARAM_FEATURETYPE._serialized_start=619
  _EXTRACTORPARAM_FEATURETYPE._serialized_end=648
  _ROIPOOLINGPARAM._serialized_start=650
  _ROIPOOLINGPARAM._serialized_end=735
  _PSROIPOOLINGPARAM._serialized_start=738
  _PSROIPOOLINGPARAM._serialized_end=933
# @@protoc_insertion_point(module_scope)
