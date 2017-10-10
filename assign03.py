# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:18:16 2017

@author: zq806676
"""
import numpy as np
import matplotlib.pyplot as plt

pa = 1e5
pb = 200
f = 1e-4
dens = 1
l = 2.4e6

ymin = 0.0
ymax = 1e6
N =10
dy = (ymax - ymin)/N   

p = np.zeros(N+1)
gradp = np.zeros(N+1)
u = np.zeros(N+1)
e = np.zeros(N+1)
y = np.zeros(N+1)
a = np.zeros(N+1)

for i in xrange(0,N+1):
    y[i] = ymin + dy*i

for i in xrange(0,N+1):
    p[i] = pa + pb*np.cos(y[i]*np.pi/l)

gradp[N] = (3*p[N] - 4*p[N-1] + p[N-2])/(2*dy)
gradp[N-1] = (3*p[N-1] - 4*p[N-2] + p[N-3])/(2*dy)
for i in xrange(0,N-1):
    gradp[i]=(4*p[i+1] - 3*p[i] - p[i+2])/(dy*2)

for i in xrange(0,N+1):
    u[i] = -gradp[i]/(dens*f)
    e[i] = abs(pb*np.pi*np.sin(np.pi*y[i]/l)/(dens*f*l) - u[i])

print(e)
plt.plot(y,e)

gradp[0] = (p[1] - p[0])/dy
gradp[N] = (p[N] - p[N-1])/dy
for i in xrange(1,N):
    gradp[i]=(p[i+1] - p[i-1])/(dy*2)
    
for i in xrange(0,N+1):
    u[i] = -gradp[i]/(dens*f)
    a[i] = abs(pb*np.pi*np.sin(np.pi*y[i]/l)/(dens*f*l) - u[i])
    
plt.plot(y,a)