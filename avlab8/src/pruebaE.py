#!/usr/bin/env python3
import rospy
from respawnGoal import *
from environment import *
from std_msgs.msg import Float32MultiArray

EPISODES = 2

if __name__ == '__main__':

  rospy.init_node("PruebaEnv")
  
  state_size = 26
  action_size = 5
 
  env = Env(action_size)
 
  scores, episodes = [], []
  global_step = 0
  start_time = time.time()

  for e in range(1, EPISODES):
    done = False
    state = env.reset()
    score = 0

    action = 1
    next_state, reward, done = env.step(action)
    
    score += reward
    state = next_state
