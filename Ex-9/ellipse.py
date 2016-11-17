# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:27:57 2016

@author: Administrator
"""
import pylab as pl
import numpy as np
class billiard_ellipse:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt  ### x^2/3+y^2/2 = 1
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i]**2/3+self.y[i]**2/2 > 1.0):
                self.x[i],self.y[i] = self.correct('x**2/3+y**2/2 < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect((2./3)*self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y      
    def reflect(self,x,y,vx,vy):
        module = np.sqrt(x**2+y**2)  ### normalization
        x = x/module
        y = y/module
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*y)/v
        cos2 = (vx*y-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*y
        vy_n = vt*y-vc*x
        return vx_n,vy_n
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
     
    def plot(self):
        pl.figure(figsize = (8,6))
        pl.xlim(-2,2)
        pl.ylim(-1.5,1.5)
        pl.xlabel('x')
        pl.ylabel('y')
        self.plot_boundary()
        pl.plot(self.x,self.y)
        pl.show()
    def phase_plot(self):
        pl.figure(figsize = (8,8))
        record_x = []
        record_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                record_vx.append(self.vx[i])
                record_x.append(self.x[i])
        pl.xlim(-2,2)
        pl.ylim(-1.5,1.5)
        pl.xlabel('x')
        pl.ylabel(r'$v_x$')
        pl.scatter(record_x,record_vx,s=1)
        pl.title('Ellipse stadium-phase space plot')
        pl.show()
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < 2*np.pi:
            x.append(np.sqrt(3)*np.cos(theta))
            y.append(np.sqrt(2)*np.sin(theta))
            theta+= 0.01
        pl.title(r'Elliptical stadium - $\frac{x^2}{3}+\frac{y^2}{2} = 1$')
        pl.plot(x,y)     
A = billiard_ellipse(0.3,0.21,0.8,0.6,500000,0.1)
A.motion_calculate()
A.phase_plot()
                     