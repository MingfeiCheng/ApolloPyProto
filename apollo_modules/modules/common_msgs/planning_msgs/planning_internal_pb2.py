# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common_msgs/planning_msgs/planning_internal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apollo_modules.modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from apollo_modules.modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from apollo_modules.modules.common_msgs.basic_msgs import pnc_point_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2
from apollo_modules.modules.common_msgs.chassis_msgs import chassis_pb2 as modules_dot_common__msgs_dot_chassis__msgs_dot_chassis__pb2
from apollo_modules.modules.common_msgs.dreamview_msgs import chart_pb2 as modules_dot_common__msgs_dot_dreamview__msgs_dot_chart__pb2
from apollo_modules.modules.common_msgs.localization_msgs import localization_pb2 as modules_dot_common__msgs_dot_localization__msgs_dot_localization__pb2
from apollo_modules.modules.common_msgs.perception_msgs import traffic_light_detection_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_traffic__light__detection__pb2
from apollo_modules.modules.common_msgs.planning_msgs import decision_pb2 as modules_dot_common__msgs_dot_planning__msgs_dot_decision__pb2
from apollo_modules.modules.common_msgs.planning_msgs import navigation_pb2 as modules_dot_common__msgs_dot_planning__msgs_dot_navigation__pb2
from apollo_modules.modules.common_msgs.planning_msgs import sl_boundary_pb2 as modules_dot_common__msgs_dot_planning__msgs_dot_sl__boundary__pb2
from apollo_modules.modules.common_msgs.routing_msgs import routing_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2
from apollo_modules.modules.common_msgs.routing_msgs import geometry_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/common_msgs/planning_msgs/planning_internal.proto\x12\x18\x61pollo.planning_internal\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a.modules/common_msgs/basic_msgs/pnc_point.proto\x1a.modules/common_msgs/chassis_msgs/chassis.proto\x1a.modules/common_msgs/dreamview_msgs/chart.proto\x1a\x38modules/common_msgs/localization_msgs/localization.proto\x1a\x41modules/common_msgs/perception_msgs/traffic_light_detection.proto\x1a\x30modules/common_msgs/planning_msgs/decision.proto\x1a\x32modules/common_msgs/planning_msgs/navigation.proto\x1a\x33modules/common_msgs/planning_msgs/sl_boundary.proto\x1a.modules/common_msgs/routing_msgs/routing.proto\x1a/modules/common_msgs/routing_msgs/geometry.proto\"F\n\x05\x44\x65\x62ug\x12=\n\rplanning_data\x18\x02 \x01(\x0b\x32&.apollo.planning_internal.PlanningData\"I\n\tSpeedPlan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x0bspeed_point\x18\x02 \x03(\x0b\x32\x19.apollo.common.SpeedPoint\"\x86\x03\n\x14StGraphBoundaryDebug\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x05point\x18\x02 \x03(\x0b\x32\x19.apollo.common.SpeedPoint\x12K\n\x04type\x18\x03 \x01(\x0e\x32=.apollo.planning_internal.StGraphBoundaryDebug.StBoundaryType\"\xe8\x01\n\x0eStBoundaryType\x12\x1c\n\x18ST_BOUNDARY_TYPE_UNKNOWN\x10\x01\x12\x19\n\x15ST_BOUNDARY_TYPE_STOP\x10\x02\x12\x1b\n\x17ST_BOUNDARY_TYPE_FOLLOW\x10\x03\x12\x1a\n\x16ST_BOUNDARY_TYPE_YIELD\x10\x04\x12\x1d\n\x19ST_BOUNDARY_TYPE_OVERTAKE\x10\x05\x12\x1f\n\x1bST_BOUNDARY_TYPE_KEEP_CLEAR\x10\x06\x12$\n ST_BOUNDARY_TYPE_DRIVABLE_REGION\x10\x07\"\x82\x03\n\x0cSLFrameDebug\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tsampled_s\x18\x02 \x03(\x01\x12#\n\x1bstatic_obstacle_lower_bound\x18\x03 \x03(\x01\x12$\n\x1c\x64ynamic_obstacle_lower_bound\x18\x04 \x03(\x01\x12#\n\x1bstatic_obstacle_upper_bound\x18\x05 \x03(\x01\x12$\n\x1c\x64ynamic_obstacle_upper_bound\x18\x06 \x03(\x01\x12\x17\n\x0fmap_lower_bound\x18\x07 \x03(\x01\x12\x17\n\x0fmap_upper_bound\x18\x08 \x03(\x01\x12\'\n\x07sl_path\x18\t \x03(\x0b\x32\x16.apollo.common.SLPoint\x12\x1d\n\x15\x61ggregated_boundary_s\x18\n \x03(\x01\x12\x1f\n\x17\x61ggregated_boundary_low\x18\x0b \x03(\x01\x12 \n\x18\x61ggregated_boundary_high\x18\x0c \x03(\x01\"\x92\x05\n\x0cSTGraphDebug\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x08\x62oundary\x18\x02 \x03(\x0b\x32..apollo.planning_internal.StGraphBoundaryDebug\x12.\n\x0bspeed_limit\x18\x03 \x03(\x0b\x32\x19.apollo.common.SpeedPoint\x12\x30\n\rspeed_profile\x18\x04 \x03(\x0b\x32\x19.apollo.common.SpeedPoint\x12W\n\x10speed_constraint\x18\x05 \x01(\x0b\x32=.apollo.planning_internal.STGraphDebug.STGraphSpeedConstraint\x12W\n\x11kernel_cruise_ref\x18\x06 \x01(\x0b\x32<.apollo.planning_internal.STGraphDebug.STGraphKernelCuiseRef\x12X\n\x11kernel_follow_ref\x18\x07 \x01(\x0b\x32=.apollo.planning_internal.STGraphDebug.STGraphKernelFollowRef\x1aM\n\x16STGraphSpeedConstraint\x12\t\n\x01t\x18\x01 \x03(\x01\x12\x13\n\x0blower_bound\x18\x02 \x03(\x01\x12\x13\n\x0bupper_bound\x18\x03 \x03(\x01\x1a\x39\n\x15STGraphKernelCuiseRef\x12\t\n\x01t\x18\x01 \x03(\x01\x12\x15\n\rcruise_line_s\x18\x02 \x03(\x01\x1a:\n\x16STGraphKernelFollowRef\x12\t\n\x01t\x18\x01 \x03(\x01\x12\x15\n\rfollow_line_s\x18\x02 \x03(\x01\"\xad\x02\n\x10SignalLightDebug\x12\x11\n\tadc_speed\x18\x01 \x01(\x01\x12\x13\n\x0b\x61\x64\x63_front_s\x18\x02 \x01(\x01\x12\x46\n\x06signal\x18\x03 \x03(\x0b\x32\x36.apollo.planning_internal.SignalLightDebug.SignalDebug\x1a\xa8\x01\n\x0bSignalDebug\x12\x10\n\x08light_id\x18\x01 \x01(\t\x12\x34\n\x05\x63olor\x18\x02 \x01(\x0e\x32%.apollo.perception.TrafficLight.Color\x12\x14\n\x0clight_stop_s\x18\x03 \x01(\x01\x12\x1d\n\x15\x61\x64\x63_stop_deceleration\x18\x04 \x01(\x01\x12\x1c\n\x14is_stop_wall_created\x18\x05 \x01(\x08\"Y\n\x0b\x44\x65\x63isionTag\x12\x13\n\x0b\x64\x65\x63ider_tag\x18\x01 \x01(\t\x12\x35\n\x08\x64\x65\x63ision\x18\x02 \x01(\x0b\x32#.apollo.planning.ObjectDecisionType\"\xc0\x01\n\rObstacleDebug\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x0bsl_boundary\x18\x02 \x01(\x0b\x32\x1b.apollo.planning.SLBoundary\x12;\n\x0c\x64\x65\x63ision_tag\x18\x03 \x03(\x0b\x32%.apollo.planning_internal.DecisionTag\x12\x19\n\x11vertices_x_coords\x18\x04 \x03(\x01\x12\x19\n\x11vertices_y_coords\x18\x05 \x03(\x01\"\xd9\x02\n\x12ReferenceLineDebug\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x0c\n\x04\x63ost\x18\x03 \x01(\x01\x12\x1b\n\x13is_change_lane_path\x18\x04 \x01(\x08\x12\x13\n\x0bis_drivable\x18\x05 \x01(\x08\x12\x14\n\x0cis_protected\x18\x06 \x01(\x08\x12\x12\n\nis_offroad\x18\x07 \x01(\x08\x12\x18\n\x10minimum_boundary\x18\x08 \x01(\x01\x12\x19\n\raverage_kappa\x18\t \x01(\x01\x42\x02\x18\x01\x12\x1a\n\x0e\x61verage_dkappa\x18\n \x01(\x01\x42\x02\x18\x01\x12\x11\n\tkappa_rms\x18\x0b \x01(\x01\x12\x12\n\ndkappa_rms\x18\x0c \x01(\x01\x12\x15\n\rkappa_max_abs\x18\r \x01(\x01\x12\x16\n\x0e\x64kappa_max_abs\x18\x0e \x01(\x01\x12\x16\n\x0e\x61verage_offset\x18\x0f \x01(\x01\"<\n\x10SampleLayerDebug\x12(\n\x08sl_point\x18\x01 \x03(\x0b\x32\x16.apollo.common.SLPoint\"\x84\x01\n\x10\x44pPolyGraphDebug\x12@\n\x0csample_layer\x18\x01 \x03(\x0b\x32*.apollo.planning_internal.SampleLayerDebug\x12.\n\x0emin_cost_point\x18\x02 \x03(\x0b\x32\x16.apollo.common.SLPoint\"\x88\x01\n\rScenarioDebug\x12\x19\n\rscenario_type\x18\x01 \x01(\x05\x42\x02\x18\x01\x12\x16\n\nstage_type\x18\x02 \x01(\x05\x42\x02\x18\x01\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\x1c\n\x14scenario_plugin_type\x18\x04 \x01(\t\x12\x19\n\x11stage_plugin_type\x18\x05 \x01(\t\"=\n\x0cTrajectories\x12-\n\ntrajectory\x18\x01 \x03(\x0b\x32\x19.apollo.common.Trajectory\"\xd5\x07\n\x0eOpenSpaceDebug\x12<\n\x0ctrajectories\x18\x01 \x01(\x0b\x32&.apollo.planning_internal.Trajectories\x12;\n\x15warm_start_trajectory\x18\x02 \x01(\x0b\x32\x1c.apollo.common.VehicleMotion\x12\x39\n\x13smoothed_trajectory\x18\x03 \x01(\x0b\x32\x1c.apollo.common.VehicleMotion\x12\x1e\n\x16warm_start_dual_lambda\x18\x04 \x03(\x01\x12\x1b\n\x13warm_start_dual_miu\x18\x05 \x03(\x01\x12\x1d\n\x15optimized_dual_lambda\x18\x06 \x03(\x01\x12\x1a\n\x12optimized_dual_miu\x18\x07 \x03(\x01\x12\x13\n\x0bxy_boundary\x18\x08 \x03(\x01\x12:\n\tobstacles\x18\t \x03(\x0b\x32\'.apollo.planning_internal.ObstacleDebug\x12\x37\n\x0froi_shift_point\x18\n \x01(\x0b\x32\x1e.apollo.common.TrajectoryPoint\x12\x31\n\tend_point\x18\x0b \x01(\x0b\x32\x1e.apollo.common.TrajectoryPoint\x12H\n\x18partitioned_trajectories\x18\x0c \x01(\x0b\x32&.apollo.planning_internal.Trajectories\x12\x41\n\x11\x63hosen_trajectory\x18\r \x01(\x0b\x32&.apollo.planning_internal.Trajectories\x12\x1e\n\x16is_fallback_trajectory\x18\x0e \x01(\x08\x12\x43\n\x13\x66\x61llback_trajectory\x18\x0f \x01(\x0b\x32&.apollo.planning_internal.Trajectories\x12\x42\n\x1atrajectory_stitching_point\x18\x10 \x01(\x0b\x32\x1e.apollo.common.TrajectoryPoint\x12>\n\x16\x66uture_collision_point\x18\x11 \x01(\x0b\x32\x1e.apollo.common.TrajectoryPoint\x12\x17\n\x0ctime_latency\x18\x12 \x01(\x01:\x01\x30\x12-\n\x0corigin_point\x18\x13 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\x1a\n\x12origin_heading_rad\x18\x14 \x01(\x01\"\xc3\x01\n\rSmootherDebug\x12\x13\n\x0bis_smoothed\x18\x01 \x01(\x08\x12Q\n\x04type\x18\x02 \x01(\x0e\x32\x34.apollo.planning_internal.SmootherDebug.SmootherType:\rSMOOTHER_NONE\x12\x0e\n\x06reason\x18\x03 \x01(\t\":\n\x0cSmootherType\x12\x11\n\rSMOOTHER_NONE\x10\x01\x12\x17\n\x13SMOOTHER_CLOSE_STOP\x10\x02\"\x9d\x01\n\rPullOverDebug\x12)\n\x08position\x18\x01 \x01(\x0b\x32\x17.apollo.common.PointENU\x12\r\n\x05theta\x18\x02 \x01(\x01\x12\x14\n\x0clength_front\x18\x03 \x01(\x01\x12\x13\n\x0blength_back\x18\x04 \x01(\x01\x12\x12\n\nwidth_left\x18\x05 \x01(\x01\x12\x13\n\x0bwidth_right\x18\x06 \x01(\x01\"\xad\n\n\x0cPlanningData\x12?\n\x0c\x61\x64\x63_position\x18\x07 \x01(\x0b\x32).apollo.localization.LocalizationEstimate\x12\'\n\x07\x63hassis\x18\x08 \x01(\x0b\x32\x16.apollo.canbus.Chassis\x12\x30\n\x07routing\x18\t \x01(\x0b\x32\x1f.apollo.routing.RoutingResponse\x12\x32\n\ninit_point\x18\n \x01(\x0b\x32\x1e.apollo.common.TrajectoryPoint\x12!\n\x04path\x18\x06 \x03(\x0b\x32\x13.apollo.common.Path\x12\x37\n\nspeed_plan\x18\r \x03(\x0b\x32#.apollo.planning_internal.SpeedPlan\x12\x38\n\x08st_graph\x18\x0e \x03(\x0b\x32&.apollo.planning_internal.STGraphDebug\x12\x38\n\x08sl_frame\x18\x0f \x03(\x0b\x32&.apollo.planning_internal.SLFrameDebug\x12\x30\n\x11prediction_header\x18\x10 \x01(\x0b\x32\x15.apollo.common.Header\x12@\n\x0csignal_light\x18\x11 \x01(\x0b\x32*.apollo.planning_internal.SignalLightDebug\x12\x39\n\x08obstacle\x18\x12 \x03(\x0b\x32\'.apollo.planning_internal.ObstacleDebug\x12\x44\n\x0ereference_line\x18\x13 \x03(\x0b\x32,.apollo.planning_internal.ReferenceLineDebug\x12\x41\n\rdp_poly_graph\x18\x14 \x01(\x0b\x32*.apollo.planning_internal.DpPolyGraphDebug\x12\x45\n\x10lattice_st_image\x18\x15 \x01(\x0b\x32+.apollo.planning_internal.LatticeStTraining\x12\x31\n\x0crelative_map\x18\x16 \x01(\x0b\x32\x1b.apollo.relative_map.MapMsg\x12S\n\x19\x61uto_tuning_training_data\x18\x17 \x01(\x0b\x32\x30.apollo.planning_internal.AutoTuningTrainingData\x12\x1c\n\x14\x66ront_clear_distance\x18\x18 \x01(\x01\x12&\n\x05\x63hart\x18\x19 \x03(\x0b\x32\x17.apollo.dreamview.Chart\x12\x39\n\x08scenario\x18\x1a \x01(\x0b\x32\'.apollo.planning_internal.ScenarioDebug\x12<\n\nopen_space\x18\x1b \x01(\x0b\x32(.apollo.planning_internal.OpenSpaceDebug\x12\x39\n\x08smoother\x18\x1c \x01(\x0b\x32\'.apollo.planning_internal.SmootherDebug\x12:\n\tpull_over\x18\x1d \x01(\x0b\x32\'.apollo.planning_internal.PullOverDebug\x12@\n\x0chybrid_model\x18\x1e \x01(\x0b\x32*.apollo.planning_internal.HybridModelDebug\"G\n\x0eLatticeStPixel\x12\t\n\x01s\x18\x01 \x01(\x05\x12\t\n\x01t\x18\x02 \x01(\x05\x12\t\n\x01r\x18\x03 \x01(\r\x12\t\n\x01g\x18\x04 \x01(\r\x12\t\n\x01\x62\x18\x05 \x01(\r\"\xc9\x01\n\x11LatticeStTraining\x12\x37\n\x05pixel\x18\x01 \x03(\x0b\x32(.apollo.planning_internal.LatticeStPixel\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x12\n\nannotation\x18\x03 \x01(\t\x12\x13\n\x0bnum_s_grids\x18\x04 \x01(\r\x12\x13\n\x0bnum_t_grids\x18\x05 \x01(\r\x12\x14\n\x0cs_resolution\x18\x06 \x01(\x01\x12\x14\n\x0ct_resolution\x18\x07 \x01(\x01\"(\n\x0e\x43ostComponents\x12\x16\n\x0e\x63ost_component\x18\x01 \x03(\x01\"\xa2\x01\n\x16\x41utoTuningTrainingData\x12\x43\n\x11teacher_component\x18\x01 \x01(\x0b\x32(.apollo.planning_internal.CostComponents\x12\x43\n\x11student_component\x18\x02 \x01(\x0b\x32(.apollo.planning_internal.CostComponents\"N\n\x19\x43loudReferenceLineRequest\x12\x31\n\x0clane_segment\x18\x01 \x03(\x0b\x32\x1b.apollo.routing.LaneSegment\"T\n CloudReferenceLineRoutingRequest\x12\x30\n\x07routing\x18\x01 \x01(\x0b\x32\x1f.apollo.routing.RoutingResponse\"B\n\x1a\x43loudReferenceLineResponse\x12$\n\x07segment\x18\x01 \x03(\x0b\x32\x13.apollo.common.Path\"\xcb\x01\n\x10HybridModelDebug\x12*\n\x1busing_learning_model_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12)\n!learning_model_output_usage_ratio\x18\x02 \x01(\x01\x12)\n!learning_model_output_fail_reason\x18\x03 \x01(\t\x12\x35\n\x18\x65valuated_path_reference\x18\x04 \x01(\x0b\x32\x13.apollo.common.Path')



