# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/planning_msgs/scenario_type.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5modules/common_msgs/planning_msgs/scenario_type.proto\x12\x0f\x61pollo.planning*\xa3\x03\n\x0cScenarioType\x12\x0f\n\x0bLANE_FOLLOW\x10\x00\x12!\n\x1d\x42\x41RE_INTERSECTION_UNPROTECTED\x10\x02\x12\x17\n\x13STOP_SIGN_PROTECTED\x10\x03\x12\x19\n\x15STOP_SIGN_UNPROTECTED\x10\x04\x12\x1b\n\x17TRAFFIC_LIGHT_PROTECTED\x10\x05\x12\'\n#TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN\x10\x06\x12(\n$TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN\x10\x07\x12\x0e\n\nYIELD_SIGN\x10\x08\x12\r\n\tPULL_OVER\x10\t\x12\x11\n\rVALET_PARKING\x10\n\x12\x17\n\x13\x45MERGENCY_PULL_OVER\x10\x0b\x12\x12\n\x0e\x45MERGENCY_STOP\x10\x0c\x12\x18\n\x14NARROW_STREET_U_TURN\x10\r\x12\x0f\n\x0bPARK_AND_GO\x10\x0e\x12\x19\n\x15LEARNING_MODEL_SAMPLE\x10\x0f\x12\x16\n\x12\x44\x45\x41\x44\x45ND_TURNAROUND\x10\x10*\x9f\n\n\tStageType\x12\x0c\n\x08NO_STAGE\x10\x00\x12\x1d\n\x19LANE_FOLLOW_DEFAULT_STAGE\x10\x01\x12+\n&BARE_INTERSECTION_UNPROTECTED_APPROACH\x10\xc8\x01\x12\x36\n1BARE_INTERSECTION_UNPROTECTED_INTERSECTION_CRUISE\x10\xc9\x01\x12#\n\x1eSTOP_SIGN_UNPROTECTED_PRE_STOP\x10\xac\x02\x12\x1f\n\x1aSTOP_SIGN_UNPROTECTED_STOP\x10\xad\x02\x12 \n\x1bSTOP_SIGN_UNPROTECTED_CREEP\x10\xae\x02\x12.\n)STOP_SIGN_UNPROTECTED_INTERSECTION_CRUISE\x10\xaf\x02\x12%\n TRAFFIC_LIGHT_PROTECTED_APPROACH\x10\x90\x03\x12\x30\n+TRAFFIC_LIGHT_PROTECTED_INTERSECTION_CRUISE\x10\x91\x03\x12\x31\n,TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_APPROACH\x10\x9a\x03\x12.\n)TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_CREEP\x10\x9b\x03\x12<\n7TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_INTERSECTION_CRUISE\x10\x9c\x03\x12.\n)TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_STOP\x10\xa4\x03\x12/\n*TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_CREEP\x10\xa5\x03\x12=\n8TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_INTERSECTION_CRUISE\x10\xa6\x03\x12\x17\n\x12PULL_OVER_APPROACH\x10\xf4\x03\x12%\n PULL_OVER_RETRY_APPROACH_PARKING\x10\xf5\x03\x12\x1c\n\x17PULL_OVER_RETRY_PARKING\x10\xf6\x03\x12\"\n\x1d\x45MERGENCY_PULL_OVER_SLOW_DOWN\x10\xd8\x04\x12!\n\x1c\x45MERGENCY_PULL_OVER_APPROACH\x10\xd9\x04\x12 \n\x1b\x45MERGENCY_PULL_OVER_STANDBY\x10\xda\x04\x12\x1c\n\x17\x45MERGENCY_STOP_APPROACH\x10\xe2\x04\x12\x1b\n\x16\x45MERGENCY_STOP_STANDBY\x10\xe3\x04\x12+\n&VALET_PARKING_APPROACHING_PARKING_SPOT\x10\xbc\x05\x12\x1a\n\x15VALET_PARKING_PARKING\x10\xbd\x05\x12\x31\n,DEADEND_TURNAROUND_APPROACHING_TURNING_POINT\x10\xcc\x08\x12\x1f\n\x1a\x44\x45\x41\x44\x45ND_TURNAROUND_TURNING\x10\xcd\x08\x12\x16\n\x11PARK_AND_GO_CHECK\x10\xa0\x06\x12\x17\n\x12PARK_AND_GO_CRUISE\x10\xa1\x06\x12\x17\n\x12PARK_AND_GO_ADJUST\x10\xa2\x06\x12\x1b\n\x16PARK_AND_GO_PRE_CRUISE\x10\xa3\x06\x12\x18\n\x13YIELD_SIGN_APPROACH\x10\x84\x07\x12\x15\n\x10YIELD_SIGN_CREEP\x10\x85\x07\x12\x17\n\x12LEARNING_MODEL_RUN\x10\xe8\x07')

