# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/scenarios/park_and_go/proto/park_and_go.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/planning/scenarios/park_and_go/proto/park_and_go.proto\x12\x0f\x61pollo.planning\"\xa7\x01\n\x17ScenarioParkAndGoConfig\x12 \n\x15\x66ront_obstacle_buffer\x18\x01 \x01(\x01:\x01\x34\x12\x1b\n\x0eheading_buffer\x18\x02 \x01(\x01:\x03\x30.5\x12\x1c\n\x10min_dist_to_dest\x18\x03 \x01(\x01:\x02\x32\x35\x12/\n#max_steering_percentage_when_cruise\x18\x04 \x01(\x01:\x02\x39\x30')



_SCENARIOPARKANDGOCONFIG = DESCRIPTOR.message_types_by_name['ScenarioParkAndGoConfig']
ScenarioParkAndGoConfig = _reflection.GeneratedProtocolMessageType('ScenarioParkAndGoConfig', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIOPARKANDGOCONFIG,
  '__module__' : 'modules.planning.scenarios.park_and_go.proto.park_and_go_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ScenarioParkAndGoConfig)
  })
_sym_db.RegisterMessage(ScenarioParkAndGoConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCENARIOPARKANDGOCONFIG._serialized_start=84
  _SCENARIOPARKANDGOCONFIG._serialized_end=251
# @@protoc_insertion_point(module_scope)