_DEBUG = DESCRIPTOR.message_types_by_name['Debug']
_SPEEDPLAN = DESCRIPTOR.message_types_by_name['SpeedPlan']
_STGRAPHBOUNDARYDEBUG = DESCRIPTOR.message_types_by_name['StGraphBoundaryDebug']
_SLFRAMEDEBUG = DESCRIPTOR.message_types_by_name['SLFrameDebug']
_STGRAPHDEBUG = DESCRIPTOR.message_types_by_name['STGraphDebug']
_STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT = _STGRAPHDEBUG.nested_types_by_name['STGraphSpeedConstraint']
_STGRAPHDEBUG_STGRAPHKERNELCUISEREF = _STGRAPHDEBUG.nested_types_by_name['STGraphKernelCuiseRef']
_STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF = _STGRAPHDEBUG.nested_types_by_name['STGraphKernelFollowRef']
_SIGNALLIGHTDEBUG = DESCRIPTOR.message_types_by_name['SignalLightDebug']
_SIGNALLIGHTDEBUG_SIGNALDEBUG = _SIGNALLIGHTDEBUG.nested_types_by_name['SignalDebug']
_DECISIONTAG = DESCRIPTOR.message_types_by_name['DecisionTag']
_OBSTACLEDEBUG = DESCRIPTOR.message_types_by_name['ObstacleDebug']
_REFERENCELINEDEBUG = DESCRIPTOR.message_types_by_name['ReferenceLineDebug']
_SAMPLELAYERDEBUG = DESCRIPTOR.message_types_by_name['SampleLayerDebug']
_DPPOLYGRAPHDEBUG = DESCRIPTOR.message_types_by_name['DpPolyGraphDebug']
_SCENARIODEBUG = DESCRIPTOR.message_types_by_name['ScenarioDebug']
_TRAJECTORIES = DESCRIPTOR.message_types_by_name['Trajectories']
_OPENSPACEDEBUG = DESCRIPTOR.message_types_by_name['OpenSpaceDebug']
_SMOOTHERDEBUG = DESCRIPTOR.message_types_by_name['SmootherDebug']
_PULLOVERDEBUG = DESCRIPTOR.message_types_by_name['PullOverDebug']
_PLANNINGDATA = DESCRIPTOR.message_types_by_name['PlanningData']
_LATTICESTPIXEL = DESCRIPTOR.message_types_by_name['LatticeStPixel']
_LATTICESTTRAINING = DESCRIPTOR.message_types_by_name['LatticeStTraining']
_COSTCOMPONENTS = DESCRIPTOR.message_types_by_name['CostComponents']
_AUTOTUNINGTRAININGDATA = DESCRIPTOR.message_types_by_name['AutoTuningTrainingData']
_CLOUDREFERENCELINEREQUEST = DESCRIPTOR.message_types_by_name['CloudReferenceLineRequest']
_CLOUDREFERENCELINEROUTINGREQUEST = DESCRIPTOR.message_types_by_name['CloudReferenceLineRoutingRequest']
_CLOUDREFERENCELINERESPONSE = DESCRIPTOR.message_types_by_name['CloudReferenceLineResponse']
_HYBRIDMODELDEBUG = DESCRIPTOR.message_types_by_name['HybridModelDebug']
_STGRAPHBOUNDARYDEBUG_STBOUNDARYTYPE = _STGRAPHBOUNDARYDEBUG.enum_types_by_name['StBoundaryType']
_SMOOTHERDEBUG_SMOOTHERTYPE = _SMOOTHERDEBUG.enum_types_by_name['SmootherType']
Debug = _reflection.GeneratedProtocolMessageType('Debug', (_message.Message,), {
  'DESCRIPTOR' : _DEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.Debug)
  })
