# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/prediction/proto/lane_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common.proto import geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from apollo_modules.modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2
from apollo_modules.modules.map.proto import map_lane_pb2 as modules_dot_map_dot_proto_dot_map__lane__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/prediction/proto/lane_graph.proto',
  package='apollo.prediction',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)modules/prediction/proto/lane_graph.proto\x12\x11\x61pollo.prediction\x1a#modules/common/proto/geometry.proto\x1a$modules/common/proto/pnc_point.proto\x1a modules/map/proto/map_lane.proto\"\xc4\x02\n\tLanePoint\x12(\n\x08position\x18\x01 \x01(\x0b\x32\x16.apollo.common.Point3D\x12\x12\n\x07heading\x18\x02 \x01(\x01:\x01\x30\x12\x10\n\x05width\x18\x03 \x01(\x01:\x01\x30\x12\x15\n\nrelative_s\x18\x04 \x01(\x01:\x01\x30\x12\x15\n\nrelative_l\x18\x05 \x01(\x01:\x01\x30\x12\x15\n\nangle_diff\x18\x06 \x01(\x01:\x01\x30\x12\x10\n\x05kappa\x18\x07 \x01(\x01:\x01\x30\x12@\n\rscenario_type\x18\x08 \x01(\x0e\x32).apollo.prediction.LanePoint.ScenarioType\x12\x13\n\x0bspeed_limit\x18\t \x01(\x01\"9\n\x0cScenarioType\x12\x0e\n\nURBAN_ROAD\x10\x00\x12\x0c\n\x08JUNCTION\x10\x01\x12\x0b\n\x07HIGHWAY\x10\x02\"\xdb\x01\n\x0bLaneSegment\x12\x0f\n\x07lane_id\x18\x01 \x01(\t\x12\x12\n\x07start_s\x18\x02 \x01(\x01:\x01\x30\x12\x10\n\x05\x65nd_s\x18\x03 \x01(\x01:\x01\x30\x12\x19\n\x0elane_turn_type\x18\x04 \x01(\r:\x01\x30\x12\x30\n\nlane_point\x18\x05 \x03(\x0b\x32\x1c.apollo.prediction.LanePoint\x12\x10\n\x05\x61\x64\x63_s\x18\x07 \x01(\x01:\x01\x30\x12\x1d\n\x12\x61\x64\x63_lane_point_idx\x18\x08 \x01(\x05:\x01\x30\x12\x17\n\x0ctotal_length\x18\x06 \x01(\x01:\x01\x30\"2\n\x0eNearbyObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01s\x18\x02 \x01(\x01\x12\t\n\x01l\x18\x03 \x01(\x01\"Z\n\x08StopSign\x12\x14\n\x0cstop_sign_id\x18\x01 \x01(\t\x12\x0f\n\x07lane_id\x18\x02 \x01(\t\x12\x0e\n\x06lane_s\x18\x03 \x01(\x01\x12\x17\n\x0flane_sequence_s\x18\x04 \x01(\x01\"\xff\x08\n\x0cLaneSequence\x12\x18\n\x10lane_sequence_id\x18\x01 \x01(\x05\x12\x34\n\x0clane_segment\x18\x02 \x03(\x0b\x32\x1e.apollo.prediction.LaneSegment\x12\x1f\n\x14\x61\x64\x63_lane_segment_idx\x18\x17 \x01(\x05:\x01\x30\x12,\n\npath_point\x18\x08 \x03(\x0b\x32\x18.apollo.common.PathPoint\x12.\n\tlane_type\x18\x16 \x01(\x0e\x32\x1b.apollo.hdmap.Lane.LaneType\x12\x0e\n\x06lane_s\x18\x11 \x01(\x01\x12\x0e\n\x06lane_l\x18\x12 \x01(\x01\x12\x17\n\x0fvehicle_on_lane\x18\n \x01(\x08\x12:\n\x0fnearby_obstacle\x18\x03 \x03(\x0b\x32!.apollo.prediction.NearbyObstacle\x12.\n\tstop_sign\x18\x14 \x01(\x0b\x32\x1b.apollo.prediction.StopSign\x12\x14\n\x0cright_of_way\x18\x15 \x01(\x05\x12:\n\x08\x66\x65\x61tures\x18\x04 \x01(\x0b\x32(.apollo.prediction.LaneSequence.Features\x12\x10\n\x05label\x18\x05 \x01(\x05:\x01\x30\x12\x16\n\x0bprobability\x18\x06 \x01(\x01:\x01\x30\x12\x17\n\x0c\x61\x63\x63\x65leration\x18\x07 \x01(\x01:\x01\x30\x12\x1b\n\x13time_to_lane_center\x18\x10 \x01(\x01\x12\x19\n\x11time_to_lane_edge\x18\x13 \x01(\x01\x12\x43\n\rbehavior_type\x18\t \x01(\x0e\x32,.apollo.prediction.LaneSequence.BehaviorType\x12\x35\n\x0f\x63urr_lane_point\x18\x0b \x03(\x0b\x32\x1c.apollo.prediction.LanePoint\x12\x39\n\x13left_neighbor_point\x18\x0c \x03(\x0b\x32\x1c.apollo.prediction.LanePoint\x12:\n\x14right_neighbor_point\x18\r \x03(\x0b\x32\x1c.apollo.prediction.LanePoint\x12?\n\x14left_nearby_obstacle\x18\x0e \x03(\x0b\x32!.apollo.prediction.NearbyObstacle\x12@\n\x15right_nearby_obstacle\x18\x0f \x03(\x0b\x32!.apollo.prediction.NearbyObstacle\x1a \n\x08\x46\x65\x61tures\x12\x14\n\x0cmlp_features\x18\x01 \x03(\x01\"\x95\x01\n\x0c\x42\x65haviorType\x12\x11\n\rNOT_GOTO_LANE\x10\x01\x12\x12\n\x0e\x43ONSTANT_SPEED\x10\x02\x12\x16\n\x12SMALL_ACCELERATION\x10\x03\x12\x16\n\x12LARGE_ACCELERATION\x10\x04\x12\x16\n\x12SMALL_DECELERATION\x10\x05\x12\x16\n\x12LARGE_DECELERATION\x10\x06\"C\n\tLaneGraph\x12\x36\n\rlane_sequence\x18\x01 \x03(\x0b\x32\x1f.apollo.prediction.LaneSequence\"T\n\x0cLaneObstacle\x12\x13\n\x0bobstacle_id\x18\x01 \x01(\x05\x12\x0f\n\x07lane_id\x18\x02 \x01(\t\x12\x0e\n\x06lane_s\x18\x03 \x01(\x01\x12\x0e\n\x06lane_l\x18\x04 \x01(\x01')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_pnc__point__pb2.DESCRIPTOR,modules_dot_map_dot_proto_dot_map__lane__pb2.DESCRIPTOR,])



