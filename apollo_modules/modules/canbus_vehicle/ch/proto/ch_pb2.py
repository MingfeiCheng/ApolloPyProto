# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/canbus_vehicle/ch/proto/ch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(modules/canbus_vehicle/ch/proto/ch.proto\x12\rapollo.canbus\"\xf7\x01\n\x14Throttle_command_110\x12^\n\x16throttle_pedal_en_ctrl\x18\x01 \x01(\x0e\x32>.apollo.canbus.Throttle_command_110.Throttle_pedal_en_ctrlType\x12\x1a\n\x12throttle_pedal_cmd\x18\x02 \x01(\x05\"c\n\x1aThrottle_pedal_en_ctrlType\x12\"\n\x1eTHROTTLE_PEDAL_EN_CTRL_DISABLE\x10\x00\x12!\n\x1dTHROTTLE_PEDAL_EN_CTRL_ENABLE\x10\x01\"\xdf\x01\n\x11\x42rake_command_111\x12U\n\x13\x62rake_pedal_en_ctrl\x18\x01 \x01(\x0e\x32\x38.apollo.canbus.Brake_command_111.Brake_pedal_en_ctrlType\x12\x17\n\x0f\x62rake_pedal_cmd\x18\x02 \x01(\x05\"Z\n\x17\x42rake_pedal_en_ctrlType\x12\x1f\n\x1b\x42RAKE_PEDAL_EN_CTRL_DISABLE\x10\x00\x12\x1e\n\x1a\x42RAKE_PEDAL_EN_CTRL_ENABLE\x10\x01\"\xdf\x01\n\x11Steer_command_112\x12U\n\x13steer_angle_en_ctrl\x18\x01 \x01(\x0e\x32\x38.apollo.canbus.Steer_command_112.Steer_angle_en_ctrlType\x12\x17\n\x0fsteer_angle_cmd\x18\x02 \x01(\x01\"Z\n\x17Steer_angle_en_ctrlType\x12\x1f\n\x1bSTEER_ANGLE_EN_CTRL_DISABLE\x10\x00\x12\x1e\n\x1aSTEER_ANGLE_EN_CTRL_ENABLE\x10\x01\"\x8c\x03\n\x16Turnsignal_command_113\x12R\n\x0fturn_signal_cmd\x18\x01 \x01(\x0e\x32\x39.apollo.canbus.Turnsignal_command_113.Turn_signal_cmdType\x12L\n\x0clow_beam_cmd\x18\x02 \x01(\x0e\x32\x36.apollo.canbus.Turnsignal_command_113.Low_beam_cmdType\"=\n\x10Low_beam_cmdType\x12\x14\n\x10LOW_BEAM_CMD_OFF\x10\x00\x12\x13\n\x0fLOW_BEAM_CMD_ON\x10\x01\"\x90\x01\n\x13Turn_signal_cmdType\x12\x18\n\x14TURN_SIGNAL_CMD_NONE\x10\x00\x12\x18\n\x14TURN_SIGNAL_CMD_LEFT\x10\x01\x12\x19\n\x15TURN_SIGNAL_CMD_RIGHT\x10\x02\x12*\n&TURN_SIGNAL_CMD_HAZARD_WARNING_LAMPSTS\x10\x03\"\xb5\x01\n\x10Gear_command_114\x12>\n\x08gear_cmd\x18\x01 \x01(\x0e\x32,.apollo.canbus.Gear_command_114.Gear_cmdType\"a\n\x0cGear_cmdType\x12\x11\n\rGEAR_CMD_PARK\x10\x01\x12\x14\n\x10GEAR_CMD_REVERSE\x10\x02\x12\x14\n\x10GEAR_CMD_NEUTRAL\x10\x03\x12\x12\n\x0eGEAR_CMD_DRIVE\x10\x04\"\xa1\x01\n\x13\x43ontrol_command_115\x12\x41\n\x08\x63trl_cmd\x18\x01 \x01(\x0e\x32/.apollo.canbus.Control_command_115.Ctrl_cmdType\"G\n\x0c\x43trl_cmdType\x12\x1b\n\x17\x43TRL_CMD_OUT_OF_CONTROL\x10\x00\x12\x1a\n\x16\x43TRL_CMD_UNDER_CONTROL\x10\x01\"\xbc\x01\n\x18Vehicle_mode_command_116\x12L\n\x0bvin_req_cmd\x18\x01 \x01(\x0e\x32\x37.apollo.canbus.Vehicle_mode_command_116.Vin_req_cmdType\"R\n\x0fVin_req_cmdType\x12\x1f\n\x1bVIN_REQ_CMD_VIN_REQ_DISABLE\x10\x00\x12\x1e\n\x1aVIN_REQ_CMD_VIN_REQ_ENABLE\x10\x01\"\xe3\x04\n\x14Throttle_status__510\x12\\\n\x15throttle_pedal_en_sts\x18\x01 \x01(\x0e\x32=.apollo.canbus.Throttle_status__510.Throttle_pedal_en_stsType\x12\x1a\n\x12throttle_pedal_sts\x18\x02 \x01(\x05\x12P\n\x0f\x64rive_motor_err\x18\x03 \x01(\x0e\x32\x37.apollo.canbus.Throttle_status__510.Drive_motor_errType\x12P\n\x0f\x62\x61ttery_bms_err\x18\x04 \x01(\x0e\x32\x37.apollo.canbus.Throttle_status__510.Battery_bms_errType\"\x84\x01\n\x19Throttle_pedal_en_stsType\x12!\n\x1dTHROTTLE_PEDAL_EN_STS_DISABLE\x10\x00\x12 \n\x1cTHROTTLE_PEDAL_EN_STS_ENABLE\x10\x01\x12\"\n\x1eTHROTTLE_PEDAL_EN_STS_TAKEOVER\x10\x02\"S\n\x13\x44rive_motor_errType\x12\x19\n\x15\x44RIVE_MOTOR_ERR_NOERR\x10\x00\x12!\n\x1d\x44RIVE_MOTOR_ERR_DRV_MOTOR_ERR\x10\x01\"Q\n\x13\x42\x61ttery_bms_errType\x12\x19\n\x15\x42\x41TTERY_BMS_ERR_NOERR\x10\x00\x12\x1f\n\x1b\x42\x41TTERY_BMS_ERR_BATTERY_ERR\x10\x01\"\xc3\t\n\x11\x42rake_status__511\x12S\n\x12\x62rake_pedal_en_sts\x18\x01 \x01(\x0e\x32\x37.apollo.canbus.Brake_status__511.Brake_pedal_en_stsType\x12\x17\n\x0f\x62rake_pedal_sts\x18\x02 \x01(\x05\x12\x41\n\tbrake_err\x18\x03 \x01(\x0e\x32..apollo.canbus.Brake_status__511.Brake_errType\x12Q\n\x11\x65mergency_btn_env\x18\x04 \x01(\x0e\x32\x36.apollo.canbus.Brake_status__511.Emergency_btn_envType\x12K\n\x0e\x66ront_bump_env\x18\x05 \x01(\x0e\x32\x33.apollo.canbus.Brake_status__511.Front_bump_envType\x12I\n\rback_bump_env\x18\x06 \x01(\x0e\x32\x32.apollo.canbus.Brake_status__511.Back_bump_envType\x12\x45\n\x0boverspd_env\x18\x07 \x01(\x0e\x32\x30.apollo.canbus.Brake_status__511.Overspd_envType\x12S\n\x12\x62rake_light_actual\x18\x08 \x01(\x0e\x32\x37.apollo.canbus.Brake_status__511.Brake_light_actualType\"G\n\x0fOverspd_envType\x12\x15\n\x11OVERSPD_ENV_NOENV\x10\x00\x12\x1d\n\x19OVERSPD_ENV_OVERSPEED_ENV\x10\x01\"x\n\x16\x42rake_pedal_en_stsType\x12\x1e\n\x1a\x42RAKE_PEDAL_EN_STS_DISABLE\x10\x00\x12\x1d\n\x19\x42RAKE_PEDAL_EN_STS_ENABLE\x10\x01\x12\x1f\n\x1b\x42RAKE_PEDAL_EN_STS_TAKEOVER\x10\x02\"D\n\rBrake_errType\x12\x13\n\x0f\x42RAKE_ERR_NOERR\x10\x00\x12\x1e\n\x1a\x42RAKE_ERR_BRAKE_SYSTEM_ERR\x10\x01\"`\n\x15\x45mergency_btn_envType\x12\x1b\n\x17\x45MERGENCY_BTN_ENV_NOENV\x10\x00\x12*\n&EMERGENCY_BTN_ENV_EMERGENCY_BUTTON_ENV\x10\x01\"S\n\x12\x46ront_bump_envType\x12\x18\n\x14\x46RONT_BUMP_ENV_NOENV\x10\x00\x12#\n\x1f\x46RONT_BUMP_ENV_FRONT_BUMPER_ENV\x10\x01\"O\n\x11\x42\x61\x63k_bump_envType\x12\x17\n\x13\x42\x41\x43K_BUMP_ENV_NOENV\x10\x00\x12!\n\x1d\x42\x41\x43K_BUMP_ENV_BACK_BUMPER_ENV\x10\x01\"e\n\x16\x42rake_light_actualType\x12%\n!BRAKE_LIGHT_ACTUAL_BRAKELIGHT_OFF\x10\x00\x12$\n BRAKE_LIGHT_ACTUAL_BRAKELIGHT_ON\x10\x01\"\x91\x04\n\x11Steer_status__512\x12S\n\x12steer_angle_en_sts\x18\x01 \x01(\x0e\x32\x37.apollo.canbus.Steer_status__512.Steer_angle_en_stsType\x12\x17\n\x0fsteer_angle_sts\x18\x02 \x01(\x01\x12\x41\n\tsteer_err\x18\x03 \x01(\x0e\x32..apollo.canbus.Steer_status__512.Steer_errType\x12\x43\n\nsensor_err\x18\x04 \x01(\x0e\x32/.apollo.canbus.Steer_status__512.Sensor_errType\"x\n\x16Steer_angle_en_stsType\x12\x1e\n\x1aSTEER_ANGLE_EN_STS_DISABLE\x10\x00\x12\x1d\n\x19STEER_ANGLE_EN_STS_ENABLE\x10\x01\x12\x1f\n\x1bSTEER_ANGLE_EN_STS_TAKEOVER\x10\x02\"C\n\rSteer_errType\x12\x13\n\x0fSTEER_ERR_NOERR\x10\x00\x12\x1d\n\x19STEER_ERR_STEER_MOTOR_ERR\x10\x01\"G\n\x0eSensor_errType\x12\x14\n\x10SENSOR_ERR_NOERR\x10\x00\x12\x1f\n\x1bSENSOR_ERR_STEER_SENSOR_ERR\x10\x01\"\x8f\x03\n\x16Turnsignal_status__513\x12R\n\x0fturn_signal_sts\x18\x01 \x01(\x0e\x32\x39.apollo.canbus.Turnsignal_status__513.Turn_signal_stsType\x12L\n\x0clow_beam_sts\x18\x02 \x01(\x0e\x32\x36.apollo.canbus.Turnsignal_status__513.Low_beam_stsType\"=\n\x10Low_beam_stsType\x12\x13\n\x0fLOW_BEAM_STS_ON\x10\x00\x12\x14\n\x10LOW_BEAM_STS_OFF\x10\x01\"\x93\x01\n\x13Turn_signal_stsType\x12\x18\n\x14TURN_SIGNAL_STS_NONE\x10\x00\x12\x18\n\x14TURN_SIGNAL_STS_LEFT\x10\x01\x12\x19\n\x15TURN_SIGNAL_STS_RIGHT\x10\x02\x12-\n)TURN_SIGNAL_STS_HAZARD_WARNING_LAMPSTS_ON\x10\x03\"\xb3\x01\n\x0fGear_status_514\x12=\n\x08gear_sts\x18\x01 \x01(\x0e\x32+.apollo.canbus.Gear_status_514.Gear_stsType\"a\n\x0cGear_stsType\x12\x11\n\rGEAR_STS_PARK\x10\x01\x12\x14\n\x10GEAR_STS_REVERSE\x10\x02\x12\x14\n\x10GEAR_STS_NEUTRAL\x10\x03\x12\x12\n\x0eGEAR_STS_DRIVE\x10\x04\"\x90\r\n\x10\x45\x63u_status_1_515\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x11\n\tacc_speed\x18\x02 \x01(\x01\x12>\n\x08\x63trl_sts\x18\x03 \x01(\x0e\x32,.apollo.canbus.Ecu_status_1_515.Ctrl_stsType\x12\x13\n\x0b\x63hassis_sts\x18\x04 \x01(\x05\x12\x13\n\x0b\x63hassis_err\x18\x05 \x01(\x05\x12L\n\x0f\x63hassis_mcu_err\x18\x06 \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_mcu_errType\x12L\n\x0f\x63hassis_mcu_can\x18\x07 \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_mcu_canType\x12L\n\x0f\x63hassis_hw_lost\x18\x08 \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_hw_lostType\x12L\n\x0f\x63hassis_eps_err\x18\t \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_eps_errType\x12L\n\x0f\x63hassis_eps_can\x18\n \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_eps_canType\x12L\n\x0f\x63hassis_ehb_err\x18\x0b \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_ehb_errType\x12L\n\x0f\x63hassis_ehb_can\x18\x0c \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_ehb_canType\x12L\n\x0f\x63hassis_bms_can\x18\r \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_bms_canType\x12L\n\x0f\x63hassis_ads_err\x18\x0e \x01(\x0e\x32\x33.apollo.canbus.Ecu_status_1_515.Chassis_ads_errType\"G\n\x0c\x43trl_stsType\x12\x1b\n\x17\x43TRL_STS_OUT_OF_CONTROL\x10\x00\x12\x1a\n\x16\x43TRL_STS_UNDER_CONTROL\x10\x01\"L\n\x13\x43hassis_mcu_errType\x12\x1a\n\x16\x43HASSIS_MCU_ERR_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_MCU_ERR_ERROR\x10\x01\"L\n\x13\x43hassis_mcu_canType\x12\x1a\n\x16\x43HASSIS_MCU_CAN_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_MCU_CAN_ERROR\x10\x01\"L\n\x13\x43hassis_hw_lostType\x12\x1a\n\x16\x43HASSIS_HW_LOST_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_HW_LOST_ERROR\x10\x01\"L\n\x13\x43hassis_eps_errType\x12\x1a\n\x16\x43HASSIS_EPS_ERR_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_EPS_ERR_ERROR\x10\x01\"L\n\x13\x43hassis_eps_canType\x12\x1a\n\x16\x43HASSIS_EPS_CAN_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_EPS_CAN_ERROR\x10\x01\"L\n\x13\x43hassis_ehb_errType\x12\x1a\n\x16\x43HASSIS_EHB_ERR_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_EHB_ERR_ERROR\x10\x01\"L\n\x13\x43hassis_ehb_canType\x12\x1a\n\x16\x43HASSIS_EHB_CAN_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_EHB_CAN_ERROR\x10\x01\"L\n\x13\x43hassis_bms_canType\x12\x1a\n\x16\x43HASSIS_BMS_CAN_NORMAL\x10\x00\x12\x19\n\x15\x43HASSIS_BMS_CAN_ERROR\x10\x01\"y\n\x13\x43hassis_ads_errType\x12\x1a\n\x16\x43HASSIS_ADS_ERR_NORMAL\x10\x00\x12 \n\x1c\x43HASSIS_ADS_ERR_ADS_CAN_LOST\x10\x01\x12$\n CHASSIS_ADS_ERR_ADS_CAN_RECOVERY\x10\x02\"\xac\x01\n\x10\x45\x63u_status_2_516\x12\x13\n\x0b\x62\x61ttery_soc\x18\x01 \x01(\x05\x12\x18\n\x10\x62\x61ttery_capacity\x18\x02 \x01(\x05\x12\x17\n\x0f\x62\x61ttery_voltage\x18\x03 \x01(\x01\x12\x17\n\x0f\x62\x61ttery_current\x18\x04 \x01(\x01\x12\x1b\n\x13\x62\x61ttery_temperature\x18\x05 \x01(\x05\x12\x1a\n\x12is_battery_soc_low\x18\x06 \x01(\x08\"\xea\x01\n\x10\x45\x63u_status_3_517\x12\x19\n\x11ultrasound_dist_1\x18\x01 \x01(\x01\x12\x19\n\x11ultrasound_dist_2\x18\x02 \x01(\x01\x12\x19\n\x11ultrasound_dist_3\x18\x03 \x01(\x01\x12\x19\n\x11ultrasound_dist_4\x18\x04 \x01(\x01\x12\x19\n\x11ultrasound_dist_5\x18\x05 \x01(\x01\x12\x19\n\x11ultrasound_dist_6\x18\x06 \x01(\x01\x12\x19\n\x11ultrasound_dist_7\x18\x07 \x01(\x01\x12\x19\n\x11ultrasound_dist_8\x18\x08 \x01(\x01\"\xf1\x01\n\x10\x45\x63u_status_4_518\x12\x19\n\x11ultrasound_dist_9\x18\x01 \x01(\x01\x12\x1a\n\x12ultrasound_dist_10\x18\x02 \x01(\x01\x12\x1a\n\x12ultrasound_dist_11\x18\x03 \x01(\x01\x12\x1a\n\x12ultrasound_dist_12\x18\x04 \x01(\x01\x12\x1a\n\x12ultrasound_dist_13\x18\x05 \x01(\x01\x12\x1a\n\x12ultrasound_dist_14\x18\x06 \x01(\x01\x12\x1a\n\x12ultrasound_dist_15\x18\x07 \x01(\x01\x12\x1a\n\x12ultrasound_dist_16\x18\x08 \x01(\x01\"\x87\x01\n\rVin_resp1_51b\x12\r\n\x05vin08\x18\x01 \x01(\t\x12\r\n\x05vin07\x18\x02 \x01(\t\x12\r\n\x05vin06\x18\x03 \x01(\t\x12\r\n\x05vin05\x18\x04 \x01(\t\x12\r\n\x05vin04\x18\x05 \x01(\t\x12\r\n\x05vin03\x18\x06 \x01(\t\x12\r\n\x05vin02\x18\x07 \x01(\t\x12\r\n\x05vin01\x18\x08 \x01(\t\"\x87\x01\n\rVin_resp2_51c\x12\r\n\x05vin16\x18\x01 \x01(\t\x12\r\n\x05vin15\x18\x02 \x01(\t\x12\r\n\x05vin14\x18\x03 \x01(\t\x12\r\n\x05vin13\x18\x04 \x01(\t\x12\r\n\x05vin12\x18\x05 \x01(\t\x12\r\n\x05vin11\x18\x06 \x01(\t\x12\r\n\x05vin10\x18\x07 \x01(\t\x12\r\n\x05vin09\x18\x08 \x01(\t\"\x1e\n\rVin_resp3_51d\x12\r\n\x05vin17\x18\x01 \x01(\t\"G\n\x15Wheelspeed_report_51e\x12\n\n\x02rr\x18\x01 \x01(\x01\x12\n\n\x02rl\x18\x02 \x01(\x01\x12\n\n\x02\x66r\x18\x03 \x01(\x01\x12\n\n\x02\x66l\x18\x04 \x01(\x01\"\xeb\x01\n\x13\x43heckResponseSignal\x12\x1c\n\ris_eps_online\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ris_epb_online\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ris_esp_online\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1d\n\x0eis_vtog_online\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ris_scu_online\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10is_switch_online\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\ris_vcu_online\x18\x07 \x01(\x08:\x05\x66\x61lse\"\x9c\n\n\x02\x43h\x12\x41\n\x14throttle_command_110\x18\x01 \x01(\x0b\x32#.apollo.canbus.Throttle_command_110\x12;\n\x11\x62rake_command_111\x18\x02 \x01(\x0b\x32 .apollo.canbus.Brake_command_111\x12;\n\x11steer_command_112\x18\x03 \x01(\x0b\x32 .apollo.canbus.Steer_command_112\x12\x45\n\x16turnsignal_command_113\x18\x04 \x01(\x0b\x32%.apollo.canbus.Turnsignal_command_113\x12\x39\n\x10gear_command_114\x18\x05 \x01(\x0b\x32\x1f.apollo.canbus.Gear_command_114\x12\x43\n\x13\x63ontrol_command_115\x18\x06 \x01(\x0b\x32\".apollo.canbus.Control_command_115B\x02\x18\x01\x12\x41\n\x14throttle_status__510\x18\x07 \x01(\x0b\x32#.apollo.canbus.Throttle_status__510\x12;\n\x11\x62rake_status__511\x18\x08 \x01(\x0b\x32 .apollo.canbus.Brake_status__511\x12;\n\x11steer_status__512\x18\t \x01(\x0b\x32 .apollo.canbus.Steer_status__512\x12\x45\n\x16turnsignal_status__513\x18\n \x01(\x0b\x32%.apollo.canbus.Turnsignal_status__513\x12\x37\n\x0fgear_status_514\x18\x0b \x01(\x0b\x32\x1e.apollo.canbus.Gear_status_514\x12\x39\n\x10\x65\x63u_status_1_515\x18\x0c \x01(\x0b\x32\x1f.apollo.canbus.Ecu_status_1_515\x12\x39\n\x10\x65\x63u_status_2_516\x18\r \x01(\x0b\x32\x1f.apollo.canbus.Ecu_status_2_516\x12\x39\n\x10\x65\x63u_status_3_517\x18\x0e \x01(\x0b\x32\x1f.apollo.canbus.Ecu_status_3_517\x12\x39\n\x10\x65\x63u_status_4_518\x18\x0f \x01(\x0b\x32\x1f.apollo.canbus.Ecu_status_4_518\x12I\n\x18vehicle_mode_command_116\x18\x10 \x01(\x0b\x32\'.apollo.canbus.Vehicle_mode_command_116\x12\x33\n\rvin_resp1_51b\x18\x11 \x01(\x0b\x32\x1c.apollo.canbus.Vin_resp1_51b\x12\x33\n\rvin_resp2_51c\x18\x12 \x01(\x0b\x32\x1c.apollo.canbus.Vin_resp2_51c\x12\x33\n\rvin_resp3_51d\x18\x13 \x01(\x0b\x32\x1c.apollo.canbus.Vin_resp3_51d\x12\x43\n\x15wheelspeed_report_51e\x18\x14 \x01(\x0b\x32$.apollo.canbus.Wheelspeed_report_51e\x12:\n\x0e\x63heck_response\x18\x64 \x01(\x0b\x32\".apollo.canbus.CheckResponseSignal')



