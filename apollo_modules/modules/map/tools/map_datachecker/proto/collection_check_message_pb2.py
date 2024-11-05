# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/map/tools/map_datachecker/proto/collection_check_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.map.tools.map_datachecker.proto import collection_error_code_pb2 as modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/map/tools/map_datachecker/proto/collection_check_message.proto',
  package='apollo.hdmap',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nFmodules/map/tools/map_datachecker/proto/collection_check_message.proto\x12\x0c\x61pollo.hdmap\x1a\x43modules/map/tools/map_datachecker/proto/collection_error_code.proto\"3\n\x0bVerifyRange\x12\x12\n\nstart_time\x18\x01 \x01(\x01\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x01\"2\n\nLoopResult\x12\x12\n\nis_reached\x18\x01 \x02(\x08\x12\x10\n\x08loop_num\x18\x02 \x01(\x01\"!\n\x0bTopicResult\x12\x12\n\ntopic_lack\x18\x01 \x03(\t\"`\n\tFrameRate\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x15\n\rexpected_rate\x18\x02 \x01(\x01\x12\x14\n\x0c\x63urrent_rate\x18\x03 \x01(\x01\x12\x17\n\x0f\x62\x61\x64_record_name\x18\x04 \x03(\t\"a\n\x0cVerifyResult\x12)\n\x06topics\x18\x01 \x01(\x0b\x32\x19.apollo.hdmap.TopicResult\x12&\n\x05rates\x18\x02 \x03(\x0b\x32\x17.apollo.hdmap.FrameRate\"\\\n\x14\x43hannelVerifyRequest\x12\"\n\x03\x63md\x18\x01 \x01(\x0e\x32\x15.apollo.hdmap.CmdType\x12\x12\n\ncollect_id\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\"j\n\x15\x43hannelVerifyResponse\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.apollo.hdmap.ErrorCode\x12*\n\x06result\x18\x02 \x01(\x0b\x32\x1a.apollo.hdmap.VerifyResult\"\x88\x01\n\x12LoopsVerifyRequest\x12\"\n\x03\x63md\x18\x01 \x01(\x0e\x32\x15.apollo.hdmap.CmdType\x12$\n\x04type\x18\x02 \x01(\x0e\x32\x16.apollo.hdmap.DataType\x12(\n\x05range\x18\x03 \x03(\x0b\x32\x19.apollo.hdmap.VerifyRange\"}\n\x13LoopsVerifyResponse\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01\x12-\n\x0bloop_result\x18\x03 \x01(\x0b\x32\x18.apollo.hdmap.LoopResult\"9\n\x13\x44ynamicAlignRequest\x12\"\n\x03\x63md\x18\x01 \x01(\x0e\x32\x15.apollo.hdmap.CmdType\"O\n\x14\x44ynamicAlignResponse\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01\"8\n\x12StaticAlignRequest\x12\"\n\x03\x63md\x18\x01 \x01(\x0e\x32\x15.apollo.hdmap.CmdType\"N\n\x13StaticAlignResponse\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01\"7\n\x11\x45ightRouteRequest\x12\"\n\x03\x63md\x18\x01 \x01(\x0e\x32\x15.apollo.hdmap.CmdType\"M\n\x12\x45ightRouteResponse\x12%\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x17.apollo.hdmap.ErrorCode\x12\x10\n\x08progress\x18\x02 \x01(\x01*)\n\x07\x43mdType\x12\t\n\x05START\x10\x01\x12\t\n\x05\x43HECK\x10\x02\x12\x08\n\x04STOP\x10\x03*,\n\x08\x44\x61taType\x12\x0e\n\nMAP_MAKING\x10\x01\x12\x10\n\x0cMAP_CHECKOUT\x10\x02')
  ,
  dependencies=[modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2.DESCRIPTOR,])

_CMDTYPE = _descriptor.EnumDescriptor(
  name='CmdType',
  full_name='apollo.hdmap.CmdType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECK', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1376,
  serialized_end=1417,
)
_sym_db.RegisterEnumDescriptor(_CMDTYPE)

CmdType = enum_type_wrapper.EnumTypeWrapper(_CMDTYPE)
_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='apollo.hdmap.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAP_MAKING', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_CHECKOUT', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1419,
  serialized_end=1463,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
