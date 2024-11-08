# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/audio_msgs/audio_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.audio_msgs import audio_common_pb2 as modules_dot_common__msgs_dot_audio__msgs_dot_audio__common__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.localization_msgs import pose_pb2 as modules_dot_common__msgs_dot_localization__msgs_dot_pose__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/common_msgs/audio_msgs/audio_event.proto\x12\x0c\x61pollo.audio\x1a\x31modules/common_msgs/audio_msgs/audio_common.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a\x30modules/common_msgs/localization_msgs/pose.proto\"\xbe\x02\n\nAudioEvent\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\n\n\x02id\x18\x02 \x01(\x05\x12:\n\rmoving_result\x18\x03 \x01(\x0e\x32\x1a.apollo.audio.MovingResult:\x07UNKNOWN\x12\x39\n\naudio_type\x18\x04 \x01(\x0e\x32\x17.apollo.audio.AudioType:\x0cUNKNOWN_TYPE\x12\x13\n\x0bsiren_is_on\x18\x05 \x01(\x08\x12H\n\x0f\x61udio_direction\x18\x06 \x01(\x0e\x32\x1c.apollo.audio.AudioDirection:\x11UNKNOWN_DIRECTION\x12\'\n\x04pose\x18\x07 \x01(\x0b\x32\x19.apollo.localization.Pose')



_AUDIOEVENT = DESCRIPTOR.message_types_by_name['AudioEvent']
AudioEvent = _reflection.GeneratedProtocolMessageType('AudioEvent', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOEVENT,
  '__module__' : 'modules.common_msgs.audio_msgs.audio_event_pb2'
  # @@protoc_insertion_point(class_scope:apollo.audio.AudioEvent)
  })
_sym_db.RegisterMessage(AudioEvent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUDIOEVENT._serialized_start=213
  _AUDIOEVENT._serialized_end=531
# @@protoc_insertion_point(module_scope)