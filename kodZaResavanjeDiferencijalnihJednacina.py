#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 00:09:01 2019

@author: milicaurosevic
"""

import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt

def model(t, z):
    I=complex(0,1)
    o=1
    d=0
    ro00 = z[0]
    ro01 = z[1]
    ro10 = z[2]
    ro11 = z[3]    
    
    dro00dt = ro11 - I*(o*ro01/2 - o*ro10/2)
    dro01dt = -ro01 - I*(-d*ro01 + o*ro00/2 - o*ro11/2)
    dro10dt = -ro10 - I*(d*ro10 - o*ro00/2 + o*ro11/2)
    dro11dt = -ro11 - I*(-o*ro01/2 + o*ro10/2)
    dzdt = [dro00dt,dro01dt,dro10dt,dro11dt]
    return dzdt

z0 = np.array([1,0,0,0], dtype='complex')
t = np.linspace(0,5,50000)
z = solve_ivp(model, (0, 5), z0)
print(z.y.shape)
t=z.t
z=np.transpose(z.y)

ro00 = z[:,0]
ro01 = z[:,1]
ro10 = z[:,2]
ro11 = z[:,3]

plt.plot(t, ro00.real+ro11.real, label='zbir realnih delova rho11 i rho00')
plt.ylabel('\rho00.real+\rho11.real')
plt.xlabel('vreme')
plt.legend(loc='best')
plt.show()
plt.plot(t,ro00.real,'g:',label='ro00 realni deo')
plt.plot(t,ro01.real,'b-',label='ro01 realni deo')
plt.plot(t,ro10.real,'r--',label='ro10 realni deo')
plt.plot(t,ro11.real,'m-',label='ro11 realni deo')
#plt.plot(t, ro00.real+ro11.real)
plt.ylabel('realni delovi \rhomn')
plt.xlabel('vreme')
plt.legend(loc='best')
plt.show()

plt.plot(t,ro00.imag,'g:',label='ro00 imaginarni deo')
plt.plot(t,ro01.imag,'b-',label='ro01 imaginarni deo')
plt.plot(t,ro10.imag,'r--',label='ro10 imaginarni deo')
plt.plot(t,ro11.imag,'m-',label='ro11 imaginarni deo')
#plt.plot(t, ro00.real+ro11.real)
plt.ylabel('imaginarni delovi rhomn')
plt.xlabel('vreme')
plt.legend(loc='best')
plt.show()

#jedan ro00 i ro11, posle im i real