# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/audio_msgs/audio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.audio_msgs import audio_common_pb2 as modules_dot_common__msgs_dot_audio__msgs_dot_audio__common__pb2
from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*modules/common_msgs/audio_msgs/audio.proto\x12\x0c\x61pollo.audio\x1a\x31modules/common_msgs/audio_msgs/audio_common.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto\"\xc6\x01\n\x0e\x41udioDetection\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x10\n\x08is_siren\x18\x02 \x01(\x08\x12:\n\rmoving_result\x18\x03 \x01(\x0e\x32\x1a.apollo.audio.MovingResult:\x07UNKNOWN\x12(\n\x08position\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x15\n\rsource_degree\x18\x05 \x01(\x01')



_AUDIODETECTION = DESCRIPTOR.message_types_by_name['AudioDetection']
AudioDetection = _reflection.GeneratedProtocolMessageType('AudioDetection', (_message.Message,), {
  'DESCRIPTOR' : _AUDIODETECTION,
  '__module__' : 'modules.common_msgs.audio_msgs.audio_pb2'
  # @@protoc_insertion_point(class_scope:apollo.audio.AudioDetection)
  })
_sym_db.RegisterMessage(AudioDetection)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUDIODETECTION._serialized_start=204
  _AUDIODETECTION._serialized_end=402
# @@protoc_insertion_point(module_scope)
