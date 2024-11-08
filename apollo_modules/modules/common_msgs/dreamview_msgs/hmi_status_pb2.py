# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/dreamview_msgs/hmi_status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.monitor_msgs import system_status_pb2 as modules_dot_common__msgs_dot_monitor__msgs_dot_system__status__pb2
from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3modules/common_msgs/dreamview_msgs/hmi_status.proto\x12\x10\x61pollo.dreamview\x1a+modules/common_msgs/basic_msgs/header.proto\x1a\x34modules/common_msgs/monitor_msgs/system_status.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\"\xa4\x01\n\x0cScenarioInfo\x12\x13\n\x0bscenario_id\x18\x01 \x01(\t\x12\x15\n\rscenario_name\x18\x02 \x01(\t\x12\x10\n\x08map_name\x18\x03 \x01(\t\x12+\n\x0bstart_point\x18\x04 \x01(\x0b\x32\x16.apollo.common.Point2D\x12)\n\tend_point\x18\x05 \x01(\x0b\x32\x16.apollo.common.Point2D\"[\n\x0bScenarioSet\x12\x19\n\x11scenario_set_name\x18\x01 \x01(\t\x12\x31\n\tscenarios\x18\x02 \x03(\x0b\x32\x1e.apollo.dreamview.ScenarioInfo\"\x8b\x01\n\x0cRecordStatus\x12\x1b\n\x11\x63urrent_record_id\x18\x01 \x01(\t:\x00\x12\x46\n\x12play_record_status\x18\x02 \x01(\x0e\x32\".apollo.dreamview.PlayRecordStatus:\x06\x43LOSED\x12\x16\n\x0b\x63urr_time_s\x18\x04 \x01(\x01:\x01\x30\"\xab\x01\n\x0eLoadRecordInfo\x12H\n\x12load_record_status\x18\x01 \x01(\x0e\x32\".apollo.dreamview.LoadRecordStatus:\x08NOT_LOAD\x12\x17\n\x0ctotal_time_s\x18\x02 \x01(\x01:\x01\x30\x12\x1a\n\x10record_file_path\x18\x03 \x01(\t:\x00\x12\x1a\n\x0f\x64ownload_status\x18\x04 \x01(\x05:\x01\x30\"\xa8\x0e\n\tHMIStatus\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\r\n\x05modes\x18\x02 \x03(\t\x12\x14\n\x0c\x63urrent_mode\x18\x03 \x01(\t\x12\x0c\n\x04maps\x18\x04 \x03(\t\x12\x13\n\x0b\x63urrent_map\x18\x05 \x01(\t\x12\x10\n\x08vehicles\x18\x06 \x03(\t\x12\x17\n\x0f\x63urrent_vehicle\x18\x07 \x01(\t\x12\x39\n\x07modules\x18\x08 \x03(\x0b\x32(.apollo.dreamview.HMIStatus.ModulesEntry\x12R\n\x14monitored_components\x18\t \x03(\x0b\x32\x34.apollo.dreamview.HMIStatus.MonitoredComponentsEntry\x12\x14\n\x0c\x64ocker_image\x18\n \x01(\t\x12\x13\n\x0butm_zone_id\x18\x0b \x01(\x05\x12\x15\n\rpassenger_msg\x18\x0c \x01(\t\x12J\n\x10other_components\x18\r \x03(\x0b\x32\x30.apollo.dreamview.HMIStatus.OtherComponentsEntry\x12\x42\n\x0cscenario_set\x18\x0f \x03(\x0b\x32,.apollo.dreamview.HMIStatus.ScenarioSetEntry\x12!\n\x17\x63urrent_scenario_set_id\x18\x10 \x01(\t:\x00\x12\x1d\n\x13\x63urrent_scenario_id\x18\x11 \x01(\t:\x00\x12\x16\n\x0e\x64ynamic_models\x18\x12 \x03(\t\x12\x1d\n\x15\x63urrent_dynamic_model\x18\x13 \x01(\t\x12\x1b\n\x11\x63urrent_record_id\x18\x14 \x01(\t:\x00\x12\x39\n\x07records\x18\x15 \x03(\x0b\x32(.apollo.dreamview.HMIStatus.RecordsEntry\x12\x1c\n\x14\x63urrent_vehicle_type\x18\x16 \x01(\x11\x12%\n\x1d\x63urrent_camera_sensor_channel\x18\x17 \x01(\t\x12#\n\x1b\x63urrent_point_cloud_channel\x18\x18 \x01(\t\x12\x36\n\noperations\x18\x19 \x03(\x0e\x32\".apollo.dreamview.HMIModeOperation\x12=\n\x11\x63urrent_operation\x18\x1a \x01(\x0e\x32\".apollo.dreamview.HMIModeOperation\x12\x16\n\x0e\x63urrent_layout\x18\x1b \x01(\t\x12=\n\x15\x63urrent_record_status\x18\x1c \x01(\x0b\x32\x1e.apollo.dreamview.RecordStatus\x12L\n\x11global_components\x18\x1d \x03(\x0b\x32\x31.apollo.dreamview.HMIStatus.GlobalComponentsEntry\x12\x1b\n\x10\x65xpected_modules\x18\x1e \x01(\r:\x01\x30\x12\x42\n\x0cmodules_lock\x18\x1f \x03(\x0b\x32,.apollo.dreamview.HMIStatus.ModulesLockEntry\x12\x1f\n\x10\x62\x61\x63kend_shutdown\x18  \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0brtk_records\x18! \x03(\t\x12\x1f\n\x15\x63urrent_rtk_record_id\x18\" \x01(\t:\x00\x1a.\n\x0cModulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a[\n\x18MonitoredComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus:\x02\x38\x01\x1aW\n\x14OtherComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.apollo.monitor.ComponentStatus:\x02\x38\x01\x1aQ\n\x10ScenarioSetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.apollo.dreamview.ScenarioSet:\x02\x38\x01\x1aP\n\x0cRecordsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .apollo.dreamview.LoadRecordInfo:\x02\x38\x01\x1aR\n\x15GlobalComponentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.apollo.monitor.Component:\x02\x38\x01\x1a\x32\n\x10ModulesLockEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01*7\n\x10PlayRecordStatus\x12\x0b\n\x07RUNNING\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\n\n\x06\x43LOSED\x10\x02*\x8a\x01\n\x10HMIModeOperation\x12\x08\n\x04None\x10\x00\x12\r\n\tSIM_DEBUG\x10\x01\x12\x0f\n\x0bSim_Control\x10\x02\x12\x0e\n\nAuto_Drive\x10\x03\x12\t\n\x05TRACE\x10\x04\x12\x10\n\x0cScenario_Sim\x10\x05\x12\n\n\x06Record\x10\x06\x12\x13\n\x0fWaypoint_Follow\x10\x07*9\n\x10LoadRecordStatus\x12\x0c\n\x08NOT_LOAD\x10\x01\x12\x0b\n\x07LOADING\x10\x02\x12\n\n\x06LOADED\x10\x03')

