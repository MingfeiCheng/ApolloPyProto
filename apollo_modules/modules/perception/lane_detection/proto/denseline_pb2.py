# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/lane_detection/proto/denseline.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7modules/perception/lane_detection/proto/denseline.proto\x12\"apollo.perception.camera.denseline\"\xbf\x01\n\x0e\x44\x65nselineParam\x12\x43\n\x0bmodel_param\x18\x01 \x01(\x0b\x32..apollo.perception.camera.denseline.ModelParam\x12\x43\n\tnet_param\x18\x02 \x01(\x0b\x32\x30.apollo.perception.camera.denseline.NetworkParam\x12\x0e\n\x06gpu_id\x18\x03 \x01(\x05\x12\x13\n\x0b\x63\x61mera_name\x18\x04 \x01(\t\"\xda\x02\n\nModelParam\x12\x1d\n\nmodel_name\x18\x01 \x01(\t:\tdenseline\x12\x1c\n\nproto_file\x18\x02 \x01(\t:\x08\x63\x61\x66\x66\x65.pt\x12 \n\x0bweight_file\x18\x03 \x01(\t:\x0b\x63\x61\x66\x66\x65.model\x12\x17\n\x0cresize_scale\x18\x04 \x01(\x02:\x01\x31\x12\x19\n\x0einput_offset_y\x18\x05 \x01(\r:\x01\x30\x12\x19\n\x0einput_offset_x\x18\x06 \x01(\r:\x01\x30\x12\x18\n\x0b\x63rop_height\x18\x07 \x01(\r:\x03\x35\x31\x32\x12\x17\n\ncrop_width\x18\x08 \x01(\r:\x03\x35\x31\x32\x12\x12\n\x06mean_b\x18\t \x01(\r:\x02\x39\x35\x12\x12\n\x06mean_g\x18\n \x01(\r:\x02\x39\x39\x12\x12\n\x06mean_r\x18\x0b \x01(\r:\x02\x39\x36\x12\x14\n\x06is_bgr\x18\x0c \x01(\x08:\x04true\x12\x19\n\nmodel_type\x18\r \x01(\t:\x05RTNet\"]\n\x0cNetworkParam\x12\x15\n\x07in_blob\x18\x01 \x01(\t:\x04\x64\x61ta\x12\x1a\n\x08out_blob\x18\x02 \x01(\t:\x08\x63onv_out\x12\x1a\n\x12internal_blob_int8\x18\x03 \x03(\t')



_DENSELINEPARAM = DESCRIPTOR.message_types_by_name['DenselineParam']
_MODELPARAM = DESCRIPTOR.message_types_by_name['ModelParam']
_NETWORKPARAM = DESCRIPTOR.message_types_by_name['NetworkParam']
DenselineParam = _reflection.GeneratedProtocolMessageType('DenselineParam', (_message.Message,), {
  'DESCRIPTOR' : _DENSELINEPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.denseline_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.denseline.DenselineParam)
  })
_sym_db.RegisterMessage(DenselineParam)

ModelParam = _reflection.GeneratedProtocolMessageType('ModelParam', (_message.Message,), {
  'DESCRIPTOR' : _MODELPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.denseline_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.denseline.ModelParam)
  })
_sym_db.RegisterMessage(ModelParam)

NetworkParam = _reflection.GeneratedProtocolMessageType('NetworkParam', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKPARAM,
  '__module__' : 'modules.perception.lane_detection.proto.denseline_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.denseline.NetworkParam)
  })
_sym_db.RegisterMessage(NetworkParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DENSELINEPARAM._serialized_start=96
  _DENSELINEPARAM._serialized_end=287
  _MODELPARAM._serialized_start=290
  _MODELPARAM._serialized_end=636
  _NETWORKPARAM._serialized_start=638
  _NETWORKPARAM._serialized_end=731
# @@protoc_insertion_point(module_scope)
