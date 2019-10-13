import math
import tkinter as tk
import numpy as np

def deg_to_rad(deg):
    return deg * (math.pi / 180)

def rad_to_deg(rad):
    return rad * (180 / math.pi)

def y_wave(amplitude, omega, time, lambda_const, dist):
    return amplitude * math.sin(omega * time - lambda_const * dist)

class Wave:
    def __init__(self, canvas, win_width, win_height):
        self.amplitude = 50
        self.omega = 4
        self.wave_lambda = 10
        self.line_each_half = 5
        
        self.canvas = canvas
        
        self.win_width = win_width
        self.win_height = win_height
        
        self.line_increment = self.wave_lambda / self.line_each_half
        self.lines = np.empty(0)
        self.make_wave()
    def make_wave(self):
        dist = 20
        lambda_const = (2 * math.pi) / self.wave_lambda
        while dist < self.win_width:
            temp_front_x = dist
            temp_front_y = y_wave(self.amplitude, self.omega, 0, lambda_const, dist)
            dist += self.line_increment
            temp_back_x = dist
            temp_back_y = y_wave(self.amplitude, self.omega, 0, lambda_const, dist)
            temp_line = self.canvas.create_line(temp_front_x, temp_front_y, temp_back_x, temp_back_x)
            self.lines = np.append(self.lines, temp_line)
            