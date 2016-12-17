# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:44:04 2016

@author: Administrator
"""
from __future__ import division

import matplotlib.pyplot as pl
import numpy as np
from copy import deepcopy

class wave:
     def __init__(self,L,c,dx,k,x0,p):
        self.L=L
        self.c=c
        self.dx=dx
        self.k=k
        self.x0=x0
        self.dt=dx/c
        self.p=p
     def initialization(self):
        self.x = np.linspace(0,self.L,101)
        self.y = np.exp(-1000*(self.x-self.x0)**2) 
        self.y[0] = 0
        self.y[-1] = 0
     def tri(self):
         self.x = np.linspace(0,self.L,101)
         self.y  = np.zeros(101)
         for i in range(101):
                 if i<=50:
                    self.y [i] = (1/50)*i
                 else:
                    self.y [i] = -(1/50)*i + 2


     def iteration(self):
        y_now = self.y 
        y_now[0] = 0
        y_now[-1] = 0
        self.d=[y_now[self.p]]
        self.t=[0]
        y_before = deepcopy(y_now)
        y_after = np.zeros(101)

        for j in range(2**(10)-1):
            for i in range(101):
                if i== 0 or i== 100:
                    y_after[i] = 0
                else:
                    y_after[i] = - y_before[i] + y_now[i+1] + y_now[i-1]
            y_before = deepcopy(y_now)
            y_now = deepcopy(y_after)
            self.d.append(y_now[self.p])
            self.t.append(self.t[-1]+self.dt)
        return self.d,self.t
     def iteration2(self):
        y_now = self.y 
        y_now[0] = 0
        y_now[-1] = 0
        self.d=[y_now[self.p]]
        self.t=[0]
        y_before = deepcopy(y_now)
        y_after = np.zeros(101)

        for j in range(2**(10)-1):
            for i in range(101):
                if i== 0:
                    y_after[i] = 0
                elif i==100:
                    y_after[i] = - y_before[i] + y_now[i-1] + y_now[i]
                else:
                    y_after[i] = - y_before[i] + y_now[i+1] + y_now[i-1]
            y_before = deepcopy(y_now)
            y_now = deepcopy(y_after)
            self.d.append(y_now[self.p])
            self.t.append(self.t[-1]+self.dt)
        return self.d,self.t
     def Flouier_analysis(self):
         d_fft = np.fft.fft(self.d)
         self.d_power = []
         self.f = []
         for i in range(1024):
             if i==0:
                 self.d_power.append(abs(d_fft[i]))
                 f = 0
                 self.f.append(f)
             else:
                 self.d_power.append(abs(d_fft[i]))
                 T = 1024*10**(-4)/(3*i)
                 f = 1/T
                 self.f.append(f)
         return self.f,self.d_power
     def signal_plot(self):
         pl.subplot(121)
         pl.plot(self.t,self.d,'r')
         pl.xlabel('Time(s)')
         pl.ylabel('Signal(m)')
         pl.title('String signal versus time')
         
     def spectrum_plot(self):
         pl.subplot(313)
         pl.plot(self.f,self.d_power,'g')
         pl.xlabel('Frequency(Hz)')
         pl.ylabel('Power')
         pl.title('Power Spectrum')
         pl.xlim(0,3000)
         pl.ylim(0,60)
         pl.title(r'$x_0$ at 50 percent')
         pl.show()
         
a=wave(1,300,0.01,1000,0.4,50)
a.initialization()
a.iteration()
a.Flouier_analysis()
#a.signal_plot()
a.spectrum_plot()
