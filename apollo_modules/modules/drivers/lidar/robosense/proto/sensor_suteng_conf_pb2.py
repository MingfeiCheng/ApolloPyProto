# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/lidar/robosense/proto/sensor_suteng_conf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.drivers.lidar.robosense.proto import sensor_suteng_pb2 as modules_dot_drivers_dot_lidar_dot_robosense_dot_proto_dot_sensor__suteng__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/drivers/lidar/robosense/proto/sensor_suteng_conf.proto\x12\x15\x61pollo.drivers.suteng\x1a\x39modules/drivers/lidar/robosense/proto/sensor_suteng.proto\"\xdd\x05\n\x0cSutengConfig\x12\x10\n\x08\x66rame_id\x18\x01 \x02(\t\x12+\n\x05model\x18\x02 \x02(\x0e\x32\x1c.apollo.drivers.suteng.Model\x12)\n\x04mode\x18\x03 \x02(\x0e\x32\x1b.apollo.drivers.suteng.Mode\x12\x11\n\tpcap_file\x18\x04 \x01(\t\x12\x10\n\x08npackets\x18\x05 \x01(\x05\x12\x0b\n\x03rpm\x18\x06 \x02(\x02\x12\x1a\n\x0cuse_gps_time\x18\x07 \x02(\x08:\x04true\x12\x14\n\ttime_zone\x18\x08 \x02(\x05:\x01\x38\x12\x18\n\x10\x66iring_data_port\x18\t \x02(\r\x12\x1d\n\x15positioning_data_port\x18\n \x01(\r\x12\x11\n\tmax_range\x18\x0b \x02(\x02\x12\x11\n\tmin_range\x18\x0c \x02(\x02\x12\x11\n\tmax_angle\x18\r \x01(\x02\x12\x11\n\tmin_angle\x18\x0e \x01(\x02\x12\x16\n\x0eview_direction\x18\x0f \x01(\x02\x12\x12\n\nview_width\x18\x10 \x01(\x02\x12\x18\n\x10\x63\x61libration_file\x18\x11 \x02(\t\x12\x18\n\torganized\x18\x12 \x02(\x08:\x05\x66\x61lse\x12\x17\n\x0ftarget_frame_id\x18\x13 \x01(\t\x12\x19\n\nmain_frame\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x13vehicle_config_path\x18\x15 \x01(\t\x12$\n\x1c\x61\x63\x63urate_vehicle_config_path\x18\x16 \x01(\t\x12!\n\x19lidars_filter_config_path\x18\x17 \x01(\t\x12!\n\x19lidar_extrinsic_file_path\x18\x18 \x01(\t\x12\x14\n\x0cscan_channel\x18\x19 \x02(\t\x12\x12\n\npc_channel\x18\x1a \x02(\t\x12\x16\n\x0e\x66usion_channel\x18\x1b \x01(\t\x12\x1b\n\x13\x63ompensator_channel\x18\x1c \x01(\t')



_SUTENGCONFIG = DESCRIPTOR.message_types_by_name['SutengConfig']
SutengConfig = _reflection.GeneratedProtocolMessageType('SutengConfig', (_message.Message,), {
  'DESCRIPTOR' : _SUTENGCONFIG,
  '__module__' : 'modules.drivers.lidar.robosense.proto.sensor_suteng_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.suteng.SutengConfig)
  })
_sym_db.RegisterMessage(SutengConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUTENGCONFIG._serialized_start=149
  _SUTENGCONFIG._serialized_end=882
# @@protoc_insertion_point(module_scope)