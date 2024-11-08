# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/perception_msgs/perception_obstacle.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import error_code_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2
from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.basic_msgs import pnc_point_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_lane_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__lane__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=modules/common_msgs/perception_msgs/perception_obstacle.proto\x12\x11\x61pollo.perception\x1a/modules/common_msgs/basic_msgs/error_code.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a.modules/common_msgs/basic_msgs/pnc_point.proto\x1a+modules/common_msgs/map_msgs/map_lane.proto\"@\n\x06\x42\x42ox2D\x12\x0c\n\x04xmin\x18\x01 \x01(\x01\x12\x0c\n\x04ymin\x18\x02 \x01(\x01\x12\x0c\n\x04xmax\x18\x03 \x01(\x01\x12\x0c\n\x04ymax\x18\x04 \x01(\x01\"\xaf\x01\n\x0bLightStatus\x12\x15\n\rbrake_visible\x18\x01 \x01(\x01\x12\x17\n\x0f\x62rake_switch_on\x18\x02 \x01(\x01\x12\x19\n\x11left_turn_visible\x18\x03 \x01(\x01\x12\x1b\n\x13left_turn_switch_on\x18\x04 \x01(\x01\x12\x1a\n\x12right_turn_visible\x18\x05 \x01(\x01\x12\x1c\n\x14right_turn_switch_on\x18\x06 \x01(\x01\"\x83\x01\n\x0eV2XInformation\x12;\n\x08v2x_type\x18\x01 \x03(\x0e\x32).apollo.perception.V2XInformation.V2XType\"4\n\x07V2XType\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bZOMBIES_CAR\x10\x01\x12\x0e\n\nBLIND_ZONE\x10\x02\"\xfa\x02\n\x11SensorMeasurement\x12\x11\n\tsensor_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12(\n\x08position\x18\x03 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\r\n\x05theta\x18\x04 \x01(\x01\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12(\n\x08velocity\x18\x08 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x38\n\x04type\x18\t \x01(\x0e\x32*.apollo.perception.PerceptionObstacle.Type\x12?\n\x08sub_type\x18\n \x01(\x0e\x32-.apollo.perception.PerceptionObstacle.SubType\x12\x11\n\ttimestamp\x18\x0b \x01(\x01\x12&\n\x03\x62ox\x18\x0c \x01(\x0b\x32\x19.apollo.perception.BBox2D\"[\n\nTrajectory\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x12\x38\n\x10trajectory_point\x18\x02 \x03(\x0b\x32\x1e.apollo.common.TrajectoryPoint\"A\n\x0c\x44\x65\x62ugMessage\x12\x31\n\ntrajectory\x18\x01 \x03(\x0b\x32\x1d.apollo.perception.Trajectory\"\xd4\x0c\n\x12PerceptionObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x12(\n\x08position\x18\x02 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\r\n\x05theta\x18\x03 \x01(\x01\x12(\n\x08velocity\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12-\n\rpolygon_point\x18\x08 \x03(\x0b\x32\x16.apollo.common.Point3D\x12\x15\n\rtracking_time\x18\t \x01(\x01\x12\x38\n\x04type\x18\n \x01(\x0e\x32*.apollo.perception.PerceptionObstacle.Type\x12\x11\n\ttimestamp\x18\x0b \x01(\x01\x12\x17\n\x0bpoint_cloud\x18\x0c \x03(\x01\x42\x02\x10\x01\x12\x12\n\nconfidence\x18\r \x01(\x01\x12Q\n\x0f\x63onfidence_type\x18\x0e \x01(\x0e\x32\x34.apollo.perception.PerceptionObstacle.ConfidenceTypeB\x02\x18\x01\x12)\n\x05\x64rops\x18\x0f \x03(\x0b\x32\x16.apollo.common.Point3DB\x02\x18\x01\x12,\n\x0c\x61\x63\x63\x65leration\x18\x10 \x01(\x0b\x32\x16.apollo.common.Point3D\x12,\n\x0c\x61nchor_point\x18\x11 \x01(\x0b\x32\x16.apollo.common.Point3D\x12)\n\x06\x62\x62ox2d\x18\x12 \x01(\x0b\x32\x19.apollo.perception.BBox2D\x12?\n\x08sub_type\x18\x13 \x01(\x0e\x32-.apollo.perception.PerceptionObstacle.SubType\x12:\n\x0cmeasurements\x18\x14 \x03(\x0b\x32$.apollo.perception.SensorMeasurement\x12 \n\x13height_above_ground\x18\x15 \x01(\x01:\x03nan\x12\x1f\n\x13position_covariance\x18\x16 \x03(\x01\x42\x02\x10\x01\x12\x1f\n\x13velocity_covariance\x18\x17 \x03(\x01\x42\x02\x10\x01\x12#\n\x17\x61\x63\x63\x65leration_covariance\x18\x18 \x03(\x01\x42\x02\x10\x01\x12\x34\n\x0clight_status\x18\x19 \x01(\x0b\x32\x1e.apollo.perception.LightStatus\x12,\n\x03msg\x18\x1a \x01(\x0b\x32\x1f.apollo.perception.DebugMessage\x12J\n\x06source\x18\x1b \x01(\x0e\x32,.apollo.perception.PerceptionObstacle.Source:\x0cHOST_VEHICLE\x12\x33\n\x08v2x_info\x18\x1c \x01(\x0b\x32!.apollo.perception.V2XInformation\"i\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07\x42ICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05\"R\n\x0e\x43onfidenceType\x12\x16\n\x12\x43ONFIDENCE_UNKNOWN\x10\x00\x12\x12\n\x0e\x43ONFIDENCE_CNN\x10\x01\x12\x14\n\x10\x43ONFIDENCE_RADAR\x10\x02\"\x8b\x02\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x16\n\x12ST_UNKNOWN_MOVABLE\x10\x01\x12\x18\n\x14ST_UNKNOWN_UNMOVABLE\x10\x02\x12\n\n\x06ST_CAR\x10\x03\x12\n\n\x06ST_VAN\x10\x04\x12\x0c\n\x08ST_TRUCK\x10\x05\x12\n\n\x06ST_BUS\x10\x06\x12\x0e\n\nST_CYCLIST\x10\x07\x12\x13\n\x0fST_MOTORCYCLIST\x10\x08\x12\x11\n\rST_TRICYCLIST\x10\t\x12\x11\n\rST_PEDESTRIAN\x10\n\x12\x12\n\x0eST_TRAFFICCONE\x10\x0b\x12\x0f\n\x0bST_SMALLMOT\x10\x0c\x12\r\n\tST_BIGMOT\x10\r\x12\r\n\tST_NONMOT\x10\x0e\"#\n\x06Source\x12\x10\n\x0cHOST_VEHICLE\x10\x00\x12\x07\n\x03V2X\x10\x01\"\x95\x02\n\nLaneMarker\x12\x36\n\tlane_type\x18\x01 \x01(\x0e\x32#.apollo.hdmap.LaneBoundaryType.Type\x12\x0f\n\x07quality\x18\x02 \x01(\x01\x12\x14\n\x0cmodel_degree\x18\x03 \x01(\x05\x12\x13\n\x0b\x63\x30_position\x18\x04 \x01(\x01\x12\x18\n\x10\x63\x31_heading_angle\x18\x05 \x01(\x01\x12\x14\n\x0c\x63\x32_curvature\x18\x06 \x01(\x01\x12\x1f\n\x17\x63\x33_curvature_derivative\x18\x07 \x01(\x01\x12\x12\n\nview_range\x18\x08 \x01(\x01\x12\x17\n\x0flongitude_start\x18\t \x01(\x01\x12\x15\n\rlongitude_end\x18\n \x01(\x01\"\xfd\x01\n\x0bLaneMarkers\x12\x37\n\x10left_lane_marker\x18\x01 \x01(\x0b\x32\x1d.apollo.perception.LaneMarker\x12\x38\n\x11right_lane_marker\x18\x02 \x01(\x0b\x32\x1d.apollo.perception.LaneMarker\x12<\n\x15next_left_lane_marker\x18\x03 \x03(\x0b\x32\x1d.apollo.perception.LaneMarker\x12=\n\x16next_right_lane_marker\x18\x04 \x03(\x0b\x32\x1d.apollo.perception.LaneMarker\"6\n\x08\x43IPVInfo\x12\x0f\n\x07\x63ipv_id\x18\x01 \x01(\x05\x12\x19\n\x11potential_cipv_id\x18\x02 \x03(\x05\"\x97\x02\n\x13PerceptionObstacles\x12\x42\n\x13perception_obstacle\x18\x01 \x03(\x0b\x32%.apollo.perception.PerceptionObstacle\x12%\n\x06header\x18\x02 \x01(\x0b\x32\x15.apollo.common.Header\x12\x30\n\nerror_code\x18\x03 \x01(\x0e\x32\x18.apollo.common.ErrorCode:\x02OK\x12\x33\n\x0blane_marker\x18\x04 \x01(\x0b\x32\x1e.apollo.perception.LaneMarkers\x12.\n\tcipv_info\x18\x05 \x01(\x0b\x32\x1b.apollo.perception.CIPVInfo')



