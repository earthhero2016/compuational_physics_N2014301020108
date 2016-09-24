# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:26:46 2016

@author: Hushuxu
"""

import os
import time
i=os.system('cls')
time.sleep(1)
def printline(para):
   for line in para:
      print(line)
stick=['','','','','','','','','','','','']
A=['#','#','#','#','#','#','#','#','#','#','#','#']
space=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
for n in range(12):
    stick[n]+=A[n]+space[n]
for x in range(6):
    stick[0]=stick[0]
    stick[1]=space[1]+stick[1]
    stick[2]=2*space[2]+stick[2]
    stick[3]=3*space[3]+stick[3]
    stick[4]=4*space[4]+stick[4]
    stick[5]=5*space[5]+stick[5]
    stick[6]=6*space[6]+stick[6]
    stick[7]=7*space[7]+stick[7]
    stick[8]=8*space[8]+stick[8]
    stick[9]=9*space[9]+stick[9]
    stick[10]=10*space[10]+stick[10]
    stick[11]=11*space[11]+stick[11]
    time.sleep(0.5)
    i=os.system('cls')
    printline(stick)
    