# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:27:53 2016

@author: Administrator
"""
import pylab as pl
import numpy as np
import math

class hyperion:
    def __init__(self,x0,y0,vx0,vy0,theta0,dt):
        self.x0=x0
        self.y0=y0
        self.vx0=vx0
        self.vy0=vy0
        self.dt=dt
        self.theta0=theta0
    def center_motion(self):
        self.x=[self.x0]
        self.y=[self.y0]
        vx=self.vx0
        vy=self.vy0
        for i in range (0,30000):
            r=np.sqrt(self.x[i]**2+self.y[i]**2)
            vx=vx-4*(np.pi**2)*self.x[i]/math.pow(r,3)*self.dt
            self.x.append(self.x[i]+vx*self.dt)
            vy=vy-4*(np.pi**2)*self.y[i]/math.pow(r,3)*self.dt
            self.y.append(self.y[i]+vy*self.dt)
        return self.x,self.y
    def spin_motion(self):
        self.theta=[self.theta0]
        self.omega=[0]
        self.t=[0]
        for i in range(len(self.x)):
            r=np.sqrt(self.x[i]**2+self.y[i]**2)
            beta=-3*4*np.pi**2/r**5*(self.x[i]*math.sin(self.theta[i])-self.y[i]*math.cos(self.theta[i]))*(self.x[i]*math.cos(self.theta[i])+self.y[i]*math.sin(self.theta[i]))
            self.omega.append(self.omega[i]+beta*self.dt)            
            self.theta.append(self.theta[i]+self.omega[-1]*self.dt)
            
            self.t.append(self.t[i]+self.dt)         
        return self.t,self.theta
    def resetting(self,theta):
        while theta>np.pi:
            theta-=2*np.pi
        while theta<-np.pi:
            theta+=2*np.pi
        return theta
    def plot_theta(self):
        pl.plot(self.t,self.theta,'r')
        pl.ylabel(r'$\theta$(rad)')
        pl.xlabel('time(yr)')
        pl.title(r'Hyperion $\theta$ versus time Elliptical orbit')
    def plot_omega(self):
        pl.plot(self.t,self.omega,'r')
        pl.xlabel('time(yr)')
        pl.ylabel(r'$\omega$(rad/yr)')
        pl.title(r'Hyperion $\omega$ versus time Elliptical orbit')
a=hyperion(1,0,0,6,0,0.0001)
a.center_motion()
x1,y1=a.spin_motion()

b=hyperion(1,0,0,6,0.01,0.0001)
b.center_motion()
x2,y2=b.spin_motion()
delta=[]
e=[]
t=[]
for i in range(len(x1)):
    d=abs(y2[i]-y1[i])
    delta.append(d)
    e.append(0.01*np.exp(0.05*x1[i]))
    t.append(0.0001*i)
pl.subplot(224)
pl.xlabel('time(yr)')
pl.ylabel(r'$\Delta$$\theta$(rad)')
pl.semilogy(t,delta)
pl.title(r'$\Delta$$\theta$ versus time $v_i$=6')
pl.show()
