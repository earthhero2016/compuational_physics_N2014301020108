# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 23:03:43 2016

@author: Administrator
"""
import numpy as np
import pylab as pl
import random
class Monte_Carlo:
    def __init__(self,l,H):
        self.l=l
        self.H=H
    def initialization(self):
        self.L=[]
        for i in range(0,self.l):
            L_i=[]
            for j in range(0,self.l):
                L_i.append(1)
            self.L.append(L_i)    
    def T_variation(self):
        self.TL=[]
        self.M=[]
        self.T=0.5
        while self.T<=5:
            M=self.calculate()
            self.M.append(M)
            self.TL.append(self.T)
            self.T+=0.2
        return self.TL,self.M
            
            
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
        self.M_avg=abs(M_avg/1000)
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
        pl.plot(self.TL,self.M,'o')
        pl.xlabel('Temperature')
        pl.ylabel('Magnetization')
        pl.title('magetization vs. temperature H=100') 
        pl.show()
        
a=Monte_Carlo(10,100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
a.initialization()
a.T_variation()
a.plot()
        
