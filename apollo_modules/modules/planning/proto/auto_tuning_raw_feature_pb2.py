# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/proto/auto_tuning_raw_feature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common.proto import pnc_point_pb2 as modules_dot_common_dot_proto_dot_pnc__point__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/planning/proto/auto_tuning_raw_feature.proto',
  package='apollo.planning.autotuning',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n4modules/planning/proto/auto_tuning_raw_feature.proto\x12\x1a\x61pollo.planning.autotuning\x1a$modules/common/proto/pnc_point.proto\"\x7f\n\x13PathPointRawFeature\x12\x31\n\x0f\x63\x61rtesian_coord\x18\x01 \x01(\x0b\x32\x18.apollo.common.PathPoint\x12\x35\n\x0c\x66renet_coord\x18\x02 \x01(\x0b\x32\x1f.apollo.common.FrenetFramePoint\"\x89\x08\n\x14SpeedPointRawFeature\x12\t\n\x01s\x18\x01 \x01(\x01\x12\t\n\x01t\x18\x02 \x01(\x01\x12\t\n\x01v\x18\x03 \x01(\x01\x12\t\n\x01\x61\x18\x04 \x01(\x01\x12\t\n\x01j\x18\x05 \x01(\x01\x12\x13\n\x0bspeed_limit\x18\x06 \x01(\x01\x12V\n\x06\x66ollow\x18\n \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12X\n\x08overtake\x18\x0b \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12`\n\x10virtual_decision\x18\r \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12T\n\x04stop\x18\x0e \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12Y\n\tcollision\x18\x0f \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12U\n\x05nudge\x18\x0c \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12^\n\x0esidepass_front\x18\x10 \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12]\n\rsidepass_rear\x18\x11 \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x12Z\n\nkeep_clear\x18\x12 \x03(\x0b\x32\x46.apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature\x1an\n\x15ObjectDecisionFeature\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nrelative_s\x18\x02 \x01(\x01\x12\x12\n\nrelative_l\x18\x03 \x01(\x01\x12\x12\n\nrelative_v\x18\x04 \x01(\x01\x12\r\n\x05speed\x18\x05 \x01(\x01\"\xdf\x04\n\x11ObstacleSTRawData\x12V\n\x10obstacle_st_data\x18\x01 \x03(\x0b\x32<.apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData\x12W\n\x11obstacle_st_nudge\x18\x02 \x03(\x0b\x32<.apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData\x12Z\n\x14obstacle_st_sidepass\x18\x03 \x03(\x0b\x32<.apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData\x1aI\n\x0bSTPointPair\x12\x0f\n\x07s_lower\x18\x01 \x01(\x01\x12\x0f\n\x07s_upper\x18\x02 \x01(\x01\x12\t\n\x01t\x18\x03 \x01(\x01\x12\r\n\x01l\x18\x04 \x01(\x01:\x02\x31\x30\x1a\xf1\x01\n\x0eObstacleSTData\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05speed\x18\x02 \x01(\x01\x12\x12\n\nis_virtual\x18\x03 \x01(\x08\x12\x13\n\x0bprobability\x18\x04 \x01(\x01\x12J\n\x07polygon\x18\x08 \x03(\x0b\x32\x39.apollo.planning.autotuning.ObstacleSTRawData.STPointPair\x12O\n\x0c\x64istribution\x18\t \x03(\x0b\x32\x39.apollo.planning.autotuning.ObstacleSTRawData.STPointPair\"\xab\x01\n\x19TrajectoryPointRawFeature\x12\x45\n\x0cpath_feature\x18\x01 \x01(\x0b\x32/.apollo.planning.autotuning.PathPointRawFeature\x12G\n\rspeed_feature\x18\x02 \x01(\x0b\x32\x30.apollo.planning.autotuning.SpeedPointRawFeature\"\xa8\x01\n\x14TrajectoryRawFeature\x12L\n\rpoint_feature\x18\x01 \x03(\x0b\x32\x35.apollo.planning.autotuning.TrajectoryPointRawFeature\x12\x42\n\x0bst_raw_data\x18\x02 \x01(\x0b\x32-.apollo.planning.autotuning.ObstacleSTRawData')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_pnc__point__pb2.DESCRIPTOR,])




_PATHPOINTRAWFEATURE = _descriptor.Descriptor(
  name='PathPointRawFeature',
  full_name='apollo.planning.autotuning.PathPointRawFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cartesian_coord', full_name='apollo.planning.autotuning.PathPointRawFeature.cartesian_coord', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frenet_coord', full_name='apollo.planning.autotuning.PathPointRawFeature.frenet_coord', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=122,
  serialized_end=249,
)


_SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE = _descriptor.Descriptor(
  name='ObjectDecisionFeature',
  full_name='apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_s', full_name='apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature.relative_s', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_l', full_name='apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature.relative_l', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_v', full_name='apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature.relative_v', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature.speed', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=1175,
  serialized_end=1285,
)

