# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/common/proto/motion_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/perception/common/proto/motion_service.proto\x12\x11\x61pollo.perception\x1a+modules/common_msgs/basic_msgs/header.proto\"\xdc\x01\n\nMotionType\x12\x0b\n\x03m00\x18\x01 \x01(\x02\x12\x0b\n\x03m01\x18\x02 \x01(\x02\x12\x0b\n\x03m02\x18\x03 \x01(\x02\x12\x0b\n\x03m03\x18\x04 \x01(\x02\x12\x0b\n\x03m10\x18\x05 \x01(\x02\x12\x0b\n\x03m11\x18\x06 \x01(\x02\x12\x0b\n\x03m12\x18\x07 \x01(\x02\x12\x0b\n\x03m13\x18\x08 \x01(\x02\x12\x0b\n\x03m20\x18\t \x01(\x02\x12\x0b\n\x03m21\x18\n \x01(\x02\x12\x0b\n\x03m22\x18\x0b \x01(\x02\x12\x0b\n\x03m23\x18\x0c \x01(\x02\x12\x0b\n\x03m30\x18\r \x01(\x02\x12\x0b\n\x03m31\x18\x0e \x01(\x02\x12\x0b\n\x03m32\x18\x0f \x01(\x02\x12\x0b\n\x03m33\x18\x10 \x01(\x02\"\xe6\x01\n\rVehicleStatus\x12\x11\n\troll_rate\x18\x01 \x01(\x02\x12\x12\n\npitch_rate\x18\x02 \x01(\x02\x12\x10\n\x08yaw_rate\x18\x03 \x01(\x02\x12\x10\n\x08velocity\x18\x04 \x01(\x02\x12\x12\n\nvelocity_x\x18\x05 \x01(\x02\x12\x12\n\nvelocity_y\x18\x06 \x01(\x02\x12\x12\n\nvelocity_z\x18\x07 \x01(\x02\x12\x0f\n\x07time_ts\x18\x08 \x01(\x01\x12\x0e\n\x06time_d\x18\t \x01(\x01\x12-\n\x06motion\x18\n \x01(\x0b\x32\x1d.apollo.perception.MotionType\"p\n\rMotionService\x12\x38\n\x0evehicle_status\x18\x01 \x03(\x0b\x32 .apollo.perception.VehicleStatus\x12%\n\x06header\x18\x02 \x01(\x0b\x32\x15.apollo.common.Header')



_MOTIONTYPE = DESCRIPTOR.message_types_by_name['MotionType']
_VEHICLESTATUS = DESCRIPTOR.message_types_by_name['VehicleStatus']
_MOTIONSERVICE = DESCRIPTOR.message_types_by_name['MotionService']
MotionType = _reflection.GeneratedProtocolMessageType('MotionType', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONTYPE,
  '__module__' : 'modules.perception.common.proto.motion_service_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.MotionType)
  })
_sym_db.RegisterMessage(MotionType)

VehicleStatus = _reflection.GeneratedProtocolMessageType('VehicleStatus', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLESTATUS,
  '__module__' : 'modules.perception.common.proto.motion_service_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.VehicleStatus)
  })
_sym_db.RegisterMessage(VehicleStatus)

MotionService = _reflection.GeneratedProtocolMessageType('MotionService', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONSERVICE,
  '__module__' : 'modules.perception.common.proto.motion_service_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.MotionService)
  })
_sym_db.RegisterMessage(MotionService)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOTIONTYPE._serialized_start=121
  _MOTIONTYPE._serialized_end=341
  _VEHICLESTATUS._serialized_start=344
  _VEHICLESTATUS._serialized_end=574
  _MOTIONSERVICE._serialized_start=576
  _MOTIONSERVICE._serialized_end=688
# @@protoc_insertion_point(module_scope)