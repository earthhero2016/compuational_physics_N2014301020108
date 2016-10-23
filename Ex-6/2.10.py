# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:32:22 2016

@author: Administrator
"""
import pylab as pl
import math
class cannon_shell_trajectory:
    def __init__(self, x=0, y=0, v=700,time_step=0.0001, g0=9.8,a=0.0065, 
alpha=2.5, B=0.00004, T=300,r=6371000,vw=-10,theta=30,x0=22000,y0=2200):
        self.x=[x]
        self.y=[y]
        self.dt=time_step
        self.v=v
        self.vw=vw
        self.g=g0*r*r/((r+self.y[-1])*(r+self.y[-1]))
        self.B=B
        self.T=T
        self.alpha=alpha
        self.a=a
        self.theta=theta
        self.v_x=self.v*math.cos(math.radians(self.theta))
        self.v_y=self.v*math.sin(math.radians(self.theta))
        self.x0=x0
        self.y0=y0
    def add(self):
      while(self.theta<60):
           self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
           self.x.append(self.x[-1]+self.v_x*self.dt)
           self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
           self.y.append(self.y[-1]+self.v_y*self.dt)
           while(self.y[-1]>self.y[-2]):
              self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
              self.x.append(self.x[-1]+self.v_x*self.dt)
              self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
              self.y.append(self.y[-1]+self.v_y*self.dt)
           while(self.y[-1]>self.y0):
              self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
              self.x.append(self.x[-1]+self.v_x*self.dt)
              self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
              self.y.append(self.y[-1]+self.v_y*self.dt)   
           if(self.x0-200<self.x[-1]<self.x0+200):
              print(self.x[-1],self.y[-1],self.theta)
              self.a1=self.theta-2
              self.theta=self.a1
              while(self.theta<self.a1+4):
                  self.x=[0]
                  self.y=[0]
                  self.theta+=0.5
                  self.v_x=self.v*math.cos(math.radians(self.theta))
                  self.v_y=self.v*math.sin(math.radians(self.theta))   
                  self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                  self.x.append(self.x[-1]+self.v_x*self.dt)
                  self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                  self.y.append(self.y[-1]+self.v_y*self.dt)
                  while(self.y[-1]>self.y[-2]):
                      self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                      self.x.append(self.x[-1]+self.v_x*self.dt)
                      self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                      self.y.append(self.y[-1]+self.v_y*self.dt)
                  while(self.y[-1]>self.y0):
                      self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                      self.x.append(self.x[-1]+self.v_x*self.dt)
                      self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                      self.y.append(self.y[-1]+self.v_y*self.dt) 
                  if(self.x0-50<self.x[-1]<self.x0+50):
                      print(self.x[-1],self.y[-1],self.theta)
                      self.a2=self.theta-0.5
                      self.theta=self.a2
                      while(self.theta<self.a2+1):
                          self.x=[0]
                          self.y=[0]
                          self.theta+=0.1
                          self.v_x=self.v*math.cos(math.radians(self.theta))
                          self.v_y=self.v*math.sin(math.radians(self.theta))   
                          self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                          self.x.append(self.x[-1]+self.v_x*self.dt)
                          self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                          self.y.append(self.y[-1]+self.v_y*self.dt)
                          while(self.y[-1]>self.y[-2]):
                              self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                              self.x.append(self.x[-1]+self.v_x*self.dt)
                              self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                              self.y.append(self.y[-1]+self.v_y*self.dt)
                          while(self.y[-1]>self.y0):
                              self.v_x=self.v_x-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*(self.v_x-self.vw)*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                              self.x.append(self.x[-1]+self.v_x*self.dt)
                              self.v_y=self.v_y-self.g*self.dt-self.B*math.sqrt(math.pow(self.v_x-self.vw,2)+math.pow(self.v_y,2))*self.v_y*math.pow(1-self.a*self.y[-1]/self.T,self.alpha)*self.dt
                              self.y.append(self.y[-1]+self.v_y*self.dt) 
                          if(self.x0-8<self.x[-1]<self.x0+8):
                              pl.plot(self.x, self.y)
                              pl.title('cannon shell trajectory')
                              pl.xlabel('x(m)')
                              pl.ylabel('y(m)')
                              pl.plot(self.x0,self.y0,'k*',linewidth=10,label='target')
                              pl.ylim(0,)
                              pl.show()
                              print(self.x[-1],self.y[-1],self.theta)
           self.x=[0]
           self.y=[0]
           self.theta+=2
           self.v_x=self.v*math.cos(math.radians(self.theta))
           self.v_y=self.v*math.sin(math.radians(self.theta))
a = cannon_shell_trajectory()
a.add() 
                     