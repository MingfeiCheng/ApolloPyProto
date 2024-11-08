# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/planning_msgs/decision.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_modules.modules.common_msgs.basic_msgs import vehicle_signal_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_vehicle__signal__pb2
from apollo_modules.modules.common_msgs.routing_msgs import geometry_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/common_msgs/planning_msgs/decision.proto\x12\x0f\x61pollo.planning\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a\x33modules/common_msgs/basic_msgs/vehicle_signal.proto\x1a/modules/common_msgs/routing_msgs/geometry.proto\"M\n\nTargetLane\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07start_s\x18\x02 \x01(\x01\x12\r\n\x05\x65nd_s\x18\x03 \x01(\x01\x12\x13\n\x0bspeed_limit\x18\x04 \x01(\x01\"\x0e\n\x0cObjectIgnore\"\xb4\x01\n\nObjectStop\x12\x34\n\x0breason_code\x18\x01 \x01(\x0e\x32\x1f.apollo.planning.StopReasonCode\x12\x12\n\ndistance_s\x18\x02 \x01(\x01\x12+\n\nstop_point\x18\x03 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\x14\n\x0cstop_heading\x18\x04 \x01(\x01\x12\x19\n\x11wait_for_obstacle\x18\x05 \x03(\t\"\xac\x01\n\x0bObjectNudge\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.apollo.planning.ObjectNudge.Type\x12\x12\n\ndistance_l\x18\x02 \x01(\x01\"X\n\x04Type\x12\x0e\n\nLEFT_NUDGE\x10\x01\x12\x0f\n\x0bRIGHT_NUDGE\x10\x02\x12\x16\n\x12\x44YNAMIC_LEFT_NUDGE\x10\x03\x12\x17\n\x13\x44YNAMIC_RIGHT_NUDGE\x10\x04\"{\n\x0bObjectYield\x12\x12\n\ndistance_s\x18\x01 \x01(\x01\x12,\n\x0b\x66\x65nce_point\x18\x02 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\x15\n\rfence_heading\x18\x03 \x01(\x01\x12\x13\n\x0btime_buffer\x18\x04 \x01(\x01\"g\n\x0cObjectFollow\x12\x12\n\ndistance_s\x18\x01 \x01(\x01\x12,\n\x0b\x66\x65nce_point\x18\x02 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\x15\n\rfence_heading\x18\x03 \x01(\x01\"~\n\x0eObjectOvertake\x12\x12\n\ndistance_s\x18\x01 \x01(\x01\x12,\n\x0b\x66\x65nce_point\x18\x02 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\x15\n\rfence_heading\x18\x03 \x01(\x01\x12\x13\n\x0btime_buffer\x18\x04 \x01(\x01\"a\n\x0eObjectSidePass\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.apollo.planning.ObjectSidePass.Type\"\x1b\n\x04Type\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\"\r\n\x0bObjectAvoid\"\x82\x01\n\x0cObjectStatus\x12\x36\n\x0bmotion_type\x18\x01 \x01(\x0b\x32!.apollo.planning.ObjectMotionType\x12:\n\rdecision_type\x18\x02 \x01(\x0b\x32#.apollo.planning.ObjectDecisionType\"\x0e\n\x0cObjectStatic\"\x0f\n\rObjectDynamic\"\x84\x01\n\x10ObjectMotionType\x12/\n\x06static\x18\x01 \x01(\x0b\x32\x1d.apollo.planning.ObjectStaticH\x00\x12\x31\n\x07\x64ynamic\x18\x02 \x01(\x0b\x32\x1e.apollo.planning.ObjectDynamicH\x00\x42\x0c\n\nmotion_tag\"\xa9\x03\n\x12ObjectDecisionType\x12/\n\x06ignore\x18\x01 \x01(\x0b\x32\x1d.apollo.planning.ObjectIgnoreH\x00\x12+\n\x04stop\x18\x02 \x01(\x0b\x32\x1b.apollo.planning.ObjectStopH\x00\x12/\n\x06\x66ollow\x18\x03 \x01(\x0b\x32\x1d.apollo.planning.ObjectFollowH\x00\x12-\n\x05yield\x18\x04 \x01(\x0b\x32\x1c.apollo.planning.ObjectYieldH\x00\x12\x33\n\x08overtake\x18\x05 \x01(\x0b\x32\x1f.apollo.planning.ObjectOvertakeH\x00\x12-\n\x05nudge\x18\x06 \x01(\x0b\x32\x1c.apollo.planning.ObjectNudgeH\x00\x12-\n\x05\x61void\x18\x07 \x01(\x0b\x32\x1c.apollo.planning.ObjectAvoidH\x00\x12\x34\n\tside_pass\x18\x08 \x01(\x0b\x32\x1f.apollo.planning.ObjectSidePassH\x00\x42\x0c\n\nobject_tag\"q\n\x0eObjectDecision\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rperception_id\x18\x02 \x01(\x05\x12<\n\x0fobject_decision\x18\x03 \x03(\x0b\x32#.apollo.planning.ObjectDecisionType\"D\n\x0fObjectDecisions\x12\x31\n\x08\x64\x65\x63ision\x18\x01 \x03(\x0b\x32\x1f.apollo.planning.ObjectDecision\"\xcd\x01\n\x08MainStop\x12\x34\n\x0breason_code\x18\x01 \x01(\x0e\x32\x1f.apollo.planning.StopReasonCode\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12+\n\nstop_point\x18\x03 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\x14\n\x0cstop_heading\x18\x04 \x01(\x01\x12\x38\n\x10\x63hange_lane_type\x18\x05 \x01(\x0e\x32\x1e.apollo.routing.ChangeLaneType\"\x18\n\x16\x45mergencyStopHardBrake\"\x1b\n\x19\x45mergencyStopCruiseToStop\"\x9f\x03\n\x11MainEmergencyStop\x12\x42\n\x0breason_code\x18\x01 \x01(\x0e\x32-.apollo.planning.MainEmergencyStop.ReasonCode\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12=\n\nhard_brake\x18\x03 \x01(\x0b\x32\'.apollo.planning.EmergencyStopHardBrakeH\x00\x12\x44\n\x0e\x63ruise_to_stop\x18\x04 \x01(\x0b\x32*.apollo.planning.EmergencyStopCruiseToStopH\x00\"\xa8\x01\n\nReasonCode\x12\x1d\n\x19\x45STOP_REASON_INTERNAL_ERR\x10\x01\x12\x1a\n\x16\x45STOP_REASON_COLLISION\x10\x02\x12\x1d\n\x19\x45STOP_REASON_ST_FIND_PATH\x10\x03\x12!\n\x1d\x45STOP_REASON_ST_MAKE_DECISION\x10\x04\x12\x1d\n\x19\x45STOP_REASON_SENSOR_ERROR\x10\x05\x42\x06\n\x04task\"F\n\nMainCruise\x12\x38\n\x10\x63hange_lane_type\x18\x01 \x01(\x0e\x32\x1e.apollo.routing.ChangeLaneType\"\xff\x01\n\x0eMainChangeLane\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.apollo.planning.MainChangeLane.Type\x12\x31\n\x0c\x64\x65\x66\x61ult_lane\x18\x02 \x03(\x0b\x32\x1b.apollo.planning.TargetLane\x12\x34\n\x11\x64\x65\x66\x61ult_lane_stop\x18\x03 \x01(\x0b\x32\x19.apollo.planning.MainStop\x12\x33\n\x10target_lane_stop\x18\x04 \x01(\x0b\x32\x19.apollo.planning.MainStop\"\x1b\n\x04Type\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\"X\n\x13MainMissionComplete\x12+\n\nstop_point\x18\x01 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\x14\n\x0cstop_heading\x18\x02 \x01(\x01\"\x1e\n\x0cMainNotReady\x12\x0e\n\x06reason\x18\x01 \x01(\t\"j\n\x0bMainParking\x12:\n\x06status\x18\x01 \x01(\x0e\x32*.apollo.planning.MainParking.ParkingStatus\"\x1f\n\rParkingStatus\x12\x0e\n\nIN_PARKING\x10\x01\"\xbe\x03\n\x0cMainDecision\x12-\n\x06\x63ruise\x18\x01 \x01(\x0b\x32\x1b.apollo.planning.MainCruiseH\x00\x12)\n\x04stop\x18\x02 \x01(\x0b\x32\x19.apollo.planning.MainStopH\x00\x12\x33\n\x05\x65stop\x18\x03 \x01(\x0b\x32\".apollo.planning.MainEmergencyStopH\x00\x12:\n\x0b\x63hange_lane\x18\x04 \x01(\x0b\x32\x1f.apollo.planning.MainChangeLaneB\x02\x18\x01H\x00\x12@\n\x10mission_complete\x18\x06 \x01(\x0b\x32$.apollo.planning.MainMissionCompleteH\x00\x12\x32\n\tnot_ready\x18\x07 \x01(\x0b\x32\x1d.apollo.planning.MainNotReadyH\x00\x12/\n\x07parking\x18\x08 \x01(\x0b\x32\x1c.apollo.planning.MainParkingH\x00\x12\x34\n\x0btarget_lane\x18\x05 \x03(\x0b\x32\x1b.apollo.planning.TargetLaneB\x02\x18\x01\x42\x06\n\x04task\"\xb7\x01\n\x0e\x44\x65\x63isionResult\x12\x34\n\rmain_decision\x18\x01 \x01(\x0b\x32\x1d.apollo.planning.MainDecision\x12\x39\n\x0fobject_decision\x18\x02 \x01(\x0b\x32 .apollo.planning.ObjectDecisions\x12\x34\n\x0evehicle_signal\x18\x03 \x01(\x0b\x32\x1c.apollo.common.VehicleSignal*\x9e\x04\n\x0eStopReasonCode\x12\x1c\n\x18STOP_REASON_HEAD_VEHICLE\x10\x01\x12\x1b\n\x17STOP_REASON_DESTINATION\x10\x02\x12\x1a\n\x16STOP_REASON_PEDESTRIAN\x10\x03\x12\x18\n\x14STOP_REASON_OBSTACLE\x10\x04\x12\x1a\n\x16STOP_REASON_PREPARKING\x10\x05\x12\x16\n\x12STOP_REASON_SIGNAL\x10\x64\x12\x19\n\x15STOP_REASON_STOP_SIGN\x10\x65\x12\x1a\n\x16STOP_REASON_YIELD_SIGN\x10\x66\x12\x1a\n\x16STOP_REASON_CLEAR_ZONE\x10g\x12\x19\n\x15STOP_REASON_CROSSWALK\x10h\x12\x17\n\x13STOP_REASON_CREEPER\x10i\x12\x1d\n\x19STOP_REASON_REFERENCE_END\x10j\x12\x1d\n\x19STOP_REASON_YELLOW_SIGNAL\x10k\x12\x19\n\x15STOP_REASON_PULL_OVER\x10l\x12\x1f\n\x1bSTOP_REASON_SIDEPASS_SAFETY\x10m\x12$\n\x1fSTOP_REASON_PRE_OPEN_SPACE_STOP\x10\xc8\x01\x12$\n\x1fSTOP_REASON_LANE_CHANGE_URGENCY\x10\xc9\x01\x12\x1a\n\x15STOP_REASON_EMERGENCY\x10\xca\x01')

