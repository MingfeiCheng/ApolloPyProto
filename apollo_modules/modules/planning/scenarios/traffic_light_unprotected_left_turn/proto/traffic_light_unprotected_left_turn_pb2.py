# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/scenarios/traffic_light_unprotected_left_turn/proto/traffic_light_unprotected_left_turn.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.planning.planning_interface_base.scenario_base.proto import creep_stage_pb2 as modules_dot_planning_dot_planning__interface__base_dot_scenario__base_dot_proto_dot_creep__stage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nnmodules/planning/scenarios/traffic_light_unprotected_left_turn/proto/traffic_light_unprotected_left_turn.proto\x12\x0f\x61pollo.planning\x1aNmodules/planning/planning_interface_base/scenario_base/proto/creep_stage.proto\"\xb4\x02\n-ScenarioTrafficLightUnprotectedLeftTurnConfig\x12\x30\n%start_traffic_light_scenario_distance\x18\x01 \x01(\x01:\x01\x35\x12#\n\x15\x61pproach_cruise_speed\x18\x02 \x01(\x01:\x04\x32.78\x12$\n\x17max_valid_stop_distance\x18\x03 \x01(\x01:\x03\x33.5\x12\x1d\n\x11\x63reep_timeout_sec\x18\x04 \x01(\x02:\x02\x31\x30\x12(\n\x1amax_adc_speed_before_creep\x18\x05 \x01(\x01:\x04\x35.56\x12=\n\x12\x63reep_stage_config\x18\x06 \x01(\x0b\x32!.apollo.planning.CreepStageConfig')



_SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG = DESCRIPTOR.message_types_by_name['ScenarioTrafficLightUnprotectedLeftTurnConfig']
ScenarioTrafficLightUnprotectedLeftTurnConfig = _reflection.GeneratedProtocolMessageType('ScenarioTrafficLightUnprotectedLeftTurnConfig', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG,
  '__module__' : 'modules.planning.scenarios.traffic_light_unprotected_left_turn.proto.traffic_light_unprotected_left_turn_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ScenarioTrafficLightUnprotectedLeftTurnConfig)
  })
_sym_db.RegisterMessage(ScenarioTrafficLightUnprotectedLeftTurnConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG._serialized_start=212
  _SCENARIOTRAFFICLIGHTUNPROTECTEDLEFTTURNCONFIG._serialized_end=520
# @@protoc_insertion_point(module_scope)