_THROTTLE_COMMAND_110 = DESCRIPTOR.message_types_by_name['Throttle_command_110']
_BRAKE_COMMAND_111 = DESCRIPTOR.message_types_by_name['Brake_command_111']
_STEER_COMMAND_112 = DESCRIPTOR.message_types_by_name['Steer_command_112']
_TURNSIGNAL_COMMAND_113 = DESCRIPTOR.message_types_by_name['Turnsignal_command_113']
_GEAR_COMMAND_114 = DESCRIPTOR.message_types_by_name['Gear_command_114']
_CONTROL_COMMAND_115 = DESCRIPTOR.message_types_by_name['Control_command_115']
_VEHICLE_MODE_COMMAND_116 = DESCRIPTOR.message_types_by_name['Vehicle_mode_command_116']
_THROTTLE_STATUS__510 = DESCRIPTOR.message_types_by_name['Throttle_status__510']
_BRAKE_STATUS__511 = DESCRIPTOR.message_types_by_name['Brake_status__511']
_STEER_STATUS__512 = DESCRIPTOR.message_types_by_name['Steer_status__512']
_TURNSIGNAL_STATUS__513 = DESCRIPTOR.message_types_by_name['Turnsignal_status__513']
_GEAR_STATUS_514 = DESCRIPTOR.message_types_by_name['Gear_status_514']
_ECU_STATUS_1_515 = DESCRIPTOR.message_types_by_name['Ecu_status_1_515']
_ECU_STATUS_2_516 = DESCRIPTOR.message_types_by_name['Ecu_status_2_516']
_ECU_STATUS_3_517 = DESCRIPTOR.message_types_by_name['Ecu_status_3_517']
_ECU_STATUS_4_518 = DESCRIPTOR.message_types_by_name['Ecu_status_4_518']
_VIN_RESP1_51B = DESCRIPTOR.message_types_by_name['Vin_resp1_51b']
_VIN_RESP2_51C = DESCRIPTOR.message_types_by_name['Vin_resp2_51c']
_VIN_RESP3_51D = DESCRIPTOR.message_types_by_name['Vin_resp3_51d']
_WHEELSPEED_REPORT_51E = DESCRIPTOR.message_types_by_name['Wheelspeed_report_51e']
_CHECKRESPONSESIGNAL = DESCRIPTOR.message_types_by_name['CheckResponseSignal']
_CH = DESCRIPTOR.message_types_by_name['Ch']
_THROTTLE_COMMAND_110_THROTTLE_PEDAL_EN_CTRLTYPE = _THROTTLE_COMMAND_110.enum_types_by_name['Throttle_pedal_en_ctrlType']
_BRAKE_COMMAND_111_BRAKE_PEDAL_EN_CTRLTYPE = _BRAKE_COMMAND_111.enum_types_by_name['Brake_pedal_en_ctrlType']
_STEER_COMMAND_112_STEER_ANGLE_EN_CTRLTYPE = _STEER_COMMAND_112.enum_types_by_name['Steer_angle_en_ctrlType']
_TURNSIGNAL_COMMAND_113_LOW_BEAM_CMDTYPE = _TURNSIGNAL_COMMAND_113.enum_types_by_name['Low_beam_cmdType']
_TURNSIGNAL_COMMAND_113_TURN_SIGNAL_CMDTYPE = _TURNSIGNAL_COMMAND_113.enum_types_by_name['Turn_signal_cmdType']
_GEAR_COMMAND_114_GEAR_CMDTYPE = _GEAR_COMMAND_114.enum_types_by_name['Gear_cmdType']
_CONTROL_COMMAND_115_CTRL_CMDTYPE = _CONTROL_COMMAND_115.enum_types_by_name['Ctrl_cmdType']
_VEHICLE_MODE_COMMAND_116_VIN_REQ_CMDTYPE = _VEHICLE_MODE_COMMAND_116.enum_types_by_name['Vin_req_cmdType']
_THROTTLE_STATUS__510_THROTTLE_PEDAL_EN_STSTYPE = _THROTTLE_STATUS__510.enum_types_by_name['Throttle_pedal_en_stsType']
_THROTTLE_STATUS__510_DRIVE_MOTOR_ERRTYPE = _THROTTLE_STATUS__510.enum_types_by_name['Drive_motor_errType']
_THROTTLE_STATUS__510_BATTERY_BMS_ERRTYPE = _THROTTLE_STATUS__510.enum_types_by_name['Battery_bms_errType']
_BRAKE_STATUS__511_OVERSPD_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Overspd_envType']
_BRAKE_STATUS__511_BRAKE_PEDAL_EN_STSTYPE = _BRAKE_STATUS__511.enum_types_by_name['Brake_pedal_en_stsType']
_BRAKE_STATUS__511_BRAKE_ERRTYPE = _BRAKE_STATUS__511.enum_types_by_name['Brake_errType']
_BRAKE_STATUS__511_EMERGENCY_BTN_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Emergency_btn_envType']
_BRAKE_STATUS__511_FRONT_BUMP_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Front_bump_envType']
_BRAKE_STATUS__511_BACK_BUMP_ENVTYPE = _BRAKE_STATUS__511.enum_types_by_name['Back_bump_envType']
_BRAKE_STATUS__511_BRAKE_LIGHT_ACTUALTYPE = _BRAKE_STATUS__511.enum_types_by_name['Brake_light_actualType']
_STEER_STATUS__512_STEER_ANGLE_EN_STSTYPE = _STEER_STATUS__512.enum_types_by_name['Steer_angle_en_stsType']
_STEER_STATUS__512_STEER_ERRTYPE = _STEER_STATUS__512.enum_types_by_name['Steer_errType']
_STEER_STATUS__512_SENSOR_ERRTYPE = _STEER_STATUS__512.enum_types_by_name['Sensor_errType']
_TURNSIGNAL_STATUS__513_LOW_BEAM_STSTYPE = _TURNSIGNAL_STATUS__513.enum_types_by_name['Low_beam_stsType']
_TURNSIGNAL_STATUS__513_TURN_SIGNAL_STSTYPE = _TURNSIGNAL_STATUS__513.enum_types_by_name['Turn_signal_stsType']
_GEAR_STATUS_514_GEAR_STSTYPE = _GEAR_STATUS_514.enum_types_by_name['Gear_stsType']
_ECU_STATUS_1_515_CTRL_STSTYPE = _ECU_STATUS_1_515.enum_types_by_name['Ctrl_stsType']
_ECU_STATUS_1_515_CHASSIS_MCU_ERRTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_mcu_errType']
_ECU_STATUS_1_515_CHASSIS_MCU_CANTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_mcu_canType']
_ECU_STATUS_1_515_CHASSIS_HW_LOSTTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_hw_lostType']
_ECU_STATUS_1_515_CHASSIS_EPS_ERRTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_eps_errType']
_ECU_STATUS_1_515_CHASSIS_EPS_CANTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_eps_canType']
_ECU_STATUS_1_515_CHASSIS_EHB_ERRTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_ehb_errType']
_ECU_STATUS_1_515_CHASSIS_EHB_CANTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_ehb_canType']
_ECU_STATUS_1_515_CHASSIS_BMS_CANTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_bms_canType']
_ECU_STATUS_1_515_CHASSIS_ADS_ERRTYPE = _ECU_STATUS_1_515.enum_types_by_name['Chassis_ads_errType']
Throttle_command_110 = _reflection.GeneratedProtocolMessageType('Throttle_command_110', (_message.Message,), {
  'DESCRIPTOR' : _THROTTLE_COMMAND_110,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Throttle_command_110)
  })
