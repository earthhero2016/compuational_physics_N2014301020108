# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:40:17 2016

@author: Administrator
"""
import numpy as np
import pylab as pl
import random
class Monte_Carlo:
    def __init__(self,l):
        self.l=l
    def initialization(self):
        self.L=[]
        for i in range(0,self.l):
            L_i=[]
            for j in range(0,self.l):
                L_i.append(1)
            self.L.append(L_i)    
    def T_variation(self):
        self.TL=[]
        self.E=[]
        self.T=0.5
        while self.T<=5:
            E=self.calculate()
            self.E.append(E)
            self.TL.append(self.T)
            self.T+=0.2
        return self.TL,self.E
    def specific_heat(self):
        self.c=[]
        self.Tc=[]
        for i in range(0,len(self.TL)-1):
            c=(self.E[i+1]-self.E[i])/0.1
            self.c.append(c)
            self.Tc.append(0.5+i*0.2)
        return self.c,self.Tc
                
            
    def calculate(self):
        self.E_T=0
        E_avg=0
        E_k=0
        for k in range(0,3000):
            
            for i in range(0,self.l):
                for j in range(0,self.l):
                    self.L[i][j]=self.MC(i,j)
            
            for a in range(0,self.l):
               for b in range(0,self.l):
                   if 0<=a<self.l-1 and 0<=b<self.l-1:
                       E_k=-((self.L[a][b])*(self.L[a-1][b]+self.L[a+1][b]+self.L[a][b+1]+self.L[a][b-1]))
                   elif a==self.l-1 and b!=self.l-1:
                       E_k=-((self.L[a][b])*(self.L[a-1][b]+self.L[0][b]+self.L[a][b+1]+self.L[a][b-1]))
                   elif a!=self.l-1 and b==self.l-1:
                       E_k=-((self.L[a][b])*(self.L[a-1][b]+self.L[a+1][b]+self.L[a][0]+self.L[a][b-1]))
                   else:
                       E_k=-((self.L[a][b])*(self.L[a-1][b]+self.L[0][b]+self.L[a][0]+self.L[a][b-1]))
                   E_avg+=E_k  
            E_avg=E_avg/self.l**2/2
            self.E_T+=E_avg
        self.E_T=self.E_T/3000
        return self.E_T
    def MC(self,a,b):
        if 0<=a<self.l-1 and 0<=b<self.l-1:
            E_f=-2*((-self.L[a][b])*(self.L[a-1][b]+self.L[a+1][b]+self.L[a][b+1]+self.L[a][b-1]))
        elif a==self.l-1 and b!=self.l-1:
            E_f=-2*((-self.L[a][b])*(self.L[a-1][b]+self.L[0][b]+self.L[a][b+1]+self.L[a][b-1]))
        elif a!=self.l-1 and b==self.l-1:
            E_f=-2*((-self.L[a][b])*(self.L[a-1][b]+self.L[a+1][b]+self.L[a][0]+self.L[a][b-1]))
        else:
            E_f=-2*((-self.L[a][b])*(self.L[a-1][b]+self.L[0][b]+self.L[a][0]+self.L[a][b-1]))
        if E_f<=0:
            self.L[a][b]=-self.L[a][b]
        else:
            r=random.random()
            if r<=np.exp(-E_f/self.T):
                self.L[a][b]=-self.L[a][b]
            else:
                pass
        return self.L[a][b]
    def plot(self):

        pl.scatter(self.TL,self.E)
        pl.xlabel('Temperature')
        pl.ylabel('Energy per spin')
        pl.title('Ising model Energy versus Temperature') 
        pl.show()
    def plot_c(self):

        pl.scatter(self.Tc,self.c)
        pl.xlabel('Temperature')
        pl.ylabel('Specific heat per spin')
        pl.title('Ising model Specific heat versus Temperature') 
        pl.show()        

a=Monte_Carlo(10)
a.initialization()
a.T_variation()
a.specific_heat()
a.plot_c()
        

