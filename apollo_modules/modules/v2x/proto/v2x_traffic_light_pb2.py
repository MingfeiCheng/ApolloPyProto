# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/v2x/proto/v2x_traffic_light.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common.proto import header_pb2 as modules_dot_common_dot_proto_dot_header__pb2
from apollo_modules.modules.common.proto import direction_pb2 as modules_dot_common_dot_proto_dot_direction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/v2x/proto/v2x_traffic_light.proto',
  package='apollo.v2x',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)modules/v2x/proto/v2x_traffic_light.proto\x12\napollo.v2x\x1a!modules/common/proto/header.proto\x1a$modules/common/proto/direction.proto\"\xb2\x03\n\x12SingleTrafficLight\x12\x33\n\x05\x63olor\x18\x01 \x01(\x0e\x32$.apollo.v2x.SingleTrafficLight.Color\x12?\n\x12traffic_light_type\x18\x02 \x03(\x0e\x32#.apollo.v2x.SingleTrafficLight.Type\x12\n\n\x02id\x18\x03 \x01(\t\x12\x1e\n\x16\x63olor_remaining_time_s\x18\x04 \x01(\x05\x12\x18\n\x10right_turn_light\x18\x05 \x01(\x08\x12\x38\n\nnext_color\x18\x06 \x01(\x0e\x32$.apollo.v2x.SingleTrafficLight.Color\x12\x1d\n\x15next_remaining_time_s\x18\x07 \x01(\x01\"P\n\x05\x43olor\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03RED\x10\x01\x12\n\n\x06YELLOW\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\t\n\x05\x42LACK\x10\x04\x12\x0f\n\x0b\x46LASH_GREEN\x10\x05\"5\n\x04Type\x12\x0c\n\x08STRAIGHT\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x12\n\n\x06U_TURN\x10\x03\"\xa4\x01\n\x10RoadTrafficLight\x12\x0f\n\x07gps_x_m\x18\x01 \x01(\x01\x12\x0f\n\x07gps_y_m\x18\x02 \x01(\x01\x12<\n\x14single_traffic_light\x18\x03 \x03(\x0b\x32\x1e.apollo.v2x.SingleTrafficLight\x12\x30\n\x0eroad_attribute\x18\x04 \x01(\x0e\x32\x18.apollo.common.Direction\"\xac\x01\n\x1cIntersectionTrafficLightData\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x38\n\x12road_traffic_light\x18\x02 \x03(\x0b\x32\x1c.apollo.v2x.RoadTrafficLight\x12\x17\n\x0fintersection_id\x18\x03 \x01(\x05\x12\x12\n\nconfidence\x18\x04 \x01(\x01')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_direction__pb2.DESCRIPTOR,])



_SINGLETRAFFICLIGHT_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='apollo.v2x.SingleTrafficLight.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH_GREEN', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=430,
  serialized_end=510,
)
_sym_db.RegisterEnumDescriptor(_SINGLETRAFFICLIGHT_COLOR)

_SINGLETRAFFICLIGHT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='apollo.v2x.SingleTrafficLight.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRAIGHT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='U_TURN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=512,
  serialized_end=565,
)
_sym_db.RegisterEnumDescriptor(_SINGLETRAFFICLIGHT_TYPE)


_SINGLETRAFFICLIGHT = _descriptor.Descriptor(
  name='SingleTrafficLight',
  full_name='apollo.v2x.SingleTrafficLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='apollo.v2x.SingleTrafficLight.color', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='traffic_light_type', full_name='apollo.v2x.SingleTrafficLight.traffic_light_type', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='apollo.v2x.SingleTrafficLight.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_remaining_time_s', full_name='apollo.v2x.SingleTrafficLight.color_remaining_time_s', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_turn_light', full_name='apollo.v2x.SingleTrafficLight.right_turn_light', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_color', full_name='apollo.v2x.SingleTrafficLight.next_color', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_remaining_time_s', full_name='apollo.v2x.SingleTrafficLight.next_remaining_time_s', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SINGLETRAFFICLIGHT_COLOR,
    _SINGLETRAFFICLIGHT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=565,
)


