# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/camera_location_refinement/location_refiner/proto/location_refiner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n[modules/perception/camera_location_refinement/location_refiner/proto/location_refiner.proto\x12)apollo.perception.camera.location_refiner\"W\n\x14LocationRefinerParam\x12\x1e\n\x12min_dist_to_camera\x18\x01 \x01(\x02:\x02\x33\x30\x12\x1f\n\x12roi_h2bottom_scale\x18\x02 \x01(\x02:\x03\x30.5')



_LOCATIONREFINERPARAM = DESCRIPTOR.message_types_by_name['LocationRefinerParam']
LocationRefinerParam = _reflection.GeneratedProtocolMessageType('LocationRefinerParam', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONREFINERPARAM,
  '__module__' : 'modules.perception.camera_location_refinement.location_refiner.proto.location_refiner_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.location_refiner.LocationRefinerParam)
  })
_sym_db.RegisterMessage(LocationRefinerParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCATIONREFINERPARAM._serialized_start=138
  _LOCATIONREFINERPARAM._serialized_end=225
# @@protoc_insertion_point(module_scope)
