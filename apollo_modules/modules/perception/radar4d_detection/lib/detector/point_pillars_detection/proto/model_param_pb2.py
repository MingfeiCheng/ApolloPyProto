# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/radar4d_detection/lib/detector/point_pillars_detection/proto/model_param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.common.proto import model_info_pb2 as modules_dot_perception_dot_common_dot_proto_dot_model__info__pb2
from apollo_modules.modules.perception.common.proto import model_process_pb2 as modules_dot_perception_dot_common_dot_proto_dot_model__process__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\namodules/perception/radar4d_detection/lib/detector/point_pillars_detection/proto/model_param.proto\x12&apollo.perception.radar4d.pointpillars\x1a\x30modules/perception/common/proto/model_info.proto\x1a\x33modules/perception/common/proto/model_process.proto\"\xc9\x01\n\nModelParam\x12\x31\n\x04info\x18\x01 \x01(\x0b\x32#.apollo.perception.common.ModelInfo\x12\x42\n\npreprocess\x18\x02 \x01(\x0b\x32..apollo.perception.common.PointCloudPreProcess\x12\x44\n\x0bpostprocess\x18\x03 \x01(\x0b\x32/.apollo.perception.common.PointCloudPostProcess')



_MODELPARAM = DESCRIPTOR.message_types_by_name['ModelParam']
ModelParam = _reflection.GeneratedProtocolMessageType('ModelParam', (_message.Message,), {
  'DESCRIPTOR' : _MODELPARAM,
  '__module__' : 'modules.perception.radar4d_detection.lib.detector.point_pillars_detection.proto.model_param_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.radar4d.pointpillars.ModelParam)
  })
_sym_db.RegisterMessage(ModelParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODELPARAM._serialized_start=245
  _MODELPARAM._serialized_end=446
# @@protoc_insertion_point(module_scope)