_ROADTRAFFICLIGHT = _descriptor.Descriptor(
  name='RoadTrafficLight',
  full_name='apollo.v2x.RoadTrafficLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gps_x_m', full_name='apollo.v2x.RoadTrafficLight.gps_x_m', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gps_y_m', full_name='apollo.v2x.RoadTrafficLight.gps_y_m', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='single_traffic_light', full_name='apollo.v2x.RoadTrafficLight.single_traffic_light', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_attribute', full_name='apollo.v2x.RoadTrafficLight.road_attribute', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=568,
  serialized_end=732,
)


_INTERSECTIONTRAFFICLIGHTDATA = _descriptor.Descriptor(
  name='IntersectionTrafficLightData',
  full_name='apollo.v2x.IntersectionTrafficLightData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.v2x.IntersectionTrafficLightData.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='road_traffic_light', full_name='apollo.v2x.IntersectionTrafficLightData.road_traffic_light', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intersection_id', full_name='apollo.v2x.IntersectionTrafficLightData.intersection_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='apollo.v2x.IntersectionTrafficLightData.confidence', index=3,
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
  serialized_start=735,
  serialized_end=907,
)

_SINGLETRAFFICLIGHT.fields_by_name['color'].enum_type = _SINGLETRAFFICLIGHT_COLOR
_SINGLETRAFFICLIGHT.fields_by_name['traffic_light_type'].enum_type = _SINGLETRAFFICLIGHT_TYPE
_SINGLETRAFFICLIGHT.fields_by_name['next_color'].enum_type = _SINGLETRAFFICLIGHT_COLOR
_SINGLETRAFFICLIGHT_COLOR.containing_type = _SINGLETRAFFICLIGHT
_SINGLETRAFFICLIGHT_TYPE.containing_type = _SINGLETRAFFICLIGHT
_ROADTRAFFICLIGHT.fields_by_name['single_traffic_light'].message_type = _SINGLETRAFFICLIGHT
_ROADTRAFFICLIGHT.fields_by_name['road_attribute'].enum_type = modules_dot_common_dot_proto_dot_direction__pb2._DIRECTION
_INTERSECTIONTRAFFICLIGHTDATA.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_INTERSECTIONTRAFFICLIGHTDATA.fields_by_name['road_traffic_light'].message_type = _ROADTRAFFICLIGHT
DESCRIPTOR.message_types_by_name['SingleTrafficLight'] = _SINGLETRAFFICLIGHT
DESCRIPTOR.message_types_by_name['RoadTrafficLight'] = _ROADTRAFFICLIGHT
DESCRIPTOR.message_types_by_name['IntersectionTrafficLightData'] = _INTERSECTIONTRAFFICLIGHTDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SingleTrafficLight = _reflection.GeneratedProtocolMessageType('SingleTrafficLight', (_message.Message,), dict(
  DESCRIPTOR = _SINGLETRAFFICLIGHT,
  __module__ = 'modules.v2x.proto.v2x_traffic_light_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.SingleTrafficLight)
  ))
_sym_db.RegisterMessage(SingleTrafficLight)

RoadTrafficLight = _reflection.GeneratedProtocolMessageType('RoadTrafficLight', (_message.Message,), dict(
  DESCRIPTOR = _ROADTRAFFICLIGHT,
  __module__ = 'modules.v2x.proto.v2x_traffic_light_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.RoadTrafficLight)
  ))
_sym_db.RegisterMessage(RoadTrafficLight)

IntersectionTrafficLightData = _reflection.GeneratedProtocolMessageType('IntersectionTrafficLightData', (_message.Message,), dict(
  DESCRIPTOR = _INTERSECTIONTRAFFICLIGHTDATA,
  __module__ = 'modules.v2x.proto.v2x_traffic_light_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.IntersectionTrafficLightData)
  ))
_sym_db.RegisterMessage(IntersectionTrafficLightData)


# @@protoc_insertion_point(module_scope)