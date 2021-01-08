import math
import matplotlib.pyplot as plt
import numpy

class MecanumDrive():

    def __init__(self, wheel_width, wheel_length, dt):
        """wheel_width: distance between left and right wheels
            wheel_length: distance between front and back wheels"""
        self(wheel_width, wheel_length, 0, 0, dt)

    def __init__(self, wheel_width, wheel_length, starting_x, starting_y, dt):
        """wheel_width: distance between left and right wheels
            wheel_length: distance between front and back wheels"""
        self.wheel_width = wheel_width
        self.wheel_length = wheel_length
        self.x = starting_x
        self.y = starting_y
        self.front_left_pos = 0
        self.front_right_pos = 0
        self.back_left_pos = 0
        self.back_right_pos = 0

        self.front_left_vel = 0
        self.front_right_vel = 0
        self.back_left_vel = 0
        self.back_right_vel = 0

        self.x_list = []
        self.y_list = []

        self.robot_x_vel = 0
        self.robot_y_vel = 0
        self.robot_angle_deg = 0
        self.robot_angle_radians = 0
        self.time = 0
        self.dt = dt

    def update(self, front_left_vel, back_left_vel, front_right_vel, back_right_vel):
#         todo
        pass


