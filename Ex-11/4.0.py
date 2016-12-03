# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:35:40 2016

@author: Administrator
"""
import pylab as pl
import numpy as np
import math

class hyperion:
    def __init__(self,x0,y0,vx0,vy0,dt):
        self.x0=x0
        self.y0=y0
        self.vx0=vx0
        self.vy0=vy0
        self.dt=dt
    def center_motion(self):
        self.x=[self.x0]
        self.y=[self.y0]
        vx=self.vx0
        vy=self.vy0
        for i in range (0,100000):
            r=np.sqrt(self.x[i]**2+self.y[i]**2)
            vx=vx-4*(np.pi**2)*self.x[i]/math.pow(r,3)*self.dt
            self.x.append(self.x[i]+vx*self.dt)
            vy=vy-4*(np.pi**2)*self.y[i]/math.pow(r,3)*self.dt
            self.y.append(self.y[i]+vy*self.dt)
        return self.x,self.y
    def spin_motion(self):
        self.theta=[0]
        self.omega=[0]
        self.t=[0]
        for i in range(len(self.x)):
            r=np.sqrt(self.x[i]**2+self.y[i]**2)
            beta=-3*4*np.pi**2/r**5*(self.x[i]*math.sin(self.theta[i])-self.y[i]*math.cos(self.theta[i]))*(self.x[i]*math.cos(self.theta[i])+self.y[i]*math.sin(self.theta[i]))
            self.omega.append(self.omega[i]+beta*self.dt)            
            self.theta.append(self.theta[i]+self.omega[-1]*self.dt)
            self.theta[-1]=self.resetting(self.theta[-1])
            self.t.append(self.t[i]+self.dt)         
        return self.omega,self.theta,self.t
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
    def plot_phase(self):
        pl.plot(self.theta,self.omega,'r')
        pl.xlabel('theta(rad)')
        pl.ylabel(r'$\omega$(rad/yr)')
        pl.title(r'Hyperion $\omega$ versus theta Circular orbit')
a=hyperion(1,0,0,6.28,0.0001)
a.center_motion()
a.spin_motion()
pl.subplot(121)
a.plot_phase()