_sym_db.RegisterMessage(Throttle_command_110)

Brake_command_111 = _reflection.GeneratedProtocolMessageType('Brake_command_111', (_message.Message,), {
  'DESCRIPTOR' : _BRAKE_COMMAND_111,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Brake_command_111)
  })
_sym_db.RegisterMessage(Brake_command_111)

Steer_command_112 = _reflection.GeneratedProtocolMessageType('Steer_command_112', (_message.Message,), {
  'DESCRIPTOR' : _STEER_COMMAND_112,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Steer_command_112)
  })
_sym_db.RegisterMessage(Steer_command_112)

Turnsignal_command_113 = _reflection.GeneratedProtocolMessageType('Turnsignal_command_113', (_message.Message,), {
  'DESCRIPTOR' : _TURNSIGNAL_COMMAND_113,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Turnsignal_command_113)
  })
_sym_db.RegisterMessage(Turnsignal_command_113)

Gear_command_114 = _reflection.GeneratedProtocolMessageType('Gear_command_114', (_message.Message,), {
  'DESCRIPTOR' : _GEAR_COMMAND_114,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Gear_command_114)
  })
_sym_db.RegisterMessage(Gear_command_114)

Control_command_115 = _reflection.GeneratedProtocolMessageType('Control_command_115', (_message.Message,), {
  'DESCRIPTOR' : _CONTROL_COMMAND_115,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Control_command_115)
  })