_sym_db.RegisterMessage(Debug)

SpeedPlan = _reflection.GeneratedProtocolMessageType('SpeedPlan', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDPLAN,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.SpeedPlan)
  })
_sym_db.RegisterMessage(SpeedPlan)

StGraphBoundaryDebug = _reflection.GeneratedProtocolMessageType('StGraphBoundaryDebug', (_message.Message,), {
  'DESCRIPTOR' : _STGRAPHBOUNDARYDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.StGraphBoundaryDebug)
  })
_sym_db.RegisterMessage(StGraphBoundaryDebug)

SLFrameDebug = _reflection.GeneratedProtocolMessageType('SLFrameDebug', (_message.Message,), {
  'DESCRIPTOR' : _SLFRAMEDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.SLFrameDebug)
  })
_sym_db.RegisterMessage(SLFrameDebug)

STGraphDebug = _reflection.GeneratedProtocolMessageType('STGraphDebug', (_message.Message,), {

  'STGraphSpeedConstraint' : _reflection.GeneratedProtocolMessageType('STGraphSpeedConstraint', (_message.Message,), {
    'DESCRIPTOR' : _STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT,
    '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning_internal.STGraphDebug.STGraphSpeedConstraint)
    })
  ,

  'STGraphKernelCuiseRef' : _reflection.GeneratedProtocolMessageType('STGraphKernelCuiseRef', (_message.Message,), {
    'DESCRIPTOR' : _STGRAPHDEBUG_STGRAPHKERNELCUISEREF,
    '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning_internal.STGraphDebug.STGraphKernelCuiseRef)
    })
  ,

  'STGraphKernelFollowRef' : _reflection.GeneratedProtocolMessageType('STGraphKernelFollowRef', (_message.Message,), {
    'DESCRIPTOR' : _STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF,
    '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning_internal.STGraphDebug.STGraphKernelFollowRef)
    })
  ,
  'DESCRIPTOR' : _STGRAPHDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.STGraphDebug)
  })