_STOPREASONCODE = DESCRIPTOR.enum_types_by_name['StopReasonCode']
StopReasonCode = enum_type_wrapper.EnumTypeWrapper(_STOPREASONCODE)
STOP_REASON_HEAD_VEHICLE = 1
STOP_REASON_DESTINATION = 2
STOP_REASON_PEDESTRIAN = 3
STOP_REASON_OBSTACLE = 4
STOP_REASON_PREPARKING = 5
STOP_REASON_SIGNAL = 100
STOP_REASON_STOP_SIGN = 101
STOP_REASON_YIELD_SIGN = 102
STOP_REASON_CLEAR_ZONE = 103
STOP_REASON_CROSSWALK = 104
STOP_REASON_CREEPER = 105
STOP_REASON_REFERENCE_END = 106
STOP_REASON_YELLOW_SIGNAL = 107
STOP_REASON_PULL_OVER = 108
STOP_REASON_SIDEPASS_SAFETY = 109
STOP_REASON_PRE_OPEN_SPACE_STOP = 200
STOP_REASON_LANE_CHANGE_URGENCY = 201
STOP_REASON_EMERGENCY = 202


_TARGETLANE = DESCRIPTOR.message_types_by_name['TargetLane']
_OBJECTIGNORE = DESCRIPTOR.message_types_by_name['ObjectIgnore']
_OBJECTSTOP = DESCRIPTOR.message_types_by_name['ObjectStop']
_OBJECTNUDGE = DESCRIPTOR.message_types_by_name['ObjectNudge']
_OBJECTYIELD = DESCRIPTOR.message_types_by_name['ObjectYield']
_OBJECTFOLLOW = DESCRIPTOR.message_types_by_name['ObjectFollow']
_OBJECTOVERTAKE = DESCRIPTOR.message_types_by_name['ObjectOvertake']
_OBJECTSIDEPASS = DESCRIPTOR.message_types_by_name['ObjectSidePass']
_OBJECTAVOID = DESCRIPTOR.message_types_by_name['ObjectAvoid']
_OBJECTSTATUS = DESCRIPTOR.message_types_by_name['ObjectStatus']
_OBJECTSTATIC = DESCRIPTOR.message_types_by_name['ObjectStatic']
_OBJECTDYNAMIC = DESCRIPTOR.message_types_by_name['ObjectDynamic']
_OBJECTMOTIONTYPE = DESCRIPTOR.message_types_by_name['ObjectMotionType']
_OBJECTDECISIONTYPE = DESCRIPTOR.message_types_by_name['ObjectDecisionType']
_OBJECTDECISION = DESCRIPTOR.message_types_by_name['ObjectDecision']
_OBJECTDECISIONS = DESCRIPTOR.message_types_by_name['ObjectDecisions']
_MAINSTOP = DESCRIPTOR.message_types_by_name['MainStop']
_EMERGENCYSTOPHARDBRAKE = DESCRIPTOR.message_types_by_name['EmergencyStopHardBrake']
_EMERGENCYSTOPCRUISETOSTOP = DESCRIPTOR.message_types_by_name['EmergencyStopCruiseToStop']
_MAINEMERGENCYSTOP = DESCRIPTOR.message_types_by_name['MainEmergencyStop']
_MAINCRUISE = DESCRIPTOR.message_types_by_name['MainCruise']
_MAINCHANGELANE = DESCRIPTOR.message_types_by_name['MainChangeLane']
_MAINMISSIONCOMPLETE = DESCRIPTOR.message_types_by_name['MainMissionComplete']
_MAINNOTREADY = DESCRIPTOR.message_types_by_name['MainNotReady']
_MAINPARKING = DESCRIPTOR.message_types_by_name['MainParking']
_MAINDECISION = DESCRIPTOR.message_types_by_name['MainDecision']
_DECISIONRESULT = DESCRIPTOR.message_types_by_name['DecisionResult']
_OBJECTNUDGE_TYPE = _OBJECTNUDGE.enum_types_by_name['Type']
_OBJECTSIDEPASS_TYPE = _OBJECTSIDEPASS.enum_types_by_name['Type']
_MAINEMERGENCYSTOP_REASONCODE = _MAINEMERGENCYSTOP.enum_types_by_name['ReasonCode']
_MAINCHANGELANE_TYPE = _MAINCHANGELANE.enum_types_by_name['Type']
_MAINPARKING_PARKINGSTATUS = _MAINPARKING.enum_types_by_name['ParkingStatus']
TargetLane = _reflection.GeneratedProtocolMessageType('TargetLane', (_message.Message,), {
  'DESCRIPTOR' : _TARGETLANE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.TargetLane)
  })
