# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/dreamview_msgs/hmi_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3modules/common_msgs/dreamview_msgs/hmi_config.proto\x12\x10\x61pollo.dreamview\"\xc0\x02\n\tHMIConfig\x12\x35\n\x05modes\x18\x01 \x03(\x0b\x32&.apollo.dreamview.HMIConfig.ModesEntry\x12\x33\n\x04maps\x18\x02 \x03(\x0b\x32%.apollo.dreamview.HMIConfig.MapsEntry\x12;\n\x08vehicles\x18\x03 \x03(\x0b\x32).apollo.dreamview.HMIConfig.VehiclesEntry\x1a,\n\nModesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tMapsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rVehiclesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\x0bVehicleData\x12:\n\ndata_files\x18\x01 \x03(\x0b\x32&.apollo.dreamview.VehicleData.DataFile\x1a\x32\n\x08\x44\x61taFile\x12\x13\n\x0bsource_path\x18\x01 \x01(\t\x12\x11\n\tdest_path\x18\x02 \x01(\t*\xb4\x04\n\tHMIAction\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nSETUP_MODE\x10\x01\x12\x0e\n\nRESET_MODE\x10\x02\x12\x13\n\x0f\x45NTER_AUTO_MODE\x10\x03\x12\r\n\tDISENGAGE\x10\x04\x12\x0f\n\x0b\x43HANGE_MODE\x10\x05\x12\x0e\n\nCHANGE_MAP\x10\x06\x12\x12\n\x0e\x43HANGE_VEHICLE\x10\x07\x12\x10\n\x0cSTART_MODULE\x10\x08\x12\x0f\n\x0bSTOP_MODULE\x10\t\x12\x13\n\x0f\x43HANGE_SCENARIO\x10\n\x12\x17\n\x13\x43HANGE_SCENARIO_SET\x10\x0b\x12\x12\n\x0eLOAD_SCENARIOS\x10\x0c\x12\x17\n\x13\x44\x45LETE_SCENARIO_SET\x10\r\x12\x17\n\x13LOAD_DYNAMIC_MODELS\x10\x0e\x12\x18\n\x14\x43HANGE_DYNAMIC_MODEL\x10\x0f\x12\x18\n\x14\x44\x45LETE_DYNAMIC_MODEL\x10\x10\x12\x11\n\rCHANGE_RECORD\x10\x11\x12\x11\n\rDELETE_RECORD\x10\x12\x12\x10\n\x0cLOAD_RECORDS\x10\x13\x12\x0f\n\x0bSTOP_RECORD\x10\x14\x12\x14\n\x10\x43HANGE_OPERATION\x10\x15\x12\x17\n\x13\x44\x45LETE_VEHICLE_CONF\x10\x16\x12\x13\n\x0f\x44\x45LETE_V2X_CONF\x10\x17\x12\x0e\n\nDELETE_MAP\x10\x18\x12\x14\n\x10LOAD_RTK_RECORDS\x10\x19\x12\x15\n\x11\x43HANGE_RTK_RECORD\x10\x1a\x12\x0f\n\x0bLOAD_RECORD\x10\x1b')

_HMIACTION = DESCRIPTOR.enum_types_by_name['HMIAction']
HMIAction = enum_type_wrapper.EnumTypeWrapper(_HMIACTION)
NONE = 0
SETUP_MODE = 1
RESET_MODE = 2
ENTER_AUTO_MODE = 3
DISENGAGE = 4
CHANGE_MODE = 5
CHANGE_MAP = 6
CHANGE_VEHICLE = 7
START_MODULE = 8
STOP_MODULE = 9
CHANGE_SCENARIO = 10
CHANGE_SCENARIO_SET = 11
LOAD_SCENARIOS = 12
DELETE_SCENARIO_SET = 13
LOAD_DYNAMIC_MODELS = 14
CHANGE_DYNAMIC_MODEL = 15
DELETE_DYNAMIC_MODEL = 16
CHANGE_RECORD = 17
DELETE_RECORD = 18
LOAD_RECORDS = 19
STOP_RECORD = 20
CHANGE_OPERATION = 21
DELETE_VEHICLE_CONF = 22
DELETE_V2X_CONF = 23
DELETE_MAP = 24
LOAD_RTK_RECORDS = 25
CHANGE_RTK_RECORD = 26
LOAD_RECORD = 27


