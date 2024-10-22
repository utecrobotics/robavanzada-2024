#!/usr/bin/env python3
import time
import roslib
import rospy
import actionlib
from control_msgs.msg import *
from trajectory_msgs.msg import *


if __name__ == '__main__':
    
    rospy.init_node("test_gazebo", disable_signals=True)

    robot_client = actionlib.SimpleActionClient('/arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

    print("Waiting for server...")
    robot_client.wait_for_server()
    print("Connected to server")

    joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
    Q0 = [0.0, 0.0, 0.0, 0.0]

    g = FollowJointTrajectoryGoal()
    g.trajectory = JointTrajectory()
    g.trajectory.joint_names = joint_names

    # Initial position
    g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*4,time_from_start=rospy.Duration(2.0))]
    robot_client.send_goal(g)
    robot_client.wait_for_result()
    rospy.sleep(1)
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        robot_client.cancel_goal()

        # Modification of the motion
        Q0[0] = Q0[0]

        g.trajectory.points = [ JointTrajectoryPoint(positions=Q0, velocities=[0]*4, time_from_start=rospy.Duration(0.01))]
        robot_client.send_goal(g)
        robot_client.wait_for_result()

        rate.sleep()

    robot_client.cancel_goal()
