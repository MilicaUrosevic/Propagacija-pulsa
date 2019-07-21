#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:43:08 2019

@author: milicaurosevic
"""
"kod za resavanje sistema ODE sa razdvajanjem promenljivih"
import numpy as np
import sympy
from sympy import *
from sympy.abc import *
from sympy.plotting import plot
#from scipy import integrate
#import matplotlib.pyplot as plt
from sympy import init_printing
init_printing()
from sympy import Function, Indexed, Tuple, sqrt, dsolve, solve, Eq, Derivative, sin, cos, symbols
from sympy.abc import h, t, o, d
from sympy import solve, Poly, Eq, Function, exp
"zbog biblioteke sympy.abc rho00=x rho01=y rho10=z i rho11=w"
#ro11 = 1 - ro00
#f = Function('f')
from sympy import Indexed, IndexedBase, Tuple, sqrt
from IPython.display import display
init_printing()

ro00=sympy.Symbol('ro00')
ro01=sympy.Symbol('ro01')
ro10=sympy.Symbol('ro10')
i = sympy.I

h, t, o, d= symbols("h t o d")
ro00, ro01, ro10= symbols("ro00 ro01 ro10", cls = Function, Function = True)
eq1 = Eq(Derivative(ro00(t),t), ro00(t)-i*(o*ro01(t)/2 - o*ro10(t)/2))
eq2 = Eq(Derivative(ro01(t),t), -ro01(t)-i*(-d*ro01(t) + o*ro00(t)/2 - o*(1-ro00(t))/2))
eq3 = Eq(Derivative(ro10(t),t), -ro10(t)-i*(d*ro10(t) - o*ro00(t)/2 + o*(1-ro00(t))/2))
#eq4 = Eq(Derivative(ro11(t),t),-w(t)-i*(-o*y(t)/2 + o*z(t)/2))
#constants = solve((soln[0].subs(t,0).subs(y(0),0), soln[0].subs(t,0).subs(z(0),0), soln[0].subs(t,0).subs(w(0),0)),{C1,C2,C3})
soln = dsolve((eq1, eq2, eq3),ics={ro00(0):1, ro01(0):0, ro10(0):0})
display(soln)