# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:35:45 2017

@author: zq806676
"""
#from _future_ import division
import numpy as np
import matplotlib.pyplot as plt
nh_temperature = np.genfromtxt('nh_temperature.txt')

#Read in data
#print nh_temperature[0,0]

#plt.plot(nh_temperature[:,0],nh_temperature[:,7])
"""
plt.figure(1)
plt.plot(nh_temperature[:,0],nh_temperature[:,7])
plt.ylabel("Temperature anomaly (K)")
plt.xlabel("Year")
plt.title("July temperature anomaly time series")
plt.show()

plt.figure(2)
plt.plot(nh_temperature[:,0],nh_temperature[:,7],label="July")
plt.plot(nh_temperature[:,0],nh_temperature[:,1],label="January")
plt.ylabel("Temperature anomaly (K)")
plt.xlabel("Year")
plt.legend()
plt.title("July and January temperature anomaly time series")
plt.show()

july_std = np.std(nh_temperature[:,7])
print (july_std)

a = np.mean(nh_temperature[160:167,1:12],axis=0)
b = np.mean(nh_temperature[160:167,1:12],axis=1)
print(b)
"""
a = [1,2,3,4,5,6,7,8,9,10,11,12]
b = np.mean(nh_temperature[0:6,1:13],axis=0)
c = np.mean(nh_temperature[160:166,1:13],axis=0)
plt.figure(3)
plt.plot(a,b,label="earlier")
plt.plot(a,c,label="later")
plt.ylabel("Temperature anomaly (K)")
plt.xlabel("month")
plt.show()