_SPEEDPOINTRAWFEATURE = _descriptor.Descriptor(
  name='SpeedPointRawFeature',
  full_name='apollo.planning.autotuning.SpeedPointRawFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='apollo.planning.autotuning.SpeedPointRawFeature.s', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='t', full_name='apollo.planning.autotuning.SpeedPointRawFeature.t', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v', full_name='apollo.planning.autotuning.SpeedPointRawFeature.v', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='a', full_name='apollo.planning.autotuning.SpeedPointRawFeature.a', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='j', full_name='apollo.planning.autotuning.SpeedPointRawFeature.j', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_limit', full_name='apollo.planning.autotuning.SpeedPointRawFeature.speed_limit', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='follow', full_name='apollo.planning.autotuning.SpeedPointRawFeature.follow', index=6,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overtake', full_name='apollo.planning.autotuning.SpeedPointRawFeature.overtake', index=7,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='virtual_decision', full_name='apollo.planning.autotuning.SpeedPointRawFeature.virtual_decision', index=8,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='apollo.planning.autotuning.SpeedPointRawFeature.stop', index=9,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collision', full_name='apollo.planning.autotuning.SpeedPointRawFeature.collision', index=10,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nudge', full_name='apollo.planning.autotuning.SpeedPointRawFeature.nudge', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sidepass_front', full_name='apollo.planning.autotuning.SpeedPointRawFeature.sidepass_front', index=12,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sidepass_rear', full_name='apollo.planning.autotuning.SpeedPointRawFeature.sidepass_rear', index=13,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keep_clear', full_name='apollo.planning.autotuning.SpeedPointRawFeature.keep_clear', index=14,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=1285,
)


_OBSTACLESTRAWDATA_STPOINTPAIR = _descriptor.Descriptor(
  name='STPointPair',
  full_name='apollo.planning.autotuning.ObstacleSTRawData.STPointPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s_lower', full_name='apollo.planning.autotuning.ObstacleSTRawData.STPointPair.s_lower', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s_upper', full_name='apollo.planning.autotuning.ObstacleSTRawData.STPointPair.s_upper', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='t', full_name='apollo.planning.autotuning.ObstacleSTRawData.STPointPair.t', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l', full_name='apollo.planning.autotuning.ObstacleSTRawData.STPointPair.l', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(10),
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
  serialized_start=1578,
  serialized_end=1651,
)

_OBSTACLESTRAWDATA_OBSTACLESTDATA = _descriptor.Descriptor(
  name='ObstacleSTData',
  full_name='apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData.speed', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_virtual', full_name='apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData.is_virtual', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='probability', full_name='apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData.probability', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polygon', full_name='apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData.polygon', index=4,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distribution', full_name='apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData.distribution', index=5,
      number=9, type=11, cpp_type=10, label=3,
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
  serialized_start=1654,
  serialized_end=1895,
)

_OBSTACLESTRAWDATA = _descriptor.Descriptor(
  name='ObstacleSTRawData',
  full_name='apollo.planning.autotuning.ObstacleSTRawData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obstacle_st_data', full_name='apollo.planning.autotuning.ObstacleSTRawData.obstacle_st_data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obstacle_st_nudge', full_name='apollo.planning.autotuning.ObstacleSTRawData.obstacle_st_nudge', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obstacle_st_sidepass', full_name='apollo.planning.autotuning.ObstacleSTRawData.obstacle_st_sidepass', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OBSTACLESTRAWDATA_STPOINTPAIR, _OBSTACLESTRAWDATA_OBSTACLESTDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1288,
  serialized_end=1895,
)


_TRAJECTORYPOINTRAWFEATURE = _descriptor.Descriptor(
  name='TrajectoryPointRawFeature',
  full_name='apollo.planning.autotuning.TrajectoryPointRawFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path_feature', full_name='apollo.planning.autotuning.TrajectoryPointRawFeature.path_feature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed_feature', full_name='apollo.planning.autotuning.TrajectoryPointRawFeature.speed_feature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1898,
  serialized_end=2069,
)


_TRAJECTORYRAWFEATURE = _descriptor.Descriptor(
  name='TrajectoryRawFeature',
  full_name='apollo.planning.autotuning.TrajectoryRawFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point_feature', full_name='apollo.planning.autotuning.TrajectoryRawFeature.point_feature', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='st_raw_data', full_name='apollo.planning.autotuning.TrajectoryRawFeature.st_raw_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=2072,
  serialized_end=2240,
)