_LANEPOINT_SCENARIOTYPE = _descriptor.EnumDescriptor(
  name='ScenarioType',
  full_name='apollo.prediction.LanePoint.ScenarioType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='URBAN_ROAD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JUNCTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGHWAY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=441,
  serialized_end=498,
)
_sym_db.RegisterEnumDescriptor(_LANEPOINT_SCENARIOTYPE)

_LANESEQUENCE_BEHAVIORTYPE = _descriptor.EnumDescriptor(
  name='BehaviorType',
  full_name='apollo.prediction.LaneSequence.BehaviorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_GOTO_LANE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSTANT_SPEED', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMALL_ACCELERATION', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LARGE_ACCELERATION', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMALL_DECELERATION', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LARGE_DECELERATION', index=5, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1869,
  serialized_end=2018,
)
_sym_db.RegisterEnumDescriptor(_LANESEQUENCE_BEHAVIORTYPE)


_LANEPOINT = _descriptor.Descriptor(
  name='LanePoint',
  full_name='apollo.prediction.LanePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='apollo.prediction.LanePoint.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='apollo.prediction.LanePoint.heading', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='apollo.prediction.LanePoint.width', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_s', full_name='apollo.prediction.LanePoint.relative_s', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_l', full_name='apollo.prediction.LanePoint.relative_l', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle_diff', full_name='apollo.prediction.LanePoint.angle_diff', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kappa', full_name='apollo.prediction.LanePoint.kappa', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scenario_type', full_name='apollo.prediction.LanePoint.scenario_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_limit', full_name='apollo.prediction.LanePoint.speed_limit', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LANEPOINT_SCENARIOTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=498,
)


_LANESEGMENT = _descriptor.Descriptor(
  name='LaneSegment',
  full_name='apollo.prediction.LaneSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='apollo.prediction.LaneSegment.lane_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_s', full_name='apollo.prediction.LaneSegment.start_s', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_s', full_name='apollo.prediction.LaneSegment.end_s', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_turn_type', full_name='apollo.prediction.LaneSegment.lane_turn_type', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_point', full_name='apollo.prediction.LaneSegment.lane_point', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adc_s', full_name='apollo.prediction.LaneSegment.adc_s', index=5,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adc_lane_point_idx', full_name='apollo.prediction.LaneSegment.adc_lane_point_idx', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_length', full_name='apollo.prediction.LaneSegment.total_length', index=7,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=720,
)


