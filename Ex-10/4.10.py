# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 22:13:43 2016

@author: Administrator
"""

import pylab as pl
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
class planetary_motion:
    def __init__(self,x0,y0,vx0,vy0,dt,alpha):
        self.x0=x0
        self.y0=y0
        self.vx0=vx0
        self.vy0=vy0
        self.dt=dt
        self.alpha=alpha
    def motion_calculate(self):
        self.x=[self.x0]
        self.y=[self.y0]
        vx=self.vx0
        vy=self.vy0
        for i in range (0,10000):
            r=np.sqrt(self.x[i]**2+self.y[i]**2)
            vx=vx-4*(np.pi**2)*self.x[i]/math.pow(r,3)*(1+self.alpha/r**2)*self.dt
            self.x.append(self.x[i]+vx*self.dt)
            vy=vy-4*(np.pi**2)*self.y[i]/math.pow(r,3)*(1+self.alpha/r**2)*self.dt
            self.y.append(self.y[i]+vy*self.dt)
        self.X=[]
        self.Y=[]
        self.Z=[]
        for j in range(0,10000): 
            self.X.append(self.x[j])
            self.Y.append(math.cos(math.radians(6.34))*self.y[j])
            self.Z.append(math.sin(math.radians(6.34))*self.y[j])
        return self.X,self.Y,self.Z    
a=planetary_motion(0.39,0,0,9.88,0.0001,0.02)
X,Y,Z=a.motion_calculate()
print(X,Y,Z)
fig = pl.figure()  
ax = fig.add_subplot(111, projection='3d')         
ax.plot(X, Y, Z)

pl.scatter([0],[0],s=500,color='red')
pl.title(r'Simulation of the precession of Mercury $\alpha$=0.02')

pl.show()