_sym_db.RegisterMessage(STGraphDebug)
_sym_db.RegisterMessage(STGraphDebug.STGraphSpeedConstraint)
_sym_db.RegisterMessage(STGraphDebug.STGraphKernelCuiseRef)
_sym_db.RegisterMessage(STGraphDebug.STGraphKernelFollowRef)

SignalLightDebug = _reflection.GeneratedProtocolMessageType('SignalLightDebug', (_message.Message,), {

  'SignalDebug' : _reflection.GeneratedProtocolMessageType('SignalDebug', (_message.Message,), {
    'DESCRIPTOR' : _SIGNALLIGHTDEBUG_SIGNALDEBUG,
    '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
    # @@protoc_insertion_point(class_scope:apollo.planning_internal.SignalLightDebug.SignalDebug)
    })
  ,
  'DESCRIPTOR' : _SIGNALLIGHTDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.SignalLightDebug)
  })
_sym_db.RegisterMessage(SignalLightDebug)
_sym_db.RegisterMessage(SignalLightDebug.SignalDebug)

DecisionTag = _reflection.GeneratedProtocolMessageType('DecisionTag', (_message.Message,), {
  'DESCRIPTOR' : _DECISIONTAG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.DecisionTag)
  })
_sym_db.RegisterMessage(DecisionTag)

