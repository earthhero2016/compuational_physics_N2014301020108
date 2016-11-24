# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:43:43 2016

@author: Administrator
"""
import pylab as pl
import numpy as np
import math
class planetary_motion:
    def __init__(self,x0,y0,vx0,vy0,dt,beta):
        self.x0=x0
        self.y0=y0
        self.vx0=vx0
        self.vy0=vy0
        self.dt=dt
        self.beta=beta
    def motion_calculate(self):
        self.x=[self.x0]
        self.y=[self.y0]
        vx=self.vx0
        vy=self.vy0
        for i in range (0,10000):
            r=np.sqrt(self.x[i]**2+self.y[i]**2)
            vx=vx-4*(np.pi**2)*self.x[i]/math.pow(r,self.beta+1)*self.dt
            self.x.append(self.x[i]+vx*self.dt)
            vy=vy-4*(np.pi**2)*self.y[i]/math.pow(r,self.beta+1)*self.dt
            self.y.append(self.y[i]+vy*self.dt)
        return self.x,self.y
a=planetary_motion(1,0,0,4,0.001,2)
x1,y1=a.motion_calculate()        
pl.plot(x1,y1)
pl.xlabel('x(AU)')
pl.ylabel('y(AU)') 

b=planetary_motion(1,0,0,6.28,0.001,2)
x2,y2=b.motion_calculate()        
pl.plot(x2,y2)
pl.xlabel('x(AU)')
pl.ylabel('y(AU)')               
pl.title(r'$\beta$=2.2')