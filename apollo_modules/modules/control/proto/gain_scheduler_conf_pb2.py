# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/control/proto/gain_scheduler_conf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/control/proto/gain_scheduler_conf.proto\x12\x0e\x61pollo.control\"E\n\rGainScheduler\x12\x34\n\tscheduler\x18\x01 \x03(\x0b\x32!.apollo.control.GainSchedulerInfo\"1\n\x11GainSchedulerInfo\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\r\n\x05ratio\x18\x02 \x01(\x01')



_GAINSCHEDULER = DESCRIPTOR.message_types_by_name['GainScheduler']
_GAINSCHEDULERINFO = DESCRIPTOR.message_types_by_name['GainSchedulerInfo']
GainScheduler = _reflection.GeneratedProtocolMessageType('GainScheduler', (_message.Message,), {
  'DESCRIPTOR' : _GAINSCHEDULER,
  '__module__' : 'modules.control.proto.gain_scheduler_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.GainScheduler)
  })
_sym_db.RegisterMessage(GainScheduler)

GainSchedulerInfo = _reflection.GeneratedProtocolMessageType('GainSchedulerInfo', (_message.Message,), {
  'DESCRIPTOR' : _GAINSCHEDULERINFO,
  '__module__' : 'modules.control.proto.gain_scheduler_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.GainSchedulerInfo)
  })
_sym_db.RegisterMessage(GainSchedulerInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GAINSCHEDULER._serialized_start=67
  _GAINSCHEDULER._serialized_end=136
  _GAINSCHEDULERINFO._serialized_start=138
  _GAINSCHEDULERINFO._serialized_end=187
# @@protoc_insertion_point(module_scope)
