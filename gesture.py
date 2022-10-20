#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import move_base_msgs.msg
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_seed_bow')

robot = moveit_commander.RobotCommander
w_group = moveit_commander.MoveGroupCommander("waist")
r_group = moveit_commander.MoveGroupCommander("rarm")
l_group = moveit_commander.MoveGroupCommander("larm")
trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

rarm_values = r_group.get_current_joint_values()
larm_values = l_group.get_current_joint_values()
waist_values = w_group.get_current_joint_values()

# Set arms down
rarm_values[0] = 0
rarm_values[1] = 0
rarm_values[2] = 0
rarm_values[3] = 0
r_group.set_joint_value_target(rarm_values)

larm_values[0] = 0
larm_values[1] = 0
larm_values[2] = 0
larm_values[3] = 0
l_group.set_joint_value_target(larm_values)

plan3 = r_group.plan()
plan4 = l_group.plan()
r_group.go(wait=True)
l_group.go(wait=True)

# Bow down
waist_values[0] = 0
waist_values[1] = 0.61
waist_values[2] = 0
w_group.set_joint_value_target(waist_values)

plan2 = w_group.plan()
w_group.go(wait=True)

# Come up
waist_values[0] = 0
waist_values[1] = 0
waist_values[2] = 0
w_group.set_joint_value_target(waist_values)

plan2 = w_group.plan()
w_group.go(wait=True)

# Finish
moveit_commander.roscpp_shutdown