_sym_db.RegisterMessage(TargetLane)

ObjectIgnore = _reflection.GeneratedProtocolMessageType('ObjectIgnore', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTIGNORE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectIgnore)
  })
_sym_db.RegisterMessage(ObjectIgnore)

ObjectStop = _reflection.GeneratedProtocolMessageType('ObjectStop', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTOP,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectStop)
  })
_sym_db.RegisterMessage(ObjectStop)

ObjectNudge = _reflection.GeneratedProtocolMessageType('ObjectNudge', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTNUDGE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectNudge)
  })
_sym_db.RegisterMessage(ObjectNudge)

ObjectYield = _reflection.GeneratedProtocolMessageType('ObjectYield', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTYIELD,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectYield)
  })
_sym_db.RegisterMessage(ObjectYield)

ObjectFollow = _reflection.GeneratedProtocolMessageType('ObjectFollow', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTFOLLOW,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectFollow)
  })
_sym_db.RegisterMessage(ObjectFollow)

ObjectOvertake = _reflection.GeneratedProtocolMessageType('ObjectOvertake', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTOVERTAKE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectOvertake)
  })
_sym_db.RegisterMessage(ObjectOvertake)

ObjectSidePass = _reflection.GeneratedProtocolMessageType('ObjectSidePass', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSIDEPASS,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectSidePass)
  })
