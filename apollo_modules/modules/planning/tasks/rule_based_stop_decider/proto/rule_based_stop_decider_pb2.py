# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/planning/tasks/rule_based_stop_decider/proto/rule_based_stop_decider.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRmodules/planning/tasks/rule_based_stop_decider/proto/rule_based_stop_decider.proto\x12\x0f\x61pollo.planning\"\xab\x03\n\x1aRuleBasedStopDeciderConfig\x12\x1f\n\x12max_adc_stop_speed\x18\x01 \x01(\x01:\x03\x30.3\x12$\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x03\x30.5\x12\x1d\n\x12search_beam_length\x18\x03 \x01(\x01:\x01\x35\x12*\n\x1csearch_beam_radius_intensity\x18\x04 \x01(\x01:\x04\x30.08\x12\x1a\n\x0csearch_range\x18\x05 \x01(\x01:\x04\x33.14\x12&\n\x18is_block_angle_threshold\x18\x06 \x01(\x01:\x04\x31.57\x12-\n!approach_distance_for_lane_change\x18\n \x01(\x01:\x02\x38\x30\x12+\n\x1furgent_distance_for_lane_change\x18\x0b \x01(\x01:\x02\x35\x30\x12\x32\n#enable_lane_change_urgency_checking\x18\x0c \x01(\x08:\x05\x66\x61lse\x12\'\n\x1bshort_path_length_threshold\x18\r \x01(\x01:\x02\x32\x30')



_RULEBASEDSTOPDECIDERCONFIG = DESCRIPTOR.message_types_by_name['RuleBasedStopDeciderConfig']
RuleBasedStopDeciderConfig = _reflection.GeneratedProtocolMessageType('RuleBasedStopDeciderConfig', (_message.Message,), {
  'DESCRIPTOR' : _RULEBASEDSTOPDECIDERCONFIG,
  '__module__' : 'modules.planning.tasks.rule_based_stop_decider.proto.rule_based_stop_decider_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning.RuleBasedStopDeciderConfig)
  })
_sym_db.RegisterMessage(RuleBasedStopDeciderConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RULEBASEDSTOPDECIDERCONFIG._serialized_start=104
  _RULEBASEDSTOPDECIDERCONFIG._serialized_end=531
# @@protoc_insertion_point(module_scope)
