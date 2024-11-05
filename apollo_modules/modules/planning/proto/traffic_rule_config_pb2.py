# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/proto/traffic_rule_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/planning/proto/traffic_rule_config.proto\x12\x0f\x61pollo.planning\"7\n\x15\x42\x61\x63ksideVehicleConfig\x12\x1e\n\x13\x62\x61\x63kside_lane_width\x18\x01 \x01(\x01:\x01\x34\"\x8e\x02\n\x0f\x43rosswalkConfig\x12\x18\n\rstop_distance\x18\x01 \x01(\x01:\x01\x31\x12 \n\x15max_stop_deceleration\x18\x02 \x01(\x01:\x01\x34\x12\x1e\n\x13min_pass_s_distance\x18\x03 \x01(\x01:\x01\x31\x12\"\n\x17max_valid_stop_distance\x18\x04 \x01(\x01:\x01\x33\x12\x1c\n\x11\x65xpand_s_distance\x18\x05 \x01(\x01:\x01\x32\x12!\n\x16stop_strict_l_distance\x18\x06 \x01(\x01:\x01\x34\x12 \n\x15stop_loose_l_distance\x18\x07 \x01(\x01:\x01\x35\x12\x18\n\x0cstop_timeout\x18\x08 \x01(\x01:\x02\x31\x30\"/\n\x11\x44\x65stinationConfig\x12\x1a\n\rstop_distance\x18\x01 \x01(\x01:\x03\x30.5\"\xa6\x01\n\x0fKeepClearConfig\x12$\n\x16\x65nable_keep_clear_zone\x18\x01 \x01(\x08:\x04true\x12\x1d\n\x0f\x65nable_junction\x18\x02 \x01(\x08:\x04true\x12\x1e\n\x13min_pass_s_distance\x18\x03 \x01(\x01:\x01\x32\x12.\n!align_with_traffic_sign_tolerance\x18\x04 \x01(\x01:\x03\x34.5\"b\n\x16ReferenceLineEndConfig\x12\x1a\n\rstop_distance\x18\x01 \x01(\x01:\x03\x30.5\x12,\n min_reference_line_remain_length\x18\x02 \x01(\x01:\x02\x35\x30\"N\n\x0fReroutingConfig\x12\x18\n\rcooldown_time\x18\x01 \x01(\x01:\x01\x33\x12!\n\x16prepare_rerouting_time\x18\x02 \x01(\x01:\x01\x32\"A\n\x0eStopSignConfig\x12\x15\n\x07\x65nabled\x18\x01 \x01(\x08:\x04true\x12\x18\n\rstop_distance\x18\x02 \x01(\x01:\x01\x31\"g\n\x12TrafficLightConfig\x12\x15\n\x07\x65nabled\x18\x01 \x01(\x08:\x04true\x12\x18\n\rstop_distance\x18\x02 \x01(\x01:\x01\x31\x12 \n\x15max_stop_deceleration\x18\x03 \x01(\x01:\x01\x34\"c\n\x0fYieldSignConfig\x12\x15\n\x07\x65nabled\x18\x01 \x01(\x08:\x04true\x12\x18\n\rstop_distance\x18\x02 \x01(\x01:\x01\x31\x12\x1f\n\x14start_watch_distance\x18\x03 \x01(\x01:\x01\x32\"\xac\x06\n\x11TrafficRuleConfig\x12:\n\x07rule_id\x18\x01 \x01(\x0e\x32).apollo.planning.TrafficRuleConfig.RuleId\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x42\n\x10\x62\x61\x63kside_vehicle\x18\x03 \x01(\x0b\x32&.apollo.planning.BacksideVehicleConfigH\x00\x12\x35\n\tcrosswalk\x18\x04 \x01(\x0b\x32 .apollo.planning.CrosswalkConfigH\x00\x12\x39\n\x0b\x64\x65stination\x18\x05 \x01(\x0b\x32\".apollo.planning.DestinationConfigH\x00\x12\x36\n\nkeep_clear\x18\x06 \x01(\x0b\x32 .apollo.planning.KeepClearConfigH\x00\x12\x45\n\x12reference_line_end\x18\x07 \x01(\x0b\x32\'.apollo.planning.ReferenceLineEndConfigH\x00\x12\x35\n\trerouting\x18\x08 \x01(\x0b\x32 .apollo.planning.ReroutingConfigH\x00\x12\x34\n\tstop_sign\x18\t \x01(\x0b\x32\x1f.apollo.planning.StopSignConfigH\x00\x12<\n\rtraffic_light\x18\n \x01(\x0b\x32#.apollo.planning.TrafficLightConfigH\x00\x12\x36\n\nyield_sign\x18\x0b \x01(\x0b\x32 .apollo.planning.YieldSignConfigH\x00\"\xa7\x01\n\x06RuleId\x12\x14\n\x10\x42\x41\x43KSIDE_VEHICLE\x10\x01\x12\r\n\tCROSSWALK\x10\x02\x12\x0f\n\x0b\x44\x45STINATION\x10\x03\x12\x0e\n\nKEEP_CLEAR\x10\x04\x12\x16\n\x12REFERENCE_LINE_END\x10\x05\x12\r\n\tREROUTING\x10\x06\x12\r\n\tSTOP_SIGN\x10\x07\x12\x11\n\rTRAFFIC_LIGHT\x10\x08\x12\x0e\n\nYIELD_SIGN\x10\tB\x08\n\x06\x63onfig\"H\n\x12TrafficRuleConfigs\x12\x32\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\".apollo.planning.TrafficRuleConfig')



