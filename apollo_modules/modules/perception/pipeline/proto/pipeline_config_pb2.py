# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/perception/pipeline/proto/pipeline_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.perception.pipeline.proto import camera_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_camera__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto import lane_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_lane__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto import lidar_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_lidar__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto import traffic_light_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_traffic__light__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import all_latest_fusion_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_all__latest__fusion__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import bev_obstacle_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_bev__obstacle__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import caddn_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_caddn__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import camera_detector_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_camera__detector__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import camera_detection_postprocessor_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_camera__detection__postprocessor__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import camera_detection_preprocessor_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_camera__detection__preprocessor__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import center_point_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_center__point__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import cnnseg_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_cnnseg__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import darkSCNN_postprocessor_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_darkSCNN__postprocessor__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import darkSCNN_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_darkSCNN__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import denseline_postprocessor_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_denseline__postprocessor__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import denseline_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_denseline__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import detection_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_detection__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import fused_classifier_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_fused__classifier__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import ground_service_detector_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_ground__service__detector__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import hdmap_roi_filter_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_hdmap__roi__filter__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import location_refiner_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_location__refiner__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import map_manager_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_map__manager__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import mask_pillars_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_mask__pillars__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import mlf_engine_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_mlf__engine__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import multicue_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_multicue__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import ncut_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_ncut__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import object_builder_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_object__builder__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import object_filter_bank_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_object__filter__bank__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import omt_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_omt__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import omt_bev_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_omt__bev__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import pbf_tracker_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_pbf__tracker__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import point_pillars_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_point__pillars__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import pointcloud_detection_postprocessor_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_pointcloud__detection__postprocessor__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import pointcloud_detection_preprocessor_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_pointcloud__detection__preprocessor__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import pointcloud_preprocessor_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_pointcloud__preprocessor__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import probabilistic_fusion_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_probabilistic__fusion__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import recognition_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_recognition__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import semantic_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_semantic__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import singlestage_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_singlestage__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import smoke_obstacle_detection_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_smoke__obstacle__detection__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import spatio_temporal_ground_detector_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_spatio__temporal__ground__detector__config__pb2
from apollo_modules.modules.perception.pipeline.proto.stage import yolo_obstacle_detector_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_stage_dot_yolo__obstacle__detector__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import camera_get_object_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_camera__get__object__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import ccrf_type_fusion_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_ccrf__type__fusion__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import filter_bbox_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_filter__bbox__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import get_image_data_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_get__image__data__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import multi_lidar_fusion_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_multi__lidar__fusion__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import pbf_gatekeeper_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_pbf__gatekeeper__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import pointcloud_downsample_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_pointcloud__downsample__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import pointcloud_get_objects_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_pointcloud__get__objects__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import recover_bbox_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_recover__bbox__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import resize_and_normalize_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_resize__and__normalize__config__pb2
from apollo_modules.modules.perception.pipeline.proto.plugin import roi_boundary_filter_config_pb2 as modules_dot_perception_dot_pipeline_dot_proto_dot_plugin_dot_roi__boundary__filter__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7modules/perception/pipeline/proto/pipeline_config.proto\x12\x1a\x61pollo.perception.pipeline\x1a?modules/perception/pipeline/proto/camera_detection_config.proto\x1a=modules/perception/pipeline/proto/lane_detection_config.proto\x1a>modules/perception/pipeline/proto/lidar_detection_config.proto\x1a<modules/perception/pipeline/proto/traffic_light_config.proto\x1a\x46modules/perception/pipeline/proto/stage/all_latest_fusion_config.proto\x1aKmodules/perception/pipeline/proto/stage/bev_obstacle_detection_config.proto\x1a\x44modules/perception/pipeline/proto/stage/caddn_detection_config.proto\x1a\x44modules/perception/pipeline/proto/stage/camera_detector_config.proto\x1aSmodules/perception/pipeline/proto/stage/camera_detection_postprocessor_config.proto\x1aRmodules/perception/pipeline/proto/stage/camera_detection_preprocessor_config.proto\x1aKmodules/perception/pipeline/proto/stage/center_point_detection_config.proto\x1a;modules/perception/pipeline/proto/stage/cnnseg_config.proto\x1a\x44modules/perception/pipeline/proto/stage/darkSCNN_postprocessor.proto\x1a\x36modules/perception/pipeline/proto/stage/darkSCNN.proto\x1a\x45modules/perception/pipeline/proto/stage/denseline_postprocessor.proto\x1a\x37modules/perception/pipeline/proto/stage/denseline.proto\x1a\x37modules/perception/pipeline/proto/stage/detection.proto\x1a\x45modules/perception/pipeline/proto/stage/fused_classifier_config.proto\x1aLmodules/perception/pipeline/proto/stage/ground_service_detector_config.proto\x1a\x45modules/perception/pipeline/proto/stage/hdmap_roi_filter_config.proto\x1a>modules/perception/pipeline/proto/stage/location_refiner.proto\x1a@modules/perception/pipeline/proto/stage/map_manager_config.proto\x1aKmodules/perception/pipeline/proto/stage/mask_pillars_detection_config.proto\x1a?modules/perception/pipeline/proto/stage/mlf_engine_config.proto\x1a\x36modules/perception/pipeline/proto/stage/multicue.proto\x1a\x39modules/perception/pipeline/proto/stage/ncut_config.proto\x1a\x43modules/perception/pipeline/proto/stage/object_builder_config.proto\x1aGmodules/perception/pipeline/proto/stage/object_filter_bank_config.proto\x1a\x31modules/perception/pipeline/proto/stage/omt.proto\x1a\x35modules/perception/pipeline/proto/stage/omt_bev.proto\x1a@modules/perception/pipeline/proto/stage/pbf_tracker_config.proto\x1aLmodules/perception/pipeline/proto/stage/point_pillars_detection_config.proto\x1aWmodules/perception/pipeline/proto/stage/pointcloud_detection_postprocessor_config.proto\x1aVmodules/perception/pipeline/proto/stage/pointcloud_detection_preprocessor_config.proto\x1aLmodules/perception/pipeline/proto/stage/pointcloud_preprocessor_config.proto\x1aImodules/perception/pipeline/proto/stage/probabilistic_fusion_config.proto\x1a\x39modules/perception/pipeline/proto/stage/recognition.proto\x1a\x36modules/perception/pipeline/proto/stage/semantic.proto\x1a\x39modules/perception/pipeline/proto/stage/singlestage.proto\x1aMmodules/perception/pipeline/proto/stage/smoke_obstacle_detection_config.proto\x1aTmodules/perception/pipeline/proto/stage/spatio_temporal_ground_detector_config.proto\x1aKmodules/perception/pipeline/proto/stage/yolo_obstacle_detector_config.proto\x1aGmodules/perception/pipeline/proto/plugin/camera_get_object_config.proto\x1a\x46modules/perception/pipeline/proto/plugin/ccrf_type_fusion_config.proto\x1a\x41modules/perception/pipeline/proto/plugin/filter_bbox_config.proto\x1a\x44modules/perception/pipeline/proto/plugin/get_image_data_config.proto\x1aHmodules/perception/pipeline/proto/plugin/multi_lidar_fusion_config.proto\x1a\x44modules/perception/pipeline/proto/plugin/pbf_gatekeeper_config.proto\x1aKmodules/perception/pipeline/proto/plugin/pointcloud_downsample_config.proto\x1aLmodules/perception/pipeline/proto/plugin/pointcloud_get_objects_config.proto\x1a\x42modules/perception/pipeline/proto/plugin/recover_bbox_config.proto\x1aJmodules/perception/pipeline/proto/plugin/resize_and_normalize_config.proto\x1aImodules/perception/pipeline/proto/plugin/roi_boundary_filter_config.proto\"\xed\x08\n\x0cPluginConfig\x12;\n\x0bplugin_type\x18\x01 \x01(\x0e\x32&.apollo.perception.pipeline.PluginType\x12\x15\n\x07\x65nabled\x18\x02 \x01(\x08:\x04true\x12S\n\x18\x63\x61mera_get_object_config\x18\n \x01(\x0b\x32/.apollo.perception.camera.CameraGetObjectConfigH\x00\x12H\n\x12\x66ilter_bbox_config\x18\x0b \x01(\x0b\x32*.apollo.perception.camera.FilterBboxConfigH\x00\x12M\n\x15get_image_data_config\x18\x0c \x01(\x0b\x32,.apollo.perception.camera.GetImageDataConfigH\x00\x12J\n\x13recover_bbox_config\x18\r \x01(\x0b\x32+.apollo.perception.camera.RecoverBboxConfigH\x00\x12Y\n\x1bresize_and_normalize_config\x18\x0e \x01(\x0b\x32\x32.apollo.perception.camera.ResizeAndNormalizeConfigH\x00\x12[\n\x1cpointcloud_downsample_config\x18\x0f \x01(\x0b\x32\x33.apollo.perception.lidar.PointcloudDownSampleConfigH\x00\x12\\\n\x1dpointcloud_get_objects_config\x18\x10 \x01(\x0b\x32\x33.apollo.perception.lidar.PointcloudGetObjectsConfigH\x00\x12V\n\x1aroi_boundary_filter_config\x18\x11 \x01(\x0b\x32\x30.apollo.perception.lidar.ROIBoundaryFilterConfigH\x00\x12_\n\x1fmlf_track_object_matcher_config\x18\x12 \x01(\x0b\x32\x34.apollo.perception.lidar.MlfTrackObjectMatcherConfigH\x00\x12G\n\x12mlf_tracker_config\x18\x13 \x01(\x0b\x32).apollo.perception.lidar.MlfTrackerConfigH\x00\x12P\n\x17\x63\x63rf_type_fusion_config\x18\x14 \x01(\x0b\x32-.apollo.perception.lidar.CcrfTypeFusionConfigH\x00\x12N\n\x15pbf_gatekeeper_config\x18\x15 \x01(\x0b\x32-.apollo.perception.fusion.PbfGatekeeperConfigH\x00\x42\x0f\n\rplugin_configJ\x04\x08\x03\x10\n\"\xa4\x1b\n\x0bStageConfig\x12\x39\n\nstage_type\x18\x01 \x01(\x0e\x32%.apollo.perception.pipeline.StageType\x12\x15\n\x07\x65nabled\x18\x02 \x01(\x08:\x04true\x12?\n\rplugin_config\x18\x03 \x03(\x0b\x32(.apollo.perception.pipeline.PluginConfig\x12\x0c\n\x04type\x18\x04 \x01(\t\x12r\n(pointcloud_detection_preprocessor_config\x18\n \x01(\x0b\x32>.apollo.perception.lidar.PointcloudDetectionPreprocessorConfigH\x00\x12t\n)pointcloud_detection_postprocessor_config\x18\x0b \x01(\x0b\x32?.apollo.perception.lidar.PointcloudDetectionPostprocessorConfigH\x00\x12_\n\x1epointcloud_preprocessor_config\x18\x0c \x01(\x0b\x32\x35.apollo.perception.lidar.PointcloudPreprocessorConfigH\x00\x12G\n\x12map_manager_config\x18\r \x01(\x0b\x32).apollo.perception.lidar.MapManagerConfigH\x00\x12T\n\x19object_filter_bank_config\x18\x0e \x01(\x0b\x32/.apollo.perception.lidar.ObjectFilterBankConfigH\x00\x12\x45\n\x11mlf_engine_config\x18\x10 \x01(\x0b\x32(.apollo.perception.lidar.MlfEngineConfigH\x00\x12Q\n\x17\x66used_classifier_config\x18\x11 \x01(\x0b\x32..apollo.perception.lidar.FusedClassifierConfigH\x00\x12>\n\rcnnseg_config\x18\x12 \x01(\x0b\x32%.apollo.perception.lidar.CNNSegConfigH\x00\x12:\n\x0bncut_config\x18\x13 \x01(\x0b\x32#.apollo.perception.lidar.NCutConfigH\x00\x12^\n\x1eground_service_detector_config\x18\x14 \x01(\x0b\x32\x34.apollo.perception.lidar.GroundServiceDetectorConfigH\x00\x12m\n&spatio_temporal_ground_detector_config\x18\x15 \x01(\x0b\x32;.apollo.perception.lidar.SpatioTemporalGroundDetectorConfigH\x00\x12P\n\x17hdmap_roi_filter_config\x18\x16 \x01(\x0b\x32-.apollo.perception.lidar.HDMapRoiFilterConfigH\x00\x12^\n\x1epoint_pillars_detection_config\x18\x17 \x01(\x0b\x32\x34.apollo.perception.lidar.PointPillarsDetectionConfigH\x00\x12M\n\x15object_builder_config\x18\x18 \x01(\x0b\x32,.apollo.perception.lidar.ObjectBuilderConfigH\x00\x12\\\n\x1d\x63\x65nter_point_detection_config\x18\x19 \x01(\x0b\x32\x33.apollo.perception.lidar.CenterPointDetectionConfigH\x00\x12\\\n\x1dmask_pillars_detection_config\x18\x1a \x01(\x0b\x32\x33.apollo.perception.lidar.MaskPillarsDetectionConfigH\x00\x12_\n\x1etraffic_light_detection_config\x18\x32 \x01(\x0b\x32\x35.apollo.perception.camera.TrafficLightDetectionConfigH\x00\x12\x63\n traffic_light_recognition_config\x18\x33 \x01(\x0b\x32\x37.apollo.perception.camera.TrafficLightRecognitionConfigH\x00\x12R\n\x17semantic_reviser_config\x18\x34 \x01(\x0b\x32/.apollo.perception.camera.SemanticReviserConfigH\x00\x12]\n\x1dyolo_obstacle_detector_config\x18\x35 \x01(\x0b\x32\x34.apollo.perception.camera.YoloObstacleDetectorConfigH\x00\x12\x61\n\x16location_refiner_param\x18\x36 \x01(\x0b\x32?.apollo.perception.camera.location_refiner.LocationRefinerParamH\x00\x12;\n\tomt_param\x18\x37 \x01(\x0b\x32&.apollo.perception.camera.omt.OmtParamH\x00\x12\x42\n\romt_bev_param\x18\x38 \x01(\x0b\x32).apollo.perception.camera.omtbev.OmtParamH\x00\x12J\n\x0emulticue_param\x18\x39 \x01(\x0b\x32\x30.apollo.perception.camera.multicue.MulticueParamH\x00\x12S\n\x11singlestage_param\x18: \x01(\x0b\x32\x36.apollo.perception.camera.singlestage.SinglestageParamH\x00\x12K\n\x0f\x64\x61rk_scnn_param\x18; \x01(\x0b\x32\x30.apollo.perception.camera.darkSCNN.DarkSCNNParamH\x00\x12M\n\x0f\x64\x65nseline_param\x18< \x01(\x0b\x32\x32.apollo.perception.camera.denseline.DenselineParamH\x00\x12j\n!darkscnn_lane_postprocessor_param\x18= \x01(\x0b\x32=.apollo.perception.camera.lane.DarkSCNNLanePostprocessorParamH\x00\x12Y\n\x18lane_postprocessor_param\x18> \x01(\x0b\x32\x35.apollo.perception.camera.lane.LanePostprocessorParamH\x00\x12\x61\n\x1fsmoke_obstacle_detection_config\x18? \x01(\x0b\x32\x36.apollo.perception.camera.SmokeObstacleDetectionConfigH\x00\x12m\n%camera_detection_postprocessor_config\x18@ \x01(\x0b\x32<.apollo.perception.camera.CameraDetectionPostprocessorConfigH\x00\x12k\n$camera_detection_preprocessor_config\x18\x41 \x01(\x0b\x32;.apollo.perception.camera.CameraDetectionPreprocessorConfigH\x00\x12]\n\x1d\x62\x65v_obstacle_detection_config\x18\x42 \x01(\x0b\x32\x34.apollo.perception.camera.BEVObstacleDetectionConfigH\x00\x12P\n\x16\x63\x61mera_detector_config\x18\x43 \x01(\x0b\x32..apollo.perception.camera.CameraDetectorConfigH\x00\x12P\n\x16\x63\x61\x64\x64n_detection_config\x18\x44 \x01(\x0b\x32..apollo.perception.camera.CaddnDetectionConfigH\x00\x12S\n\x18\x61ll_latest_fusion_config\x18\x64 \x01(\x0b\x32/.apollo.perception.fusion.AllLatestFusionConfigH\x00\x12Z\n\x1bprobabilistic_fusion_config\x18\x65 \x01(\x0b\x32\x33.apollo.perception.fusion.ProbabilisticFusionConfigH\x00\x42\x0e\n\x0cstage_configJ\x04\x08\x05\x10\n\"\xb0\x04\n\x0ePipelineConfig\x12?\n\rpipeline_type\x18\x01 \x01(\x0e\x32(.apollo.perception.pipeline.PipelineType\x12\x39\n\nstage_type\x18\x02 \x03(\x0e\x32%.apollo.perception.pipeline.StageType\x12=\n\x0cstage_config\x18\x03 \x03(\x0b\x32\'.apollo.perception.pipeline.StageConfig\x12T\n\x17\x63\x61mera_detection_config\x18\n \x01(\x0b\x32\x31.apollo.perception.pipeline.CameraDetectionConfigH\x00\x12R\n\x16lidar_detection_config\x18\x0b \x01(\x0b\x32\x30.apollo.perception.pipeline.LidarDetectionConfigH\x00\x12N\n\x14traffic_light_config\x18\x0c \x01(\x0b\x32..apollo.perception.pipeline.TrafficLightConfigH\x00\x12P\n\x15lane_detection_config\x18\r \x01(\x0b\x32/.apollo.perception.pipeline.LaneDetectionConfigH\x00\x42\x11\n\x0fpipeline_configJ\x04\x08\x04\x10\n*\xe1\x02\n\nPluginType\x12\x15\n\x11\x43\x41MERA_GET_OBJECT\x10\x01\x12\x1a\n\x16POINTCLOUD_DOWN_SAMPLE\x10\x02\x12\x19\n\x15RESIZIE_AND_NORMALIZE\x10\x03\x12\x1a\n\x16POINTCLOUD_GET_OBJECTS\x10\x04\x12\x12\n\x0eGET_IMAGE_DATA\x10\x05\x12\x17\n\x13ROI_BOUNDARY_FILTER\x10\x06\x12\x0f\n\x0b\x46ILTER_BBOX\x10\x07\x12\x10\n\x0cRECOVER_BBOX\x10\x08\x12\x1c\n\x18MLF_TRACK_OBJECT_MATCHER\x10\t\x12\x0f\n\x0bMLF_TRACKER\x10\n\x12\x1c\n\x18\x43\x43RF_ONESHOT_TYPE_FUSION\x10\x0b\x12\x1d\n\x19\x43\x43RF_SEQUENCE_TYPE_FUSION\x10\x0c\x12\x12\n\x0ePBF_GATEKEEPER\x10\r\x12\x19\n\x15POINTCLOUD_DOWNSAMPLE\x10\x0e*\xab\t\n\tStageType\x12!\n\x1d\x43\x41MERA_DETECTION_PREPROCESSOR\x10\x01\x12\x13\n\x0fTL_PREPROCESSOR\x10\x02\x12\x1b\n\x17POINTCLOUD_PREPROCESSOR\x10\x03\x12%\n!POINTCLOUD_DETECTION_PREPROCESSOR\x10\x04\x12\x1a\n\x16\x43ONTI_ARS_PREPROCESSOR\x10\x05\x12\x0f\n\x0bMAP_MANAGER\x10\x06\x12\x15\n\x11\x41LL_LATEST_FUSION\x10\x07\x12\x19\n\x15\x42\x45V_OBSTACLE_DETECTOR\x10\x14\x12\x1c\n\x18SMOKE_OBSTACLE_DETECTION\x10\x15\x12\x1a\n\x16YOLO_OBSTACLE_DETECTOR\x10\x16\x12\x1c\n\x18YOLOV4_OBSTACLE_DETECTOR\x10\x17\x12\x13\n\x0f\x43\x41\x44\x44N_DETECTION\x10\x18\x12\x1a\n\x16\x44\x41RKSCNN_LANE_DETECTOR\x10\x19\x12\x1b\n\x17\x44\x45NSELINE_LANE_DETECTOR\x10\x1a\x12\x1b\n\x17TRAFFIC_LIGHT_DETECTION\x10\x1b\x12\x1d\n\x19TRAFFIC_LIGHT_RECOGNITION\x10\x1c\x12\x14\n\x10\x43NN_SEGMENTATION\x10\x1d\x12\x1a\n\x16MASK_PILLARS_DETECTION\x10\x1e\x12\x15\n\x11NCUT_SEGMENTATION\x10\x1f\x12\x1b\n\x17POINT_PILLARS_DETECTION\x10 \x12\x1a\n\x16\x43\x45NTER_POINT_DETECTION\x10!\x12\x16\n\x12\x43ONTI_ARS_DETECTOR\x10\"\x12\x16\n\x12OBJ_POST_PROCESSOR\x10\x64\x12+\n\'LOCATION_REFINER_OBSTACLE_POSTPROCESSOR\x10\x65\x12\"\n\x1e\x43\x41MERA_DETECTION_POSTPROCESSOR\x10\x66\x12\x1f\n\x1b\x44\x41RKSCNN_LANE_POSTPROCESSOR\x10g\x12 \n\x1c\x44\x45NSELINE_LANE_POSTPROCESSOR\x10h\x12&\n\"POINTCLOUD_DETECTION_POSTPROCESSOR\x10i\x12\x12\n\x0eOBJECT_BUILDER\x10j\x12\x16\n\x12OBJECT_FILTER_BANK\x10k\x12\x1c\n\x18OMT_BEV_OBSTACLE_TRACKER\x10w\x12\x18\n\x14OMT_OBSTACLE_TRACKER\x10x\x12\x14\n\x10SEMANTIC_REVISER\x10y\x12\x15\n\x11\x43ONTI_ARS_TRACKER\x10{\x12\x0f\n\x0bPBF_TRACKER\x10|\x12\x0e\n\nMLF_ENGINE\x10}\x12\x14\n\x10\x46USED_CLASSIFIER\x10~\x12\x1a\n\x16HDMAP_RADAR_ROI_FILTER\x10\x7f\x12\x13\n\x0eHM_ASSOCIATION\x10\x80\x01\x12\x1f\n\x1a\x45XTERNAL_FEATURE_EXTRACTOR\x10\x82\x01\x12#\n\x1eMULTI_CUE_OBSTACLE_TRANSFORMER\x10\x83\x01\x12\x19\n\x14PROBABILISTIC_FUSION\x10\x84\x01\x12\x19\n\x14\x43OLLECT_FUSED_OBJECT\x10\x85\x01*#\n\x0cPipelineType\x12\x13\n\x0fLIDAR_DETECTION\x10\x01')

