# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/dreamview/proto/record.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$modules/dreamview/proto/record.proto\x12\x10\x61pollo.dreamview\"q\n\nRecordList\x12\x11\n\trecord_id\x18\x01 \x03(\t\x12\x0e\n\x06userid\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\x05\x12\x16\n\x0e\x64\x65scription_cn\x18\x04 \x01(\t\x12\x16\n\x0e\x64\x65scription_en\x18\x05 \x01(\t\"m\n\x06Record\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x0e\n\x06userid\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\x05\x12\x16\n\x0e\x64\x65scription_cn\x18\x04 \x01(\t\x12\x16\n\x0e\x64\x65scription_en\x18\x05 \x01(\t')



_RECORDLIST = DESCRIPTOR.message_types_by_name['RecordList']
_RECORD = DESCRIPTOR.message_types_by_name['Record']
RecordList = _reflection.GeneratedProtocolMessageType('RecordList', (_message.Message,), {
  'DESCRIPTOR' : _RECORDLIST,
  '__module__' : 'modules.dreamview.proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.RecordList)
  })
_sym_db.RegisterMessage(RecordList)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'modules.dreamview.proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.Record)
  })
_sym_db.RegisterMessage(Record)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECORDLIST._serialized_start=58
  _RECORDLIST._serialized_end=171
  _RECORD._serialized_start=173
  _RECORD._serialized_end=282
# @@protoc_insertion_point(module_scope)
