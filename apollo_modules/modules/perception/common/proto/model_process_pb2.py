# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/common/proto/model_process.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3modules/perception/common/proto/model_process.proto\x12\x18\x61pollo.perception.common\"?\n\x06Resize\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\n\n\x02\x66x\x18\x03 \x01(\x02\x12\n\n\x02\x66y\x18\x04 \x01(\x02\"&\n\tNormalize\x12\x0c\n\x04mean\x18\x01 \x03(\x02\x12\x0b\n\x03std\x18\x02 \x03(\x02\";\n\x04\x43rop\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\"\xb1\x04\n\x14PointCloudPreProcess\x12\x0e\n\x06gpu_id\x18\x01 \x01(\x05\x12\x1a\n\x12normalizing_factor\x18\x02 \x01(\x01\x12\x19\n\x11num_point_feature\x18\x03 \x01(\x05\x12\x1d\n\x15\x65nable_ground_removal\x18\x04 \x01(\x08\x12\x1d\n\x15ground_removal_height\x18\x05 \x01(\x01\x12\x1f\n\x17\x65nable_downsample_beams\x18\x06 \x01(\x08\x12\x1f\n\x17\x64ownsample_beams_factor\x18\x07 \x01(\x05\x12$\n\x1c\x65nable_downsample_pointcloud\x18\x08 \x01(\x08\x12\x1f\n\x17\x64ownsample_voxel_size_x\x18\t \x01(\x01\x12\x1f\n\x17\x64ownsample_voxel_size_y\x18\n \x01(\x01\x12\x1f\n\x17\x64ownsample_voxel_size_z\x18\x0b \x01(\x01\x12\x1a\n\x12\x65nable_fuse_frames\x18\x0c \x01(\x08\x12\x17\n\x0fnum_fuse_frames\x18\r \x01(\x05\x12\x1a\n\x12\x66use_time_interval\x18\x0e \x01(\x01\x12\x1d\n\x15\x65nable_shuffle_points\x18\x0f \x01(\x08\x12\x16\n\x0emax_num_points\x18\x10 \x01(\x05\x12\x1d\n\x15reproduce_result_mode\x18\x11 \x01(\x08\x12\"\n\x1a\x65nable_roi_outside_removal\x18\x12 \x01(\x08\"\xe5\x01\n\x15PointCloudPostProcess\x12\x17\n\x0fscore_threshold\x18\x01 \x01(\x02\x12\x1d\n\x15nms_overlap_threshold\x18\x02 \x01(\x02\x12\x1e\n\x16num_output_box_feature\x18\x03 \x01(\x05\x12\x1d\n\x15\x62ottom_enlarge_height\x18\x04 \x01(\x02\x12\x1a\n\x12top_enlarge_height\x18\x05 \x01(\x02\x12\x1b\n\x13width_enlarge_value\x18\x06 \x01(\x02\x12\x1c\n\x14length_enlarge_value\x18\x07 \x01(\x02\"\xe3\x01\n\x0ePaddleSettings\x12\x16\n\x07use_trt\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x18\n\rtrt_precision\x18\x02 \x01(\x05:\x01\x30\x12\x1d\n\x0etrt_use_static\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fuse_calibration\x18\x04 \x01(\x08:\x05\x66\x61lse\x12!\n\x12\x63ollect_shape_info\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10use_dynamicshape\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x12\x64ynamic_shape_file\x18\x07 \x01(\t:\x00')



_RESIZE = DESCRIPTOR.message_types_by_name['Resize']
_NORMALIZE = DESCRIPTOR.message_types_by_name['Normalize']
_CROP = DESCRIPTOR.message_types_by_name['Crop']
_POINTCLOUDPREPROCESS = DESCRIPTOR.message_types_by_name['PointCloudPreProcess']
_POINTCLOUDPOSTPROCESS = DESCRIPTOR.message_types_by_name['PointCloudPostProcess']
_PADDLESETTINGS = DESCRIPTOR.message_types_by_name['PaddleSettings']
Resize = _reflection.GeneratedProtocolMessageType('Resize', (_message.Message,), {
  'DESCRIPTOR' : _RESIZE,
  '__module__' : 'modules.perception.common.proto.model_process_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.common.Resize)
  })
_sym_db.RegisterMessage(Resize)

Normalize = _reflection.GeneratedProtocolMessageType('Normalize', (_message.Message,), {
  'DESCRIPTOR' : _NORMALIZE,
  '__module__' : 'modules.perception.common.proto.model_process_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.common.Normalize)
  })
_sym_db.RegisterMessage(Normalize)

Crop = _reflection.GeneratedProtocolMessageType('Crop', (_message.Message,), {
  'DESCRIPTOR' : _CROP,
  '__module__' : 'modules.perception.common.proto.model_process_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.common.Crop)
  })
_sym_db.RegisterMessage(Crop)

PointCloudPreProcess = _reflection.GeneratedProtocolMessageType('PointCloudPreProcess', (_message.Message,), {
  'DESCRIPTOR' : _POINTCLOUDPREPROCESS,
  '__module__' : 'modules.perception.common.proto.model_process_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.common.PointCloudPreProcess)
  })
_sym_db.RegisterMessage(PointCloudPreProcess)

PointCloudPostProcess = _reflection.GeneratedProtocolMessageType('PointCloudPostProcess', (_message.Message,), {
  'DESCRIPTOR' : _POINTCLOUDPOSTPROCESS,
  '__module__' : 'modules.perception.common.proto.model_process_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.common.PointCloudPostProcess)
  })
_sym_db.RegisterMessage(PointCloudPostProcess)

PaddleSettings = _reflection.GeneratedProtocolMessageType('PaddleSettings', (_message.Message,), {
  'DESCRIPTOR' : _PADDLESETTINGS,
  '__module__' : 'modules.perception.common.proto.model_process_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.common.PaddleSettings)
  })
_sym_db.RegisterMessage(PaddleSettings)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESIZE._serialized_start=81
  _RESIZE._serialized_end=144
  _NORMALIZE._serialized_start=146
  _NORMALIZE._serialized_end=184
  _CROP._serialized_start=186
  _CROP._serialized_end=245
  _POINTCLOUDPREPROCESS._serialized_start=248
  _POINTCLOUDPREPROCESS._serialized_end=809
  _POINTCLOUDPOSTPROCESS._serialized_start=812
  _POINTCLOUDPOSTPROCESS._serialized_end=1041
  _PADDLESETTINGS._serialized_start=1044
  _PADDLESETTINGS._serialized_end=1271
# @@protoc_insertion_point(module_scope)