# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/prediction/proto/offline_features.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import pnc_point_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2
from apollo_modules.modules.common_msgs.prediction_msgs import feature_pb2 as modules_dot_common__msgs_dot_prediction__msgs_dot_feature__pb2
from apollo_modules.modules.prediction.proto import prediction_conf_pb2 as modules_dot_prediction_dot_proto_dot_prediction__conf__pb2
from apollo_modules.modules.common_msgs.prediction_msgs import scenario_pb2 as modules_dot_common__msgs_dot_prediction__msgs_dot_scenario__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/prediction/proto/offline_features.proto\x12\x11\x61pollo.prediction\x1a.modules/common_msgs/basic_msgs/pnc_point.proto\x1a\x31modules/common_msgs/prediction_msgs/feature.proto\x1a.modules/prediction/proto/prediction_conf.proto\x1a\x32modules/common_msgs/prediction_msgs/scenario.proto\"\xb1\x01\n\x0f\x44\x61taForLearning\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x1d\n\x15\x66\x65\x61tures_for_learning\x18\x03 \x03(\x01\x12$\n\x1cstring_features_for_learning\x18\x07 \x03(\t\x12\x0e\n\x06labels\x18\x04 \x03(\x01\x12\x18\n\x10lane_sequence_id\x18\x06 \x01(\x05\"T\n\x13ListDataForLearning\x12=\n\x11\x64\x61ta_for_learning\x18\x01 \x03(\x0b\x32\".apollo.prediction.DataForLearning\"\xcb\x01\n\x10PredictionResult\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x31\n\ntrajectory\x18\x03 \x03(\x0b\x32\x1d.apollo.prediction.Trajectory\x12\x36\n\robstacle_conf\x18\x04 \x01(\x0b\x32\x1f.apollo.prediction.ObstacleConf\x12-\n\x08scenario\x18\x05 \x01(\x0b\x32\x1b.apollo.prediction.Scenario\"V\n\x14ListPredictionResult\x12>\n\x11prediction_result\x18\x01 \x03(\x0b\x32#.apollo.prediction.PredictionResult\">\n\x0cListFrameEnv\x12.\n\tframe_env\x18\x01 \x03(\x0b\x32\x1b.apollo.prediction.FrameEnv\"\xcc\x01\n\rDataForTuning\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\x12\x19\n\x11values_for_tuning\x18\x04 \x03(\x01\x12\x17\n\x0freal_cost_value\x18\x05 \x03(\x01\x12\x18\n\x10lane_sequence_id\x18\x06 \x01(\x05\x12<\n\x14\x61\x64\x63_trajectory_point\x18\x07 \x03(\x0b\x32\x1e.apollo.common.TrajectoryPoint\"N\n\x11ListDataForTuning\x12\x39\n\x0f\x64\x61ta_for_tuning\x18\x01 \x03(\x0b\x32 .apollo.prediction.DataForTuning\"7\n\x08\x46\x65\x61tures\x12+\n\x07\x66\x65\x61ture\x18\x01 \x03(\x0b\x32\x1a.apollo.prediction.Feature')



_DATAFORLEARNING = DESCRIPTOR.message_types_by_name['DataForLearning']
_LISTDATAFORLEARNING = DESCRIPTOR.message_types_by_name['ListDataForLearning']
_PREDICTIONRESULT = DESCRIPTOR.message_types_by_name['PredictionResult']
_LISTPREDICTIONRESULT = DESCRIPTOR.message_types_by_name['ListPredictionResult']
_LISTFRAMEENV = DESCRIPTOR.message_types_by_name['ListFrameEnv']
_DATAFORTUNING = DESCRIPTOR.message_types_by_name['DataForTuning']
_LISTDATAFORTUNING = DESCRIPTOR.message_types_by_name['ListDataForTuning']
_FEATURES = DESCRIPTOR.message_types_by_name['Features']
DataForLearning = _reflection.GeneratedProtocolMessageType('DataForLearning', (_message.Message,), {
  'DESCRIPTOR' : _DATAFORLEARNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.DataForLearning)
  })
_sym_db.RegisterMessage(DataForLearning)

ListDataForLearning = _reflection.GeneratedProtocolMessageType('ListDataForLearning', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATAFORLEARNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListDataForLearning)
  })
_sym_db.RegisterMessage(ListDataForLearning)

PredictionResult = _reflection.GeneratedProtocolMessageType('PredictionResult', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONRESULT,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.PredictionResult)
  })
_sym_db.RegisterMessage(PredictionResult)

ListPredictionResult = _reflection.GeneratedProtocolMessageType('ListPredictionResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTPREDICTIONRESULT,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListPredictionResult)
  })
_sym_db.RegisterMessage(ListPredictionResult)

ListFrameEnv = _reflection.GeneratedProtocolMessageType('ListFrameEnv', (_message.Message,), {
  'DESCRIPTOR' : _LISTFRAMEENV,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListFrameEnv)
  })
_sym_db.RegisterMessage(ListFrameEnv)

DataForTuning = _reflection.GeneratedProtocolMessageType('DataForTuning', (_message.Message,), {
  'DESCRIPTOR' : _DATAFORTUNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.DataForTuning)
  })
_sym_db.RegisterMessage(DataForTuning)

ListDataForTuning = _reflection.GeneratedProtocolMessageType('ListDataForTuning', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATAFORTUNING,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.ListDataForTuning)
  })
_sym_db.RegisterMessage(ListDataForTuning)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {
  'DESCRIPTOR' : _FEATURES,
  '__module__' : 'modules.prediction.proto.offline_features_pb2'
  # @@protoc_insertion_point(class_scope:apollo.prediction.Features)
  })
_sym_db.RegisterMessage(Features)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATAFORLEARNING._serialized_start=270
  _DATAFORLEARNING._serialized_end=447
  _LISTDATAFORLEARNING._serialized_start=449
  _LISTDATAFORLEARNING._serialized_end=533
  _PREDICTIONRESULT._serialized_start=536
  _PREDICTIONRESULT._serialized_end=739
  _LISTPREDICTIONRESULT._serialized_start=741
  _LISTPREDICTIONRESULT._serialized_end=827
  _LISTFRAMEENV._serialized_start=829
  _LISTFRAMEENV._serialized_end=891
  _DATAFORTUNING._serialized_start=894
  _DATAFORTUNING._serialized_end=1098
  _LISTDATAFORTUNING._serialized_start=1100
  _LISTDATAFORTUNING._serialized_end=1178
  _FEATURES._serialized_start=1180
  _FEATURES._serialized_end=1235
# @@protoc_insertion_point(module_scope)
