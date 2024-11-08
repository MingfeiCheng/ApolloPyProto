# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/monitor_msgs/system_status.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/common_msgs/monitor_msgs/system_status.proto\x12\x0e\x61pollo.monitor\x1a+modules/common_msgs/basic_msgs/header.proto\"\xa2\x01\n\x0f\x43omponentStatus\x12?\n\x06status\x18\x01 \x01(\x0e\x32&.apollo.monitor.ComponentStatus.Status:\x07UNKNOWN\x12\x0f\n\x07message\x18\x02 \x01(\t\"=\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x08\n\x04WARN\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\t\n\x05\x46\x41TAL\x10\x04\"\xd8\x02\n\tComponent\x12\x30\n\x07summary\x18\x01 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus\x12\x37\n\x0eprocess_status\x18\x02 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus\x12\x37\n\x0e\x63hannel_status\x18\x03 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus\x12\x38\n\x0fresource_status\x18\x04 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus\x12\x35\n\x0cother_status\x18\x05 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus\x12\x36\n\rmodule_status\x18\x06 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus\"\xd0\x06\n\x0cSystemStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x41\n\x0bhmi_modules\x18\x07 \x03(\x0b\x32,.apollo.monitor.SystemStatus.HmiModulesEntry\x12@\n\ncomponents\x18\x08 \x03(\x0b\x32,.apollo.monitor.SystemStatus.ComponentsEntry\x12\x15\n\rpassenger_msg\x18\x04 \x01(\t\x12 \n\x18safety_mode_trigger_time\x18\x05 \x01(\x01\x12\x1e\n\x16require_emergency_stop\x18\x06 \x01(\x08\x12!\n\x19is_realtime_in_simulation\x18\t \x01(\x08\x12K\n\x10other_components\x18\n \x03(\x0b\x32\x31.apollo.monitor.SystemStatus.OtherComponentsEntry\x12M\n\x11global_components\x18\x0b \x03(\x0b\x32\x32.apollo.monitor.SystemStatus.GlobalComponentsEntry\x12!\n\x12\x64\x65tect_immediately\x18\x0c \x01(\x08:\x05\x66\x61lse\x1aR\n\x0fHmiModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus:\x02\x38\x01\x1aL\n\x0f\x43omponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.apollo.monitor.Component:\x02\x38\x01\x1aW\n\x14OtherComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus:\x02\x38\x01\x1aR\n\x15GlobalComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.apollo.monitor.Component:\x02\x38\x01J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04')



_COMPONENTSTATUS = DESCRIPTOR.message_types_by_name['ComponentStatus']
_COMPONENT = DESCRIPTOR.message_types_by_name['Component']
_SYSTEMSTATUS = DESCRIPTOR.message_types_by_name['SystemStatus']
_SYSTEMSTATUS_HMIMODULESENTRY = _SYSTEMSTATUS.nested_types_by_name['HmiModulesEntry']
_SYSTEMSTATUS_COMPONENTSENTRY = _SYSTEMSTATUS.nested_types_by_name['ComponentsEntry']
_SYSTEMSTATUS_OTHERCOMPONENTSENTRY = _SYSTEMSTATUS.nested_types_by_name['OtherComponentsEntry']
_SYSTEMSTATUS_GLOBALCOMPONENTSENTRY = _SYSTEMSTATUS.nested_types_by_name['GlobalComponentsEntry']
_COMPONENTSTATUS_STATUS = _COMPONENTSTATUS.enum_types_by_name['Status']
ComponentStatus = _reflection.GeneratedProtocolMessageType('ComponentStatus', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENTSTATUS,
  '__module__' : 'modules.common_msgs.monitor_msgs.system_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.monitor.ComponentStatus)
  })
_sym_db.RegisterMessage(ComponentStatus)

Component = _reflection.GeneratedProtocolMessageType('Component', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENT,
  '__module__' : 'modules.common_msgs.monitor_msgs.system_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.monitor.Component)
  })
_sym_db.RegisterMessage(Component)

SystemStatus = _reflection.GeneratedProtocolMessageType('SystemStatus', (_message.Message,), {

  'HmiModulesEntry' : _reflection.GeneratedProtocolMessageType('HmiModulesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYSTEMSTATUS_HMIMODULESENTRY,
    '__module__' : 'modules.common_msgs.monitor_msgs.system_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.monitor.SystemStatus.HmiModulesEntry)
    })
  ,

  'ComponentsEntry' : _reflection.GeneratedProtocolMessageType('ComponentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYSTEMSTATUS_COMPONENTSENTRY,
    '__module__' : 'modules.common_msgs.monitor_msgs.system_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.monitor.SystemStatus.ComponentsEntry)
    })
  ,

  'OtherComponentsEntry' : _reflection.GeneratedProtocolMessageType('OtherComponentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYSTEMSTATUS_OTHERCOMPONENTSENTRY,
    '__module__' : 'modules.common_msgs.monitor_msgs.system_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.monitor.SystemStatus.OtherComponentsEntry)
    })
  ,

  'GlobalComponentsEntry' : _reflection.GeneratedProtocolMessageType('GlobalComponentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYSTEMSTATUS_GLOBALCOMPONENTSENTRY,
    '__module__' : 'modules.common_msgs.monitor_msgs.system_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.monitor.SystemStatus.GlobalComponentsEntry)
    })
  ,
  'DESCRIPTOR' : _SYSTEMSTATUS,
  '__module__' : 'modules.common_msgs.monitor_msgs.system_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.monitor.SystemStatus)
  })
_sym_db.RegisterMessage(SystemStatus)
_sym_db.RegisterMessage(SystemStatus.HmiModulesEntry)
_sym_db.RegisterMessage(SystemStatus.ComponentsEntry)
_sym_db.RegisterMessage(SystemStatus.OtherComponentsEntry)
_sym_db.RegisterMessage(SystemStatus.GlobalComponentsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYSTEMSTATUS_HMIMODULESENTRY._options = None
  _SYSTEMSTATUS_HMIMODULESENTRY._serialized_options = b'8\001'
  _SYSTEMSTATUS_COMPONENTSENTRY._options = None
  _SYSTEMSTATUS_COMPONENTSENTRY._serialized_options = b'8\001'
  _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._options = None
  _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._serialized_options = b'8\001'
  _SYSTEMSTATUS_GLOBALCOMPONENTSENTRY._options = None
  _SYSTEMSTATUS_GLOBALCOMPONENTSENTRY._serialized_options = b'8\001'
  _COMPONENTSTATUS._serialized_start=118
  _COMPONENTSTATUS._serialized_end=280
  _COMPONENTSTATUS_STATUS._serialized_start=219
  _COMPONENTSTATUS_STATUS._serialized_end=280
  _COMPONENT._serialized_start=283
  _COMPONENT._serialized_end=627
  _SYSTEMSTATUS._serialized_start=630
  _SYSTEMSTATUS._serialized_end=1478
  _SYSTEMSTATUS_HMIMODULESENTRY._serialized_start=1133
  _SYSTEMSTATUS_HMIMODULESENTRY._serialized_end=1215
  _SYSTEMSTATUS_COMPONENTSENTRY._serialized_start=1217
  _SYSTEMSTATUS_COMPONENTSENTRY._serialized_end=1293
  _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._serialized_start=1295
  _SYSTEMSTATUS_OTHERCOMPONENTSENTRY._serialized_end=1382
  _SYSTEMSTATUS_GLOBALCOMPONENTSENTRY._serialized_start=1384
  _SYSTEMSTATUS_GLOBALCOMPONENTSENTRY._serialized_end=1466
# @@protoc_insertion_point(module_scope)
