# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/canbus/proto/sensor_canbus_conf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.drivers_msgs import can_card_parameter_pb2 as modules_dot_common__msgs_dot_drivers__msgs_dot_can__card__parameter__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/drivers/canbus/proto/sensor_canbus_conf.proto\x12\x15\x61pollo.drivers.canbus\x1a\x39modules/common_msgs/drivers_msgs/can_card_parameter.proto\"\x9d\x01\n\x10SensorCanbusConf\x12\x43\n\x12\x63\x61n_card_parameter\x18\x01 \x01(\x0b\x32\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11\x65nable_debug_mode\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x65nable_receiver_log\x18\x03 \x01(\x08:\x05\x66\x61lse')



_SENSORCANBUSCONF = DESCRIPTOR.message_types_by_name['SensorCanbusConf']
SensorCanbusConf = _reflection.GeneratedProtocolMessageType('SensorCanbusConf', (_message.Message,), {
  'DESCRIPTOR' : _SENSORCANBUSCONF,
  '__module__' : 'modules.drivers.canbus.proto.sensor_canbus_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.canbus.SensorCanbusConf)
  })
_sym_db.RegisterMessage(SensorCanbusConf)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SENSORCANBUSCONF._serialized_start=140
  _SENSORCANBUSCONF._serialized_end=297
# @@protoc_insertion_point(module_scope)