_PATHPOINTRAWFEATURE.fields_by_name['cartesian_coord'].message_type = modules_dot_common_dot_proto_dot_pnc__point__pb2._PATHPOINT
_PATHPOINTRAWFEATURE.fields_by_name['frenet_coord'].message_type = modules_dot_common_dot_proto_dot_pnc__point__pb2._FRENETFRAMEPOINT
_SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE.containing_type = _SPEEDPOINTRAWFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['follow'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['overtake'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['virtual_decision'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['stop'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['collision'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['nudge'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['sidepass_front'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['sidepass_rear'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_SPEEDPOINTRAWFEATURE.fields_by_name['keep_clear'].message_type = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE
_OBSTACLESTRAWDATA_STPOINTPAIR.containing_type = _OBSTACLESTRAWDATA
_OBSTACLESTRAWDATA_OBSTACLESTDATA.fields_by_name['polygon'].message_type = _OBSTACLESTRAWDATA_STPOINTPAIR
_OBSTACLESTRAWDATA_OBSTACLESTDATA.fields_by_name['distribution'].message_type = _OBSTACLESTRAWDATA_STPOINTPAIR
_OBSTACLESTRAWDATA_OBSTACLESTDATA.containing_type = _OBSTACLESTRAWDATA
_OBSTACLESTRAWDATA.fields_by_name['obstacle_st_data'].message_type = _OBSTACLESTRAWDATA_OBSTACLESTDATA
_OBSTACLESTRAWDATA.fields_by_name['obstacle_st_nudge'].message_type = _OBSTACLESTRAWDATA_OBSTACLESTDATA
_OBSTACLESTRAWDATA.fields_by_name['obstacle_st_sidepass'].message_type = _OBSTACLESTRAWDATA_OBSTACLESTDATA
_TRAJECTORYPOINTRAWFEATURE.fields_by_name['path_feature'].message_type = _PATHPOINTRAWFEATURE
_TRAJECTORYPOINTRAWFEATURE.fields_by_name['speed_feature'].message_type = _SPEEDPOINTRAWFEATURE
_TRAJECTORYRAWFEATURE.fields_by_name['point_feature'].message_type = _TRAJECTORYPOINTRAWFEATURE
_TRAJECTORYRAWFEATURE.fields_by_name['st_raw_data'].message_type = _OBSTACLESTRAWDATA
DESCRIPTOR.message_types_by_name['PathPointRawFeature'] = _PATHPOINTRAWFEATURE
DESCRIPTOR.message_types_by_name['SpeedPointRawFeature'] = _SPEEDPOINTRAWFEATURE
DESCRIPTOR.message_types_by_name['ObstacleSTRawData'] = _OBSTACLESTRAWDATA
DESCRIPTOR.message_types_by_name['TrajectoryPointRawFeature'] = _TRAJECTORYPOINTRAWFEATURE
DESCRIPTOR.message_types_by_name['TrajectoryRawFeature'] = _TRAJECTORYRAWFEATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PathPointRawFeature = _reflection.GeneratedProtocolMessageType('PathPointRawFeature', (_message.Message,), dict(
  DESCRIPTOR = _PATHPOINTRAWFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.PathPointRawFeature)
  ))
_sym_db.RegisterMessage(PathPointRawFeature)

SpeedPointRawFeature = _reflection.GeneratedProtocolMessageType('SpeedPointRawFeature', (_message.Message,), dict(

  ObjectDecisionFeature = _reflection.GeneratedProtocolMessageType('ObjectDecisionFeature', (_message.Message,), dict(
    DESCRIPTOR = _SPEEDPOINTRAWFEATURE_OBJECTDECISIONFEATURE,
    __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.SpeedPointRawFeature.ObjectDecisionFeature)
    ))
  ,
  DESCRIPTOR = _SPEEDPOINTRAWFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.SpeedPointRawFeature)
  ))
_sym_db.RegisterMessage(SpeedPointRawFeature)
_sym_db.RegisterMessage(SpeedPointRawFeature.ObjectDecisionFeature)

ObstacleSTRawData = _reflection.GeneratedProtocolMessageType('ObstacleSTRawData', (_message.Message,), dict(

  STPointPair = _reflection.GeneratedProtocolMessageType('STPointPair', (_message.Message,), dict(
    DESCRIPTOR = _OBSTACLESTRAWDATA_STPOINTPAIR,
    __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.ObstacleSTRawData.STPointPair)
    ))
  ,

  ObstacleSTData = _reflection.GeneratedProtocolMessageType('ObstacleSTData', (_message.Message,), dict(
    DESCRIPTOR = _OBSTACLESTRAWDATA_OBSTACLESTDATA,
    __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.ObstacleSTRawData.ObstacleSTData)
    ))
  ,
  DESCRIPTOR = _OBSTACLESTRAWDATA,
  __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.ObstacleSTRawData)
  ))
_sym_db.RegisterMessage(ObstacleSTRawData)
_sym_db.RegisterMessage(ObstacleSTRawData.STPointPair)
_sym_db.RegisterMessage(ObstacleSTRawData.ObstacleSTData)

TrajectoryPointRawFeature = _reflection.GeneratedProtocolMessageType('TrajectoryPointRawFeature', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYPOINTRAWFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.TrajectoryPointRawFeature)
  ))
_sym_db.RegisterMessage(TrajectoryPointRawFeature)

TrajectoryRawFeature = _reflection.GeneratedProtocolMessageType('TrajectoryRawFeature', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYRAWFEATURE,
  __module__ = 'modules.planning.proto.auto_tuning_raw_feature_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.autotuning.TrajectoryRawFeature)
  ))
_sym_db.RegisterMessage(TrajectoryRawFeature)


# @@protoc_insertion_point(module_scope)
