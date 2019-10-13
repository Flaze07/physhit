import tkinter as tk
import numpy as np
import math
import time
import wave

class Manager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("parabol")
        self.root.pack_propagate(0)
        self.root.geometry('1000x600')
        
        self.canvas = tk.Canvas(self.root)
        
        self.lbl = tk.Label(self.canvas,text="parabola")
        temp = self.root.winfo_width()//2
        
        self.wave = wave.Wave(self.canvas, 1000, 600)
        self.lbl.grid(column=temp, row=0)
        self.lbl.pack()
        
        self.canvas.pack()
    def run(self):
        self.root.mainloop()
        