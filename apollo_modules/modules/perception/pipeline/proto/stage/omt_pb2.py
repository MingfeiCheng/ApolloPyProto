# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/stage/omt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/perception/pipeline/proto/stage/omt.proto\x12\x1c\x61pollo.perception.camera.omt\"X\n\x0bKalmanParam\x12\x15\n\rinit_variance\x18\x01 \x01(\x02\x12\x18\n\x10process_variance\x18\x02 \x01(\x02\x12\x18\n\x10measure_variance\x18\x03 \x01(\x02\"\x88\t\n\x0bTargetParam\x12\x1d\n\x12velocity_threshold\x18\x01 \x01(\x02:\x01\x32\x12 \n\x15velocity_output_delay\x18\x02 \x01(\x05:\x01\x32\x12?\n\x0cworld_center\x18\x03 \x01(\x0b\x32).apollo.perception.camera.omt.KalmanParam\x12?\n\x0cimage_center\x18\x04 \x01(\x0b\x32).apollo.perception.camera.omt.KalmanParam\x12\x1c\n\x14image_wh_update_rate\x18\x05 \x01(\x02\x12\x1d\n\x11world_lhw_history\x18\x06 \x01(\x05:\x02\x31\x35\x12\x1e\n\x11height_diff_ratio\x18\x07 \x01(\x02:\x03\x30.1\x12\x1f\n\x13world_state_history\x18\x08 \x01(\x05:\x02\x33\x30\x12.\n#min_cached_world_state_history_size\x18\t \x01(\x05:\x01\x35\x12$\n\x18min_cached_velocity_size\x18\n \x01(\x05:\x02\x31\x30\x12$\n\x18min_cached_position_size\x18\x0b \x01(\x05:\x02\x32\x35\x12(\n\x1d\x63\x61lc_avg_position_window_size\x18\x0c \x01(\x05:\x01\x37\x12#\n\x16static_speed_threshold\x18\r \x01(\x02:\x03\x30.5\x12\'\n\x1astatic_speed_threshold_ped\x18\x0e \x01(\x02:\x03\x30.3\x12\x1f\n\x14min_moving_avg_speed\x18\x0f \x01(\x02:\x01\x31\x12%\n\x18min_moving_avg_speed_ped\x18\x10 \x01(\x02:\x03\x30.5\x12!\n\x16\x61\x62normal_acc_threshold\x18\x11 \x01(\x02:\x01\x36\x12%\n\x1a\x61\x62normal_acc_threshold_ped\x18\x12 \x01(\x02:\x01\x33\x12\x39\n)abnormal_velocity_heading_angle_threshold\x18\x13 \x01(\x02:\x06\x30.7854\x12 \n\x11\x63lapping_velocity\x18\x14 \x01(\x08:\x05\x66\x61lse\x12(\n\x1cworld_mean_velocity_duration\x18\x15 \x01(\x05:\x02\x31\x30\x12\x17\n\x0ctracked_life\x18\x16 \x01(\x05:\x01\x33\x12\x1c\n\x0ftype_filter_var\x18\x17 \x01(\x02:\x03\x30.3\x12!\n\x14large_velocity_ratio\x18\x18 \x01(\x02:\x03\x32.5\x12%\n\x18too_large_velocity_ratio\x18\x19 \x01(\x02:\x03\x31.5\x12\x1e\n\x12mean_filter_window\x18\x1a \x01(\x05:\x02\x31\x30\x12#\n\x16\x64irection_filter_ratio\x18\x1b \x01(\x02:\x03\x30.7\x12$\n\x16\x64isplacement_theta_var\x18\x1c \x01(\x02:\x04\x30.25\x12\x1f\n\x12velocity_theta_var\x18\x1d \x01(\x02:\x03\x30.5\x12\x1e\n\x13stable_moving_speed\x18\x1e \x01(\x02:\x01\x32\"\x96\x01\n\x0eReferenceParam\x12\x11\n\x06margin\x18\x01 \x01(\x05:\x01\x32\x12\x1c\n\x10min_allow_height\x18\x02 \x01(\x05:\x02\x35\x30\x12\x18\n\narea_decay\x18\x03 \x01(\x02:\x04\x30.99\x12\x19\n\rdown_sampling\x18\x04 \x01(\x05:\x02\x34\x30\x12\x1e\n\x11height_diff_ratio\x18\x05 \x01(\x02:\x03\x30.1\"r\n\x0bWeightParam\x12\x15\n\nappearance\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06motion\x18\x02 \x01(\x02:\x01\x30\x12\x10\n\x05shape\x18\x03 \x01(\x02:\x01\x30\x12\x13\n\x08tracklet\x18\x04 \x01(\x02:\x01\x30\x12\x12\n\x07overlap\x18\x05 \x01(\x02:\x01\x30\"\xce\x05\n\x08OmtParam\x12\x19\n\x0eimg_capability\x18\x01 \x01(\x05:\x01\x37\x12\x13\n\x08lost_age\x18\x02 \x01(\x05:\x01\x32\x12\x16\n\x0breserve_age\x18\x03 \x01(\x05:\x01\x33\x12\x45\n\x12weight_same_camera\x18\x04 \x01(\x0b\x32).apollo.perception.camera.omt.WeightParam\x12\x45\n\x12weight_diff_camera\x18\x05 \x01(\x0b\x32).apollo.perception.camera.omt.WeightParam\x12\x12\n\x06\x62order\x18\t \x01(\x02:\x02\x33\x30\x12\x1b\n\rtarget_thresh\x18\n \x01(\x02:\x04\x30.65\x12\x1b\n\x0c\x63orrect_type\x18\x0b \x01(\x08:\x05\x66\x61lse\x12?\n\x0ctarget_param\x18\x0c \x01(\x0b\x32).apollo.perception.camera.omt.TargetParam\x12!\n\x15min_init_height_ratio\x18\r \x01(\x02:\x02\x31\x37\x12)\n\x1ctarget_combine_iou_threshold\x18\x0e \x01(\x02:\x03\x30.5\x12\"\n\x14\x66usion_target_thresh\x18\x0f \x01(\x02:\x04\x30.45\x12\x1e\n\x12image_displacement\x18\x10 \x01(\x02:\x02\x35\x30\x12\x1e\n\x11\x61\x62normal_movement\x18\x11 \x01(\x02:\x03\x30.3\x12\x19\n\x0bsame_ts_eps\x18\x12 \x01(\x01:\x04\x30.05\x12?\n\treference\x18\x13 \x01(\x0b\x32,.apollo.perception.camera.omt.ReferenceParam\x12\x18\n\x10type_change_cost\x18\x14 \x01(\t\x12\x0e\n\x06gpu_id\x18\x15 \x01(\x05\x12\x10\n\x08root_dir\x18\x16 \x01(\t\x12\x13\n\x0b\x63\x61mera_name\x18\x17 \x01(\t')



