# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/v2x/proto/v2x_service_car_to_obu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.v2x.proto import v2x_car_status_pb2 as modules_dot_v2x_dot_proto_dot_v2x__car__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/v2x/proto/v2x_service_car_to_obu.proto',
  package='apollo.v2x',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n.modules/v2x/proto/v2x_service_car_to_obu.proto\x12\napollo.v2x\x1a&modules/v2x/proto/v2x_car_status.proto\"&\n\x0cUpdateStatus\x12\x16\n\x07updated\x18\x01 \x02(\x08:\x05\x66\x61lse2N\n\x08\x43\x61rToObu\x12\x42\n\rPushCarStatus\x12\x15.apollo.v2x.CarStatus\x1a\x18.apollo.v2x.UpdateStatus\"\x00')
  ,
  dependencies=[modules_dot_v2x_dot_proto_dot_v2x__car__status__pb2.DESCRIPTOR,])




_UPDATESTATUS = _descriptor.Descriptor(
  name='UpdateStatus',
  full_name='apollo.v2x.UpdateStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated', full_name='apollo.v2x.UpdateStatus.updated', index=0,
      number=1, type=8, cpp_type=7, label=2,
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
  serialized_start=102,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['UpdateStatus'] = _UPDATESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateStatus = _reflection.GeneratedProtocolMessageType('UpdateStatus', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESTATUS,
  __module__ = 'modules.v2x.proto.v2x_service_car_to_obu_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.UpdateStatus)
  ))
_sym_db.RegisterMessage(UpdateStatus)



_CARTOOBU = _descriptor.ServiceDescriptor(
  name='CarToObu',
  full_name='apollo.v2x.CarToObu',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=142,
  serialized_end=220,
  methods=[
  _descriptor.MethodDescriptor(
    name='PushCarStatus',
    full_name='apollo.v2x.CarToObu.PushCarStatus',
    index=0,
    containing_service=None,
    input_type=modules_dot_v2x_dot_proto_dot_v2x__car__status__pb2._CARSTATUS,
    output_type=_UPDATESTATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CARTOOBU)

DESCRIPTOR.services_by_name['CarToObu'] = _CARTOOBU

# @@protoc_insertion_point(module_scope)
