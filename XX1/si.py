# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:58:55 2016

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
       
        self.f=np.linspace(0,0,10)
        
        for k in range(0,3000):
            
            for i in range(0,self.l):
                for j in range(0,self.l):
                    self.L[i][j]=self.MC(i,j)
            
            for n in range(6,16):
                s_n=0
                s_n=self.L[10][5]*self.L[10][n]
                self.f[n-6]+=s_n/3000
        print(self.f)
            
        return self.f
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
        self.n=np.linspace(1,10,10)
        pl.subplot(224)
        pl.plot(self.n,self.f,'.--')
        pl.xlabel('i=Distance')
        pl.ylabel(r'f(i)=<$s_i$$s_o$>')
        pl.ylim(-0.1,1.1)
        pl.title('Ising model Correlations T=4') 
        pl.show()
        
a=Monte_Carlo(4,20)
a.initialization()
a.calculate()
a.plot()
