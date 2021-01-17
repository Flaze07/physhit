from tkinter import *
import numpy as np
import math
import time
from wave import makeview

class Manager:
    def __init__(self):
        self.root = Tk()

        self.root.title("Masukkan data - data Gelombang !")
        self.root["padx"] = 40
        self.root["pady"] = 20       

        # Create a text frame to hold the text Label and the Entry widget
        self.textFrame_1 = Frame(self.root)
        self.textFrame_2 = Frame(self.root)
        self.textFrame_3 = Frame(self.root)
        self.textFrame_4 = Frame(self.root)
        self.textFrame_5 = Frame(self.root)

        #Create a Label in textFrame
        self.entryLabel = Label(self.textFrame_1)
        self.entryLabel["text"] = "Masukkan Amplitudo :"
        self.entryLabel.pack(side=LEFT)

        self.entryLabel = Label(self.textFrame_2)
        self.entryLabel["text"] = "Masukkan Omega :"
        self.entryLabel.pack(side=LEFT)

        self.entryLabel = Label(self.textFrame_3)
        self.entryLabel["text"] = "Masukkan Waktu :"
        self.entryLabel.pack(side=LEFT)

        self.entryLabel = Label(self.textFrame_4)
        self.entryLabel["text"] = "Masukkan Konstanta :"
        self.entryLabel.pack(side=LEFT)

        self.entryLabel = Label(self.textFrame_5)
        self.entryLabel["text"] = "Masukkan Jarak :"
        self.entryLabel.pack(side=LEFT)

        # Create an Entry Widget in textFrame
        self.entryamplitudo = Entry(self.textFrame_1)
        self.entryamplitudo["width"] = 50
        self.entryamplitudo.pack(side=LEFT)

        self.entryomega = Entry(self.textFrame_2)
        self.entryomega["width"] = 50
        self.entryomega.pack(side=LEFT)

        self.entrytime = Entry(self.textFrame_3)
        self.entrytime["width"] = 50
        self.entrytime.pack(side=LEFT)

        self.entryconstant = Entry(self.textFrame_4)
        self.entryconstant["width"] = 50
        self.entryconstant.pack(side=LEFT)

        self.entrydistance = Entry(self.textFrame_5)
        self.entrydistance["width"] = 50
        self.entrydistance.pack(side=LEFT)

        self.textFrame_1.pack()
        self.textFrame_2.pack()
        self.textFrame_3.pack()
        self.textFrame_4.pack()
        self.textFrame_5.pack()

        self.button = Button(self.root, text="Tampilkan Gelombang", command=self.displayText)
        self.button.pack() 

        self.root.mainloop()
    def displayText(self):
        global amplitude,omega,time,constant,distance
        amplitude=float(self.entryamplitudo.get())
        time=float(self.entrytime.get())
        omega=float(self.entryomega.get())
        constant=float(self.entryconstant.get())
        distance=float(self.entrydistance.get())
        graph=makeview(amplitude,omega,time,constant,distance )
        graph.show()