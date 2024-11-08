# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/planning_base/proto/reference_line_smoother_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.planning.planning_base.proto.math import cos_theta_smoother_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_math_dot_cos__theta__smoother__config__pb2
from apollo_modules.modules.planning.planning_base.proto.math import fem_pos_deviation_smoother_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_math_dot_fem__pos__deviation__smoother__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nImodules/planning/planning_base/proto/reference_line_smoother_config.proto\x12\x0f\x61pollo.planning\x1aImodules/planning/planning_base/proto/math/cos_theta_smoother_config.proto\x1aQmodules/planning/planning_base/proto/math/fem_pos_deviation_smoother_config.proto\"\xbf\x01\n\x16QpSplineSmootherConfig\x12\x17\n\x0cspline_order\x18\x01 \x01(\r:\x01\x35\x12\x1d\n\x11max_spline_length\x18\x02 \x01(\x01:\x02\x32\x35\x12\"\n\x15regularization_weight\x18\x03 \x01(\x01:\x03\x30.1\x12#\n\x18second_derivative_weight\x18\x04 \x01(\x01:\x01\x30\x12$\n\x17third_derivative_weight\x18\x05 \x01(\x01:\x03\x31\x30\x30\"\xa3\x02\n\x14SpiralSmootherConfig\x12\x1a\n\rmax_deviation\x18\x01 \x01(\x01:\x03\x30.1\x12\x1c\n\x10piecewise_length\x18\x02 \x01(\x01:\x02\x31\x30\x12\x1b\n\rmax_iteration\x18\x03 \x01(\r:\x04\x31\x30\x30\x30\x12\x16\n\x07opt_tol\x18\x04 \x01(\x01:\x05\x31\x65-08\x12!\n\x12opt_acceptable_tol\x18\x05 \x01(\x01:\x05\x31\x65-06\x12$\n\x18opt_acceptable_iteration\x18\x06 \x01(\r:\x02\x31\x35\x12\x1e\n\x13weight_curve_length\x18\x07 \x01(\x01:\x01\x31\x12\x17\n\x0cweight_kappa\x18\x08 \x01(\x01:\x01\x31\x12\x1a\n\rweight_dkappa\x18\t \x01(\x01:\x03\x31\x30\x30\"\xa3\x03\n\x1c\x44iscretePointsSmootherConfig\x12t\n\x10smoothing_method\x18\x03 \x01(\x0e\x32=.apollo.planning.DiscretePointsSmootherConfig.SmoothingMethod:\x1b\x46\x45M_POS_DEVIATION_SMOOTHING\x12\x46\n\x13\x63os_theta_smoothing\x18\x04 \x01(\x0b\x32\'.apollo.planning.CosThetaSmootherConfigH\x00\x12U\n\x1b\x66\x65m_pos_deviation_smoothing\x18\x05 \x01(\x0b\x32..apollo.planning.FemPosDeviationSmootherConfigH\x00\"\\\n\x0fSmoothingMethod\x12\x0f\n\x0bNOT_DEFINED\x10\x00\x12\x17\n\x13\x43OS_THETA_SMOOTHING\x10\x01\x12\x1f\n\x1b\x46\x45M_POS_DEVIATION_SMOOTHING\x10\x02\x42\x10\n\x0eSmootherConfig\"\x80\x04\n\x1bReferenceLineSmootherConfig\x12\"\n\x17max_constraint_interval\x18\x01 \x01(\x01:\x01\x35\x12&\n\x1blongitudinal_boundary_bound\x18\x02 \x01(\x01:\x01\x31\x12\'\n\x1amax_lateral_boundary_bound\x18\x03 \x01(\x01:\x03\x30.5\x12\'\n\x1amin_lateral_boundary_bound\x18\x04 \x01(\x01:\x03\x30.2\x12 \n\x13num_of_total_points\x18\x05 \x01(\r:\x03\x35\x30\x30\x12\x17\n\ncurb_shift\x18\x06 \x01(\x01:\x03\x30.2\x12\x1b\n\x0elateral_buffer\x18\x07 \x01(\x01:\x03\x30.2\x12\x18\n\nresolution\x18\x08 \x01(\x01:\x04\x30.02\x12<\n\tqp_spline\x18\x14 \x01(\x0b\x32\'.apollo.planning.QpSplineSmootherConfigH\x00\x12\x37\n\x06spiral\x18\x15 \x01(\x0b\x32%.apollo.planning.SpiralSmootherConfigH\x00\x12H\n\x0f\x64iscrete_points\x18\x16 \x01(\x0b\x32-.apollo.planning.DiscretePointsSmootherConfigH\x00\x42\x10\n\x0eSmootherConfig')



_QPSPLINESMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['QpSplineSmootherConfig']
_SPIRALSMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['SpiralSmootherConfig']
_DISCRETEPOINTSSMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['DiscretePointsSmootherConfig']
_REFERENCELINESMOOTHERCONFIG = DESCRIPTOR.message_types_by_name['ReferenceLineSmootherConfig']
_DISCRETEPOINTSSMOOTHERCONFIG_SMOOTHINGMETHOD = _DISCRETEPOINTSSMOOTHERCONFIG.enum_types_by_name['SmoothingMethod']
QpSplineSmootherConfig = _reflection.GeneratedProtocolMessageType('QpSplineSmootherConfig', (_message.Message,), {
  'DESCRIPTOR' : _QPSPLINESMOOTHERCONFIG,
  '__module__' : 'modules.planning.planning_base.proto.reference_line_smoother_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.QpSplineSmootherConfig)
  })
_sym_db.RegisterMessage(QpSplineSmootherConfig)

SpiralSmootherConfig = _reflection.GeneratedProtocolMessageType('SpiralSmootherConfig', (_message.Message,), {
  'DESCRIPTOR' : _SPIRALSMOOTHERCONFIG,
  '__module__' : 'modules.planning.planning_base.proto.reference_line_smoother_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.SpiralSmootherConfig)
  })
_sym_db.RegisterMessage(SpiralSmootherConfig)

DiscretePointsSmootherConfig = _reflection.GeneratedProtocolMessageType('DiscretePointsSmootherConfig', (_message.Message,), {
  'DESCRIPTOR' : _DISCRETEPOINTSSMOOTHERCONFIG,
  '__module__' : 'modules.planning.planning_base.proto.reference_line_smoother_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.DiscretePointsSmootherConfig)
  })
_sym_db.RegisterMessage(DiscretePointsSmootherConfig)

ReferenceLineSmootherConfig = _reflection.GeneratedProtocolMessageType('ReferenceLineSmootherConfig', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCELINESMOOTHERCONFIG,
  '__module__' : 'modules.planning.planning_base.proto.reference_line_smoother_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ReferenceLineSmootherConfig)
  })
_sym_db.RegisterMessage(ReferenceLineSmootherConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QPSPLINESMOOTHERCONFIG._serialized_start=253
  _QPSPLINESMOOTHERCONFIG._serialized_end=444
  _SPIRALSMOOTHERCONFIG._serialized_start=447
  _SPIRALSMOOTHERCONFIG._serialized_end=738
  _DISCRETEPOINTSSMOOTHERCONFIG._serialized_start=741
  _DISCRETEPOINTSSMOOTHERCONFIG._serialized_end=1160
  _DISCRETEPOINTSSMOOTHERCONFIG_SMOOTHINGMETHOD._serialized_start=1050
  _DISCRETEPOINTSSMOOTHERCONFIG_SMOOTHINGMETHOD._serialized_end=1142
  _REFERENCELINESMOOTHERCONFIG._serialized_start=1163
  _REFERENCELINESMOOTHERCONFIG._serialized_end=1675
# @@protoc_insertion_point(module_scope)
