# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/motion_service/proto/motion_service_component.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFmodules/perception/motion_service/proto/motion_service_component.proto\x12\x19\x61pollo.perception.onboard\"\x8e\x02\n\x16MotionServiceComponent\x12\x1f\n\x0c\x63\x61mera_names\x18\x01 \x01(\t:\tfront_6mm\x12I\n\x1ainput_camera_channel_names\x18\x02 \x01(\t:%/apollo/sensor/camera/front_6mm/image\x12\x42\n\x1finput_localization_channel_name\x18\x03 \x01(\t:\x19/apollo/localization/pose\x12\x44\n\x19output_topic_channel_name\x18\x04 \x01(\t:!/apollo/perception/motion_service')



_MOTIONSERVICECOMPONENT = DESCRIPTOR.message_types_by_name['MotionServiceComponent']
MotionServiceComponent = _reflection.GeneratedProtocolMessageType('MotionServiceComponent', (_message.Message,), {
  'DESCRIPTOR' : _MOTIONSERVICECOMPONENT,
  '__module__' : 'modules.perception.motion_service.proto.motion_service_component_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.onboard.MotionServiceComponent)
  })
_sym_db.RegisterMessage(MotionServiceComponent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOTIONSERVICECOMPONENT._serialized_start=102
  _MOTIONSERVICECOMPONENT._serialized_end=372
# @@protoc_insertion_point(module_scope)