_HMICONFIG = DESCRIPTOR.message_types_by_name['HMIConfig']
_HMICONFIG_MODESENTRY = _HMICONFIG.nested_types_by_name['ModesEntry']
_HMICONFIG_MAPSENTRY = _HMICONFIG.nested_types_by_name['MapsEntry']
_HMICONFIG_VEHICLESENTRY = _HMICONFIG.nested_types_by_name['VehiclesEntry']
_VEHICLEDATA = DESCRIPTOR.message_types_by_name['VehicleData']
_VEHICLEDATA_DATAFILE = _VEHICLEDATA.nested_types_by_name['DataFile']
HMIConfig = _reflection.GeneratedProtocolMessageType('HMIConfig', (_message.Message,), {

  'ModesEntry' : _reflection.GeneratedProtocolMessageType('ModesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMICONFIG_MODESENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIConfig.ModesEntry)
    })
  ,

  'MapsEntry' : _reflection.GeneratedProtocolMessageType('MapsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMICONFIG_MAPSENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIConfig.MapsEntry)
    })
  ,

  'VehiclesEntry' : _reflection.GeneratedProtocolMessageType('VehiclesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HMICONFIG_VEHICLESENTRY,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIConfig.VehiclesEntry)
    })
  ,
  'DESCRIPTOR' : _HMICONFIG,
  '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.HMIConfig)
  })
_sym_db.RegisterMessage(HMIConfig)
_sym_db.RegisterMessage(HMIConfig.ModesEntry)
_sym_db.RegisterMessage(HMIConfig.MapsEntry)
_sym_db.RegisterMessage(HMIConfig.VehiclesEntry)

VehicleData = _reflection.GeneratedProtocolMessageType('VehicleData', (_message.Message,), {

  'DataFile' : _reflection.GeneratedProtocolMessageType('DataFile', (_message.Message,), {
    'DESCRIPTOR' : _VEHICLEDATA_DATAFILE,
    '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_config_pb2'
    # @@protoc_insertion_point(class_scope:apollo.dreamview.VehicleData.DataFile)
    })
  ,
  'DESCRIPTOR' : _VEHICLEDATA,
  '__module__' : 'modules.common_msgs.dreamview_msgs.hmi_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.dreamview.VehicleData)
  })
_sym_db.RegisterMessage(VehicleData)
_sym_db.RegisterMessage(VehicleData.DataFile)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HMICONFIG_MODESENTRY._options = None
  _HMICONFIG_MODESENTRY._serialized_options = b'8\001'
  _HMICONFIG_MAPSENTRY._options = None
  _HMICONFIG_MAPSENTRY._serialized_options = b'8\001'
  _HMICONFIG_VEHICLESENTRY._options = None
  _HMICONFIG_VEHICLESENTRY._serialized_options = b'8\001'
  _HMIACTION._serialized_start=524
  _HMIACTION._serialized_end=1088
  _HMICONFIG._serialized_start=74
  _HMICONFIG._serialized_end=394
  _HMICONFIG_MODESENTRY._serialized_start=256
  _HMICONFIG_MODESENTRY._serialized_end=300
  _HMICONFIG_MAPSENTRY._serialized_start=302
  _HMICONFIG_MAPSENTRY._serialized_end=345
  _HMICONFIG_VEHICLESENTRY._serialized_start=347
  _HMICONFIG_VEHICLESENTRY._serialized_end=394
  _VEHICLEDATA._serialized_start=396
  _VEHICLEDATA._serialized_end=521
  _VEHICLEDATA_DATAFILE._serialized_start=471
  _VEHICLEDATA_DATAFILE._serialized_end=521
# @@protoc_insertion_point(module_scope)