_PLUGINTYPE = DESCRIPTOR.enum_types_by_name['PluginType']
PluginType = enum_type_wrapper.EnumTypeWrapper(_PLUGINTYPE)
_STAGETYPE = DESCRIPTOR.enum_types_by_name['StageType']
StageType = enum_type_wrapper.EnumTypeWrapper(_STAGETYPE)
_PIPELINETYPE = DESCRIPTOR.enum_types_by_name['PipelineType']
PipelineType = enum_type_wrapper.EnumTypeWrapper(_PIPELINETYPE)
CAMERA_GET_OBJECT = 1
POINTCLOUD_DOWN_SAMPLE = 2
RESIZIE_AND_NORMALIZE = 3
POINTCLOUD_GET_OBJECTS = 4
GET_IMAGE_DATA = 5
ROI_BOUNDARY_FILTER = 6
FILTER_BBOX = 7
RECOVER_BBOX = 8
MLF_TRACK_OBJECT_MATCHER = 9
MLF_TRACKER = 10
CCRF_ONESHOT_TYPE_FUSION = 11
CCRF_SEQUENCE_TYPE_FUSION = 12
PBF_GATEKEEPER = 13
POINTCLOUD_DOWNSAMPLE = 14
CAMERA_DETECTION_PREPROCESSOR = 1
TL_PREPROCESSOR = 2
POINTCLOUD_PREPROCESSOR = 3
POINTCLOUD_DETECTION_PREPROCESSOR = 4
CONTI_ARS_PREPROCESSOR = 5
MAP_MANAGER = 6
ALL_LATEST_FUSION = 7
BEV_OBSTACLE_DETECTOR = 20
SMOKE_OBSTACLE_DETECTION = 21
YOLO_OBSTACLE_DETECTOR = 22
YOLOV4_OBSTACLE_DETECTOR = 23
CADDN_DETECTION = 24
DARKSCNN_LANE_DETECTOR = 25
DENSELINE_LANE_DETECTOR = 26
TRAFFIC_LIGHT_DETECTION = 27
TRAFFIC_LIGHT_RECOGNITION = 28
CNN_SEGMENTATION = 29
MASK_PILLARS_DETECTION = 30
NCUT_SEGMENTATION = 31
POINT_PILLARS_DETECTION = 32
CENTER_POINT_DETECTION = 33
CONTI_ARS_DETECTOR = 34
OBJ_POST_PROCESSOR = 100
LOCATION_REFINER_OBSTACLE_POSTPROCESSOR = 101
CAMERA_DETECTION_POSTPROCESSOR = 102
DARKSCNN_LANE_POSTPROCESSOR = 103
DENSELINE_LANE_POSTPROCESSOR = 104
POINTCLOUD_DETECTION_POSTPROCESSOR = 105
OBJECT_BUILDER = 106
OBJECT_FILTER_BANK = 107
OMT_BEV_OBSTACLE_TRACKER = 119
OMT_OBSTACLE_TRACKER = 120
SEMANTIC_REVISER = 121
CONTI_ARS_TRACKER = 123
PBF_TRACKER = 124
MLF_ENGINE = 125
FUSED_CLASSIFIER = 126
HDMAP_RADAR_ROI_FILTER = 127
HM_ASSOCIATION = 128
EXTERNAL_FEATURE_EXTRACTOR = 130
MULTI_CUE_OBSTACLE_TRANSFORMER = 131
PROBABILISTIC_FUSION = 132
COLLECT_FUSED_OBJECT = 133
LIDAR_DETECTION = 1


