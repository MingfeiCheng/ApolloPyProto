# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar/lib/detector/ncut_segmentation/proto/ncut_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/lidar/lib/detector/ncut_segmentation/proto/ncut_config.proto',
  package='apollo.perception.lidar',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nOmodules/perception/lidar/lib/detector/ncut_segmentation/proto/ncut_config.proto\x12\x17\x61pollo.perception.lidar\"?\n\nNCutConfig\x12\x31\n\nparam_file\x18\x01 \x01(\t:\x1d./data/models/ncut/param.conf')
)




_NCUTCONFIG = _descriptor.Descriptor(
  name='NCutConfig',
  full_name='apollo.perception.lidar.NCutConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_file', full_name='apollo.perception.lidar.NCutConfig.param_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("./data/models/ncut/param.conf").decode('utf-8'),
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
  serialized_start=108,
  serialized_end=171,
)

DESCRIPTOR.message_types_by_name['NCutConfig'] = _NCUTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NCutConfig = _reflection.GeneratedProtocolMessageType('NCutConfig', (_message.Message,), dict(
  DESCRIPTOR = _NCUTCONFIG,
  __module__ = 'modules.perception.lidar.lib.detector.ncut_segmentation.proto.ncut_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.NCutConfig)
  ))
_sym_db.RegisterMessage(NCutConfig)


# @@protoc_insertion_point(module_scope)