ObstacleDebug = _reflection.GeneratedProtocolMessageType('ObstacleDebug', (_message.Message,), {
  'DESCRIPTOR' : _OBSTACLEDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.ObstacleDebug)
  })
_sym_db.RegisterMessage(ObstacleDebug)

ReferenceLineDebug = _reflection.GeneratedProtocolMessageType('ReferenceLineDebug', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCELINEDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.ReferenceLineDebug)
  })
_sym_db.RegisterMessage(ReferenceLineDebug)

SampleLayerDebug = _reflection.GeneratedProtocolMessageType('SampleLayerDebug', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLELAYERDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.SampleLayerDebug)
  })
_sym_db.RegisterMessage(SampleLayerDebug)

DpPolyGraphDebug = _reflection.GeneratedProtocolMessageType('DpPolyGraphDebug', (_message.Message,), {
  'DESCRIPTOR' : _DPPOLYGRAPHDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.DpPolyGraphDebug)
  })
_sym_db.RegisterMessage(DpPolyGraphDebug)

ScenarioDebug = _reflection.GeneratedProtocolMessageType('ScenarioDebug', (_message.Message,), {
  'DESCRIPTOR' : _SCENARIODEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.ScenarioDebug)
  })
_sym_db.RegisterMessage(ScenarioDebug)