_NEARBYOBSTACLE = _descriptor.Descriptor(
  name='NearbyObstacle',
  full_name='apollo.prediction.NearbyObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.prediction.NearbyObstacle.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s', full_name='apollo.prediction.NearbyObstacle.s', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l', full_name='apollo.prediction.NearbyObstacle.l', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=772,
)


_STOPSIGN = _descriptor.Descriptor(
  name='StopSign',
  full_name='apollo.prediction.StopSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stop_sign_id', full_name='apollo.prediction.StopSign.stop_sign_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='apollo.prediction.StopSign.lane_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_s', full_name='apollo.prediction.StopSign.lane_s', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_sequence_s', full_name='apollo.prediction.StopSign.lane_sequence_s', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=864,
)


_LANESEQUENCE_FEATURES = _descriptor.Descriptor(
  name='Features',
  full_name='apollo.prediction.LaneSequence.Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mlp_features', full_name='apollo.prediction.LaneSequence.Features.mlp_features', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1834,
  serialized_end=1866,
)

_LANESEQUENCE = _descriptor.Descriptor(
  name='LaneSequence',
  full_name='apollo.prediction.LaneSequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lane_sequence_id', full_name='apollo.prediction.LaneSequence.lane_sequence_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_segment', full_name='apollo.prediction.LaneSequence.lane_segment', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adc_lane_segment_idx', full_name='apollo.prediction.LaneSequence.adc_lane_segment_idx', index=2,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path_point', full_name='apollo.prediction.LaneSequence.path_point', index=3,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_type', full_name='apollo.prediction.LaneSequence.lane_type', index=4,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_s', full_name='apollo.prediction.LaneSequence.lane_s', index=5,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_l', full_name='apollo.prediction.LaneSequence.lane_l', index=6,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_on_lane', full_name='apollo.prediction.LaneSequence.vehicle_on_lane', index=7,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nearby_obstacle', full_name='apollo.prediction.LaneSequence.nearby_obstacle', index=8,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_sign', full_name='apollo.prediction.LaneSequence.stop_sign', index=9,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_of_way', full_name='apollo.prediction.LaneSequence.right_of_way', index=10,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='apollo.prediction.LaneSequence.features', index=11,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='apollo.prediction.LaneSequence.label', index=12,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='probability', full_name='apollo.prediction.LaneSequence.probability', index=13,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='apollo.prediction.LaneSequence.acceleration', index=14,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_to_lane_center', full_name='apollo.prediction.LaneSequence.time_to_lane_center', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_to_lane_edge', full_name='apollo.prediction.LaneSequence.time_to_lane_edge', index=16,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='behavior_type', full_name='apollo.prediction.LaneSequence.behavior_type', index=17,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curr_lane_point', full_name='apollo.prediction.LaneSequence.curr_lane_point', index=18,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_neighbor_point', full_name='apollo.prediction.LaneSequence.left_neighbor_point', index=19,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_neighbor_point', full_name='apollo.prediction.LaneSequence.right_neighbor_point', index=20,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_nearby_obstacle', full_name='apollo.prediction.LaneSequence.left_nearby_obstacle', index=21,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_nearby_obstacle', full_name='apollo.prediction.LaneSequence.right_nearby_obstacle', index=22,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LANESEQUENCE_FEATURES, ],
  enum_types=[
    _LANESEQUENCE_BEHAVIORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=2018,
)


_LANEGRAPH = _descriptor.Descriptor(
  name='LaneGraph',
  full_name='apollo.prediction.LaneGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lane_sequence', full_name='apollo.prediction.LaneGraph.lane_sequence', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2020,
  serialized_end=2087,
)


_LANEOBSTACLE = _descriptor.Descriptor(
  name='LaneObstacle',
  full_name='apollo.prediction.LaneObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obstacle_id', full_name='apollo.prediction.LaneObstacle.obstacle_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='apollo.prediction.LaneObstacle.lane_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_s', full_name='apollo.prediction.LaneObstacle.lane_s', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lane_l', full_name='apollo.prediction.LaneObstacle.lane_l', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2089,
  serialized_end=2173,
)