_SCENARIOTYPE = DESCRIPTOR.enum_types_by_name['ScenarioType']
ScenarioType = enum_type_wrapper.EnumTypeWrapper(_SCENARIOTYPE)
_STAGETYPE = DESCRIPTOR.enum_types_by_name['StageType']
StageType = enum_type_wrapper.EnumTypeWrapper(_STAGETYPE)
LANE_FOLLOW = 0
BARE_INTERSECTION_UNPROTECTED = 2
STOP_SIGN_PROTECTED = 3
STOP_SIGN_UNPROTECTED = 4
TRAFFIC_LIGHT_PROTECTED = 5
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN = 6
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN = 7
YIELD_SIGN = 8
PULL_OVER = 9
VALET_PARKING = 10
EMERGENCY_PULL_OVER = 11
EMERGENCY_STOP = 12
NARROW_STREET_U_TURN = 13
PARK_AND_GO = 14
LEARNING_MODEL_SAMPLE = 15
DEADEND_TURNAROUND = 16
NO_STAGE = 0
LANE_FOLLOW_DEFAULT_STAGE = 1
BARE_INTERSECTION_UNPROTECTED_APPROACH = 200
BARE_INTERSECTION_UNPROTECTED_INTERSECTION_CRUISE = 201
STOP_SIGN_UNPROTECTED_PRE_STOP = 300
STOP_SIGN_UNPROTECTED_STOP = 301
STOP_SIGN_UNPROTECTED_CREEP = 302
STOP_SIGN_UNPROTECTED_INTERSECTION_CRUISE = 303
TRAFFIC_LIGHT_PROTECTED_APPROACH = 400
TRAFFIC_LIGHT_PROTECTED_INTERSECTION_CRUISE = 401
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_APPROACH = 410
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_CREEP = 411
TRAFFIC_LIGHT_UNPROTECTED_LEFT_TURN_INTERSECTION_CRUISE = 412
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_STOP = 420
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_CREEP = 421
TRAFFIC_LIGHT_UNPROTECTED_RIGHT_TURN_INTERSECTION_CRUISE = 422
PULL_OVER_APPROACH = 500
PULL_OVER_RETRY_APPROACH_PARKING = 501
PULL_OVER_RETRY_PARKING = 502
EMERGENCY_PULL_OVER_SLOW_DOWN = 600
EMERGENCY_PULL_OVER_APPROACH = 601
EMERGENCY_PULL_OVER_STANDBY = 602
EMERGENCY_STOP_APPROACH = 610
EMERGENCY_STOP_STANDBY = 611
VALET_PARKING_APPROACHING_PARKING_SPOT = 700
VALET_PARKING_PARKING = 701
DEADEND_TURNAROUND_APPROACHING_TURNING_POINT = 1100
DEADEND_TURNAROUND_TURNING = 1101
PARK_AND_GO_CHECK = 800
PARK_AND_GO_CRUISE = 801
PARK_AND_GO_ADJUST = 802
PARK_AND_GO_PRE_CRUISE = 803
YIELD_SIGN_APPROACH = 900
YIELD_SIGN_CREEP = 901
LEARNING_MODEL_RUN = 1000


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCENARIOTYPE._serialized_start=75
  _SCENARIOTYPE._serialized_end=494
  _STAGETYPE._serialized_start=497
  _STAGETYPE._serialized_end=1808
# @@protoc_insertion_point(module_scope)
