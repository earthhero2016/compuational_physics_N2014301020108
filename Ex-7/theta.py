# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:04:29 2016

@author: Administrator
"""
import pylab as pl
import math
class chaos:
    def __init__(self,theta=0.2,omega=0,t=0,time_step=0.04,F_D=0.5,q=0.5,
l=9.8,g=9.8,OMEGA_D=2/3):
        self.theta=[theta]
        self.o=[omega]
        self.t=[t]
        self.dt=time_step
        self.F_D=F_D
        self.O=OMEGA_D
        self.q=q
        self.l=l
        self.g=g
    def calculate(self):
        while(self.t[-1]<=60):  
            
            o_new=self.o[-1]-((self.g/self.l)*math.sin(self.theta[-1])+self.q*self.o[-1]-self.F_D*math.sin(self.O*self.t[-1]))*self.dt
            self.o.append(o_new)
            theta_new=self.theta[-1]+self.o[-1]*self.dt
            while(theta_new<-math.pi):
                theta_new+=2*math.pi
            while(theta_new>math.pi):
                theta_new-=2*math.pi
            self.theta.append(theta_new)
            t_new=self.t[-1]+self.dt
            self.t.append(t_new)

    def show_results(self):
        

        pl.subplot(121)          
        pl.plot(self.t, self.theta)
        pl.title(r'$\theta$ versus time')
        pl.xlabel('time(s)')
        pl.ylabel(r'$\theta$(rad/s)')
        pl.legend(['$F_D$=0.5'])
        pl.show()


        self.theta=[0.2]
        self.o=[0]
        self.t=[0]
        self.F_D=1.2
    def calculate1(self):
        while(self.t[-1]<=60):  
            
            o_new1=self.o[-1]-((self.g/self.l)*math.sin(self.theta[-1])+self.q*self.o[-1]-self.F_D*math.sin(self.O*self.t[-1]))*self.dt
            self.o.append(o_new1)
            theta_new1=self.theta[-1]+self.o[-1]*self.dt
            while(theta_new1<-math.pi):
                theta_new1+=2*math.pi
            while(theta_new1>math.pi):
                theta_new1-=2*math.pi
            self.theta.append(theta_new1)
            t_new1=self.t[-1]+self.dt
            self.t.append(t_new1)

    def show_results1(self):        

        pl.subplot(122)
        pl.plot(self.t, self.theta)
        pl.title(r'$\theta$ versus time')
        pl.xlabel('time(s)')
        pl.ylabel(r'$\theta$(rad/s)')
        pl.legend(['$F_D$=1.2'])
        pl.show()
a = chaos()
a.calculate()
a.show_results()  
a.calculate1()
a.show_results1() 
            
    