_PLAYRECORDSTATUS = DESCRIPTOR.enum_types_by_name['PlayRecordStatus']
PlayRecordStatus = enum_type_wrapper.EnumTypeWrapper(_PLAYRECORDSTATUS)
_HMIMODEOPERATION = DESCRIPTOR.enum_types_by_name['HMIModeOperation']
HMIModeOperation = enum_type_wrapper.EnumTypeWrapper(_HMIMODEOPERATION)
_LOADRECORDSTATUS = DESCRIPTOR.enum_types_by_name['LoadRecordStatus']
LoadRecordStatus = enum_type_wrapper.EnumTypeWrapper(_LOADRECORDSTATUS)
RUNNING = 0
PAUSED = 1
CLOSED = 2
globals()['None'] = 0
SIM_DEBUG = 1
Sim_Control = 2
Auto_Drive = 3
TRACE = 4
Scenario_Sim = 5
Record = 6
Waypoint_Follow = 7
NOT_LOAD = 1
LOADING = 2
LOADED = 3


_SCENARIOINFO = DESCRIPTOR.message_types_by_name['ScenarioInfo']
_SCENARIOSET = DESCRIPTOR.message_types_by_name['ScenarioSet']
_RECORDSTATUS = DESCRIPTOR.message_types_by_name['RecordStatus']
_LOADRECORDINFO = DESCRIPTOR.message_types_by_name['LoadRecordInfo']
_HMISTATUS = DESCRIPTOR.message_types_by_name['HMIStatus']
_HMISTATUS_MODULESENTRY = _HMISTATUS.nested_types_by_name['ModulesEntry']
_HMISTATUS_MONITOREDCOMPONENTSENTRY = _HMISTATUS.nested_types_by_name['MonitoredComponentsEntry']
_HMISTATUS_OTHERCOMPONENTSENTRY = _HMISTATUS.nested_types_by_name['OtherComponentsEntry']
_HMISTATUS_SCENARIOSETENTRY = _HMISTATUS.nested_types_by_name['ScenarioSetEntry']
_HMISTATUS_RECORDSENTRY = _HMISTATUS.nested_types_by_name['RecordsEntry']
_HMISTATUS_GLOBALCOMPONENTSENTRY = _HMISTATUS.nested_types_by_name['GlobalComponentsEntry']
_HMISTATUS_MODULESLOCKENTRY = _HMISTATUS.nested_types_by_name['ModulesLockEntry']
ScenarioInfo = _reflection.GeneratedProtocolMessageType('ScenarioInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIOINFO,
  '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.ScenarioInfo)
  })
