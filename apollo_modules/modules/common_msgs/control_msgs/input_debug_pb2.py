# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/control_msgs/input_debug.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2modules/common_msgs/control_msgs/input_debug.proto\x12\x0e\x61pollo.control\x1a+modules/common_msgs/basic_msgs/header.proto\"\xe0\x01\n\nInputDebug\x12\x32\n\x13localization_header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12,\n\rcanbus_header\x18\x02 \x01(\x0b\x32\x15.apollo.common.Header\x12\x30\n\x11trajectory_header\x18\x03 \x01(\x0b\x32\x15.apollo.common.Header\x12>\n\x1flatest_replan_trajectory_header\x18\x04 \x01(\x0b\x32\x15.apollo.common.Header')



_INPUTDEBUG = DESCRIPTOR.message_types_by_name['InputDebug']
InputDebug = _reflection.GeneratedProtocolMessageType('InputDebug', (_message.Message,), {
  'DESCRIPTOR' : _INPUTDEBUG,
  '__module__' : 'modules.common_msgs.control_msgs.input_debug_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.InputDebug)
  })
_sym_db.RegisterMessage(InputDebug)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INPUTDEBUG._serialized_start=116
  _INPUTDEBUG._serialized_end=340
# @@protoc_insertion_point(module_scope)
