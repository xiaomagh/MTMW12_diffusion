#!/usr/bin/python

# Outer code for setting up the diffusion problem on a uniform
# grid and calling the function to perform the diffusion and plot.

from __future__ import absolute_import, division, print_function

import matplotlib.pyplot as plt

# read in all the linear advection schemes, initial conditions and other
# code associated with this application
execfile("diffusionSchemes.py")
execfile("diagnostics.py")
execfile("initialConditions.py")

def main():
    # Insert the rest of the code for main here
    "Diffuse a squareWave  between squareWaveMin and squareWaveMax on a"
    "domain between x = xmin and x = xmax spilit over nx spatial steps"
    "with diffusion coeffient K, time step dt for nt time steps"
    
    # Parameters
    xmin = 0.
    xmax = 1.
    nx = 41
    nt = 40
    dt = 0.1
    K = 1e-3
    squareWaveMin = 0.4
    squareWaveMax = 0.6
    xx = np.zeros(nx-2)
    
    # Derived parameters
    dx = (xmax - xmin)/(nx - 1)
    d = K*dt/dx**2   #Non-dimensional diffusion coeffient
    print("non-dimensional diffusion coefficient = ", d)
    print("dx = ", dx, "dt = ", dt, "nt = ", nt)
    print("end time = ", nt*dt)
    
    # spatial point for plotting and for defining initial conditions
    x = np.zeros(nx)
    for j in xrange(nx):
        x[j] = xmin + j*dx
    for k in xrange(1,nx-1):
        xx[k-1] = xmin + k*dx
        
    print('x=',x)
    print(xx)
    
    # Initial conditions
    phiOld = squareWave(x, squareWaveMin, squareWaveMax)
    # Analytic solution (of square wave profile in an infinite domain)
    phiAnalytic = analyticErf(x, K*dt*nt, squareWaveMin, squareWaveMax)
    
    # Diffusion using FTCS and BTCS
    phiFTCS = FTCS(phiOld.copy(), d, nt)
    phiBTCS = BTCS(phiOld.copy(), d, nt)
    
    # Calculate and print out error norms
    FTCSErrorNorm, FTCSError = L2ErrorNorm(phiFTCS, phiAnalytic)
    BTCSErrorNorm, BTCSError = L2ErrorNorm(phiBTCS, phiAnalytic)
    print("FTCS L2 error norm = ", FTCSErrorNorm)
    print("BTCS L2 error norm = ", BTCSErrorNorm)
    
    # plot the solutions
    font = {'size'  :15}
    plt.rc('font', **font)
    plt.figure(1)
    plt.clf()
    plt.ion()
    plt.plot(x, phiOld, label='Initial', color='black')
    plt.plot(x, phiAnalytic, label='Analytic', color='black', linestyle='-', linewidth=2)
    plt.plot(x, phiFTCS, label='FTCS', color='blue')
    plt.plot(x, phiBTCS, label='BTCS', color='red')
    plt.axhline(0, linestyle=':', color='black')
    plt.ylim([0,1.0])
    plt.legend(bbox_to_anchor=(1.1, 1))
    plt.xlabel('$x$')
    plt.savefig('FTCS_BTCS.pdf')
    
    font = {'size'  :15}
    plt.rc('font', **font)
    plt.figure(2)
    plt.clf()
    plt.ion()
    plt.plot(xx, FTCSError, label='FTCS Error', color='blue')
    plt.plot(xx, BTCSError, label='BTCS Error', color='red')
    plt.legend(bbox_to_anchor=(1.1, 1))
    plt.xlabel('$x$')
    plt.savefig('ERROR.pdf')
    
main()


#To run FTCS for a sufficiently long duration 
#def main02():
    # Parameters
    #xmin = 0.
    #xmax = 1.
    #nx = 41
    #nt = 40
    #K = 2e-3
    #squareWaveMin = 0.4
    #squareWaveMax = 0.6
    
     # Derived parameters
    
    #dx = (xmax - xmin)/(nx - 1)
    #d = K*dt/dx**2   #Non-dimensional diffusion coeffient
    #print("non-dimensional diffusion coefficient = ", d)
    #print("dx = ", dx, "dt = ", dt, "nt = ", nt)
    #print("end time = ", nt*dt)
    
     # spatial point for plotting and for defining initial conditions
    #x = np.zeros(nx)
    #for j in xrange(nx):
        #x[j] = xmin + j*dx

     # Initial conditions
    #phiOld = squareWave(x, squareWaveMin, squareWaveMax)
    # Analytic solution (of square wave profile in an infinite domain)
    #phiAnalytic = analyticErf(x, K*dt*nt, squareWaveMin, squareWaveMax)
    
     # Diffusion using FTCS 
    #phiFTCS = FTCS(phiOld.copy(), d, nt)
    
    
    
#main02()

    