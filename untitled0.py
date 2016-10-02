# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:14:28 2016

@author: Administrator
"""
import pylab as pl
class two_types_of_decay:
   def __init__(self, number_of_A = 100, number_of_B=0, time_constant = 1, time_of_duration = 10, time_step
 = 0.1):
        self.n_A = [number_of_A]
        self.n_B = [number_of_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.nsteps = int(time_of_duration // time_step + 1)
   def calculate(self):
        for i in range(self.nsteps):
            NA = self.n_A[i] + ( self.n_B[i] / self.tau - self.n_A[i] / self.tau) * self.dt
            NB = self.n_B[i] + ( self.n_A[i] / self.tau - self.n_B[i] / self.tau) * self.dt
            self.n_A.append(NA)
            self.n_B.append(NB)
            self.t.append(self.t[i] + self.dt)
        for self.nsteps in range(100,101):
          print(self.n_A)
   def show_results(self):
        pl.plot(self.t, self.n_A)
        pl.plot(self.t, self.n_B, 'r') 
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(['$N_A$','$N_B$'])
        pl.grid()
        pl.show()
a = two_types_of_decay()
a.calculate()
a.show_results()
 