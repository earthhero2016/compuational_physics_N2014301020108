# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:35:17 2016

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:22:51 2016
@author: AF
"""

import pylab as pl

class billiard_rectangular:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
    
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
            if (self.x[i] < -1.0):
                
                self.vx[i] = - self.vx[i]
            elif(self.x[i] > 1.0):
                
                self.vx[i] = - self.vx[i]
            elif(self.y[i] < -1.0):
                
                self.vy[i] = -self.vy[i]
            elif(self.y[i] > 1.0):
                
                self.vy[i] = -self.vy[i] 
            else:
                pass
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y

    def plot(self):
        pl.figure(figsize = (8,8))
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.xlabel('x')
        pl.ylabel('y')
        pl.plot(self.x,self.y)
        pl.savefig('chapter3_3.31.png',dpi = 144)
        pl.show()
A = billiard_rectangular(0.5,1,0.5,0.3,5000,0.1)
A.motion_calculate()
A.plot()