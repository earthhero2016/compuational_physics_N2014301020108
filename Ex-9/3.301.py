# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:37:29 2016

@author: Administrator
"""
import pylab as pl
import numpy as np

class billiard_circle:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt,a):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
        self.a=a
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
            if (np.sqrt( self.x[i]**2+(self.y[i]-self.a)**2 ) > 1.0 and self.y[i]>0):
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y-a)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1],self.a)
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1],self.a)
            self.t.append(self.t[i - 1] + self.dt)
            if (np.sqrt( self.x[i]**2+(self.y[i]+self.a)**2 ) > 1.0 and self.y[i]<0):
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y+a)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1],self.a)
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1],self.a)
            self.t.append(self.t[i - 1] + self.dt)

        return self.x, self.y
    def correct(self,condition,x,y,vx,vy,a):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
    def reflect(self,x,y,vx,vy,a):
        if(y>0):            
           v = np.sqrt(vx**2+vy**2)
           cos1 = (vx*x+vy*(y-a))/v
           cos2 = (vx*(y-a)-vy*x)/v
           vt = -v*cos1
           vc = v*cos2 
           vx_n = vt*x+vc*(y-a)
           vy_n = vt*(y-a)-vc*x
        if(y<0):            
           v = np.sqrt(vx**2+vy**2)
           cos1 = (vx*x+vy*(y+a))/v
           cos2 = (vx*(y+a)-vy*x)/v
           vt = -v*cos1
           vc = v*cos2 
           vx_n = vt*x+vc*(y+a)
           vy_n = vt*(y+a)-vc*x
        return vx_n,vy_n
        
    def plot1(self):
        
        pl.subplot(131)
        pl.xlim(-1.2,1.2)
        pl.ylim(-1.2,1.2)
        pl.xlabel('x')
        pl.ylabel('y')
        self.plot_boundary()
        pl.plot(self.x,self.y,'r')
        pl.title(r'Stadium billiard $\alpha$=0.1')
        pl.show()
    def plot2(self):
        
        pl.subplot(132)
        pl.xlim(-1.2,1.2)
        pl.ylim(-1.2,1.2)
        pl.xlabel('x')
        pl.ylabel('y')
        self.plot_boundary()
        pl.plot(self.x,self.y,'r')
        pl.title(r'Stadium billiard $\alpha$=0.01')
        pl.show()
    def plot3(self):
        
        pl.subplot(133)
        pl.xlim(-1.2,1.2)
        pl.ylim(-1.2,1.2)
        pl.xlabel('x')
        pl.ylabel('y')
        self.plot_boundary()
        pl.plot(self.x,self.y,'r')
        pl.title(r'Stadium billiard $\alpha$=0.001')
        pl.show()
    def phase_plot(self):
        pl.figure(figsize = (8,8))
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        record_x = []
        record_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                record_vx.append(self.vx[i])
                record_x.append(self.x[i])
        pl.xlabel('x')
        pl.ylabel(r'$v_x$')
        pl.scatter(record_x,record_vx,s=1)
        pl.title('Circular stadium-phase space plot')
        pl.show()
        
                
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta <np.pi:
            x.append(np.cos(theta))
            y.append(self.a+np.sin(theta))
            theta+= 0.01
        theta=-np.pi
        while theta <0:
            x.append(np.cos(theta))
            y.append(-self.a+np.sin(theta))
            theta+= 0.01
        x.append(1)
        y.append(self.a)
        pl.plot(x,y)

a=billiard_circle(-0.1,0.1,0.6,-0.8,5000,0.01,0.1)
x1,y1=a.motion_calculate()
b=billiard_circle(-0.1,0.1,0.6,-0.8,5000,0.01,0.01)
x2,y2=b.motion_calculate()
c=billiard_circle(-0.1,0.1,0.6,-0.8,5000,0.01,0.001)
x3,y3=c.motion_calculate()
pl.subplot(131)
pl.xlim(-1.2,1.2)
pl.ylim(-1.2,1.2)
pl.xlabel('x')
pl.ylabel('y')
a.plot_boundary()
pl.plot(x1,y1,'r')
pl.title(r'Stadium billiard $\alpha$=0.1')
pl.show()
pl.subplot(132)
pl.xlim(-1.2,1.2)
pl.ylim(-1.2,1.2)
pl.xlabel('x')
pl.ylabel('y')
b.plot_boundary()
pl.plot(x2,y2,'r')
pl.title(r'Stadium billiard $\alpha$=0.01')
pl.show()
pl.subplot(133)
pl.xlim(-1.2,1.2)
pl.ylim(-1.2,1.2)
pl.xlabel('x')
pl.ylabel('y')
c.plot_boundary()
pl.plot(x3,y3,'r')
pl.title(r'Stadium billiard $\alpha$=0.001')
pl.show()
        


