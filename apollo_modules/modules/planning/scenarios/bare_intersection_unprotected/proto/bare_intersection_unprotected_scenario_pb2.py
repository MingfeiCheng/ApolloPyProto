# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/scenarios/bare_intersection_unprotected/proto/bare_intersection_unprotected_scenario.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nkmodules/planning/scenarios/bare_intersection_unprotected/proto/bare_intersection_unprotected_scenario.proto\x12\x0f\x61pollo.planning\"\xca\x01\n)ScenarioBareIntersectionUnprotectedConfig\x12\x35\n)start_bare_intersection_scenario_distance\x18\x01 \x01(\x01:\x02\x32\x35\x12#\n\x14\x65nable_explicit_stop\x18\x02 \x01(\x08:\x05\x66\x61lse\x12%\n\x15\x61pproach_cruise_speed\x18\x03 \x01(\x01:\x06\x36.7056\x12\x1a\n\rstop_distance\x18\x04 \x01(\x01:\x03\x30.5')



_SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG = DESCRIPTOR.message_types_by_name['ScenarioBareIntersectionUnprotectedConfig']
ScenarioBareIntersectionUnprotectedConfig = _reflection.GeneratedProtocolMessageType('ScenarioBareIntersectionUnprotectedConfig', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG,
  '__module__' : 'modules.planning.scenarios.bare_intersection_unprotected.proto.bare_intersection_unprotected_scenario_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ScenarioBareIntersectionUnprotectedConfig)
  })
_sym_db.RegisterMessage(ScenarioBareIntersectionUnprotectedConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG._serialized_start=129
  _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG._serialized_end=331
# @@protoc_insertion_point(module_scope)
