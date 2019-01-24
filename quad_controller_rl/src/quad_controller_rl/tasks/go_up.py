import numpy as np
from gym import spaces
from geometry_msgs.msg import Vector3, Point, Quaternion, Pose, Twist, Wrench
from quad_controller_rl.tasks.base_task import BaseTask


class GoUp(BaseTask):
    def __init__(self):
        self.max_duration = 5
        print("****1")

