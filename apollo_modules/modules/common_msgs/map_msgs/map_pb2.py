# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/map_msgs/map.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.map_msgs import map_clear_area_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__clear__area__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_crosswalk_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__crosswalk__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_junction_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__junction__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_lane_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__lane__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_overlap_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__overlap__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_parking_space_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__parking__space__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_pnc_junction_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__pnc__junction__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_road_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__road__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_rsu_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__rsu__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_signal_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__signal__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_speed_bump_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__speed__bump__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_stop_sign_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__stop__sign__pb2
from apollo_modules.modules.common_msgs.map_msgs import map_yield_sign_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__yield__sign__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/common_msgs/map_msgs/map.proto\x12\x0c\x61pollo.hdmap\x1a\x31modules/common_msgs/map_msgs/map_clear_area.proto\x1a\x30modules/common_msgs/map_msgs/map_crosswalk.proto\x1a/modules/common_msgs/map_msgs/map_junction.proto\x1a+modules/common_msgs/map_msgs/map_lane.proto\x1a.modules/common_msgs/map_msgs/map_overlap.proto\x1a\x34modules/common_msgs/map_msgs/map_parking_space.proto\x1a\x33modules/common_msgs/map_msgs/map_pnc_junction.proto\x1a+modules/common_msgs/map_msgs/map_road.proto\x1a*modules/common_msgs/map_msgs/map_rsu.proto\x1a-modules/common_msgs/map_msgs/map_signal.proto\x1a\x31modules/common_msgs/map_msgs/map_speed_bump.proto\x1a\x30modules/common_msgs/map_msgs/map_stop_sign.proto\x1a\x31modules/common_msgs/map_msgs/map_yield_sign.proto\"\x1a\n\nProjection\x12\x0c\n\x04proj\x18\x01 \x01(\t\"\xeb\x01\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\x0c\x12,\n\nprojection\x18\x03 \x01(\x0b\x32\x18.apollo.hdmap.Projection\x12\x10\n\x08\x64istrict\x18\x04 \x01(\x0c\x12\x12\n\ngeneration\x18\x05 \x01(\x0c\x12\x11\n\trev_major\x18\x06 \x01(\x0c\x12\x11\n\trev_minor\x18\x07 \x01(\x0c\x12\x0c\n\x04left\x18\x08 \x01(\x01\x12\x0b\n\x03top\x18\t \x01(\x01\x12\r\n\x05right\x18\n \x01(\x01\x12\x0e\n\x06\x62ottom\x18\x0b \x01(\x01\x12\x0e\n\x06vendor\x18\x0c \x01(\x0c\"\xc4\x04\n\x03Map\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.apollo.hdmap.Header\x12*\n\tcrosswalk\x18\x02 \x03(\x0b\x32\x17.apollo.hdmap.Crosswalk\x12(\n\x08junction\x18\x03 \x03(\x0b\x32\x16.apollo.hdmap.Junction\x12 \n\x04lane\x18\x04 \x03(\x0b\x32\x12.apollo.hdmap.Lane\x12)\n\tstop_sign\x18\x05 \x03(\x0b\x32\x16.apollo.hdmap.StopSign\x12$\n\x06signal\x18\x06 \x03(\x0b\x32\x14.apollo.hdmap.Signal\x12&\n\x05yield\x18\x07 \x03(\x0b\x32\x17.apollo.hdmap.YieldSign\x12&\n\x07overlap\x18\x08 \x03(\x0b\x32\x15.apollo.hdmap.Overlap\x12+\n\nclear_area\x18\t \x03(\x0b\x32\x17.apollo.hdmap.ClearArea\x12+\n\nspeed_bump\x18\n \x03(\x0b\x32\x17.apollo.hdmap.SpeedBump\x12 \n\x04road\x18\x0b \x03(\x0b\x32\x12.apollo.hdmap.Road\x12\x31\n\rparking_space\x18\x0c \x03(\x0b\x32\x1a.apollo.hdmap.ParkingSpace\x12/\n\x0cpnc_junction\x18\r \x03(\x0b\x32\x19.apollo.hdmap.PNCJunction\x12\x1e\n\x03rsu\x18\x0e \x03(\x0b\x32\x11.apollo.hdmap.RSU')



_PROJECTION = DESCRIPTOR.message_types_by_name['Projection']
_HEADER = DESCRIPTOR.message_types_by_name['Header']
_MAP = DESCRIPTOR.message_types_by_name['Map']
Projection = _reflection.GeneratedProtocolMessageType('Projection', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTION,
  '__module__' : 'modules.common_msgs.map_msgs.map_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Projection)
  })
_sym_db.RegisterMessage(Projection)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'modules.common_msgs.map_msgs.map_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Header)
  })
_sym_db.RegisterMessage(Header)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
  'DESCRIPTOR' : _MAP,
  '__module__' : 'modules.common_msgs.map_msgs.map_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.Map)
  })
_sym_db.RegisterMessage(Map)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROJECTION._serialized_start=694
  _PROJECTION._serialized_end=720
  _HEADER._serialized_start=723
  _HEADER._serialized_end=958
  _MAP._serialized_start=961
  _MAP._serialized_end=1541
# @@protoc_insertion_point(module_scope)