_sym_db.RegisterMessage(Control_command_115)

Vehicle_mode_command_116 = _reflection.GeneratedProtocolMessageType('Vehicle_mode_command_116', (_message.Message,), {
  'DESCRIPTOR' : _VEHICLE_MODE_COMMAND_116,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Vehicle_mode_command_116)
  })
_sym_db.RegisterMessage(Vehicle_mode_command_116)

Throttle_status__510 = _reflection.GeneratedProtocolMessageType('Throttle_status__510', (_message.Message,), {
  'DESCRIPTOR' : _THROTTLE_STATUS__510,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Throttle_status__510)
  })
_sym_db.RegisterMessage(Throttle_status__510)

Brake_status__511 = _reflection.GeneratedProtocolMessageType('Brake_status__511', (_message.Message,), {
  'DESCRIPTOR' : _BRAKE_STATUS__511,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Brake_status__511)
  })
_sym_db.RegisterMessage(Brake_status__511)

Steer_status__512 = _reflection.GeneratedProtocolMessageType('Steer_status__512', (_message.Message,), {
  'DESCRIPTOR' : _STEER_STATUS__512,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Steer_status__512)
  })
_sym_db.RegisterMessage(Steer_status__512)

Turnsignal_status__513 = _reflection.GeneratedProtocolMessageType('Turnsignal_status__513', (_message.Message,), {
  'DESCRIPTOR' : _TURNSIGNAL_STATUS__513,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Turnsignal_status__513)
  })
