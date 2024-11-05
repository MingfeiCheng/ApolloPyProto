# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/dreamview/backend/teleop/proto/modem_info.proto

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
  name='modules/dreamview/backend/teleop/proto/modem_info.proto',
  package='modules.teleop.modem',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n7modules/dreamview/backend/teleop/proto/modem_info.proto\x12\x14modules.teleop.modem\x1a!modules/common/proto/header.proto\"\xde\x02\n\tModemInfo\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x10\n\x08provider\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x10\n\x08ip_count\x18\x04 \x01(\x05\x12\x0f\n\x07gateway\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\t\x12\x0b\n\x03\x64\x65v\x18\x07 \x01(\t\x12\n\n\x02tx\x18\x08 \x01(\x04\x12\n\n\x02rx\x18\t \x01(\x04\x12\x0c\n\x04ping\x18\n \x01(\t\x12\r\n\x05smoni\x18\x0b \x01(\t\x12\x12\n\ntechnology\x18\x0c \x01(\t\x12\x12\n\nconnection\x18\r \x01(\t\x12\x0e\n\x06signal\x18\x0e \x01(\x05\x12\x0f\n\x07quality\x18\x0f \x01(\x05\x12\x14\n\x0c\x62\x61ndwidth_ul\x18\x10 \x01(\x05\x12\x14\n\x0c\x62\x61ndwidth_dl\x18\x11 \x01(\x05\x12\x16\n\x0e\x63\x61_aggregation\x18\x12 \x01(\x08\x12\x0c\n\x04rank\x18\x13 \x01(\x05')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,])




_MODEMINFO = _descriptor.Descriptor(
  name='ModemInfo',
  full_name='modules.teleop.modem.ModemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='modules.teleop.modem.ModemInfo.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='modules.teleop.modem.ModemInfo.provider', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='modules.teleop.modem.ModemInfo.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_count', full_name='modules.teleop.modem.ModemInfo.ip_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='modules.teleop.modem.ModemInfo.gateway', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='modules.teleop.modem.ModemInfo.port', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev', full_name='modules.teleop.modem.ModemInfo.dev', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx', full_name='modules.teleop.modem.ModemInfo.tx', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx', full_name='modules.teleop.modem.ModemInfo.rx', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ping', full_name='modules.teleop.modem.ModemInfo.ping', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='smoni', full_name='modules.teleop.modem.ModemInfo.smoni', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='technology', full_name='modules.teleop.modem.ModemInfo.technology', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection', full_name='modules.teleop.modem.ModemInfo.connection', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signal', full_name='modules.teleop.modem.ModemInfo.signal', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quality', full_name='modules.teleop.modem.ModemInfo.quality', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bandwidth_ul', full_name='modules.teleop.modem.ModemInfo.bandwidth_ul', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bandwidth_dl', full_name='modules.teleop.modem.ModemInfo.bandwidth_dl', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ca_aggregation', full_name='modules.teleop.modem.ModemInfo.ca_aggregation', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='modules.teleop.modem.ModemInfo.rank', index=18,
      number=19, type=5, cpp_type=1, label=1,
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
  serialized_start=117,
  serialized_end=467,
)

_MODEMINFO.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
DESCRIPTOR.message_types_by_name['ModemInfo'] = _MODEMINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModemInfo = _reflection.GeneratedProtocolMessageType('ModemInfo', (_message.Message,), dict(
  DESCRIPTOR = _MODEMINFO,
  __module__ = 'modules.dreamview.backend.teleop.proto.modem_info_pb2'
  # @@protoc_insertion_point(class_scope:modules.teleop.modem.ModemInfo)
  ))
_sym_db.RegisterMessage(ModemInfo)


# @@protoc_insertion_point(module_scope)
