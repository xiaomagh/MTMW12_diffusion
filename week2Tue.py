# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 13:50:02 2017

@author: zq806676
"""

def solveByBisect(f,a,b,nmax=100,e=1e-6):
    "solve function f b bisection method."
    "solve to error e starting from a and b. Maximum nmax iterations."
    
    #Iterate until the solution is within the error or too many iterations
    for it in range(nmax):
        c = 0.5*(a+b)
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
#        if abs(f(c)) < abs(e):
#            break    #Break out of the for loop
#    else:            #If you haven't broken out of the for loop by the end,
                     #raise an exception
#        raise Exception("No root found by solveByBisect")
    if nmax <= 0:
        raise ValueError('Argument nmax to solveByBisect should be >0')
    if e <= 0:
        raise ValueError('Argument e to solveByBisect should be >0')
    if not(isinstance(a,float)) or not(isinstance(b,float)):
        raise TypeError('Arguments a and b to solveByBisect should be a floats')
    if not (callable(f)):
        raise Exception('A callable function must be sent to solveByBisect' )
        
    return c,it+1
    
import numpy as np
assert abs(np.cos(solveByBisect(np.cos,0,np.pi)[0])) < 1e-6, \
       "solveByBisect gave the wrong answer for cos"
def mx01(x):
    return 2*x+3
    
solution = solveByBisect(mx01,-10.,10.)[0]
print(solution)
assert abs(mx01(solveByBisect(mx01, -10.,10.)[0])) < 1e-6,\
       "solveByBisect gave the wrong answer for a linear function"
       
try:
    solveByBisect(np.cos,-1.,1.)
except:
    pass
else:
    print("Error in solveByBisect, an exception should be raised as there is no root of cos between -1. and 1.")

try:
    solveByBisect(0,1.,3.)
except:
    pass
else:
    print("Error in solveByBisect, an exception should be raised if no function is passed")
    
try:
    solveByBisect(np.cos,1.,1.,0)
except ValueError:
    pass
else:
    print("Error in solveByBisect,an exception should be raised if nmax <= 0")
    
try:
    solveByBisect(np.cos,1.,1.,1,0)
except ValueError:
    pass
else:
    print("Error in solveByBisect, an exception should be raised if e <= 0")
     
   