START = 1
CHECK = 2
STOP = 3
MAP_MAKING = 1
MAP_CHECKOUT = 2



_VERIFYRANGE = _descriptor.Descriptor(
  name='VerifyRange',
  full_name='apollo.hdmap.VerifyRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='apollo.hdmap.VerifyRange.start_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='apollo.hdmap.VerifyRange.end_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=157,
  serialized_end=208,
)


_LOOPRESULT = _descriptor.Descriptor(
  name='LoopResult',
  full_name='apollo.hdmap.LoopResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_reached', full_name='apollo.hdmap.LoopResult.is_reached', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loop_num', full_name='apollo.hdmap.LoopResult.loop_num', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=210,
  serialized_end=260,
)


_TOPICRESULT = _descriptor.Descriptor(
  name='TopicResult',
  full_name='apollo.hdmap.TopicResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_lack', full_name='apollo.hdmap.TopicResult.topic_lack', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=262,
  serialized_end=295,
)


_FRAMERATE = _descriptor.Descriptor(
  name='FrameRate',
  full_name='apollo.hdmap.FrameRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='apollo.hdmap.FrameRate.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expected_rate', full_name='apollo.hdmap.FrameRate.expected_rate', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_rate', full_name='apollo.hdmap.FrameRate.current_rate', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bad_record_name', full_name='apollo.hdmap.FrameRate.bad_record_name', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=297,
  serialized_end=393,
)


_VERIFYRESULT = _descriptor.Descriptor(
  name='VerifyResult',
  full_name='apollo.hdmap.VerifyResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topics', full_name='apollo.hdmap.VerifyResult.topics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rates', full_name='apollo.hdmap.VerifyResult.rates', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=395,
  serialized_end=492,
)


_CHANNELVERIFYREQUEST = _descriptor.Descriptor(
  name='ChannelVerifyRequest',
  full_name='apollo.hdmap.ChannelVerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='apollo.hdmap.ChannelVerifyRequest.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collect_id', full_name='apollo.hdmap.ChannelVerifyRequest.collect_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='apollo.hdmap.ChannelVerifyRequest.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=494,
  serialized_end=586,
)


_CHANNELVERIFYRESPONSE = _descriptor.Descriptor(
  name='ChannelVerifyResponse',
  full_name='apollo.hdmap.ChannelVerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='apollo.hdmap.ChannelVerifyResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='apollo.hdmap.ChannelVerifyResponse.result', index=1,
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
  serialized_start=588,
  serialized_end=694,
)


_LOOPSVERIFYREQUEST = _descriptor.Descriptor(
  name='LoopsVerifyRequest',
  full_name='apollo.hdmap.LoopsVerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='apollo.hdmap.LoopsVerifyRequest.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.hdmap.LoopsVerifyRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='apollo.hdmap.LoopsVerifyRequest.range', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=697,
  serialized_end=833,
)


_LOOPSVERIFYRESPONSE = _descriptor.Descriptor(
  name='LoopsVerifyResponse',
  full_name='apollo.hdmap.LoopsVerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='apollo.hdmap.LoopsVerifyResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='apollo.hdmap.LoopsVerifyResponse.progress', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loop_result', full_name='apollo.hdmap.LoopsVerifyResponse.loop_result', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=835,
  serialized_end=960,
)


_DYNAMICALIGNREQUEST = _descriptor.Descriptor(
  name='DynamicAlignRequest',
  full_name='apollo.hdmap.DynamicAlignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='apollo.hdmap.DynamicAlignRequest.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=962,
  serialized_end=1019,
)


_DYNAMICALIGNRESPONSE = _descriptor.Descriptor(
  name='DynamicAlignResponse',
  full_name='apollo.hdmap.DynamicAlignResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='apollo.hdmap.DynamicAlignResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='apollo.hdmap.DynamicAlignResponse.progress', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=1021,
  serialized_end=1100,
)


_STATICALIGNREQUEST = _descriptor.Descriptor(
  name='StaticAlignRequest',
  full_name='apollo.hdmap.StaticAlignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='apollo.hdmap.StaticAlignRequest.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=1102,
  serialized_end=1158,
)