_sym_db.RegisterMessage(Turnsignal_status__513)

Gear_status_514 = _reflection.GeneratedProtocolMessageType('Gear_status_514', (_message.Message,), {
  'DESCRIPTOR' : _GEAR_STATUS_514,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Gear_status_514)
  })
_sym_db.RegisterMessage(Gear_status_514)

Ecu_status_1_515 = _reflection.GeneratedProtocolMessageType('Ecu_status_1_515', (_message.Message,), {
  'DESCRIPTOR' : _ECU_STATUS_1_515,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Ecu_status_1_515)
  })
_sym_db.RegisterMessage(Ecu_status_1_515)

Ecu_status_2_516 = _reflection.GeneratedProtocolMessageType('Ecu_status_2_516', (_message.Message,), {
  'DESCRIPTOR' : _ECU_STATUS_2_516,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Ecu_status_2_516)
  })
_sym_db.RegisterMessage(Ecu_status_2_516)

Ecu_status_3_517 = _reflection.GeneratedProtocolMessageType('Ecu_status_3_517', (_message.Message,), {
  'DESCRIPTOR' : _ECU_STATUS_3_517,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Ecu_status_3_517)
  })
_sym_db.RegisterMessage(Ecu_status_3_517)

Ecu_status_4_518 = _reflection.GeneratedProtocolMessageType('Ecu_status_4_518', (_message.Message,), {
  'DESCRIPTOR' : _ECU_STATUS_4_518,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Ecu_status_4_518)
  })
