# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/camera/lib/traffic_light/detector/recognition/proto/recognition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/perception/camera/lib/traffic_light/detector/recognition/proto/recognition.proto',
  package='apollo.perception.camera.traffic_light.recognition',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\nXmodules/perception/camera/lib/traffic_light/detector/recognition/proto/recognition.proto\x12\x32\x61pollo.perception.camera.traffic_light.recognition\"\xcf\x02\n\rClassifyParam\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x1c\n\nmodel_type\x18\x02 \x01(\t:\x08\x43\x61\x66\x66\x65Net\x12\x12\n\ninput_blob\x18\x03 \x01(\t\x12\x13\n\x0boutput_blob\x18\x04 \x01(\t\x12\x13\n\x0bweight_file\x18\x05 \x01(\t\x12\x12\n\nproto_file\x18\x06 \x01(\t\x12\x1a\n\x12\x63lassify_threshold\x18\x07 \x01(\x02\x12\x1d\n\x15\x63lassify_resize_width\x18\x08 \x01(\x05\x12\x1e\n\x16\x63lassify_resize_height\x18\t \x01(\x05\x12\r\n\x05scale\x18\n \x01(\x02\x12\x12\n\x06mean_b\x18\x0c \x01(\x02:\x02\x39\x35\x12\x12\n\x06mean_g\x18\r \x01(\x02:\x02\x39\x39\x12\x12\n\x06mean_r\x18\x0e \x01(\x02:\x02\x39\x36\x12\x14\n\x06is_bgr\x18\x0f \x01(\x08:\x04true\"\xa6\x02\n\x11RecognizeBoxParam\x12Y\n\x0evertical_model\x18\x01 \x01(\x0b\x32\x41.apollo.perception.camera.traffic_light.recognition.ClassifyParam\x12Y\n\x0equadrate_model\x18\x02 \x01(\x0b\x32\x41.apollo.perception.camera.traffic_light.recognition.ClassifyParam\x12[\n\x10horizontal_model\x18\x03 \x01(\x0b\x32\x41.apollo.perception.camera.traffic_light.recognition.ClassifyParam')
)




_CLASSIFYPARAM = _descriptor.Descriptor(
  name='ClassifyParam',
  full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_name', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.model_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_type', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.model_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("CaffeNet").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_blob', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.input_blob', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_blob', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.output_blob', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight_file', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.weight_file', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto_file', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.proto_file', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classify_threshold', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.classify_threshold', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classify_resize_width', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.classify_resize_width', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classify_resize_height', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.classify_resize_height', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.scale', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_b', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.mean_b', index=10,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(95),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_g', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.mean_g', index=11,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(99),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_r', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.mean_r', index=12,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(96),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_bgr', full_name='apollo.perception.camera.traffic_light.recognition.ClassifyParam.is_bgr', index=13,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=145,
  serialized_end=480,
)


_RECOGNIZEBOXPARAM = _descriptor.Descriptor(
  name='RecognizeBoxParam',
  full_name='apollo.perception.camera.traffic_light.recognition.RecognizeBoxParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertical_model', full_name='apollo.perception.camera.traffic_light.recognition.RecognizeBoxParam.vertical_model', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quadrate_model', full_name='apollo.perception.camera.traffic_light.recognition.RecognizeBoxParam.quadrate_model', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_model', full_name='apollo.perception.camera.traffic_light.recognition.RecognizeBoxParam.horizontal_model', index=2,
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
  serialized_start=483,
  serialized_end=777,
)

_RECOGNIZEBOXPARAM.fields_by_name['vertical_model'].message_type = _CLASSIFYPARAM
_RECOGNIZEBOXPARAM.fields_by_name['quadrate_model'].message_type = _CLASSIFYPARAM
_RECOGNIZEBOXPARAM.fields_by_name['horizontal_model'].message_type = _CLASSIFYPARAM
DESCRIPTOR.message_types_by_name['ClassifyParam'] = _CLASSIFYPARAM
DESCRIPTOR.message_types_by_name['RecognizeBoxParam'] = _RECOGNIZEBOXPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifyParam = _reflection.GeneratedProtocolMessageType('ClassifyParam', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFYPARAM,
  __module__ = 'modules.perception.camera.lib.traffic_light.detector.recognition.proto.recognition_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.traffic_light.recognition.ClassifyParam)
  ))
_sym_db.RegisterMessage(ClassifyParam)

RecognizeBoxParam = _reflection.GeneratedProtocolMessageType('RecognizeBoxParam', (_message.Message,), dict(
  DESCRIPTOR = _RECOGNIZEBOXPARAM,
  __module__ = 'modules.perception.camera.lib.traffic_light.detector.recognition.proto.recognition_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.traffic_light.recognition.RecognizeBoxParam)
  ))
_sym_db.RegisterMessage(RecognizeBoxParam)


# @@protoc_insertion_point(module_scope)