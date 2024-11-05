# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/drivers/radar/racobit_radar/proto/racobit_radar_conf.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.sensor_msgs import racobit_radar_pb2 as modules_dot_common__msgs_dot_sensor__msgs_dot_racobit__radar__pb2
from apollo_modules.modules.common_msgs.drivers_msgs import can_card_parameter_pb2 as modules_dot_common__msgs_dot_drivers__msgs_dot_can__card__parameter__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBmodules/drivers/radar/racobit_radar/proto/racobit_radar_conf.proto\x12\x1c\x61pollo.drivers.racobit_radar\x1a\x33modules/common_msgs/sensor_msgs/racobit_radar.proto\x1a\x39modules/common_msgs/drivers_msgs/can_card_parameter.proto\"\xb6\x01\n\x07\x43\x61nConf\x12\x43\n\x12\x63\x61n_card_parameter\x18\x01 \x01(\x0b\x32\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11\x65nable_debug_mode\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x65nable_receiver_log\x18\x03 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x65nable_sender_log\x18\x04 \x01(\x08:\x05\x66\x61lse\"\xe5\x05\n\tRadarConf\x12!\n\x12max_distance_valid\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fsensor_id_valid\x18\x02 \x01(\x08:\x05\x66\x61lse\x12 \n\x11radar_power_valid\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x11output_type_valid\x18\x04 \x01(\x08:\x04true\x12 \n\x12send_quality_valid\x18\x05 \x01(\x08:\x04true\x12!\n\x13send_ext_info_valid\x18\x06 \x01(\x08:\x04true\x12\x1f\n\x10sort_index_valid\x18\x07 \x01(\x08:\x05\x66\x61lse\x12 \n\x12store_in_nvm_valid\x18\x08 \x01(\x08:\x04true\x12\x1f\n\x10\x63trl_relay_valid\x18\t \x01(\x08:\x05\x66\x61lse\x12!\n\x13rcs_threshold_valid\x18\n \x01(\x08:\x04true\x12\x19\n\x0cmax_distance\x18\x0b \x01(\r:\x03\x32\x34\x38\x12\x14\n\tsensor_id\x18\x0c \x01(\r:\x01\x30\x12Z\n\x0boutput_type\x18\r \x01(\x0e\x32\x30.apollo.drivers.RacobitRadarState_201.OutputType:\x13OUTPUT_TYPE_OBJECTS\x12\x16\n\x0bradar_power\x18\x0e \x01(\r:\x01\x30\x12\x15\n\nctrl_relay\x18\x0f \x01(\r:\x01\x30\x12\x1b\n\rsend_ext_info\x18\x10 \x01(\x08:\x04true\x12\x1a\n\x0csend_quality\x18\x11 \x01(\x08:\x04true\x12\x15\n\nsort_index\x18\x12 \x01(\r:\x01\x30\x12\x17\n\x0cstore_in_nvm\x18\x13 \x01(\r:\x01\x31\x12\x61\n\rrcs_threshold\x18\x14 \x01(\x0e\x32\x32.apollo.drivers.RacobitRadarState_201.RcsThreshold:\x16RCS_THRESHOLD_STANDARD\"\x88\x01\n\x10RacobitRadarConf\x12\x37\n\x08\x63\x61n_conf\x18\x01 \x01(\x0b\x32%.apollo.drivers.racobit_radar.CanConf\x12;\n\nradar_conf\x18\x02 \x01(\x0b\x32\'.apollo.drivers.racobit_radar.RadarConf')



_CANCONF = DESCRIPTOR.message_types_by_name['CanConf']
_RADARCONF = DESCRIPTOR.message_types_by_name['RadarConf']
_RACOBITRADARCONF = DESCRIPTOR.message_types_by_name['RacobitRadarConf']
CanConf = _reflection.GeneratedProtocolMessageType('CanConf', (_message.Message,), {
  'DESCRIPTOR' : _CANCONF,
  '__module__' : 'modules.drivers.radar.racobit_radar.proto.racobit_radar_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.racobit_radar.CanConf)
  })
_sym_db.RegisterMessage(CanConf)

RadarConf = _reflection.GeneratedProtocolMessageType('RadarConf', (_message.Message,), {
  'DESCRIPTOR' : _RADARCONF,
  '__module__' : 'modules.drivers.radar.racobit_radar.proto.racobit_radar_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.racobit_radar.RadarConf)
  })
_sym_db.RegisterMessage(RadarConf)

RacobitRadarConf = _reflection.GeneratedProtocolMessageType('RacobitRadarConf', (_message.Message,), {
  'DESCRIPTOR' : _RACOBITRADARCONF,
  '__module__' : 'modules.drivers.radar.racobit_radar.proto.racobit_radar_conf_pb2'
  # @@protoc_insertion_point(class_scope:apollo.drivers.racobit_radar.RacobitRadarConf)
  })
_sym_db.RegisterMessage(RacobitRadarConf)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CANCONF._serialized_start=213
  _CANCONF._serialized_end=395
  _RADARCONF._serialized_start=398
  _RADARCONF._serialized_end=1139
  _RACOBITRADARCONF._serialized_start=1142
  _RACOBITRADARCONF._serialized_end=1278
# @@protoc_insertion_point(module_scope)
