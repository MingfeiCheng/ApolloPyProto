# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/routing_msgs/routing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.routing_msgs import geometry_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_geometry__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.basic_msgs import error_code_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2
from apollo_modules.modules.common_msgs.routing_msgs import poi_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_poi__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.modules/common_msgs/routing_msgs/routing.proto\x12\x0e\x61pollo.routing\x1a/modules/common_msgs/routing_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a/modules/common_msgs/basic_msgs/error_code.proto\x1a*modules/common_msgs/routing_msgs/poi.proto\"\xaa\x02\n\x0eRoutingRequest\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12.\n\x08waypoint\x18\x02 \x03(\x0b\x32\x1c.apollo.routing.LaneWaypoint\x12\x35\n\x10\x62lacklisted_lane\x18\x03 \x03(\x0b\x32\x1b.apollo.routing.LaneSegment\x12\x18\n\x10\x62lacklisted_road\x18\x04 \x03(\t\x12\x17\n\tbroadcast\x18\x05 \x01(\x08:\x04true\x12\x35\n\x0cparking_info\x18\x06 \x01(\x0b\x32\x1b.apollo.routing.ParkingInfoB\x02\x18\x01\x12 \n\x11is_start_pose_set\x18\x07 \x01(\x08:\x05\x66\x61lse\"\x8c\x02\n\x0fRoutingResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12)\n\x04road\x18\x02 \x03(\x0b\x32\x1b.apollo.routing.RoadSegment\x12\x30\n\x0bmeasurement\x18\x03 \x01(\x0b\x32\x1b.apollo.routing.Measurement\x12\x37\n\x0frouting_request\x18\x04 \x01(\x0b\x32\x1e.apollo.routing.RoutingRequest\x12\x13\n\x0bmap_version\x18\x05 \x01(\x0c\x12\'\n\x06status\x18\x06 \x01(\x0b\x32\x17.apollo.common.StatusPb')



_ROUTINGREQUEST = DESCRIPTOR.message_types_by_name['RoutingRequest']
_ROUTINGRESPONSE = DESCRIPTOR.message_types_by_name['RoutingResponse']
RoutingRequest = _reflection.GeneratedProtocolMessageType('RoutingRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGREQUEST,
  '__module__' : 'modules.common_msgs.routing_msgs.routing_pb2'
  # @@protoc_insertion_point(class_scope:apollo.routing.RoutingRequest)
  })
_sym_db.RegisterMessage(RoutingRequest)

RoutingResponse = _reflection.GeneratedProtocolMessageType('RoutingResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGRESPONSE,
  '__module__' : 'modules.common_msgs.routing_msgs.routing_pb2'
  # @@protoc_insertion_point(class_scope:apollo.routing.RoutingResponse)
  })
_sym_db.RegisterMessage(RoutingResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROUTINGREQUEST.fields_by_name['parking_info']._options = None
  _ROUTINGREQUEST.fields_by_name['parking_info']._serialized_options = b'\030\001'
  _ROUTINGREQUEST._serialized_start=254
  _ROUTINGREQUEST._serialized_end=552
  _ROUTINGRESPONSE._serialized_start=555
  _ROUTINGRESPONSE._serialized_end=823
# @@protoc_insertion_point(module_scope)
