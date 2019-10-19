import numpy as np
import matplotlib.pyplot as plot
import math 

class makeview:
    def __init__(self, amplitude=0,omega=0,time=0,constant=0,distance=0):
        self.amplitude=amplitude
        self.omega=omega
        self.time=time
        self.constant=constant
        self.distance=distance
    def show(self):
        time        = np.arange(0, self.time, 0.001)
        dataamplitude=[]
        for x in time :
            dataamplitude.append(self.amplitude * math.sin(self.omega*x - self.constant*self.distance))
        amplitude   = dataamplitude
        plot.plot(time, amplitude)
        plot.title('Gelombang')
        plot.xlabel('Waktu')
        plot.ylabel('Amplitudo ')
        plot.grid(True, which='both')
        plot.axhline(y=0, color='k')
        plot.show()