_sym_db.RegisterMessage(ObjectSidePass)

ObjectAvoid = _reflection.GeneratedProtocolMessageType('ObjectAvoid', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTAVOID,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectAvoid)
  })
_sym_db.RegisterMessage(ObjectAvoid)

ObjectStatus = _reflection.GeneratedProtocolMessageType('ObjectStatus', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTATUS,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectStatus)
  })
_sym_db.RegisterMessage(ObjectStatus)

ObjectStatic = _reflection.GeneratedProtocolMessageType('ObjectStatic', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTATIC,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectStatic)
  })
_sym_db.RegisterMessage(ObjectStatic)

ObjectDynamic = _reflection.GeneratedProtocolMessageType('ObjectDynamic', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDYNAMIC,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectDynamic)
  })
_sym_db.RegisterMessage(ObjectDynamic)

ObjectMotionType = _reflection.GeneratedProtocolMessageType('ObjectMotionType', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMOTIONTYPE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectMotionType)
  })
_sym_db.RegisterMessage(ObjectMotionType)

ObjectDecisionType = _reflection.GeneratedProtocolMessageType('ObjectDecisionType', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDECISIONTYPE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectDecisionType)
  })
_sym_db.RegisterMessage(ObjectDecisionType)

ObjectDecision = _reflection.GeneratedProtocolMessageType('ObjectDecision', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDECISION,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectDecision)
  })
