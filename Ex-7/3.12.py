# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 23:38:33 2016

@author: Administrator
"""
import pylab as pl
import math
class chaos:
    def __init__(self,theta=0.2,omega=0,t=0,time_step=3*math.pi/1000,F_D=0.5,q=0.5,
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
        self.i=0
        self.th1=[]
        self.om1=[]
        self.th2=[]
        self.om2=[]
        self.th3=[]
        self.om3=[]
        self.th4=[]
        self.om4=[]
    def calculate(self ):
        while(self.t[-1]<=6000):  
            
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
        while(self.i<637):
            self.th1.append(self.theta[1000*self.i])
            self.om1.append(self.o[1000*self.i])
            self.i+=1
        self.i=0          
        while(self.i<637):
            self.th2.append(self.theta[1000*self.i+125])
            self.om2.append(self.o[1000*self.i+125])
            self.i+=1  
        self.i=0          
        while(self.i<637):
            self.th3.append(self.theta[1000*self.i+250])
            self.om3.append(self.o[1000*self.i+250])
            self.i+=1  
        self.i=0          
        while(self.i<637):
            self.th4.append(self.theta[1000*self.i+375])
            self.om4.append(self.o[1000*self.i+375])
            self.i+=1  

    def show2(self):       
        pl.subplot(221)
        pl.plot(self.th1,self.om1,'.')
        pl.title(r'$\omega$ versus $\theta$')
        pl.xlabel(r'$\theta$(rad)')
        pl.ylabel('$\omega$(rad/s)')   

        pl.subplot(222)
        pl.plot(self.th2,self.om2,'.')
        pl.xlabel(r'$\theta$(rad)')
    
        
        pl.subplot(223)
        pl.plot(self.th3,self.om3,'.')
        pl.xlabel(r'$\theta$(rad)')
        pl.ylabel('$\omega$(rad/s)')
        
        pl.subplot(224)
        pl.plot(self.th4,self.om4,'.')
        pl.xlabel(r'$\theta$(rad)')
     
        pl.show()

a = chaos()
a.calculate()
a.show2()



