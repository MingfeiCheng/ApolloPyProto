# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/gnss/proto/heading.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/drivers/gnss/proto/heading.proto',
  package='apollo.drivers.gnss',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(modules/drivers/gnss/proto/heading.proto\x12\x13\x61pollo.drivers.gnss\x1a!modules/common/proto/header.proto\"\x87\x04\n\x07Heading\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12\x17\n\x0fsolution_status\x18\x03 \x01(\r\x12\x15\n\rposition_type\x18\x04 \x01(\r\x12\x17\n\x0f\x62\x61seline_length\x18\x05 \x01(\x02\x12\x0f\n\x07heading\x18\x06 \x01(\x02\x12\r\n\x05pitch\x18\x07 \x01(\x02\x12\x10\n\x08reserved\x18\x08 \x01(\x02\x12\x17\n\x0fheading_std_dev\x18\t \x01(\x02\x12\x15\n\rpitch_std_dev\x18\n \x01(\x02\x12\x12\n\nstation_id\x18\x0b \x01(\x0c\x12 \n\x18satellite_tracked_number\x18\x0c \x01(\r\x12\"\n\x1asatellite_soulution_number\x18\r \x01(\r\x12\x1c\n\x14satellite_number_obs\x18\x0e \x01(\r\x12\x1e\n\x16satellite_number_multi\x18\x0f \x01(\r\x12\x17\n\x0fsolution_source\x18\x10 \x01(\r\x12 \n\x18\x65xtended_solution_status\x18\x11 \x01(\r\x12\x1f\n\x17galileo_beidou_sig_mask\x18\x12 \x01(\r\x12\x1c\n\x14gps_glonass_sig_mask\x18\x13 \x01(\r')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])




_HEADING = _descriptor.Descriptor(
  name='Heading',
  full_name='apollo.drivers.gnss.Heading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.drivers.gnss.Heading.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='apollo.drivers.gnss.Heading.measurement_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution_status', full_name='apollo.drivers.gnss.Heading.solution_status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position_type', full_name='apollo.drivers.gnss.Heading.position_type', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baseline_length', full_name='apollo.drivers.gnss.Heading.baseline_length', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='apollo.drivers.gnss.Heading.heading', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='apollo.drivers.gnss.Heading.pitch', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reserved', full_name='apollo.drivers.gnss.Heading.reserved', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading_std_dev', full_name='apollo.drivers.gnss.Heading.heading_std_dev', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch_std_dev', full_name='apollo.drivers.gnss.Heading.pitch_std_dev', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='station_id', full_name='apollo.drivers.gnss.Heading.station_id', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='satellite_tracked_number', full_name='apollo.drivers.gnss.Heading.satellite_tracked_number', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='satellite_soulution_number', full_name='apollo.drivers.gnss.Heading.satellite_soulution_number', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='satellite_number_obs', full_name='apollo.drivers.gnss.Heading.satellite_number_obs', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='satellite_number_multi', full_name='apollo.drivers.gnss.Heading.satellite_number_multi', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution_source', full_name='apollo.drivers.gnss.Heading.solution_source', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extended_solution_status', full_name='apollo.drivers.gnss.Heading.extended_solution_status', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='galileo_beidou_sig_mask', full_name='apollo.drivers.gnss.Heading.galileo_beidou_sig_mask', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gps_glonass_sig_mask', full_name='apollo.drivers.gnss.Heading.gps_glonass_sig_mask', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=101,
  serialized_end=620,
)

_HEADING.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['Heading'] = _HEADING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Heading = _reflection.GeneratedProtocolMessageType('Heading', (_message.Message,), dict(
  DESCRIPTOR = _HEADING,
  __module__ = 'modules.drivers.gnss.proto.heading_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.gnss.Heading)
  ))
_sym_db.RegisterMessage(Heading)


# @@protoc_insertion_point(module_scope)