Trajectories = _reflection.GeneratedProtocolMessageType('Trajectories', (_message.Message,), {
  'DESCRIPTOR' : _TRAJECTORIES,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.Trajectories)
  })
_sym_db.RegisterMessage(Trajectories)

OpenSpaceDebug = _reflection.GeneratedProtocolMessageType('OpenSpaceDebug', (_message.Message,), {
  'DESCRIPTOR' : _OPENSPACEDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.OpenSpaceDebug)
  })
_sym_db.RegisterMessage(OpenSpaceDebug)

SmootherDebug = _reflection.GeneratedProtocolMessageType('SmootherDebug', (_message.Message,), {
  'DESCRIPTOR' : _SMOOTHERDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.SmootherDebug)
  })
_sym_db.RegisterMessage(SmootherDebug)

PullOverDebug = _reflection.GeneratedProtocolMessageType('PullOverDebug', (_message.Message,), {
  'DESCRIPTOR' : _PULLOVERDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.PullOverDebug)
  })
_sym_db.RegisterMessage(PullOverDebug)

PlanningData = _reflection.GeneratedProtocolMessageType('PlanningData', (_message.Message,), {
  'DESCRIPTOR' : _PLANNINGDATA,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.PlanningData)
  })
_sym_db.RegisterMessage(PlanningData)

