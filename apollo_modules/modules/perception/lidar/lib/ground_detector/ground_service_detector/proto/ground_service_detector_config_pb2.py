# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar/lib/ground_detector/ground_service_detector/proto/ground_service_detector_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/lidar/lib/ground_detector/ground_service_detector/proto/ground_service_detector_config.proto',
  package='apollo.perception.lidar',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nomodules/perception/lidar/lib/ground_detector/ground_service_detector/proto/ground_service_detector_config.proto\x12\x17\x61pollo.perception.lidar\"=\n\x1bGroundServiceDetectorConfig\x12\x1e\n\x10ground_threshold\x18\x01 \x01(\x01:\x04\x30.25')
)




_GROUNDSERVICEDETECTORCONFIG = _descriptor.Descriptor(
  name='GroundServiceDetectorConfig',
  full_name='apollo.perception.lidar.GroundServiceDetectorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ground_threshold', full_name='apollo.perception.lidar.GroundServiceDetectorConfig.ground_threshold', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.25),
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
  serialized_start=140,
  serialized_end=201,
)

DESCRIPTOR.message_types_by_name['GroundServiceDetectorConfig'] = _GROUNDSERVICEDETECTORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GroundServiceDetectorConfig = _reflection.GeneratedProtocolMessageType('GroundServiceDetectorConfig', (_message.Message,), dict(
  DESCRIPTOR = _GROUNDSERVICEDETECTORCONFIG,
  __module__ = 'modules.perception.lidar.lib.ground_detector.ground_service_detector.proto.ground_service_detector_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.GroundServiceDetectorConfig)
  ))
_sym_db.RegisterMessage(GroundServiceDetectorConfig)


# @@protoc_insertion_point(module_scope)
