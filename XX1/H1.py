# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:02:12 2016

@author: Administrator
"""
import numpy as np
import pylab as pl
import random
class Monte_Carlo:
    def __init__(self,T,l):
        self.T=T
        self.l=l

    def initialization(self):
        self.L=[]
        for i in range(0,self.l):
            L_i=[]
            for j in range(0,self.l):
                L_i.append(1)
            self.L.append(L_i)    
    def H_variation(self):
        self.HL=[]
        self.M=[]
        self.H=-5
        while self.H<=5:
            M=self.calculate()
            self.M.append(M)
            self.HL.append(self.H)
            self.H+=0.2
        return self.HL,self.M    
    def calculate(self):
        
        M_avg=0
        M_k=0
        for k in range(0,1000):
            
            for i in range(0,self.l):
                for j in range(0,self.l):
                    self.L[i][j]=self.MC(i,j)
            
            for m in range(0,self.l):
               for n in range(0,self.l):
                   M_k+=self.L[m][n]
            M_k=M_k/self.l**2
            M_avg+=M_k
        self.M_avg=M_avg/1000
            
        return self.M_avg
    def MC(self,a,b):
        if 0<=a<self.l-1 and 0<=b<self.l-1:
            E_f=-2*(-self.L[a][b])*(self.L[a-1][b]+self.L[a+1][b]+self.L[a][b+1]+self.L[a][b-1])-2*self.H*(-self.L[a][b])
        elif a==self.l-1 and b!=self.l-1:
            E_f=-2*((-self.L[a][b])*(self.L[a-1][b]+self.L[0][b]+self.L[a][b+1]+self.L[a][b-1]))-2*self.H*(-self.L[a][b])
        elif a!=self.l-1 and b==self.l-1:
            E_f=-2*((-self.L[a][b])*(self.L[a-1][b]+self.L[a+1][b]+self.L[a][0]+self.L[a][b-1]))-2*self.H*(-self.L[a][b])
        else:
            E_f=-2*((-self.L[a][b])*(self.L[a-1][b]+self.L[0][b]+self.L[a][0]+self.L[a][b-1]))-2*self.H*(-self.L[a][b])
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
        #pl.subplot(122)
        pl.plot(self.HL,self.M,'o-')
        pl.xlabel('H')
        pl.ylabel('Magnetization')
        pl.title('Ising model Magnetization vs.H T=100') 
        pl.show()
        pl.ylim(-1.1,1.1)
a=Monte_Carlo(100,10)
a.initialization()
a.H_variation()
a.plot()