_BBOX2D = DESCRIPTOR.message_types_by_name['BBox2D']
_LIGHTSTATUS = DESCRIPTOR.message_types_by_name['LightStatus']
_V2XINFORMATION = DESCRIPTOR.message_types_by_name['V2XInformation']
_SENSORMEASUREMENT = DESCRIPTOR.message_types_by_name['SensorMeasurement']
_TRAJECTORY = DESCRIPTOR.message_types_by_name['Trajectory']
_DEBUGMESSAGE = DESCRIPTOR.message_types_by_name['DebugMessage']
_PERCEPTIONOBSTACLE = DESCRIPTOR.message_types_by_name['PerceptionObstacle']
_LANEMARKER = DESCRIPTOR.message_types_by_name['LaneMarker']
_LANEMARKERS = DESCRIPTOR.message_types_by_name['LaneMarkers']
_CIPVINFO = DESCRIPTOR.message_types_by_name['CIPVInfo']
_PERCEPTIONOBSTACLES = DESCRIPTOR.message_types_by_name['PerceptionObstacles']
_V2XINFORMATION_V2XTYPE = _V2XINFORMATION.enum_types_by_name['V2XType']
_PERCEPTIONOBSTACLE_TYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['Type']
_PERCEPTIONOBSTACLE_CONFIDENCETYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['ConfidenceType']
_PERCEPTIONOBSTACLE_SUBTYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['SubType']
_PERCEPTIONOBSTACLE_SOURCE = _PERCEPTIONOBSTACLE.enum_types_by_name['Source']
BBox2D = _reflection.GeneratedProtocolMessageType('BBox2D', (_message.Message,), {
  'DESCRIPTOR' : _BBOX2D,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.BBox2D)
  })