_sym_db.RegisterMessage(Ecu_status_4_518)

Vin_resp1_51b = _reflection.GeneratedProtocolMessageType('Vin_resp1_51b', (_message.Message,), {
  'DESCRIPTOR' : _VIN_RESP1_51B,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Vin_resp1_51b)
  })
_sym_db.RegisterMessage(Vin_resp1_51b)

Vin_resp2_51c = _reflection.GeneratedProtocolMessageType('Vin_resp2_51c', (_message.Message,), {
  'DESCRIPTOR' : _VIN_RESP2_51C,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Vin_resp2_51c)
  })
_sym_db.RegisterMessage(Vin_resp2_51c)

Vin_resp3_51d = _reflection.GeneratedProtocolMessageType('Vin_resp3_51d', (_message.Message,), {
  'DESCRIPTOR' : _VIN_RESP3_51D,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Vin_resp3_51d)
  })
_sym_db.RegisterMessage(Vin_resp3_51d)

Wheelspeed_report_51e = _reflection.GeneratedProtocolMessageType('Wheelspeed_report_51e', (_message.Message,), {
  'DESCRIPTOR' : _WHEELSPEED_REPORT_51E,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Wheelspeed_report_51e)
  })
_sym_db.RegisterMessage(Wheelspeed_report_51e)

