# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar/lib/ground_detector/spatio_temporal_ground_detector/proto/spatio_temporal_ground_detector_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/lidar/lib/ground_detector/spatio_temporal_ground_detector/proto/spatio_temporal_ground_detector_config.proto',
  package='apollo.perception.lidar',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x7fmodules/perception/lidar/lib/ground_detector/spatio_temporal_ground_detector/proto/spatio_temporal_ground_detector_config.proto\x12\x17\x61pollo.perception.lidar\"\xf3\x01\n\"SpatioTemporalGroundDetectorConfig\x12\x15\n\tgrid_size\x18\x01 \x01(\r:\x02\x31\x36\x12\x1a\n\x0cground_thres\x18\x02 \x01(\x02:\x04\x30.25\x12\x16\n\troi_rad_x\x18\x03 \x01(\x02:\x03\x31\x32\x30\x12\x16\n\troi_rad_y\x18\x04 \x01(\x02:\x03\x31\x32\x30\x12\x16\n\troi_rad_z\x18\x05 \x01(\x02:\x03\x31\x30\x30\x12\x19\n\x0enr_smooth_iter\x18\x06 \x01(\r:\x01\x35\x12\x15\n\x07use_roi\x18\x07 \x01(\x08:\x04true\x12 \n\x12use_ground_service\x18\x08 \x01(\x08:\x04true')
)




_SPATIOTEMPORALGROUNDDETECTORCONFIG = _descriptor.Descriptor(
  name='SpatioTemporalGroundDetectorConfig',
  full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grid_size', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.grid_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ground_thres', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.ground_thres', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.25),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roi_rad_x', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.roi_rad_x', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(120),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roi_rad_y', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.roi_rad_y', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(120),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roi_rad_z', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.roi_rad_z', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(100),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nr_smooth_iter', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.nr_smooth_iter', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_roi', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.use_roi', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_ground_service', full_name='apollo.perception.lidar.SpatioTemporalGroundDetectorConfig.use_ground_service', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=400,
)

DESCRIPTOR.message_types_by_name['SpatioTemporalGroundDetectorConfig'] = _SPATIOTEMPORALGROUNDDETECTORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpatioTemporalGroundDetectorConfig = _reflection.GeneratedProtocolMessageType('SpatioTemporalGroundDetectorConfig', (_message.Message,), dict(
  DESCRIPTOR = _SPATIOTEMPORALGROUNDDETECTORCONFIG,
  __module__ = 'modules.perception.lidar.lib.ground_detector.spatio_temporal_ground_detector.proto.spatio_temporal_ground_detector_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.SpatioTemporalGroundDetectorConfig)
  ))
_sym_db.RegisterMessage(SpatioTemporalGroundDetectorConfig)


# @@protoc_insertion_point(module_scope)