#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 00:09:01 2019

@author: milicaurosevic
"""

import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt


I=complex(0,1)
op=1/2
oc=1/2
dp=0
dc=0

gamma00=1
gamma01=1
gamma02=1
gamma10=1
gamma11=1
gamma12=1
gamma20=1
gamma21=1
gamma22=1

Gamma00=1
Gamma01=1
Gamma02=1
Gamma10=1
Gamma11=1
Gamma12=1
Gamma20=1
Gamma21=1
Gamma22=1


def model(z,t):
    ro00 = z[0]
    ro01 = z[1]
    ro02 = z[2]
    ro10 = z[3]  
    ro11 = z[4]
    ro12 = z[5]
    ro20 = z[6]
    ro21 = z[7] 
    ro22 = z[8]   
    dro00dt = Gamma01*ro11 + Gamma02*ro22 - I*(op*ro02 - op*ro20)/2
    dro01dt = -gamma01*ro01 - I*(oc*ro02/2 - op*ro21/2 - ro01*(dc - dp))
    dro02dt = -gamma02*ro02 - I*(dp*ro02 + oc*ro01/2 + op*ro00/2 - op*ro22/2)
    dro10dt = -gamma10*ro10 - I*(-oc*ro20/2 + op*ro12/2 + ro10*(dc - dp))
    dro11dt = -Gamma01*ro11 + Gamma12*ro22 - I*(oc*ro12/2 - oc*ro21/2)
    dro12dt = -gamma12*ro12 - I*(dp*ro12 + oc*ro11/2 - oc*ro22/2 + op*ro10/2 + ro12*(dc - dp))
    dro20dt = -gamma20*ro20 - I*(-dp*ro20 - oc*ro10/2 - op*ro00/2 + op*ro22/2)
    dro21dt = -gamma21*ro21 - I*(-dp*ro21 - oc*ro11/2 + oc*ro22/2 - op*ro01/2 - ro21*(dc - dp))
    dro22dt = -Gamma02*ro22 - Gamma12*ro22 - I*(-oc*ro12/2 + oc*ro21/2 - op*ro02/2 + op*ro20/2)
    dzdt = [dro00dt, dro01dt, dro02dt, dro10dt, dro11dt, dro12dt, dro20dt, dro21dt, dro22dt]
    return dzdt

z0 = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0], dtype='complex')
t = np.linspace(0,5,50000)
z = solve_ivp(model, (0, 5), z0)
print(z.y.shape)
t=z.t
z=np.transpose(z.y)

ro00 = z[:,0]
ro01 = z[:,1]
ro02 = z[:,2]
ro10 = z[:,3]
ro11 = z[:,4]
ro12 = z[:,5]
ro20 = z[:,6]
ro21 = z[:,7]
ro22 = z[:,8]

plt.plot(t, ro00.real+ro11.real+ro00.real, label='zbir realnih delova ro22 i rho11 i rho00')
plt.ylabel('\rho00.real+\rho11.real')
plt.xlabel('vreme')
plt.legend(loc='best')
plt.show()
plt.plot(t,ro00.real,'g:',label='ro00 realni deo')
plt.plot(t,ro01.real,'b:',label='ro01 realni deo')
plt.plot(t,ro02.real,'r:',label='ro02 realni deo')
plt.plot(t,ro10.real,'m:',label='ro10 realni deo')
plt.plot(t,ro11.real,'g-',label='ro11 realni deo')
plt.plot(t,ro12.real,'b-',label='ro12 realni deo')
plt.plot(t,ro20.real,'r-',label='ro20 realni deo')
plt.plot(t,ro21.real,'m-',label='ro21 realni deo')
plt.plot(t,ro22.real,'m--',label='ro22 realni deo')
#plt.plot(t, ro00.real+ro11.real)
plt.ylabel('realni delovi \rhomn')
plt.xlabel('vreme')
plt.legend(loc='best')
plt.show()

plt.plot(t,ro00.imag,'g:',label='ro00 imaginarni deo')
plt.plot(t,ro01.imag,'b:',label='ro01 imaginarni deo')
plt.plot(t,ro02.imag,'r:',label='ro02 imaginarni deo')
plt.plot(t,ro10.imag,'m:',label='ro10 imaginarni deo')
plt.plot(t,ro11.imag,'g-',label='ro11 imaginarni deo')
plt.plot(t,ro12.imag,'b-',label='ro12 imaginarni deo')
plt.plot(t,ro20.imag,'r-',label='ro20 imaginarni deo')
plt.plot(t,ro21.imag,'m-',label='ro21 imaginarni deo')
plt.plot(t,ro22.imag,'m--',label='ro22 imaginarni deo')
#plt.plot(t, ro00.real+ro11.real)
plt.ylabel('imaginarni delovi rhomn')
plt.xlabel('vreme')
plt.legend(loc='best')
plt.show()

#jedan ro00 i ro11, posle im i real