_STATICALIGNRESPONSE = _descriptor.Descriptor(
  name='StaticAlignResponse',
  full_name='apollo.hdmap.StaticAlignResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='apollo.hdmap.StaticAlignResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='apollo.hdmap.StaticAlignResponse.progress', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=1160,
  serialized_end=1238,
)


_EIGHTROUTEREQUEST = _descriptor.Descriptor(
  name='EightRouteRequest',
  full_name='apollo.hdmap.EightRouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='apollo.hdmap.EightRouteRequest.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=1240,
  serialized_end=1295,
)


_EIGHTROUTERESPONSE = _descriptor.Descriptor(
  name='EightRouteResponse',
  full_name='apollo.hdmap.EightRouteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='apollo.hdmap.EightRouteResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='apollo.hdmap.EightRouteResponse.progress', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=1297,
  serialized_end=1374,
)

_VERIFYRESULT.fields_by_name['topics'].message_type = _TOPICRESULT
_VERIFYRESULT.fields_by_name['rates'].message_type = _FRAMERATE
_CHANNELVERIFYREQUEST.fields_by_name['cmd'].enum_type = _CMDTYPE
_CHANNELVERIFYRESPONSE.fields_by_name['code'].enum_type = modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2._ERRORCODE
_CHANNELVERIFYRESPONSE.fields_by_name['result'].message_type = _VERIFYRESULT
_LOOPSVERIFYREQUEST.fields_by_name['cmd'].enum_type = _CMDTYPE
_LOOPSVERIFYREQUEST.fields_by_name['type'].enum_type = _DATATYPE
_LOOPSVERIFYREQUEST.fields_by_name['range'].message_type = _VERIFYRANGE
_LOOPSVERIFYRESPONSE.fields_by_name['code'].enum_type = modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2._ERRORCODE
_LOOPSVERIFYRESPONSE.fields_by_name['loop_result'].message_type = _LOOPRESULT
_DYNAMICALIGNREQUEST.fields_by_name['cmd'].enum_type = _CMDTYPE
_DYNAMICALIGNRESPONSE.fields_by_name['code'].enum_type = modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2._ERRORCODE
_STATICALIGNREQUEST.fields_by_name['cmd'].enum_type = _CMDTYPE
_STATICALIGNRESPONSE.fields_by_name['code'].enum_type = modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2._ERRORCODE
_EIGHTROUTEREQUEST.fields_by_name['cmd'].enum_type = _CMDTYPE
_EIGHTROUTERESPONSE.fields_by_name['code'].enum_type = modules_dot_map_dot_tools_dot_map__datachecker_dot_proto_dot_collection__error__code__pb2._ERRORCODE
DESCRIPTOR.message_types_by_name['VerifyRange'] = _VERIFYRANGE
DESCRIPTOR.message_types_by_name['LoopResult'] = _LOOPRESULT
DESCRIPTOR.message_types_by_name['TopicResult'] = _TOPICRESULT
DESCRIPTOR.message_types_by_name['FrameRate'] = _FRAMERATE
DESCRIPTOR.message_types_by_name['VerifyResult'] = _VERIFYRESULT
DESCRIPTOR.message_types_by_name['ChannelVerifyRequest'] = _CHANNELVERIFYREQUEST
DESCRIPTOR.message_types_by_name['ChannelVerifyResponse'] = _CHANNELVERIFYRESPONSE
DESCRIPTOR.message_types_by_name['LoopsVerifyRequest'] = _LOOPSVERIFYREQUEST
DESCRIPTOR.message_types_by_name['LoopsVerifyResponse'] = _LOOPSVERIFYRESPONSE
DESCRIPTOR.message_types_by_name['DynamicAlignRequest'] = _DYNAMICALIGNREQUEST
DESCRIPTOR.message_types_by_name['DynamicAlignResponse'] = _DYNAMICALIGNRESPONSE
DESCRIPTOR.message_types_by_name['StaticAlignRequest'] = _STATICALIGNREQUEST
DESCRIPTOR.message_types_by_name['StaticAlignResponse'] = _STATICALIGNRESPONSE
DESCRIPTOR.message_types_by_name['EightRouteRequest'] = _EIGHTROUTEREQUEST
DESCRIPTOR.message_types_by_name['EightRouteResponse'] = _EIGHTROUTERESPONSE
DESCRIPTOR.enum_types_by_name['CmdType'] = _CMDTYPE
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VerifyRange = _reflection.GeneratedProtocolMessageType('VerifyRange', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYRANGE,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.VerifyRange)
  ))
