# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/scenarios/stop_sign_unprotected/proto/stop_sign_unprotected.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.planning.planning_interface_base.scenario_base.proto import creep_stage_pb2 as modules_dot_planning_dot_planning__interface__base_dot_scenario__base_dot_proto_dot_creep__stage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRmodules/planning/scenarios/stop_sign_unprotected/proto/stop_sign_unprotected.proto\x12\x0f\x61pollo.planning\x1aNmodules/planning/planning_interface_base/scenario_base/proto/creep_stage.proto\"\xc2\x02\n!ScenarioStopSignUnprotectedConfig\x12,\n!start_stop_sign_scenario_distance\x18\x01 \x01(\x01:\x01\x35\x12\x30\n%watch_vehicle_max_valid_stop_distance\x18\x02 \x01(\x01:\x01\x35\x12$\n\x17max_valid_stop_distance\x18\x03 \x01(\x01:\x03\x33.5\x12\x1c\n\x11stop_duration_sec\x18\x04 \x01(\x02:\x01\x31\x12\x1b\n\x10stop_timeout_sec\x18\x05 \x01(\x02:\x01\x38\x12\x1d\n\x11\x63reep_timeout_sec\x18\x06 \x01(\x02:\x02\x31\x30\x12=\n\x12\x63reep_stage_config\x18\x07 \x01(\x0b\x32!.apollo.planning.CreepStageConfig')



_SCENARIOSTOPSIGNUNPROTECTEDCONFIG = DESCRIPTOR.message_types_by_name['ScenarioStopSignUnprotectedConfig']
ScenarioStopSignUnprotectedConfig = _reflection.GeneratedProtocolMessageType('ScenarioStopSignUnprotectedConfig', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIOSTOPSIGNUNPROTECTEDCONFIG,
  '__module__' : 'modules.planning.scenarios.stop_sign_unprotected.proto.stop_sign_unprotected_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ScenarioStopSignUnprotectedConfig)
  })
_sym_db.RegisterMessage(ScenarioStopSignUnprotectedConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCENARIOSTOPSIGNUNPROTECTEDCONFIG._serialized_start=184
  _SCENARIOSTOPSIGNUNPROTECTEDCONFIG._serialized_end=506
# @@protoc_insertion_point(module_scope)
