# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 19:56:44 2016

@author: Administrator
"""
import numpy as np
import pylab as pl
class Mean_field:
     def __init__(self,z):
         self.z=z
     def calculate(self):
         self.T=[]
         self.M=[]
         for i in range(1,401):
             self.T_i=0.02*i
             M_i=self.newton(self.T_i)
             self.T.append(self.T_i)            
             self.M.append(M_i)

     def comparison(self):
         for j in range(396,401):
             
               M_j=self.newton(j*0.01)
               M_0=np.sqrt(3/(j*0.01)*(j*0.01/self.z)**3)*np.sqrt(self.z-j*0.01)
               d=abs(M_0-M_j)
               
               print(M_j)
     def newton(self,Ti):
         self.s=1 
         while abs(self.s-np.tanh(self.z*self.s/Ti))>0.0001:
             self.s=self.s-(self.s-np.tanh(self.z*self.s/Ti))/(1-1/(np.cosh(self.z*self.s/Ti))**2*self.z/Ti)
         return self.s
     def plot(self):
         pl.plot(self.T,self.M,'r')
         pl.xlabel('Temperature')
         pl.ylabel('Magnetization')
         pl.title('Numerical solution of the mean field equation')
         pl.xlim(0,8)
         pl.ylim(-0.02,1.02)
         pl.show
a=Mean_field(4)
a.calculate()
a.comparison()
                 
         
         