_sym_db.RegisterMessage(BBox2D)

LightStatus = _reflection.GeneratedProtocolMessageType('LightStatus', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTSTATUS,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.LightStatus)
  })
_sym_db.RegisterMessage(LightStatus)

V2XInformation = _reflection.GeneratedProtocolMessageType('V2XInformation', (_message.Message,), {
  'DESCRIPTOR' : _V2XINFORMATION,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.V2XInformation)
  })
_sym_db.RegisterMessage(V2XInformation)

SensorMeasurement = _reflection.GeneratedProtocolMessageType('SensorMeasurement', (_message.Message,), {
  'DESCRIPTOR' : _SENSORMEASUREMENT,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.SensorMeasurement)
  })
_sym_db.RegisterMessage(SensorMeasurement)

Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), {
  'DESCRIPTOR' : _TRAJECTORY,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.Trajectory)
  })
_sym_db.RegisterMessage(Trajectory)

DebugMessage = _reflection.GeneratedProtocolMessageType('DebugMessage', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGMESSAGE,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.DebugMessage)
  })
_sym_db.RegisterMessage(DebugMessage)

PerceptionObstacle = _reflection.GeneratedProtocolMessageType('PerceptionObstacle', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONOBSTACLE,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.PerceptionObstacle)
  })
_sym_db.RegisterMessage(PerceptionObstacle)

LaneMarker = _reflection.GeneratedProtocolMessageType('LaneMarker', (_message.Message,), {
  'DESCRIPTOR' : _LANEMARKER,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.LaneMarker)
  })
_sym_db.RegisterMessage(LaneMarker)

