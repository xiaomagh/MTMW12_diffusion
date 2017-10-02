import numpy as np
import matplotlib.pyplot as plt
a=0.0
b=np.pi
e=[0.001,0.0001,0.00001,0.000001]
N=[4000,40000,400000,4000000]
arraySize=4
dx=np.zeros(arraySize)
I=np.zeros(arraySize)
error=np.zeros(arraySize)
n=np.zeros(3)
exact=-np.cos(b)+np.cos(a)
for i in xrange(0,3):
    dx[i] = (b-a)/N[i]
    I[i] =0.0
    for j in xrange(0,N[i]):
        I[i] += np.sin(a+(j+0.5)*dx[i])
    I[i] = I[i]*dx[i]
    error[i]=I[i]-exact
    
for k in xrange(0,2):
    for l in xrange(1,3):
        n[k] = (np.log(e[k])-np.log(e[l]))/(np.log(dx[k])-np.log(dx[l]))
        
print(I)
print(error)
plt.plot(dx,error)
print(n)