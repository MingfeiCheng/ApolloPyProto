# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/storytelling_msgs/story.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/common_msgs/storytelling_msgs/story.proto\x12\x13\x61pollo.storytelling\x1a+modules/common_msgs/basic_msgs/header.proto\"5\n\x10\x43loseToCrosswalk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"5\n\x10\x43loseToClearArea\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"\xa5\x01\n\x0f\x43loseToJunction\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.apollo.storytelling.CloseToJunction.JunctionType\x12\x15\n\x08\x64istance\x18\x03 \x01(\x01:\x03nan\".\n\x0cJunctionType\x12\x10\n\x0cPNC_JUNCTION\x10\x01\x12\x0c\n\x08JUNCTION\x10\x02\"2\n\rCloseToSignal\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"4\n\x0f\x43loseToStopSign\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"5\n\x10\x43loseToYieldSign\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\x08\x64istance\x18\x02 \x01(\x01:\x03nan\"\xbb\x03\n\x07Stories\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x42\n\x13\x63lose_to_clear_area\x18\x02 \x01(\x0b\x32%.apollo.storytelling.CloseToClearArea\x12\x41\n\x12\x63lose_to_crosswalk\x18\x03 \x01(\x0b\x32%.apollo.storytelling.CloseToCrosswalk\x12?\n\x11\x63lose_to_junction\x18\x04 \x01(\x0b\x32$.apollo.storytelling.CloseToJunction\x12;\n\x0f\x63lose_to_signal\x18\x05 \x01(\x0b\x32\".apollo.storytelling.CloseToSignal\x12@\n\x12\x63lose_to_stop_sign\x18\x06 \x01(\x0b\x32$.apollo.storytelling.CloseToStopSign\x12\x42\n\x13\x63lose_to_yield_sign\x18\x07 \x01(\x0b\x32%.apollo.storytelling.CloseToYieldSign')



_CLOSETOCROSSWALK = DESCRIPTOR.message_types_by_name['CloseToCrosswalk']
_CLOSETOCLEARAREA = DESCRIPTOR.message_types_by_name['CloseToClearArea']
_CLOSETOJUNCTION = DESCRIPTOR.message_types_by_name['CloseToJunction']
_CLOSETOSIGNAL = DESCRIPTOR.message_types_by_name['CloseToSignal']
_CLOSETOSTOPSIGN = DESCRIPTOR.message_types_by_name['CloseToStopSign']
_CLOSETOYIELDSIGN = DESCRIPTOR.message_types_by_name['CloseToYieldSign']
_STORIES = DESCRIPTOR.message_types_by_name['Stories']
_CLOSETOJUNCTION_JUNCTIONTYPE = _CLOSETOJUNCTION.enum_types_by_name['JunctionType']
CloseToCrosswalk = _reflection.GeneratedProtocolMessageType('CloseToCrosswalk', (_message.Message,), {
  'DESCRIPTOR' : _CLOSETOCROSSWALK,
  '__module__' : 'modules.common_msgs.storytelling_msgs.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToCrosswalk)
  })
_sym_db.RegisterMessage(CloseToCrosswalk)

CloseToClearArea = _reflection.GeneratedProtocolMessageType('CloseToClearArea', (_message.Message,), {
  'DESCRIPTOR' : _CLOSETOCLEARAREA,
  '__module__' : 'modules.common_msgs.storytelling_msgs.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToClearArea)
  })
_sym_db.RegisterMessage(CloseToClearArea)

CloseToJunction = _reflection.GeneratedProtocolMessageType('CloseToJunction', (_message.Message,), {
  'DESCRIPTOR' : _CLOSETOJUNCTION,
  '__module__' : 'modules.common_msgs.storytelling_msgs.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToJunction)
  })
_sym_db.RegisterMessage(CloseToJunction)

CloseToSignal = _reflection.GeneratedProtocolMessageType('CloseToSignal', (_message.Message,), {
  'DESCRIPTOR' : _CLOSETOSIGNAL,
  '__module__' : 'modules.common_msgs.storytelling_msgs.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToSignal)
  })
_sym_db.RegisterMessage(CloseToSignal)

CloseToStopSign = _reflection.GeneratedProtocolMessageType('CloseToStopSign', (_message.Message,), {
  'DESCRIPTOR' : _CLOSETOSTOPSIGN,
  '__module__' : 'modules.common_msgs.storytelling_msgs.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToStopSign)
  })
_sym_db.RegisterMessage(CloseToStopSign)

CloseToYieldSign = _reflection.GeneratedProtocolMessageType('CloseToYieldSign', (_message.Message,), {
  'DESCRIPTOR' : _CLOSETOYIELDSIGN,
  '__module__' : 'modules.common_msgs.storytelling_msgs.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.CloseToYieldSign)
  })
_sym_db.RegisterMessage(CloseToYieldSign)

Stories = _reflection.GeneratedProtocolMessageType('Stories', (_message.Message,), {
  'DESCRIPTOR' : _STORIES,
  '__module__' : 'modules.common_msgs.storytelling_msgs.story_pb2'
  # @@protoc_insertion_point(class_scope:apollo.storytelling.Stories)
  })
_sym_db.RegisterMessage(Stories)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLOSETOCROSSWALK._serialized_start=119
  _CLOSETOCROSSWALK._serialized_end=172
  _CLOSETOCLEARAREA._serialized_start=174
  _CLOSETOCLEARAREA._serialized_end=227
  _CLOSETOJUNCTION._serialized_start=230
  _CLOSETOJUNCTION._serialized_end=395
  _CLOSETOJUNCTION_JUNCTIONTYPE._serialized_start=349
  _CLOSETOJUNCTION_JUNCTIONTYPE._serialized_end=395
  _CLOSETOSIGNAL._serialized_start=397
  _CLOSETOSIGNAL._serialized_end=447
  _CLOSETOSTOPSIGN._serialized_start=449
  _CLOSETOSTOPSIGN._serialized_end=501
  _CLOSETOYIELDSIGN._serialized_start=503
  _CLOSETOYIELDSIGN._serialized_end=556
  _STORIES._serialized_start=559
  _STORIES._serialized_end=1002
# @@protoc_insertion_point(module_scope)