_KALMANPARAM = DESCRIPTOR.message_types_by_name['KalmanParam']
_TARGETPARAM = DESCRIPTOR.message_types_by_name['TargetParam']
_REFERENCEPARAM = DESCRIPTOR.message_types_by_name['ReferenceParam']
_WEIGHTPARAM = DESCRIPTOR.message_types_by_name['WeightParam']
_OMTPARAM = DESCRIPTOR.message_types_by_name['OmtParam']
KalmanParam = _reflection.GeneratedProtocolMessageType('KalmanParam', (_message.Message,), {
  'DESCRIPTOR' : _KALMANPARAM,
  '__module__' : 'modules.perception.pipeline.proto.stage.omt_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.omt.KalmanParam)
  })
_sym_db.RegisterMessage(KalmanParam)

TargetParam = _reflection.GeneratedProtocolMessageType('TargetParam', (_message.Message,), {
  'DESCRIPTOR' : _TARGETPARAM,
  '__module__' : 'modules.perception.pipeline.proto.stage.omt_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.omt.TargetParam)
  })
_sym_db.RegisterMessage(TargetParam)

ReferenceParam = _reflection.GeneratedProtocolMessageType('ReferenceParam', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCEPARAM,
  '__module__' : 'modules.perception.pipeline.proto.stage.omt_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.omt.ReferenceParam)
  })
_sym_db.RegisterMessage(ReferenceParam)

WeightParam = _reflection.GeneratedProtocolMessageType('WeightParam', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTPARAM,
  '__module__' : 'modules.perception.pipeline.proto.stage.omt_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.omt.WeightParam)
  })
_sym_db.RegisterMessage(WeightParam)

OmtParam = _reflection.GeneratedProtocolMessageType('OmtParam', (_message.Message,), {
  'DESCRIPTOR' : _OMTPARAM,
  '__module__' : 'modules.perception.pipeline.proto.stage.omt_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.camera.omt.OmtParam)
  })
_sym_db.RegisterMessage(OmtParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _KALMANPARAM._serialized_start=83
  _KALMANPARAM._serialized_end=171
  _TARGETPARAM._serialized_start=174
  _TARGETPARAM._serialized_end=1334
  _REFERENCEPARAM._serialized_start=1337
  _REFERENCEPARAM._serialized_end=1487
  _WEIGHTPARAM._serialized_start=1489
  _WEIGHTPARAM._serialized_end=1603
  _OMTPARAM._serialized_start=1606
  _OMTPARAM._serialized_end=2324
# @@protoc_insertion_point(module_scope)