_sym_db.RegisterMessage(VerifyRange)

LoopResult = _reflection.GeneratedProtocolMessageType('LoopResult', (_message.Message,), dict(
  DESCRIPTOR = _LOOPRESULT,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.LoopResult)
  ))
_sym_db.RegisterMessage(LoopResult)

TopicResult = _reflection.GeneratedProtocolMessageType('TopicResult', (_message.Message,), dict(
  DESCRIPTOR = _TOPICRESULT,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.TopicResult)
  ))
_sym_db.RegisterMessage(TopicResult)

FrameRate = _reflection.GeneratedProtocolMessageType('FrameRate', (_message.Message,), dict(
  DESCRIPTOR = _FRAMERATE,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.FrameRate)
  ))
_sym_db.RegisterMessage(FrameRate)

VerifyResult = _reflection.GeneratedProtocolMessageType('VerifyResult', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYRESULT,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.VerifyResult)
  ))
_sym_db.RegisterMessage(VerifyResult)

ChannelVerifyRequest = _reflection.GeneratedProtocolMessageType('ChannelVerifyRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELVERIFYREQUEST,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.ChannelVerifyRequest)
  ))
_sym_db.RegisterMessage(ChannelVerifyRequest)

ChannelVerifyResponse = _reflection.GeneratedProtocolMessageType('ChannelVerifyResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELVERIFYRESPONSE,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.ChannelVerifyResponse)
  ))
_sym_db.RegisterMessage(ChannelVerifyResponse)

LoopsVerifyRequest = _reflection.GeneratedProtocolMessageType('LoopsVerifyRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOOPSVERIFYREQUEST,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.LoopsVerifyRequest)
  ))
_sym_db.RegisterMessage(LoopsVerifyRequest)

LoopsVerifyResponse = _reflection.GeneratedProtocolMessageType('LoopsVerifyResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOOPSVERIFYRESPONSE,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.LoopsVerifyResponse)
  ))
_sym_db.RegisterMessage(LoopsVerifyResponse)

DynamicAlignRequest = _reflection.GeneratedProtocolMessageType('DynamicAlignRequest', (_message.Message,), dict(
  DESCRIPTOR = _DYNAMICALIGNREQUEST,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.DynamicAlignRequest)
  ))
_sym_db.RegisterMessage(DynamicAlignRequest)

DynamicAlignResponse = _reflection.GeneratedProtocolMessageType('DynamicAlignResponse', (_message.Message,), dict(
  DESCRIPTOR = _DYNAMICALIGNRESPONSE,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.DynamicAlignResponse)
  ))
_sym_db.RegisterMessage(DynamicAlignResponse)

StaticAlignRequest = _reflection.GeneratedProtocolMessageType('StaticAlignRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATICALIGNREQUEST,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.StaticAlignRequest)
  ))
_sym_db.RegisterMessage(StaticAlignRequest)

StaticAlignResponse = _reflection.GeneratedProtocolMessageType('StaticAlignResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATICALIGNRESPONSE,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.StaticAlignResponse)
  ))
_sym_db.RegisterMessage(StaticAlignResponse)

EightRouteRequest = _reflection.GeneratedProtocolMessageType('EightRouteRequest', (_message.Message,), dict(
  DESCRIPTOR = _EIGHTROUTEREQUEST,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.EightRouteRequest)
  ))
_sym_db.RegisterMessage(EightRouteRequest)

EightRouteResponse = _reflection.GeneratedProtocolMessageType('EightRouteResponse', (_message.Message,), dict(
  DESCRIPTOR = _EIGHTROUTERESPONSE,
  __module__ = 'modules.map.tools.map_datachecker.proto.collection_check_message_pb2'
  # @@protoc_insertion_point(class_scope:apollo.hdmap.EightRouteResponse)
  ))
_sym_db.RegisterMessage(EightRouteResponse)


# @@protoc_insertion_point(module_scope)