_sym_db.RegisterMessage(ObjectDecision)

ObjectDecisions = _reflection.GeneratedProtocolMessageType('ObjectDecisions', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDECISIONS,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ObjectDecisions)
  })
_sym_db.RegisterMessage(ObjectDecisions)

MainStop = _reflection.GeneratedProtocolMessageType('MainStop', (_message.Message,), {
  'DESCRIPTOR' : _MAINSTOP,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainStop)
  })
_sym_db.RegisterMessage(MainStop)

EmergencyStopHardBrake = _reflection.GeneratedProtocolMessageType('EmergencyStopHardBrake', (_message.Message,), {
  'DESCRIPTOR' : _EMERGENCYSTOPHARDBRAKE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.EmergencyStopHardBrake)
  })
_sym_db.RegisterMessage(EmergencyStopHardBrake)

EmergencyStopCruiseToStop = _reflection.GeneratedProtocolMessageType('EmergencyStopCruiseToStop', (_message.Message,), {
  'DESCRIPTOR' : _EMERGENCYSTOPCRUISETOSTOP,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.EmergencyStopCruiseToStop)
  })
_sym_db.RegisterMessage(EmergencyStopCruiseToStop)

MainEmergencyStop = _reflection.GeneratedProtocolMessageType('MainEmergencyStop', (_message.Message,), {
  'DESCRIPTOR' : _MAINEMERGENCYSTOP,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainEmergencyStop)
  })
_sym_db.RegisterMessage(MainEmergencyStop)

MainCruise = _reflection.GeneratedProtocolMessageType('MainCruise', (_message.Message,), {
  'DESCRIPTOR' : _MAINCRUISE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainCruise)
  })
_sym_db.RegisterMessage(MainCruise)

MainChangeLane = _reflection.GeneratedProtocolMessageType('MainChangeLane', (_message.Message,), {
  'DESCRIPTOR' : _MAINCHANGELANE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainChangeLane)
  })
_sym_db.RegisterMessage(MainChangeLane)

MainMissionComplete = _reflection.GeneratedProtocolMessageType('MainMissionComplete', (_message.Message,), {
  'DESCRIPTOR' : _MAINMISSIONCOMPLETE,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainMissionComplete)
  })
_sym_db.RegisterMessage(MainMissionComplete)

MainNotReady = _reflection.GeneratedProtocolMessageType('MainNotReady', (_message.Message,), {
  'DESCRIPTOR' : _MAINNOTREADY,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainNotReady)
  })
_sym_db.RegisterMessage(MainNotReady)

MainParking = _reflection.GeneratedProtocolMessageType('MainParking', (_message.Message,), {
  'DESCRIPTOR' : _MAINPARKING,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainParking)
  })
_sym_db.RegisterMessage(MainParking)

MainDecision = _reflection.GeneratedProtocolMessageType('MainDecision', (_message.Message,), {
  'DESCRIPTOR' : _MAINDECISION,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.MainDecision)
  })
_sym_db.RegisterMessage(MainDecision)

DecisionResult = _reflection.GeneratedProtocolMessageType('DecisionResult', (_message.Message,), {
  'DESCRIPTOR' : _DECISIONRESULT,
  '__module__' : 'modules.common_msgs.planning_msgs.decision_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.DecisionResult)
  })
