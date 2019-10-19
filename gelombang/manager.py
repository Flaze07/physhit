import Tkinter as tk
import numpy as np
import math
import time
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
        self.root.title("Gelombang")
        self.root.pack_propagate(0)
        self.root.geometry('1920x1680')

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

        self.lbl = tk.Label(self.canvas,text="Gelombang") #Start of Freddie Code
        self.lam = tk.Label ( text = "Lambda    : " , font=("arial",16,"bold")).grid(row=0)
        self.omg  = tk.Label( text = "Omega     : ", font=("arial",16,"bold")).grid(row=2)
        self.amp = tk.Label ( text = "Amplitude : " , font=("arial",16,"bold")).grid(row=1)
        self.cm1  = tk.Label( text = "cm" , font=("arial",16,"bold")).grid(row=0,column = 3)
        self.cm2 = tk.Label ( text = "cm" , font = ("arial",16,"bold")).grid(row=1 ,column = 3)
        inp_lam = tk.Entry (self.root)  # lambda input
        inp_omg = tk.Entry (self.root) # frekuensi input
        inp_ampli = tk.Entry(self.root) # amplitudo input
        inp_lam.grid(row=0, column =1)
        inp_omg.grid(row = 2 , column = 1 )
        inp_ampli.grid(row = 1 , column = 1 )
        button = tk.Button(self.root, text = "Enter",font = ("arial",16,"bold"),width = 10) #Insert Button Command Here!
        button.grid(row = 3 , column = 0  )
        button.pack
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
