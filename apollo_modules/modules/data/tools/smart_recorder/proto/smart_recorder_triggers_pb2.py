# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/data/tools/smart_recorder/proto/smart_recorder_triggers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEmodules/data/tools/smart_recorder/proto/smart_recorder_triggers.proto\x12\x0b\x61pollo.data\"L\n\x14RecordSegmentSetting\x12\x19\n\x0csize_segment\x18\x01 \x01(\x05:\x03\x35\x30\x30\x12\x19\n\x0ctime_segment\x18\x02 \x01(\x05:\x03\x31\x38\x30\"r\n\x07Trigger\x12\x14\n\x0ctrigger_name\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x15\n\rbackward_time\x18\x03 \x01(\x01\x12\x14\n\x0c\x66orward_time\x18\x04 \x01(\x01\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"\xf3\x01\n\x12SmartRecordTrigger\x12:\n\x0fsegment_setting\x18\x01 \x01(\x0b\x32!.apollo.data.RecordSegmentSetting\x12&\n\x08triggers\x18\x02 \x03(\x0b\x32\x14.apollo.data.Trigger\x12\x1d\n\x11max_backward_time\x18\x03 \x01(\x01:\x02\x33\x30\x12\x1c\n\x11min_restore_chunk\x18\x04 \x01(\x01:\x01\x35\x12\x1d\n\x15trigger_log_file_path\x18\x05 \x01(\t\x12\x1d\n\x11reused_record_num\x18\x06 \x01(\x05:\x02\x31\x30')



_RECORDSEGMENTSETTING = DESCRIPTOR.message_types_by_name['RecordSegmentSetting']
_TRIGGER = DESCRIPTOR.message_types_by_name['Trigger']
_SMARTRECORDTRIGGER = DESCRIPTOR.message_types_by_name['SmartRecordTrigger']
RecordSegmentSetting = _reflection.GeneratedProtocolMessageType('RecordSegmentSetting', (_message.Message,), {
  'DESCRIPTOR' : _RECORDSEGMENTSETTING,
  '__module__' : 'modules.data.tools.smart_recorder.proto.smart_recorder_triggers_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.RecordSegmentSetting)
  })
_sym_db.RegisterMessage(RecordSegmentSetting)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGER,
  '__module__' : 'modules.data.tools.smart_recorder.proto.smart_recorder_triggers_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.Trigger)
  })
_sym_db.RegisterMessage(Trigger)

SmartRecordTrigger = _reflection.GeneratedProtocolMessageType('SmartRecordTrigger', (_message.Message,), {
  'DESCRIPTOR' : _SMARTRECORDTRIGGER,
  '__module__' : 'modules.data.tools.smart_recorder.proto.smart_recorder_triggers_pb2'
  # @@protoc_insertion_point(class_scope:apollo.data.SmartRecordTrigger)
  })
_sym_db.RegisterMessage(SmartRecordTrigger)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECORDSEGMENTSETTING._serialized_start=86
  _RECORDSEGMENTSETTING._serialized_end=162
  _TRIGGER._serialized_start=164
  _TRIGGER._serialized_end=278
  _SMARTRECORDTRIGGER._serialized_start=281
  _SMARTRECORDTRIGGER._serialized_end=524
# @@protoc_insertion_point(module_scope)