CheckResponseSignal = _reflection.GeneratedProtocolMessageType('CheckResponseSignal', (_message.Message,), {
  'DESCRIPTOR' : _CHECKRESPONSESIGNAL,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.CheckResponseSignal)
  })
_sym_db.RegisterMessage(CheckResponseSignal)

Ch = _reflection.GeneratedProtocolMessageType('Ch', (_message.Message,), {
  'DESCRIPTOR' : _CH,
  '__module__' : 'modules.canbus_vehicle.ch.proto.ch_pb2'
  # @@protoc_insertion_point(class_scope:apollo.canbus.Ch)
  })
_sym_db.RegisterMessage(Ch)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CH.fields_by_name['control_command_115']._options = None
  _CH.fields_by_name['control_command_115']._serialized_options = b'\030\001'
  _THROTTLE_COMMAND_110._serialized_start=60
  _THROTTLE_COMMAND_110._serialized_end=307
  _THROTTLE_COMMAND_110_THROTTLE_PEDAL_EN_CTRLTYPE._serialized_start=208
  _THROTTLE_COMMAND_110_THROTTLE_PEDAL_EN_CTRLTYPE._serialized_end=307
  _BRAKE_COMMAND_111._serialized_start=310
  _BRAKE_COMMAND_111._serialized_end=533
  _BRAKE_COMMAND_111_BRAKE_PEDAL_EN_CTRLTYPE._serialized_start=443
  _BRAKE_COMMAND_111_BRAKE_PEDAL_EN_CTRLTYPE._serialized_end=533
  _STEER_COMMAND_112._serialized_start=536
  _STEER_COMMAND_112._serialized_end=759
  _STEER_COMMAND_112_STEER_ANGLE_EN_CTRLTYPE._serialized_start=669
  _STEER_COMMAND_112_STEER_ANGLE_EN_CTRLTYPE._serialized_end=759
  _TURNSIGNAL_COMMAND_113._serialized_start=762
  _TURNSIGNAL_COMMAND_113._serialized_end=1158
  _TURNSIGNAL_COMMAND_113_LOW_BEAM_CMDTYPE._serialized_start=950
  _TURNSIGNAL_COMMAND_113_LOW_BEAM_CMDTYPE._serialized_end=1011
  _TURNSIGNAL_COMMAND_113_TURN_SIGNAL_CMDTYPE._serialized_start=1014
  _TURNSIGNAL_COMMAND_113_TURN_SIGNAL_CMDTYPE._serialized_end=1158
  _GEAR_COMMAND_114._serialized_start=1161
  _GEAR_COMMAND_114._serialized_end=1342
  _GEAR_COMMAND_114_GEAR_CMDTYPE._serialized_start=1245
  _GEAR_COMMAND_114_GEAR_CMDTYPE._serialized_end=1342
  _CONTROL_COMMAND_115._serialized_start=1345
  _CONTROL_COMMAND_115._serialized_end=1506
  _CONTROL_COMMAND_115_CTRL_CMDTYPE._serialized_start=1435
  _CONTROL_COMMAND_115_CTRL_CMDTYPE._serialized_end=1506
  _VEHICLE_MODE_COMMAND_116._serialized_start=1509
  _VEHICLE_MODE_COMMAND_116._serialized_end=1697
  _VEHICLE_MODE_COMMAND_116_VIN_REQ_CMDTYPE._serialized_start=1615
  _VEHICLE_MODE_COMMAND_116_VIN_REQ_CMDTYPE._serialized_end=1697
  _THROTTLE_STATUS__510._serialized_start=1700
  _THROTTLE_STATUS__510._serialized_end=2311
  _THROTTLE_STATUS__510_THROTTLE_PEDAL_EN_STSTYPE._serialized_start=2011
  _THROTTLE_STATUS__510_THROTTLE_PEDAL_EN_STSTYPE._serialized_end=2143
  _THROTTLE_STATUS__510_DRIVE_MOTOR_ERRTYPE._serialized_start=2145
  _THROTTLE_STATUS__510_DRIVE_MOTOR_ERRTYPE._serialized_end=2228
  _THROTTLE_STATUS__510_BATTERY_BMS_ERRTYPE._serialized_start=2230
  _THROTTLE_STATUS__510_BATTERY_BMS_ERRTYPE._serialized_end=2311
  _BRAKE_STATUS__511._serialized_start=2314
  _BRAKE_STATUS__511._serialized_end=3533
  _BRAKE_STATUS__511_OVERSPD_ENVTYPE._serialized_start=2903
  _BRAKE_STATUS__511_OVERSPD_ENVTYPE._serialized_end=2974
  _BRAKE_STATUS__511_BRAKE_PEDAL_EN_STSTYPE._serialized_start=2976
  _BRAKE_STATUS__511_BRAKE_PEDAL_EN_STSTYPE._serialized_end=3096
  _BRAKE_STATUS__511_BRAKE_ERRTYPE._serialized_start=3098
  _BRAKE_STATUS__511_BRAKE_ERRTYPE._serialized_end=3166
  _BRAKE_STATUS__511_EMERGENCY_BTN_ENVTYPE._serialized_start=3168
  _BRAKE_STATUS__511_EMERGENCY_BTN_ENVTYPE._serialized_end=3264
  _BRAKE_STATUS__511_FRONT_BUMP_ENVTYPE._serialized_start=3266
  _BRAKE_STATUS__511_FRONT_BUMP_ENVTYPE._serialized_end=3349
  _BRAKE_STATUS__511_BACK_BUMP_ENVTYPE._serialized_start=3351
  _BRAKE_STATUS__511_BACK_BUMP_ENVTYPE._serialized_end=3430
  _BRAKE_STATUS__511_BRAKE_LIGHT_ACTUALTYPE._serialized_start=3432
  _BRAKE_STATUS__511_BRAKE_LIGHT_ACTUALTYPE._serialized_end=3533
  _STEER_STATUS__512._serialized_start=3536
  _STEER_STATUS__512._serialized_end=4065
  _STEER_STATUS__512_STEER_ANGLE_EN_STSTYPE._serialized_start=3803
  _STEER_STATUS__512_STEER_ANGLE_EN_STSTYPE._serialized_end=3923
  _STEER_STATUS__512_STEER_ERRTYPE._serialized_start=3925
  _STEER_STATUS__512_STEER_ERRTYPE._serialized_end=3992
  _STEER_STATUS__512_SENSOR_ERRTYPE._serialized_start=3994
  _STEER_STATUS__512_SENSOR_ERRTYPE._serialized_end=4065
  _TURNSIGNAL_STATUS__513._serialized_start=4068
  _TURNSIGNAL_STATUS__513._serialized_end=4467
  _TURNSIGNAL_STATUS__513_LOW_BEAM_STSTYPE._serialized_start=4256
  _TURNSIGNAL_STATUS__513_LOW_BEAM_STSTYPE._serialized_end=4317
  _TURNSIGNAL_STATUS__513_TURN_SIGNAL_STSTYPE._serialized_start=4320
  _TURNSIGNAL_STATUS__513_TURN_SIGNAL_STSTYPE._serialized_end=4467
  _GEAR_STATUS_514._serialized_start=4470
  _GEAR_STATUS_514._serialized_end=4649
  _GEAR_STATUS_514_GEAR_STSTYPE._serialized_start=4552
  _GEAR_STATUS_514_GEAR_STSTYPE._serialized_end=4649
  _ECU_STATUS_1_515._serialized_start=4652
  _ECU_STATUS_1_515._serialized_end=6332
  _ECU_STATUS_1_515_CTRL_STSTYPE._serialized_start=5514
  _ECU_STATUS_1_515_CTRL_STSTYPE._serialized_end=5585
  _ECU_STATUS_1_515_CHASSIS_MCU_ERRTYPE._serialized_start=5587
  _ECU_STATUS_1_515_CHASSIS_MCU_ERRTYPE._serialized_end=5663
  _ECU_STATUS_1_515_CHASSIS_MCU_CANTYPE._serialized_start=5665
  _ECU_STATUS_1_515_CHASSIS_MCU_CANTYPE._serialized_end=5741
  _ECU_STATUS_1_515_CHASSIS_HW_LOSTTYPE._serialized_start=5743
  _ECU_STATUS_1_515_CHASSIS_HW_LOSTTYPE._serialized_end=5819
  _ECU_STATUS_1_515_CHASSIS_EPS_ERRTYPE._serialized_start=5821
  _ECU_STATUS_1_515_CHASSIS_EPS_ERRTYPE._serialized_end=5897
  _ECU_STATUS_1_515_CHASSIS_EPS_CANTYPE._serialized_start=5899
  _ECU_STATUS_1_515_CHASSIS_EPS_CANTYPE._serialized_end=5975
  _ECU_STATUS_1_515_CHASSIS_EHB_ERRTYPE._serialized_start=5977
  _ECU_STATUS_1_515_CHASSIS_EHB_ERRTYPE._serialized_end=6053
  _ECU_STATUS_1_515_CHASSIS_EHB_CANTYPE._serialized_start=6055
  _ECU_STATUS_1_515_CHASSIS_EHB_CANTYPE._serialized_end=6131
  _ECU_STATUS_1_515_CHASSIS_BMS_CANTYPE._serialized_start=6133
  _ECU_STATUS_1_515_CHASSIS_BMS_CANTYPE._serialized_end=6209
  _ECU_STATUS_1_515_CHASSIS_ADS_ERRTYPE._serialized_start=6211
  _ECU_STATUS_1_515_CHASSIS_ADS_ERRTYPE._serialized_end=6332
  _ECU_STATUS_2_516._serialized_start=6335
  _ECU_STATUS_2_516._serialized_end=6507
  _ECU_STATUS_3_517._serialized_start=6510
  _ECU_STATUS_3_517._serialized_end=6744
  _ECU_STATUS_4_518._serialized_start=6747
  _ECU_STATUS_4_518._serialized_end=6988
  _VIN_RESP1_51B._serialized_start=6991
  _VIN_RESP1_51B._serialized_end=7126
  _VIN_RESP2_51C._serialized_start=7129
  _VIN_RESP2_51C._serialized_end=7264
  _VIN_RESP3_51D._serialized_start=7266
  _VIN_RESP3_51D._serialized_end=7296
  _WHEELSPEED_REPORT_51E._serialized_start=7298
  _WHEELSPEED_REPORT_51E._serialized_end=7369
  _CHECKRESPONSESIGNAL._serialized_start=7372
  _CHECKRESPONSESIGNAL._serialized_end=7607
  _CH._serialized_start=7610
  _CH._serialized_end=8918
# @@protoc_insertion_point(module_scope)