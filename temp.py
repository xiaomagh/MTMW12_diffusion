# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from _future_ import division,print,print_function
import numpy as np

N = int(1e4)
I = 0.0

for i in xrange(0,N):
    I += 0.01
    
print('the result is ',I)
