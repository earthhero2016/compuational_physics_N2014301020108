# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 22:59:02 2016

@author: Administrator
"""
from __future__ import division
import numpy as np
import pylab as pl
import matplotlib
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
class SOR:
    def __init__(self):
        pass
    def initialization(self):
        self.dist=[]
        for i in range(201):
            V_i=[]
            for j in range(201):
                if j==150 and i==150:
                    V=10

                else:
                    V=0
                V_i.append(V)
            self.dist.append(V_i)
        return 0
    def update_V(self):
        self.delta_V = 0
        for i in range(201):
            for j in range(201):
                if i==0 or j==0 or i==200 or j==200:
                    pass
                elif j==150 and i==150:
                    pass
                elif i==0 or i==200 or j==0 or j==200:
                    pass
                elif i==1 or j==1:
                    V_new = (self.dist[i+1][j]+self.dist[i-1][j]+self.dist[i][j+1]+self.dist[i][j-1])/4
                    V_old = self.dist[i][j]
                    self.delta_V += (1+np.pi/40000)/2*abs(V_new -V_old)
                    self.dist[i][j] = V_new
                else:
                    V_new1 = (self.dist[i][j]+self.dist[i-2][j]+self.dist[i-1][j+1]+self.dist[i-1][j-1])/4
                    V_new2 = (self.dist[i+1][j-1]+self.dist[i-1][j-1]+self.dist[i][j]+self.dist[i][j-2])/4
                    V_old = self.dist[i][j]
                    V_new=(self.dist[i+1][j]+V_new1+self.dist[i][j+1]+V_new2)/4
                    self.delta_V += (1+np.pi/40000)/2*abs(V_new -V_old)
                    self.dist[i][j] = V_new
        return self.dist,self.delta_V
    def Laplace_calculate(self):
         self.delta_V = 2
         epsilon = 0.4
         N=0

         while self.delta_V>=epsilon:
            self.dist,self.delta_V = self.update_V()
            N+=1
         print(self.delta_V,N)
         return self.dist
    def plot_field(self):
        Ex = deepcopy(self.dist)
        Ey = deepcopy(self.dist)
        E =  deepcopy(self.dist)

        for i in range(201):
            for j in range(201):
                if i == 0 or i == 200 or j == 0 or j == 200:
                    Ex[i][j] = 0
                    Ey[i][j] = 0
                elif i==150 and j==150:
                    Ex[i][j] = 0
                    Ey[i][j] = 0
                else:
                    Ex_value = -(self.dist[i+1][j] - self.dist[i-1][j])/0.02
                    Ey_value = -(self.dist[i][j+1] - self.dist[i][j-1])/0.02
                    Ex[i][j] = Ex_value
                    Ey[i][j] = Ey_value

        for i in range(201):
            for j in range(201):
                E_value = np.sqrt(Ex[i][j]**2 + Ey[i][j]**2)
                E[i][j] = E_value
            
        fig0, ax0 = pl.subplots()
        strm = ax0.streamplot(X, Y, np.array(Ey), np.array(Ex), color=np.array(E), linewidth=2, cmap=pl.cm.autumn)
        fig0.colorbar(strm.lines)
        ax0.set_xlabel('x')
        ax0.set_ylabel('y')
        ax0.set_title('Electric field')
        pl.show()
   
    def plot_surface(self):
         fig = pl.figure()
         ax = fig.add_subplot(111, projection='3d')
         ax.plot_surface(X, Y, self.dist,rstride=5, cstride=5,cmap=cm.YlGnBu_r)
         ax.set_xlabel('x')
         ax.set_ylabel('y')
         ax.set_zlabel('voltage(V)')
         ax.set_title('voltage distribution')

    def plot_contour(self):
         pl.figure()
         CS = pl.contour(X,Y,self.dist,10)
         pl.clabel(CS, inline=1, fontsize=15)
         pl.title('Equipotential lines')
         pl.xlabel('x')
         pl.ylabel('y')
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'
a=SOR()
a.initialization()

x = np.linspace(0,200,201)
y = np.linspace(0,200,201)
X, Y = np.meshgrid(x, y)
a.Laplace_calculate()
a.plot_field()
a.plot_surface()
a.plot_contour()
