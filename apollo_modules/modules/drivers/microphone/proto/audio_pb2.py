# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/microphone/proto/audio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.drivers.microphone.proto import microphone_config_pb2 as modules_dot_drivers_dot_microphone_dot_proto_dot_microphone__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,modules/drivers/microphone/proto/audio.proto\x12 apollo.drivers.microphone.config\x1a+modules/common_msgs/basic_msgs/header.proto\x1a\x38modules/drivers/microphone/proto/microphone_config.proto\"`\n\x0b\x43hannelData\x12\x43\n\x0c\x63hannel_type\x18\x01 \x01(\x0e\x32-.apollo.drivers.microphone.config.ChannelType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xc6\x01\n\tAudioData\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12M\n\x11microphone_config\x18\x02 \x01(\x0b\x32\x32.apollo.drivers.microphone.config.MicrophoneConfig\x12\x43\n\x0c\x63hannel_data\x18\x03 \x03(\x0b\x32-.apollo.drivers.microphone.config.ChannelData')



_CHANNELDATA = DESCRIPTOR.message_types_by_name['ChannelData']
_AUDIODATA = DESCRIPTOR.message_types_by_name['AudioData']
ChannelData = _reflection.GeneratedProtocolMessageType('ChannelData', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELDATA,
  '__module__' : 'modules.drivers.microphone.proto.audio_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.microphone.config.ChannelData)
  })
_sym_db.RegisterMessage(ChannelData)

AudioData = _reflection.GeneratedProtocolMessageType('AudioData', (_message.Message,), {
  'DESCRIPTOR' : _AUDIODATA,
  '__module__' : 'modules.drivers.microphone.proto.audio_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.microphone.config.AudioData)
  })
_sym_db.RegisterMessage(AudioData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHANNELDATA._serialized_start=185
  _CHANNELDATA._serialized_end=281
  _AUDIODATA._serialized_start=284
  _AUDIODATA._serialized_end=482
# @@protoc_insertion_point(module_scope)
