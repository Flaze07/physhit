import tkinter as tk
import numpy as np
import math
import time

#evert 1/2 wave uses 10 lines

def cm_to_pixel(cm):#every 10 pixels are 1 cm
    return cm*10


def deg_to_rad(deg):
    return deg * (math.pi / 180)

def rad_to_deg(rad):
    return rad * (180 / math.pi)

def y_parabola(amplitude, omega, time, constant, distance):
    return amplitude * math.sin(omega*time - constant*distance)

class Manager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("parabol")
        self.root.pack_propagate(0)
        self.root.geometry('1000x600')
        
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()
        
        self.lbl = tk.Label(self.canvas,text="parabola")
        temp = self.root.winfo_width()//2
        self.lbl.grid(column=temp, row=0)
        self.lbl.pack()
        
        self.lm = cm_to_pixel(10)
        self.amplitude = cm_to_pixel(5)
        self.omega = 1
        
        self.run()
    #def make_line(self):
        
    def run(self):
        self.root.mainloop()
        