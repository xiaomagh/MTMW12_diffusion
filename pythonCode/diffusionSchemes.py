# Numerical schemes for simulating diffusion for outer code diffusion.py

from __future__ import absolute_import, division, print_function
import numpy as np

# The linear algebra package for BTCS (for solving the matrix equation)
import scipy.linalg as la

def FTCS(phiOld, d, nt):
    "Diffusion of profile in phiOld using FTCS using non-dimensional"
    "diffusion coeffient, d"
    
    nx = len(phiOld)
    
    # new time-step array for phi
    phi = phiOld.copy()
    
    #array 
    
    #FCTS for all time steps
    for it in xrange(int(nt)):
        
                  