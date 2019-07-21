#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:13:44 2019

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
from sympy.abc import h, t, o, d, i
from sympy import solve, Poly, Eq, Function, exp
"zbog biblioteke sympy.abc rho00=x rho01=y rho10=z i rho11=w"
from sympy.abc import x, y, z, w
#f = Function('f')
from sympy import Indexed, IndexedBase, Tuple, sqrt
from IPython.display import display
init_printing()

h, t, o, d, i= symbols("h t o d i")
x, y, z, w = symbols("x y z w", cls = Function, Function = True)
eq1 = Eq(Derivative(x(t),t), x(t)-i*(o*y(t)/2 - o*z(t)/2))
eq2 = Eq(Derivative(y(t),t), -y(t)-i*(-d*y(t) + o*x(t)/2 - o*w(t)/2))
eq3 = Eq(Derivative(z(t),t), -z(t)-i*(d*z(t) - o*x(t)/2 + o*w(t)/2))
eq4 = Eq(Derivative(w(t),t),-w(t)-i*(-o*y(t)/2 + o*z(t)/2))
#constants = solve((soln[0].subs(t,0).subs(y(0),0), soln[0].subs(t,0).subs(z(0),0), soln[0].subs(t,0).subs(w(0),0)),{C1,C2,C3})
soln = dsolve((eq1, eq2, eq3, eq4),ics={x(0):1, y(0):0, z(0):0, w(0):0})
display(soln)