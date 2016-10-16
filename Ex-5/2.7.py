# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:10:23 2016

@author: Administrator
"""
import pylab as pl
import math
class cannon_shell_trajectory:
    def __init__(self, x=0, y=0, v=700,time_step=0.0001, g=9.8,theta=35, 
y_0=10000, B=0.00004):
        self.x=[x]
        self.y=[y]
        self.dt=time_step
        self.theta=theta
        self.v_x=v*math.cos(math.radians(self.theta))
        self.v_y=v*math.sin(math.radians(self.theta))
        self.v=v
        self.g=g
        self.B=B
        self.y_0=y_0
    def run(self):
        while(self.y[-1]>=0):
            self.v_x=self.v_x-self.B*self.v*self.v_x*math.exp(-self.y[-1]/self.y_0)*self.dt
            self.x.append(self.x[-1]+self.v_x*self.dt)
            self.v_y=self.v_y-self.g*self.dt-self.B*self.v*self.v_y*math.exp(-self.y[-1]/self.y_0)*self.dt
            self.y.append(self.y[-1]+self.v_y*self.dt)            
    def show_results(self):
        pl.plot(self.x, self.y)
        pl.title('cannon shell trajectories with density correction')
        pl.xlabel('x(m)')
        pl.ylabel('y(m)')
        pl.show()
        print(self.x[-1],self.y[-1])
a = cannon_shell_trajectory()
a.run()
a.show_results()     