_LANEPOINT.fields_by_name['position'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_LANEPOINT.fields_by_name['scenario_type'].enum_type = _LANEPOINT_SCENARIOTYPE
_LANEPOINT_SCENARIOTYPE.containing_type = _LANEPOINT
_LANESEGMENT.fields_by_name['lane_point'].message_type = _LANEPOINT
_LANESEQUENCE_FEATURES.containing_type = _LANESEQUENCE
_LANESEQUENCE.fields_by_name['lane_segment'].message_type = _LANESEGMENT
_LANESEQUENCE.fields_by_name['path_point'].message_type = modules_dot_common_dot_proto_dot_pnc__point__pb2._PATHPOINT
_LANESEQUENCE.fields_by_name['lane_type'].enum_type = modules_dot_map_dot_proto_dot_map__lane__pb2._LANE_LANETYPE
_LANESEQUENCE.fields_by_name['nearby_obstacle'].message_type = _NEARBYOBSTACLE
_LANESEQUENCE.fields_by_name['stop_sign'].message_type = _STOPSIGN
_LANESEQUENCE.fields_by_name['features'].message_type = _LANESEQUENCE_FEATURES
_LANESEQUENCE.fields_by_name['behavior_type'].enum_type = _LANESEQUENCE_BEHAVIORTYPE
_LANESEQUENCE.fields_by_name['curr_lane_point'].message_type = _LANEPOINT
_LANESEQUENCE.fields_by_name['left_neighbor_point'].message_type = _LANEPOINT
_LANESEQUENCE.fields_by_name['right_neighbor_point'].message_type = _LANEPOINT
_LANESEQUENCE.fields_by_name['left_nearby_obstacle'].message_type = _NEARBYOBSTACLE
_LANESEQUENCE.fields_by_name['right_nearby_obstacle'].message_type = _NEARBYOBSTACLE
_LANESEQUENCE_BEHAVIORTYPE.containing_type = _LANESEQUENCE
_LANEGRAPH.fields_by_name['lane_sequence'].message_type = _LANESEQUENCE
DESCRIPTOR.message_types_by_name['LanePoint'] = _LANEPOINT
DESCRIPTOR.message_types_by_name['LaneSegment'] = _LANESEGMENT
DESCRIPTOR.message_types_by_name['NearbyObstacle'] = _NEARBYOBSTACLE
DESCRIPTOR.message_types_by_name['StopSign'] = _STOPSIGN
DESCRIPTOR.message_types_by_name['LaneSequence'] = _LANESEQUENCE
DESCRIPTOR.message_types_by_name['LaneGraph'] = _LANEGRAPH
DESCRIPTOR.message_types_by_name['LaneObstacle'] = _LANEOBSTACLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LanePoint = _reflection.GeneratedProtocolMessageType('LanePoint', (_message.Message,), dict(
  DESCRIPTOR = _LANEPOINT,
  __module__ = 'modules.prediction.proto.lane_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.LanePoint)
  ))
_sym_db.RegisterMessage(LanePoint)

LaneSegment = _reflection.GeneratedProtocolMessageType('LaneSegment', (_message.Message,), dict(
  DESCRIPTOR = _LANESEGMENT,
  __module__ = 'modules.prediction.proto.lane_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.LaneSegment)
  ))
_sym_db.RegisterMessage(LaneSegment)

NearbyObstacle = _reflection.GeneratedProtocolMessageType('NearbyObstacle', (_message.Message,), dict(
  DESCRIPTOR = _NEARBYOBSTACLE,
  __module__ = 'modules.prediction.proto.lane_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.NearbyObstacle)
  ))
_sym_db.RegisterMessage(NearbyObstacle)

StopSign = _reflection.GeneratedProtocolMessageType('StopSign', (_message.Message,), dict(
  DESCRIPTOR = _STOPSIGN,
  __module__ = 'modules.prediction.proto.lane_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.StopSign)
  ))
_sym_db.RegisterMessage(StopSign)

LaneSequence = _reflection.GeneratedProtocolMessageType('LaneSequence', (_message.Message,), dict(

  Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), dict(
    DESCRIPTOR = _LANESEQUENCE_FEATURES,
    __module__ = 'modules.prediction.proto.lane_graph_pb2'
    # @@protoc_insertion_point(class_scope:apollo.prediction.LaneSequence.Features)
    ))
  ,
  DESCRIPTOR = _LANESEQUENCE,
  __module__ = 'modules.prediction.proto.lane_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.LaneSequence)
  ))
_sym_db.RegisterMessage(LaneSequence)
_sym_db.RegisterMessage(LaneSequence.Features)

LaneGraph = _reflection.GeneratedProtocolMessageType('LaneGraph', (_message.Message,), dict(
  DESCRIPTOR = _LANEGRAPH,
  __module__ = 'modules.prediction.proto.lane_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.LaneGraph)
  ))
_sym_db.RegisterMessage(LaneGraph)

LaneObstacle = _reflection.GeneratedProtocolMessageType('LaneObstacle', (_message.Message,), dict(
  DESCRIPTOR = _LANEOBSTACLE,
  __module__ = 'modules.prediction.proto.lane_graph_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.LaneObstacle)
  ))
_sym_db.RegisterMessage(LaneObstacle)


# @@protoc_insertion_point(module_scope)