LatticeStPixel = _reflection.GeneratedProtocolMessageType('LatticeStPixel', (_message.Message,), {
  'DESCRIPTOR' : _LATTICESTPIXEL,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.LatticeStPixel)
  })
_sym_db.RegisterMessage(LatticeStPixel)

LatticeStTraining = _reflection.GeneratedProtocolMessageType('LatticeStTraining', (_message.Message,), {
  'DESCRIPTOR' : _LATTICESTTRAINING,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.LatticeStTraining)
  })
_sym_db.RegisterMessage(LatticeStTraining)

CostComponents = _reflection.GeneratedProtocolMessageType('CostComponents', (_message.Message,), {
  'DESCRIPTOR' : _COSTCOMPONENTS,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.CostComponents)
  })
_sym_db.RegisterMessage(CostComponents)

AutoTuningTrainingData = _reflection.GeneratedProtocolMessageType('AutoTuningTrainingData', (_message.Message,), {
  'DESCRIPTOR' : _AUTOTUNINGTRAININGDATA,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.AutoTuningTrainingData)
  })
_sym_db.RegisterMessage(AutoTuningTrainingData)

CloudReferenceLineRequest = _reflection.GeneratedProtocolMessageType('CloudReferenceLineRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDREFERENCELINEREQUEST,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.CloudReferenceLineRequest)
  })
_sym_db.RegisterMessage(CloudReferenceLineRequest)

CloudReferenceLineRoutingRequest = _reflection.GeneratedProtocolMessageType('CloudReferenceLineRoutingRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDREFERENCELINEROUTINGREQUEST,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.CloudReferenceLineRoutingRequest)
  })
_sym_db.RegisterMessage(CloudReferenceLineRoutingRequest)

CloudReferenceLineResponse = _reflection.GeneratedProtocolMessageType('CloudReferenceLineResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDREFERENCELINERESPONSE,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.CloudReferenceLineResponse)
  })
_sym_db.RegisterMessage(CloudReferenceLineResponse)

HybridModelDebug = _reflection.GeneratedProtocolMessageType('HybridModelDebug', (_message.Message,), {
  'DESCRIPTOR' : _HYBRIDMODELDEBUG,
  '__module__' : 'modules.common_msgs.planning_msgs.planning_internal_pb2'
  # @@protoc_insertion_point(class_scope:apollo.planning_internal.HybridModelDebug)
  })