LaneMarkers = _reflection.GeneratedProtocolMessageType('LaneMarkers', (_message.Message,), {
  'DESCRIPTOR' : _LANEMARKERS,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.LaneMarkers)
  })
_sym_db.RegisterMessage(LaneMarkers)

CIPVInfo = _reflection.GeneratedProtocolMessageType('CIPVInfo', (_message.Message,), {
  'DESCRIPTOR' : _CIPVINFO,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.CIPVInfo)
  })
_sym_db.RegisterMessage(CIPVInfo)

PerceptionObstacles = _reflection.GeneratedProtocolMessageType('PerceptionObstacles', (_message.Message,), {
  'DESCRIPTOR' : _PERCEPTIONOBSTACLES,
  '__module__' : 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.PerceptionObstacles)
  })
_sym_db.RegisterMessage(PerceptionObstacles)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERCEPTIONOBSTACLE.fields_by_name['point_cloud']._options = None
  _PERCEPTIONOBSTACLE.fields_by_name['point_cloud']._serialized_options = b'\020\001'
  _PERCEPTIONOBSTACLE.fields_by_name['confidence_type']._options = None
  _PERCEPTIONOBSTACLE.fields_by_name['confidence_type']._serialized_options = b'\030\001'
  _PERCEPTIONOBSTACLE.fields_by_name['drops']._options = None
  _PERCEPTIONOBSTACLE.fields_by_name['drops']._serialized_options = b'\030\001'
  _PERCEPTIONOBSTACLE.fields_by_name['position_covariance']._options = None
  _PERCEPTIONOBSTACLE.fields_by_name['position_covariance']._serialized_options = b'\020\001'
  _PERCEPTIONOBSTACLE.fields_by_name['velocity_covariance']._options = None
  _PERCEPTIONOBSTACLE.fields_by_name['velocity_covariance']._serialized_options = b'\020\001'
  _PERCEPTIONOBSTACLE.fields_by_name['acceleration_covariance']._options = None
  _PERCEPTIONOBSTACLE.fields_by_name['acceleration_covariance']._serialized_options = b'\020\001'
  _BBOX2D._serialized_start=318
  _BBOX2D._serialized_end=382
  _LIGHTSTATUS._serialized_start=385
  _LIGHTSTATUS._serialized_end=560
  _V2XINFORMATION._serialized_start=563
  _V2XINFORMATION._serialized_end=694
  _V2XINFORMATION_V2XTYPE._serialized_start=642
  _V2XINFORMATION_V2XTYPE._serialized_end=694
  _SENSORMEASUREMENT._serialized_start=697
  _SENSORMEASUREMENT._serialized_end=1075
  _TRAJECTORY._serialized_start=1077
  _TRAJECTORY._serialized_end=1168
  _DEBUGMESSAGE._serialized_start=1170
  _DEBUGMESSAGE._serialized_end=1235
  _PERCEPTIONOBSTACLE._serialized_start=1238
  _PERCEPTIONOBSTACLE._serialized_end=2858
  _PERCEPTIONOBSTACLE_TYPE._serialized_start=2362
  _PERCEPTIONOBSTACLE_TYPE._serialized_end=2467
  _PERCEPTIONOBSTACLE_CONFIDENCETYPE._serialized_start=2469
  _PERCEPTIONOBSTACLE_CONFIDENCETYPE._serialized_end=2551
  _PERCEPTIONOBSTACLE_SUBTYPE._serialized_start=2554
  _PERCEPTIONOBSTACLE_SUBTYPE._serialized_end=2821
  _PERCEPTIONOBSTACLE_SOURCE._serialized_start=2823
  _PERCEPTIONOBSTACLE_SOURCE._serialized_end=2858
  _LANEMARKER._serialized_start=2861
  _LANEMARKER._serialized_end=3138
  _LANEMARKERS._serialized_start=3141
  _LANEMARKERS._serialized_end=3394
  _CIPVINFO._serialized_start=3396
  _CIPVINFO._serialized_end=3450
  _PERCEPTIONOBSTACLES._serialized_start=3453
  _PERCEPTIONOBSTACLES._serialized_end=3732
# @@protoc_insertion_point(module_scope)