_sym_db.RegisterMessage(ScenarioInfo)

ScenarioSet = _reflection.GeneratedProtocolMessageType('ScenarioSet', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIOSET,
  '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.ScenarioSet)
  })
_sym_db.RegisterMessage(ScenarioSet)

RecordStatus = _reflection.GeneratedProtocolMessageType('RecordStatus', (_message.Message,), {
  'DESCRIPTOR' : _RECORDSTATUS,
  '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.RecordStatus)
  })
_sym_db.RegisterMessage(RecordStatus)

LoadRecordInfo = _reflection.GeneratedProtocolMessageType('LoadRecordInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOADRECORDINFO,
  '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.LoadRecordInfo)
  })
_sym_db.RegisterMessage(LoadRecordInfo)

HMIStatus = _reflection.GeneratedProtocolMessageType('HMIStatus', (_message.Message,), {

  'ModulesEntry' : _reflection.GeneratedProtocolMessageType('ModulesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMISTATUS_MODULESENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.ModulesEntry)
    })
  ,

  'MonitoredComponentsEntry' : _reflection.GeneratedProtocolMessageType('MonitoredComponentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMISTATUS_MONITOREDCOMPONENTSENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.MonitoredComponentsEntry)
    })
  ,

  'OtherComponentsEntry' : _reflection.GeneratedProtocolMessageType('OtherComponentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMISTATUS_OTHERCOMPONENTSENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.OtherComponentsEntry)
    })
  ,

  'ScenarioSetEntry' : _reflection.GeneratedProtocolMessageType('ScenarioSetEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMISTATUS_SCENARIOSETENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.ScenarioSetEntry)
    })
  ,

  'RecordsEntry' : _reflection.GeneratedProtocolMessageType('RecordsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMISTATUS_RECORDSENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.RecordsEntry)
    })
  ,

  'GlobalComponentsEntry' : _reflection.GeneratedProtocolMessageType('GlobalComponentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMISTATUS_GLOBALCOMPONENTSENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.GlobalComponentsEntry)
    })
  ,

  'ModulesLockEntry' : _reflection.GeneratedProtocolMessageType('ModulesLockEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMISTATUS_MODULESLOCKENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus.ModulesLockEntry)
    })
  ,
  'DESCRIPTOR' : _HMISTATUS,
  '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_status_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIStatus)
  })
