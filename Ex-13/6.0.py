# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 11:31:50 2016

@author: Administrator
"""

from __future__ import division
from matplotlib import animation
import matplotlib.pyplot as pl
import numpy as np
from copy import deepcopy

fig = pl.figure()
ax = fig.add_subplot(1,1,1,xlim=(0,1),ylim=(-1,1))
line, = ax.plot([],[],lw=2)
note = ax.text(0.05,1.4,'',fontsize=12)
class wave:
     def __init__(self,L,c,dx,k,x0):
        self.L=L
        self.c=c
        self.dx=dx
        self.k=k
        self.x0=x0
        self.dt=dx/c
     def initialization(self):
        self.x = np.linspace(0,self.L,101)
        self.y = np.exp(-1000*(self.x-self.x0)**2) 
        self.y[0] = 0
        self.y[-1] = 0
        line.set_data(self.x,self.y)
        note.set_text('')
        return line,note
     def tri(self):
         self.x = np.linspace(0,self.L,101)
         self.y  = np.zeros(101)
         for i in range(101):
                 if i<=20:
                    self.y [i] = (1/20)*i
                 else:
                    self.y [i] = -(1/80)*i + 10/8
         line.set_data(self.x,self.y)
         note.set_text('')
         return line,note
     def iteration(self,num):
        self.y_now = self.y 
        self.y_now[0] = 0
        self.y_now[-1] = 0

        y_before = deepcopy(self.y_now)
        y_after = np.zeros(101)

        for j in range(num):
            for i in range(101):
                if i== 0 or i== 100:
                    y_after[i] = 0
                else:
                    y_after[i] = - y_before[i] + self.y_now[i+1] + self.y_now[i-1]
            y_before = deepcopy(self.y_now)
            self.y_now = deepcopy(y_after)

        return self.y_now
     def iteration2(self,num):
        self.y_now = self.y 
        self.y_now[0] = 0
        self.y_now[-1] = 0

        y_before = deepcopy(self.y_now)
        y_after = np.zeros(101)

        for j in range(num):
            for i in range(101):
                if i== 0:
                    y_after[i] = 0
                elif i==100:
                    y_after[i] = - y_before[i]+self.y_now[i]+self.y_now[i-1]
                else:
                    y_after[i] = - y_before[i] + self.y_now[i+1] + self.y_now[i-1]
            y_before = deepcopy(self.y_now)
            self.y_now = deepcopy(y_after)

        return self.y_now

    
     def animate(self,i): 

         x = np.linspace(0,1,101)
         y = self.iteration2(i)                                                                        
         line.set_data(x,y)
         note.set_text(r'$y_0=exp[-%s\times (x-%s)^2]$'%(self.k,self.x0)+'\nstep n=%s'%i)
         return line,note
a=wave(1,300,0.01,1000,0.5)
anim1=animation.FuncAnimation(fig, a.animate, init_func=a.tri, frames=200, interval=2)
pl.xlabel('x(m)')
pl.ylabel('y(m)')
pl.title('Gaussian pluck Free right end')
pl.show()
    
                    