_PLUGINCONFIG = DESCRIPTOR.message_types_by_name['PluginConfig']
_STAGECONFIG = DESCRIPTOR.message_types_by_name['StageConfig']
_PIPELINECONFIG = DESCRIPTOR.message_types_by_name['PipelineConfig']
PluginConfig = _reflection.GeneratedProtocolMessageType('PluginConfig', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINCONFIG,
  '__module__' : 'modules.perception.pipeline.proto.pipeline_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.pipeline.PluginConfig)
  })
_sym_db.RegisterMessage(PluginConfig)

StageConfig = _reflection.GeneratedProtocolMessageType('StageConfig', (_message.Message,), {
  'DESCRIPTOR' : _STAGECONFIG,
  '__module__' : 'modules.perception.pipeline.proto.pipeline_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.pipeline.StageConfig)
  })
_sym_db.RegisterMessage(StageConfig)

PipelineConfig = _reflection.GeneratedProtocolMessageType('PipelineConfig', (_message.Message,), {
  'DESCRIPTOR' : _PIPELINECONFIG,
  '__module__' : 'modules.perception.pipeline.proto.pipeline_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.perception.pipeline.PipelineConfig)
  })
_sym_db.RegisterMessage(PipelineConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLUGINTYPE._serialized_start=8988
  _PLUGINTYPE._serialized_end=9341
  _STAGETYPE._serialized_start=9344
  _STAGETYPE._serialized_end=10539
  _PIPELINETYPE._serialized_start=10541
  _PIPELINETYPE._serialized_end=10576
  _PLUGINCONFIG._serialized_start=3794
  _PLUGINCONFIG._serialized_end=4927
  _STAGECONFIG._serialized_start=4930
  _STAGECONFIG._serialized_end=8422
  _PIPELINECONFIG._serialized_start=8425
  _PIPELINECONFIG._serialized_end=8985
# @@protoc_insertion_point(module_scope)
