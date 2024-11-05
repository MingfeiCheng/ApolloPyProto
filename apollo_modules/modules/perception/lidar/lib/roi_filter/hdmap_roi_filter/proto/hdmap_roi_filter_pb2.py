# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lidar/lib/roi_filter/hdmap_roi_filter/proto/hdmap_roi_filter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/lidar/lib/roi_filter/hdmap_roi_filter/proto/hdmap_roi_filter.proto',
  package='apollo.perception.lidar',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nUmodules/perception/lidar/lib/roi_filter/hdmap_roi_filter/proto/hdmap_roi_filter.proto\x12\x17\x61pollo.perception.lidar\"\x99\x01\n\x14HDMapRoiFilterConfig\x12\x12\n\x05range\x18\x01 \x01(\x01:\x03\x31\x32\x30\x12\x17\n\tcell_size\x18\x02 \x01(\x01:\x04\x30.25\x12\x16\n\x0b\x65xtend_dist\x18\x03 \x01(\x01:\x01\x30\x12\x1c\n\rno_edge_table\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fset_roi_service\x18\x05 \x01(\x08:\x05\x66\x61lse')
)




_HDMAPROIFILTERCONFIG = _descriptor.Descriptor(
  name='HDMapRoiFilterConfig',
  full_name='apollo.perception.lidar.HDMapRoiFilterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='apollo.perception.lidar.HDMapRoiFilterConfig.range', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(120),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cell_size', full_name='apollo.perception.lidar.HDMapRoiFilterConfig.cell_size', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0.25),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extend_dist', full_name='apollo.perception.lidar.HDMapRoiFilterConfig.extend_dist', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_edge_table', full_name='apollo.perception.lidar.HDMapRoiFilterConfig.no_edge_table', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_roi_service', full_name='apollo.perception.lidar.HDMapRoiFilterConfig.set_roi_service', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=115,
  serialized_end=268,
)

DESCRIPTOR.message_types_by_name['HDMapRoiFilterConfig'] = _HDMAPROIFILTERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HDMapRoiFilterConfig = _reflection.GeneratedProtocolMessageType('HDMapRoiFilterConfig', (_message.Message,), dict(
  DESCRIPTOR = _HDMAPROIFILTERCONFIG,
  __module__ = 'modules.perception.lidar.lib.roi_filter.hdmap_roi_filter.proto.hdmap_roi_filter_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.lidar.HDMapRoiFilterConfig)
  ))
_sym_db.RegisterMessage(HDMapRoiFilterConfig)


# @@protoc_insertion_point(module_scope)
