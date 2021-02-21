#coding: utf_8


import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def f(x, expr):
	result = float(expr.subs(symbols('t'), x))
	return result

def df(x, expr):
	expr2 = diff(expr, symbols('t'))
	result =  float(expr2.subs(symbols('t'), x))
	return result

def matrix(x1, x2):
	l1 = [x1**3, x1**2, x1, 1]
	l2 = [x2**3, x2**2, x2, 1]
	l3 = [3 * x1**2, 2 * x1, 1, 0]
	l4 = [3 * x2**2, 2 * x2, 1, 0]
	return np.array([l1, l2, l3, l4])

def last(y1, y2, dy1, dy2):
	return np.array([y1, y2, dy1, dy2])

def parametres(a, b):
	x = np.linalg.solve(a, b)
	return x

def Q(x1, x2, y1, y2, dy1, dy2):
	a = matrix(x1, x2)
	b = last(y1, y2, dy1, dy2)
	x = parametres(a, b)
	t = symbols('t')

	return x[0] * t**3 + x[1] * t**2 + x[2] * t + x[3]