_sym_db.RegisterMessage(HMIStatus)
_sym_db.RegisterMessage(HMIStatus.ModulesEntry)
_sym_db.RegisterMessage(HMIStatus.MonitoredComponentsEntry)
_sym_db.RegisterMessage(HMIStatus.OtherComponentsEntry)
_sym_db.RegisterMessage(HMIStatus.ScenarioSetEntry)
_sym_db.RegisterMessage(HMIStatus.RecordsEntry)
_sym_db.RegisterMessage(HMIStatus.GlobalComponentsEntry)
_sym_db.RegisterMessage(HMIStatus.ModulesLockEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HMISTATUS_MODULESENTRY._options = None
  _HMISTATUS_MODULESENTRY._serialized_options = b'8\001'
  _HMISTATUS_MONITOREDCOMPONENTSENTRY._options = None
  _HMISTATUS_MONITOREDCOMPONENTSENTRY._serialized_options = b'8\001'
  _HMISTATUS_OTHERCOMPONENTSENTRY._options = None
  _HMISTATUS_OTHERCOMPONENTSENTRY._serialized_options = b'8\001'
  _HMISTATUS_SCENARIOSETENTRY._options = None
  _HMISTATUS_SCENARIOSETENTRY._serialized_options = b'8\001'
  _HMISTATUS_RECORDSENTRY._options = None
  _HMISTATUS_RECORDSENTRY._serialized_options = b'8\001'
  _HMISTATUS_GLOBALCOMPONENTSENTRY._options = None
  _HMISTATUS_GLOBALCOMPONENTSENTRY._serialized_options = b'8\001'
  _HMISTATUS_MODULESLOCKENTRY._options = None
  _HMISTATUS_MODULESLOCKENTRY._serialized_options = b'8\001'
  _PLAYRECORDSTATUS._serialized_start=2630
  _PLAYRECORDSTATUS._serialized_end=2685
  _HMIMODEOPERATION._serialized_start=2688
  _HMIMODEOPERATION._serialized_end=2826
  _LOADRECORDSTATUS._serialized_start=2828
  _LOADRECORDSTATUS._serialized_end=2885
  _SCENARIOINFO._serialized_start=220
  _SCENARIOINFO._serialized_end=384
  _SCENARIOSET._serialized_start=386
  _SCENARIOSET._serialized_end=477
  _RECORDSTATUS._serialized_start=480
  _RECORDSTATUS._serialized_end=619
  _LOADRECORDINFO._serialized_start=622
  _LOADRECORDINFO._serialized_end=793
  _HMISTATUS._serialized_start=796
  _HMISTATUS._serialized_end=2628
  _HMISTATUS_MODULESENTRY._serialized_start=2099
  _HMISTATUS_MODULESENTRY._serialized_end=2145
  _HMISTATUS_MONITOREDCOMPONENTSENTRY._serialized_start=2147
  _HMISTATUS_MONITOREDCOMPONENTSENTRY._serialized_end=2238
  _HMISTATUS_OTHERCOMPONENTSENTRY._serialized_start=2240
  _HMISTATUS_OTHERCOMPONENTSENTRY._serialized_end=2327
  _HMISTATUS_SCENARIOSETENTRY._serialized_start=2329
  _HMISTATUS_SCENARIOSETENTRY._serialized_end=2410
  _HMISTATUS_RECORDSENTRY._serialized_start=2412
  _HMISTATUS_RECORDSENTRY._serialized_end=2492
  _HMISTATUS_GLOBALCOMPONENTSENTRY._serialized_start=2494
  _HMISTATUS_GLOBALCOMPONENTSENTRY._serialized_end=2576
  _HMISTATUS_MODULESLOCKENTRY._serialized_start=2578
  _HMISTATUS_MODULESLOCKENTRY._serialized_end=2628
# @@protoc_insertion_point(module_scope)
