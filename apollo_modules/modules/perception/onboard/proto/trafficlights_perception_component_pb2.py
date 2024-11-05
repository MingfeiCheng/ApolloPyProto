# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/onboard/proto/trafficlights_perception_component.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nImodules/perception/onboard/proto/trafficlights_perception_component.proto\x12\x19\x61pollo.perception.onboard\"\x8e\x08\n\x0cTrafficLight\x12\x1e\n\x0ftl_tf2_frame_id\x18\x01 \x01(\t:\x05world\x12<\n\x15tl_tf2_child_frame_id\x18\x02 \x01(\t:\x1dperception_localization_100hz\x12 \n\x12tf2_timeout_second\x18\x03 \x01(\x01:\x04\x30.01\x12*\n\x0c\x63\x61mera_names\x18\x04 \x01(\t:\x14\x66ront_6mm,front_12mm\x12^\n\x14\x63\x61mera_channel_names\x18\x05 \x01(\t:@/apollo/sensor/camera/front_6mm,/apollo/sensor/camera/front_12mm\x12$\n\x19tl_image_timestamp_offset\x18\x06 \x01(\x01:\x01\x30\x12 \n\x15max_process_image_fps\x18\x07 \x01(\x05:\x01\x38\x12&\n\x19query_tf_interval_seconds\x18\x08 \x01(\x01:\x03\x30.3\x12!\n\x14valid_hdmap_interval\x18\t \x01(\x01:\x03\x31.5\x12(\n\x1bimage_sys_ts_diff_threshold\x18\n \x01(\x01:\x03\x30.5\x12\"\n\x15sync_interval_seconds\x18\x0b \x01(\x01:\x03\x30.5\x12H\n(camera_traffic_light_perception_conf_dir\x18\x0c \x01(\t:\x16\x63onf/perception/camera\x12\x42\n)camera_traffic_light_perception_conf_file\x18\r \x01(\t:\x0ftrafficlight.pt\x12&\n\x19\x64\x65\x66\x61ult_image_border_size\x18\x0e \x01(\x05:\x03\x31\x30\x30\x12K\n!traffic_light_output_channel_name\x18\x0f \x01(\t: /apollo/perception/traffic_light\x12L\n\x17simulation_channel_name\x18\x10 \x01(\t:+/apollo/perception/traffic_light_simulation\x12G\n$v2x_trafficlights_input_channel_name\x18\x11 \x01(\t:\x19/apollo/v2x/traffic_light\x12&\n\x19v2x_sync_interval_seconds\x18\x12 \x01(\x01:\x03\x30.1\x12!\n\x15max_v2x_msg_buff_size\x18\x13 \x01(\x05:\x02\x35\x30\x12,\n\x14tl_preprocessor_name\x18\x14 \x01(\t:\x0eTLPreprocessor')



_TRAFFICLIGHT = DESCRIPTOR.message_types_by_name['TrafficLight']
TrafficLight = _reflection.GeneratedProtocolMessageType('TrafficLight', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICLIGHT,
  '__module__' : 'modules.perception.onboard.proto.trafficlights_perception_component_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.onboard.TrafficLight)
  })
_sym_db.RegisterMessage(TrafficLight)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRAFFICLIGHT._serialized_start=105
  _TRAFFICLIGHT._serialized_end=1143
# @@protoc_insertion_point(module_scope)