_BACKSIDEVEHICLECONFIG = DESCRIPTOR.message_types_by_name['BacksideVehicleConfig']
_CROSSWALKCONFIG = DESCRIPTOR.message_types_by_name['CrosswalkConfig']
_DESTINATIONCONFIG = DESCRIPTOR.message_types_by_name['DestinationConfig']
_KEEPCLEARCONFIG = DESCRIPTOR.message_types_by_name['KeepClearConfig']
_REFERENCELINEENDCONFIG = DESCRIPTOR.message_types_by_name['ReferenceLineEndConfig']
_REROUTINGCONFIG = DESCRIPTOR.message_types_by_name['ReroutingConfig']
_STOPSIGNCONFIG = DESCRIPTOR.message_types_by_name['StopSignConfig']
_TRAFFICLIGHTCONFIG = DESCRIPTOR.message_types_by_name['TrafficLightConfig']
_YIELDSIGNCONFIG = DESCRIPTOR.message_types_by_name['YieldSignConfig']
_TRAFFICRULECONFIG = DESCRIPTOR.message_types_by_name['TrafficRuleConfig']
_TRAFFICRULECONFIGS = DESCRIPTOR.message_types_by_name['TrafficRuleConfigs']
_TRAFFICRULECONFIG_RULEID = _TRAFFICRULECONFIG.enum_types_by_name['RuleId']
BacksideVehicleConfig = _reflection.GeneratedProtocolMessageType('BacksideVehicleConfig', (_message.Message,), {
  'DESCRIPTOR' : _BACKSIDEVEHICLECONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.BacksideVehicleConfig)
  })
_sym_db.RegisterMessage(BacksideVehicleConfig)

CrosswalkConfig = _reflection.GeneratedProtocolMessageType('CrosswalkConfig', (_message.Message,), {
  'DESCRIPTOR' : _CROSSWALKCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.CrosswalkConfig)
  })
_sym_db.RegisterMessage(CrosswalkConfig)

DestinationConfig = _reflection.GeneratedProtocolMessageType('DestinationConfig', (_message.Message,), {
  'DESCRIPTOR' : _DESTINATIONCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.DestinationConfig)
  })
_sym_db.RegisterMessage(DestinationConfig)

KeepClearConfig = _reflection.GeneratedProtocolMessageType('KeepClearConfig', (_message.Message,), {
  'DESCRIPTOR' : _KEEPCLEARCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.KeepClearConfig)
  })
_sym_db.RegisterMessage(KeepClearConfig)

ReferenceLineEndConfig = _reflection.GeneratedProtocolMessageType('ReferenceLineEndConfig', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCELINEENDCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ReferenceLineEndConfig)
  })
_sym_db.RegisterMessage(ReferenceLineEndConfig)

ReroutingConfig = _reflection.GeneratedProtocolMessageType('ReroutingConfig', (_message.Message,), {
  'DESCRIPTOR' : _REROUTINGCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.ReroutingConfig)
  })
_sym_db.RegisterMessage(ReroutingConfig)

StopSignConfig = _reflection.GeneratedProtocolMessageType('StopSignConfig', (_message.Message,), {
  'DESCRIPTOR' : _STOPSIGNCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.StopSignConfig)
  })
_sym_db.RegisterMessage(StopSignConfig)

TrafficLightConfig = _reflection.GeneratedProtocolMessageType('TrafficLightConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICLIGHTCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.TrafficLightConfig)
  })
_sym_db.RegisterMessage(TrafficLightConfig)

YieldSignConfig = _reflection.GeneratedProtocolMessageType('YieldSignConfig', (_message.Message,), {
  'DESCRIPTOR' : _YIELDSIGNCONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.YieldSignConfig)
  })
_sym_db.RegisterMessage(YieldSignConfig)

TrafficRuleConfig = _reflection.GeneratedProtocolMessageType('TrafficRuleConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICRULECONFIG,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.TrafficRuleConfig)
  })
_sym_db.RegisterMessage(TrafficRuleConfig)

TrafficRuleConfigs = _reflection.GeneratedProtocolMessageType('TrafficRuleConfigs', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICRULECONFIGS,
  '__module__' : 'modules.planning.proto.traffic_rule_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.TrafficRuleConfigs)
  })
_sym_db.RegisterMessage(TrafficRuleConfigs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BACKSIDEVEHICLECONFIG._serialized_start=69
  _BACKSIDEVEHICLECONFIG._serialized_end=124
  _CROSSWALKCONFIG._serialized_start=127
  _CROSSWALKCONFIG._serialized_end=397
  _DESTINATIONCONFIG._serialized_start=399
  _DESTINATIONCONFIG._serialized_end=446
  _KEEPCLEARCONFIG._serialized_start=449
  _KEEPCLEARCONFIG._serialized_end=615
  _REFERENCELINEENDCONFIG._serialized_start=617
  _REFERENCELINEENDCONFIG._serialized_end=715
  _REROUTINGCONFIG._serialized_start=717
  _REROUTINGCONFIG._serialized_end=795
  _STOPSIGNCONFIG._serialized_start=797
  _STOPSIGNCONFIG._serialized_end=862
  _TRAFFICLIGHTCONFIG._serialized_start=864
  _TRAFFICLIGHTCONFIG._serialized_end=967
  _YIELDSIGNCONFIG._serialized_start=969
  _YIELDSIGNCONFIG._serialized_end=1068
  _TRAFFICRULECONFIG._serialized_start=1071
  _TRAFFICRULECONFIG._serialized_end=1883
  _TRAFFICRULECONFIG_RULEID._serialized_start=1706
  _TRAFFICRULECONFIG_RULEID._serialized_end=1873
  _TRAFFICRULECONFIGS._serialized_start=1885
  _TRAFFICRULECONFIGS._serialized_end=1957
# @@protoc_insertion_point(module_scope)
