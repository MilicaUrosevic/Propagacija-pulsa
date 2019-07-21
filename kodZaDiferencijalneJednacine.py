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
import matplotlib.pyplot as plt
from sympy import init_printing
init_printing()
integrate(t)
from sympy import Function, Indexed, Tuple, sqrt, dsolve, solve, Eq, Derivative, sin, cos, symbols
from sympy.abc import h, t, o, d, i
from sympy import solve, Poly, Eq, Function, exp
"zbog biblioteke sympy.abc rho00=x rho01=y rho10=z i rho11=w"
from sympy.abc import x, y, z, w
f = Function('f')
from sympy import Indexed, IndexedBase, Tuple, sqrt
from IPython.display import display
from sympy import *
from sympy.abc import *
from sympy.plotting import plot
init_printing()
h, t, o, d, i= symbols("h t o d i")
x, y, z, w = symbols("x y z w", cls = Function, Function = True)

eq1 = Eq(Derivative(y(t),t), i*(-d*h*y(t) + h*o*x(t)/2 - h*o*w(t)/2)/h)
eq2 = Eq(Derivative(z(t),t), i*(d*h*z(t) - h*o*x(t)/2 + h*o*w(t)/2)/h)
eq3 = Eq(Derivative(w(t),t),i*(-h*o*y(t)/2 + h*o*z(t)/2)/h )
"resenje je sa konstantama C1, C2 i C3"
soln = dsolve((eq1, eq2, eq3))
display(soln)
print(soln)

























