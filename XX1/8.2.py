# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:12:32 2016

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
        
    def calculate(self):
        self.t=[]
        self.M=[]
        M_k=0
        for k in range(0,1000):
            
            for i in range(0,self.l):
                for j in range(0,self.l):
                    self.L[i][j]=self.MC(i,j)
            self.t.append(k)
            for m in range(0,self.l):
               for n in range(0,self.l):
                   M_k+=self.L[m][n]
            M_k=M_k/self.l**2
            self.M.append(M_k)
            
        return self.t,self.M
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
        pl.subplot(224)
        pl.plot(self.t,self.M)
        pl.xlabel('time')
        pl.ylabel('Magnetization')
        pl.title('Ising model Magnetization vc. time T=4') 
        pl.ylim(-1.2,1.2)
        pl.show()
        
a=Monte_Carlo(4,10)
a.initialization()
a.calculate()
a.plot()
        