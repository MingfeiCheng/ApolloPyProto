# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/localization/proto/measure.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from apollo_modules.modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/localization/proto/measure.proto',
  package='apollo.localization',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(modules/localization/proto/measure.proto\x12\x13\x61pollo.localization\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\"\xd6\x04\n\x0cIntegMeasure\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x43\n\x0cmeasure_type\x18\x02 \x01(\x0e\x32-.apollo.localization.IntegMeasure.MeasureType\x12?\n\nframe_type\x18\x03 \x01(\x0e\x32+.apollo.localization.IntegMeasure.FrameType\x12(\n\x08position\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point3D\x12(\n\x08velocity\x18\x05 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x0b\n\x03yaw\x18\x06 \x01(\x01\x12\x0f\n\x07zone_id\x18\x07 \x01(\x05\x12\x18\n\x10is_have_variance\x18\x08 \x01(\x08\x12\x1e\n\x16is_gnss_double_antenna\x18\t \x01(\x08\x12\x19\n\rmeasure_covar\x18\n \x03(\x01\x42\x02\x10\x01\"\x9a\x01\n\x0bMeasureType\x12\x11\n\rGNSS_POS_ONLY\x10\x00\x12\x10\n\x0cGNSS_POS_VEL\x10\x01\x12\x0f\n\x0bGNSS_POS_XY\x10\x02\x12\x11\n\rGNSS_VEL_ONLY\x10\x03\x12\x13\n\x0fPOINT_CLOUD_POS\x10\x04\x12\x15\n\x11ODOMETER_VEL_ONLY\x10\x05\x12\x16\n\x12VEHICLE_CONSTRAINT\x10\x06\"5\n\tFrameType\x12\x07\n\x03\x45NU\x10\x00\x12\x08\n\x04\x45\x43\x45\x46\x10\x01\x12\x07\n\x03UTM\x10\x02\x12\x0c\n\x08ODOMETER\x10\x03')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,])



_INTEGMEASURE_MEASURETYPE = _descriptor.EnumDescriptor(
  name='MeasureType',
  full_name='apollo.localization.IntegMeasure.MeasureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GNSS_POS_ONLY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GNSS_POS_VEL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GNSS_POS_XY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GNSS_VEL_ONLY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POINT_CLOUD_POS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ODOMETER_VEL_ONLY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VEHICLE_CONSTRAINT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=527,
  serialized_end=681,
)
_sym_db.RegisterEnumDescriptor(_INTEGMEASURE_MEASURETYPE)

_INTEGMEASURE_FRAMETYPE = _descriptor.EnumDescriptor(
  name='FrameType',
  full_name='apollo.localization.IntegMeasure.FrameType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENU', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECEF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UTM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ODOMETER', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=683,
  serialized_end=736,
)
_sym_db.RegisterEnumDescriptor(_INTEGMEASURE_FRAMETYPE)


_INTEGMEASURE = _descriptor.Descriptor(
  name='IntegMeasure',
  full_name='apollo.localization.IntegMeasure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.localization.IntegMeasure.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measure_type', full_name='apollo.localization.IntegMeasure.measure_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_type', full_name='apollo.localization.IntegMeasure.frame_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='apollo.localization.IntegMeasure.position', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='apollo.localization.IntegMeasure.velocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='apollo.localization.IntegMeasure.yaw', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='apollo.localization.IntegMeasure.zone_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_have_variance', full_name='apollo.localization.IntegMeasure.is_have_variance', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_gnss_double_antenna', full_name='apollo.localization.IntegMeasure.is_gnss_double_antenna', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measure_covar', full_name='apollo.localization.IntegMeasure.measure_covar', index=9,
      number=10, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INTEGMEASURE_MEASURETYPE,
    _INTEGMEASURE_FRAMETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=736,
)

_INTEGMEASURE.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INTEGMEASURE.fields_by_name['measure_type'].enum_type = _INTEGMEASURE_MEASURETYPE
_INTEGMEASURE.fields_by_name['frame_type'].enum_type = _INTEGMEASURE_FRAMETYPE
_INTEGMEASURE.fields_by_name['position'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_INTEGMEASURE.fields_by_name['velocity'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_INTEGMEASURE_MEASURETYPE.containing_type = _INTEGMEASURE
_INTEGMEASURE_FRAMETYPE.containing_type = _INTEGMEASURE
DESCRIPTOR.message_types_by_name['IntegMeasure'] = _INTEGMEASURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IntegMeasure = _reflection.GeneratedProtocolMessageType('IntegMeasure', (_message.Message,), dict(
  DESCRIPTOR = _INTEGMEASURE,
  __module__ = 'modules.localization.proto.measure_pb2'
  # @@protoc_insertion_point(class_scope:apollo.localization.IntegMeasure)
  ))
_sym_db.RegisterMessage(IntegMeasure)


_INTEGMEASURE.fields_by_name['measure_covar']._options = None
# @@protoc_insertion_point(module_scope)