_sym_db.RegisterMessage(HybridModelDebug)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REFERENCELINEDEBUG.fields_by_name['average_kappa']._options = None
  _REFERENCELINEDEBUG.fields_by_name['average_kappa']._serialized_options = b'\030\001'
  _REFERENCELINEDEBUG.fields_by_name['average_dkappa']._options = None
  _REFERENCELINEDEBUG.fields_by_name['average_dkappa']._serialized_options = b'\030\001'
  _SCENARIODEBUG.fields_by_name['scenario_type']._options = None
  _SCENARIODEBUG.fields_by_name['scenario_type']._serialized_options = b'\030\001'
  _SCENARIODEBUG.fields_by_name['stage_type']._options = None
  _SCENARIODEBUG.fields_by_name['stage_type']._serialized_options = b'\030\001'
  _DEBUG._serialized_start=700
  _DEBUG._serialized_end=770
  _SPEEDPLAN._serialized_start=772
  _SPEEDPLAN._serialized_end=845
  _STGRAPHBOUNDARYDEBUG._serialized_start=848
  _STGRAPHBOUNDARYDEBUG._serialized_end=1238
  _STGRAPHBOUNDARYDEBUG_STBOUNDARYTYPE._serialized_start=1006
  _STGRAPHBOUNDARYDEBUG_STBOUNDARYTYPE._serialized_end=1238
  _SLFRAMEDEBUG._serialized_start=1241
  _SLFRAMEDEBUG._serialized_end=1627
  _STGRAPHDEBUG._serialized_start=1630
  _STGRAPHDEBUG._serialized_end=2288
  _STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT._serialized_start=2092
  _STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT._serialized_end=2169
  _STGRAPHDEBUG_STGRAPHKERNELCUISEREF._serialized_start=2171
  _STGRAPHDEBUG_STGRAPHKERNELCUISEREF._serialized_end=2228
  _STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF._serialized_start=2230
  _STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF._serialized_end=2288
  _SIGNALLIGHTDEBUG._serialized_start=2291
  _SIGNALLIGHTDEBUG._serialized_end=2592
  _SIGNALLIGHTDEBUG_SIGNALDEBUG._serialized_start=2424
  _SIGNALLIGHTDEBUG_SIGNALDEBUG._serialized_end=2592
  _DECISIONTAG._serialized_start=2594
  _DECISIONTAG._serialized_end=2683
  _OBSTACLEDEBUG._serialized_start=2686
  _OBSTACLEDEBUG._serialized_end=2878
  _REFERENCELINEDEBUG._serialized_start=2881
  _REFERENCELINEDEBUG._serialized_end=3226
  _SAMPLELAYERDEBUG._serialized_start=3228
  _SAMPLELAYERDEBUG._serialized_end=3288
  _DPPOLYGRAPHDEBUG._serialized_start=3291
  _DPPOLYGRAPHDEBUG._serialized_end=3423
  _SCENARIODEBUG._serialized_start=3426
  _SCENARIODEBUG._serialized_end=3562
  _TRAJECTORIES._serialized_start=3564
  _TRAJECTORIES._serialized_end=3625
  _OPENSPACEDEBUG._serialized_start=3628
  _OPENSPACEDEBUG._serialized_end=4609
  _SMOOTHERDEBUG._serialized_start=4612
  _SMOOTHERDEBUG._serialized_end=4807
  _SMOOTHERDEBUG_SMOOTHERTYPE._serialized_start=4749
  _SMOOTHERDEBUG_SMOOTHERTYPE._serialized_end=4807
  _PULLOVERDEBUG._serialized_start=4810
  _PULLOVERDEBUG._serialized_end=4967
  _PLANNINGDATA._serialized_start=4970
  _PLANNINGDATA._serialized_end=6295
  _LATTICESTPIXEL._serialized_start=6297
  _LATTICESTPIXEL._serialized_end=6368
  _LATTICESTTRAINING._serialized_start=6371
  _LATTICESTTRAINING._serialized_end=6572
  _COSTCOMPONENTS._serialized_start=6574
  _COSTCOMPONENTS._serialized_end=6614
  _AUTOTUNINGTRAININGDATA._serialized_start=6617
  _AUTOTUNINGTRAININGDATA._serialized_end=6779
  _CLOUDREFERENCELINEREQUEST._serialized_start=6781
  _CLOUDREFERENCELINEREQUEST._serialized_end=6859
  _CLOUDREFERENCELINEROUTINGREQUEST._serialized_start=6861
  _CLOUDREFERENCELINEROUTINGREQUEST._serialized_end=6945
  _CLOUDREFERENCELINERESPONSE._serialized_start=6947
  _CLOUDREFERENCELINERESPONSE._serialized_end=7013
  _HYBRIDMODELDEBUG._serialized_start=7016
  _HYBRIDMODELDEBUG._serialized_end=7219
# @@protoc_insertion_point(module_scope)
