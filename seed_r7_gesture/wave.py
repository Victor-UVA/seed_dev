#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import moveit_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_seed_wave')

robot = moveit_commander.RobotCommander
rarm_group = moveit_commander.MoveGroupCommander('rarm')
trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

rarm_values = rarm_group.get_current_joint_values()

# Pick arm up and put it in wave location
rarm_values[0] = -1.75
rarm_values[1] = -0.25
rarm_values[2] = -0.5
rarm_values[3] = 0

rarm_group.set_joint_value_target(rarm_values)
rarm_group.set_max_velocity_scaling_factor(0.4)

plan = rarm_group.plan()
rarm_group.go(wait=True)



# Finish
moveit_commander.roscpp_shutdown