_sym_db.RegisterMessage(DecisionResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAINDECISION.fields_by_name['change_lane']._options = None
  _MAINDECISION.fields_by_name['change_lane']._serialized_options = b'\030\001'
  _MAINDECISION.fields_by_name['target_lane']._options = None
  _MAINDECISION.fields_by_name['target_lane']._serialized_options = b'\030\001'
  _STOPREASONCODE._serialized_start=3934
  _STOPREASONCODE._serialized_end=4476
  _TARGETLANE._serialized_start=218
  _TARGETLANE._serialized_end=295
  _OBJECTIGNORE._serialized_start=297
  _OBJECTIGNORE._serialized_end=311
  _OBJECTSTOP._serialized_start=314
  _OBJECTSTOP._serialized_end=494
  _OBJECTNUDGE._serialized_start=497
  _OBJECTNUDGE._serialized_end=669
  _OBJECTNUDGE_TYPE._serialized_start=581
  _OBJECTNUDGE_TYPE._serialized_end=669
  _OBJECTYIELD._serialized_start=671
  _OBJECTYIELD._serialized_end=794
  _OBJECTFOLLOW._serialized_start=796
  _OBJECTFOLLOW._serialized_end=899
  _OBJECTOVERTAKE._serialized_start=901
  _OBJECTOVERTAKE._serialized_end=1027
  _OBJECTSIDEPASS._serialized_start=1029
  _OBJECTSIDEPASS._serialized_end=1126
  _OBJECTSIDEPASS_TYPE._serialized_start=1099
  _OBJECTSIDEPASS_TYPE._serialized_end=1126
  _OBJECTAVOID._serialized_start=1128
  _OBJECTAVOID._serialized_end=1141
  _OBJECTSTATUS._serialized_start=1144
  _OBJECTSTATUS._serialized_end=1274
  _OBJECTSTATIC._serialized_start=1276
  _OBJECTSTATIC._serialized_end=1290
  _OBJECTDYNAMIC._serialized_start=1292
  _OBJECTDYNAMIC._serialized_end=1307
  _OBJECTMOTIONTYPE._serialized_start=1310
  _OBJECTMOTIONTYPE._serialized_end=1442
  _OBJECTDECISIONTYPE._serialized_start=1445
  _OBJECTDECISIONTYPE._serialized_end=1870
  _OBJECTDECISION._serialized_start=1872
  _OBJECTDECISION._serialized_end=1985
  _OBJECTDECISIONS._serialized_start=1987
  _OBJECTDECISIONS._serialized_end=2055
  _MAINSTOP._serialized_start=2058
  _MAINSTOP._serialized_end=2263
  _EMERGENCYSTOPHARDBRAKE._serialized_start=2265
  _EMERGENCYSTOPHARDBRAKE._serialized_end=2289
  _EMERGENCYSTOPCRUISETOSTOP._serialized_start=2291
  _EMERGENCYSTOPCRUISETOSTOP._serialized_end=2318
  _MAINEMERGENCYSTOP._serialized_start=2321
  _MAINEMERGENCYSTOP._serialized_end=2736
  _MAINEMERGENCYSTOP_REASONCODE._serialized_start=2560
  _MAINEMERGENCYSTOP_REASONCODE._serialized_end=2728
  _MAINCRUISE._serialized_start=2738
  _MAINCRUISE._serialized_end=2808
  _MAINCHANGELANE._serialized_start=2811
  _MAINCHANGELANE._serialized_end=3066
  _MAINCHANGELANE_TYPE._serialized_start=1099
  _MAINCHANGELANE_TYPE._serialized_end=1126
  _MAINMISSIONCOMPLETE._serialized_start=3068
  _MAINMISSIONCOMPLETE._serialized_end=3156
  _MAINNOTREADY._serialized_start=3158
  _MAINNOTREADY._serialized_end=3188
  _MAINPARKING._serialized_start=3190
  _MAINPARKING._serialized_end=3296
  _MAINPARKING_PARKINGSTATUS._serialized_start=3265
  _MAINPARKING_PARKINGSTATUS._serialized_end=3296
  _MAINDECISION._serialized_start=3299
  _MAINDECISION._serialized_end=3745
  _DECISIONRESULT._serialized_start=3748
  _DECISIONRESULT._serialized_end=3931
# @@protoc_insertion_point(module_scope)
