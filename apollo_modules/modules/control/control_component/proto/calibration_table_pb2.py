# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/control/control_component/proto/calibration_table.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?modules/control/control_component/proto/calibration_table.proto\x12\x0e\x61pollo.control\"P\n\x11\x63\x61libration_table\x12;\n\x0b\x63\x61libration\x18\x01 \x03(\x0b\x32&.apollo.control.ControlCalibrationInfo\"N\n\x16\x43ontrolCalibrationInfo\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x02 \x01(\x01\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\x01')



_CALIBRATION_TABLE = DESCRIPTOR.message_types_by_name['calibration_table']
_CONTROLCALIBRATIONINFO = DESCRIPTOR.message_types_by_name['ControlCalibrationInfo']
calibration_table = _reflection.GeneratedProtocolMessageType('calibration_table', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATION_TABLE,
  '__module__' : 'modules.control.control_component.proto.calibration_table_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.calibration_table)
  })
_sym_db.RegisterMessage(calibration_table)

ControlCalibrationInfo = _reflection.GeneratedProtocolMessageType('ControlCalibrationInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLCALIBRATIONINFO,
  '__module__' : 'modules.control.control_component.proto.calibration_table_pb2'
  # @@protoc_insertion_point(class_scope:apollo.control.ControlCalibrationInfo)
  })
_sym_db.RegisterMessage(ControlCalibrationInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CALIBRATION_TABLE._serialized_start=83
  _CALIBRATION_TABLE._serialized_end=163
  _CONTROLCALIBRATIONINFO._serialized_start=165
  _CONTROLCALIBRATIONINFO._serialized_end=243
# @@protoc_insertion_point(module_scope)
