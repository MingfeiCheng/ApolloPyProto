# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/external_command_msgs/chassis_command.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.basic_msgs import vehicle_signal_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_vehicle__signal__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?modules/common_msgs/external_command_msgs/chassis_command.proto\x12\x17\x61pollo.external_command\x1a\x19google/protobuf/any.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a\x33modules/common_msgs/basic_msgs/vehicle_signal.proto\"\xb3\x01\n\x0e\x43hassisCommand\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x16\n\ncommand_id\x18\x02 \x01(\x03:\x02-1\x12\x32\n\x0c\x62\x61sic_signal\x18\x03 \x01(\x0b\x32\x1c.apollo.common.VehicleSignal\x12.\n\x10\x63ustom_operation\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any')



_CHASSISCOMMAND = DESCRIPTOR.message_types_by_name['ChassisCommand']
ChassisCommand = _reflection.GeneratedProtocolMessageType('ChassisCommand', (_message.Message,), {
  'DESCRIPTOR' : _CHASSISCOMMAND,
  '__module__' : 'modules.common_msgs.external_command_msgs.chassis_command_pb2'
  # @@protoc_insertion_point(class_scope:apollo.external_command.ChassisCommand)
  })
_sym_db.RegisterMessage(ChassisCommand)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHASSISCOMMAND._serialized_start=218
  _CHASSISCOMMAND._serialized_end=397
# @@protoc_insertion_point(module_scope)
