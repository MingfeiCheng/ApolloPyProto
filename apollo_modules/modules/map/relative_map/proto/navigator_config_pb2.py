# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/relative_map/proto/navigator_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/map/relative_map/proto/navigator_config.proto\x12\x13\x61pollo.relative_map\"\x83\x02\n\x0bSampleParam\x12#\n\x18straight_sample_interval\x18\x01 \x01(\x01:\x01\x33\x12&\n\x1bsmall_kappa_sample_interval\x18\x02 \x01(\x01:\x01\x31\x12)\n\x1cmiddle_kappa_sample_interval\x18\x03 \x01(\x01:\x03\x30.4\x12(\n\x1blarge_kappa_sample_interval\x18\x04 \x01(\x01:\x03\x30.1\x12\x1a\n\x0bsmall_kappa\x18\x05 \x01(\x01:\x05\x30.002\x12\x1b\n\x0cmiddle_kappa\x18\x06 \x01(\x01:\x05\x30.008\x12\x19\n\x0blarge_kappa\x18\x07 \x01(\x01:\x04\x30.02\"t\n\x0fNavigatorConfig\x12)\n\x1b\x65nable_navigator_downsample\x18\x01 \x01(\x08:\x04true\x12\x36\n\x0csample_param\x18\x02 \x01(\x0b\x32 .apollo.relative_map.SampleParam')



_SAMPLEPARAM = DESCRIPTOR.message_types_by_name['SampleParam']
_NAVIGATORCONFIG = DESCRIPTOR.message_types_by_name['NavigatorConfig']
SampleParam = _reflection.GeneratedProtocolMessageType('SampleParam', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLEPARAM,
  '__module__' : 'modules.map.relative_map.proto.navigator_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.relative_map.SampleParam)
  })
_sym_db.RegisterMessage(SampleParam)

NavigatorConfig = _reflection.GeneratedProtocolMessageType('NavigatorConfig', (_message.Message,), {
  'DESCRIPTOR' : _NAVIGATORCONFIG,
  '__module__' : 'modules.map.relative_map.proto.navigator_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.relative_map.NavigatorConfig)
  })
_sym_db.RegisterMessage(NavigatorConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SAMPLEPARAM._serialized_start=79
  _SAMPLEPARAM._serialized_end=338
  _NAVIGATORCONFIG._serialized_start=340
  _NAVIGATORCONFIG._serialized_end=456
# @@protoc_insertion_point(module_scope)
