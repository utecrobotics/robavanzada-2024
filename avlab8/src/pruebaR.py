#!/usr/bin/env python3
import rospy
from respawnGoal import *
from environment import *
from std_msgs.msg import Float32MultiArray

EPISODES = 2

if __name__ == '__main__':

  rospy.init_node("PruebaRespawn")
  
  res = Respawn()
  
