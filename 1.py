# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:49:07 2017

@author: zq806676
"""

import numpy as np

def maxiao(f,a,b,N=20,I=0.0):
    dx = (b-a)/N
    for i in xrange(0,N):
        I +=f((i+0.5)*dx+a)
    I *= dx
    return I

   # return I,i+1

#def mx01(x):
 #return 3.0*x-2.0

def mx02(x):
    return np.sin(x*1)
 
solution = maxiao(mx02,0.0,np.pi,N=20,I=0.0)
print(solution)
                               
 
 