# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/proto/math/cos_theta_smoother_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;modules/planning/proto/math/cos_theta_smoother_config.proto\x12\x0f\x61pollo.planning\"\xc8\x02\n\x16\x43osThetaSmootherConfig\x12(\n\x19weight_cos_included_angle\x18\x01 \x01(\x01:\x05\x31\x30\x30\x30\x30\x12\x1f\n\x14weight_anchor_points\x18\x02 \x01(\x01:\x01\x31\x12\x18\n\rweight_length\x18\x03 \x01(\x01:\x01\x31\x12\x16\n\x0bprint_level\x18\x04 \x01(\x05:\x01\x30\x12\"\n\x15max_num_of_iterations\x18\x05 \x01(\x05:\x03\x35\x30\x30\x12(\n\x1c\x61\x63\x63\x65ptable_num_of_iterations\x18\x06 \x01(\x05:\x02\x31\x35\x12\x12\n\x03tol\x18\x07 \x01(\x01:\x05\x31\x65-08\x12\x1b\n\x0e\x61\x63\x63\x65ptable_tol\x18\x08 \x01(\x01:\x03\x30.1\x12\x32\n#ipopt_use_automatic_differentiation\x18\t \x01(\x08:\x05\x66\x61lse')



_COSTHETASMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['CosThetaSmootherConfig']
CosThetaSmootherConfig = _reflection.GeneratedProtocolMessageType('CosThetaSmootherConfig', (_message.Message,), {
  'DESCRIPTOR' : _COSTHETASMOOTHERCONFIG,
  '__module__' : 'modules.planning.proto.math.cos_theta_smoother_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.CosThetaSmootherConfig)
  })
_sym_db.RegisterMessage(CosThetaSmootherConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COSTHETASMOOTHERCONFIG._serialized_start=81
  _COSTHETASMOOTHERCONFIG._serialized_end=409
# @@protoc_insertion_point(module_scope)
