# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/planners/navi/proto/planner_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.planning.planners.navi.proto import navi_task_config_pb2 as modules_dot_planning_dot_planners_dot_navi_dot_proto_dot_navi__task__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/planning/planners/navi/proto/planner_config.proto\x12\x0f\x61pollo.planning\x1a;modules/planning/planners/navi/proto/navi_task_config.proto\"\xa8\x02\n\x11PlannerNaviConfig\x12+\n\x04task\x18\x01 \x03(\x0e\x32\x1d.apollo.planning.NaviTaskType\x12H\n\x18navi_path_decider_config\x18\x02 \x01(\x0b\x32&.apollo.planning.NaviPathDeciderConfig\x12J\n\x19navi_speed_decider_config\x18\x03 \x01(\x0b\x32\'.apollo.planning.NaviSpeedDeciderConfig\x12P\n\x1cnavi_obstacle_decider_config\x18\x04 \x01(\x0b\x32*.apollo.planning.NaviObstacleDeciderConfig')



_PLANNERNAVICONFIG = DESCRIPTOR.message_types_by_name['PlannerNaviConfig']
PlannerNaviConfig = _reflection.GeneratedProtocolMessageType('PlannerNaviConfig', (_message.Message,), {
  'DESCRIPTOR' : _PLANNERNAVICONFIG,
  '__module__' : 'modules.planning.planners.navi.proto.planner_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.PlannerNaviConfig)
  })
_sym_db.RegisterMessage(PlannerNaviConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLANNERNAVICONFIG._serialized_start=140
  _PLANNERNAVICONFIG._serialized_end=436
# @@protoc_insertion_point(module_scope)
