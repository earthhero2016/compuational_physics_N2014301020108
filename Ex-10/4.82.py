# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:12:28 2016

@author: Administrator
"""

import pylab as pl
import numpy as np

class planetary_motion:
    def __init__(self,Ms,Mp,e,a):
        self.Ms=Ms
        self.Mp=Mp
        self.e=e
        self.a=a
        self.mu=Mp*Ms/(Ms+Mp)
        self.GM=4*np.pi**2
        self.dtheta=np.pi/1000
        self.L=np.sqrt(self.mu*self.GM*Mp*a*(1-self.e**2))
    def motion_calculate(self):
        self.x=[]
        self.y=[]
        for i in range(0,2001):
            r=self.L**2/(self.mu*self.GM*self.Mp)/(1-self.e*np.cos(i*self.dtheta))
            self.x.append(r*np.cos(i*self.dtheta))
            self.y.append(r*np.sin(i*self.dtheta))
        return self.x,self.y
    def period_calculate(self):
        b=self.a*np.sqrt(1-self.e**2)
        rmin=self.a*(1-self.e)
        vmax=np.sqrt(self.GM*self.Ms/199800)*np.sqrt((1+self.e)/(self.a*(1-self.e))*(1+self.Mp/self.Ms))
        T=np.pi*self.a*b*2/(vmax*rmin)
        print(T)
a=planetary_motion(19980,7,0.1,3)
x1,y1=a.motion_calculate()
a.period_calculate()
pl.scatter([0],[0],s=100,color='red')
pl.plot(x1,y1)
pl.xlabel('x(AU)')
pl.ylabel('y(AU)')

b=planetary_motion(19980,60,0.05,13)
x2,y2=b.motion_calculate()
b.period_calculate()
pl.plot(x2,y2)
pl.xlabel('x(AU)')
pl.ylabel('y(AU)')

c=planetary_motion(19980,200,0.5,25)
x3,y3=c.motion_calculate()
c.period_calculate()
pl.plot(x3,y3)
pl.xlabel('x(AU)')
pl.ylabel('y(AU)')
pl.title('Imaginary orbits of a different system')

