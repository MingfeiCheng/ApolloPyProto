# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/tasks/speed_decider/proto/speed_decider.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/planning/tasks/speed_decider/proto/speed_decider.proto\x12\x0f\x61pollo.planning\"\x99\x02\n\x12SpeedDeciderConfig\x12,\n\x1f\x66ollow_min_obs_lateral_distance\x18\x01 \x01(\x01:\x03\x32.5\x12\x1e\n\x13\x66ollow_min_time_sec\x18\x02 \x01(\x01:\x01\x32\x12%\n\x16is_stop_for_pedestrain\x18\x03 \x01(\x08:\x05\x66\x61lse\x12(\n\x1bkeep_clear_last_point_speed\x18\x04 \x01(\x01:\x03\x30.8\x12\x1f\n\x14overtake_time_buffer\x18\x05 \x01(\x01:\x01\x33\x12!\n\x15overtake_min_distance\x18\x06 \x01(\x01:\x02\x31\x30\x12 \n\x15yield_distance_buffer\x18\x07 \x01(\x01:\x01\x35')



_SPEEDDECIDERCONFIG = DESCRIPTOR.message_types_by_name['SpeedDeciderConfig']
SpeedDeciderConfig = _reflection.GeneratedProtocolMessageType('SpeedDeciderConfig', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDDECIDERCONFIG,
  '__module__' : 'modules.planning.tasks.speed_decider.proto.speed_decider_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.SpeedDeciderConfig)
  })
_sym_db.RegisterMessage(SpeedDeciderConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SPEEDDECIDERCONFIG._serialized_start=84
  _SPEEDDECIDERCONFIG._serialized_end=365
# @@protoc_insertion_point(module_scope)
