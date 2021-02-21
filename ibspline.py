#coding: utf_8


import numpy as np
from sympy import *
import matplotlib.pyplot as plt




def H(x, mu, lam):
	n = len(mu)
	h_matrix = 2 * np.identity(n)
	for i in range(n-1):
		h_matrix[i+1][i] = mu[i+1]
	for i in range(n-1):
		h_matrix[i][i+1] = lam[i]
	return h_matrix

#divided difference
def fdd(x, y, i, k):
	if k == 0:
		return y[i]
	if k == 1:
		return (y[i+1] - y[i]) / (x[i+1] - x[i])
	if k == 2:
		return (fdd(x, y, i+1, 1) - fdd(x, y, i, 1)) / (x[i+2] - x[i])

#cubic spline
def get_s(t, x, y, h, m):
	n = len(x)
	s = list()
	for i in range(1, n):
		term1 = (m[i-1] * (x[i] - t)**3) / (6 * h[i-1])
		term2 = (m[i] * (t - x[i-1])**3) / (6 * h[i-1])
		term3 = (y[i-1] - (m[i-1] * h[i-1]**2) / 6) * (x[i] - t) / h[i-1]
		term4 = (y[i] - (m[i] * h[i-1]**2) / 6) * (t - x[i-1]) / h[i-1]
		s.append(term1 + term2 + term3 + term4)
	for i in range(n-1):
		if x[i] <= t <= x[i+1]:
			return s[i]

def s_ibspline(t, p, boundry_condition, c1, c2):
	x = np.array([pp[0] for pp in p])
	y = np.array([pp[1] for pp in p])
	n = len(x)
	h = [(x[i] - x[i-1]) for i in range(1, n)]
	if (boundry_condition == 1):
		mu = np.array([0] + [(h[i] / (h[i] + h[i+1])) for i in range(n-2)] + [1])
		lam = 1 - mu
		df0 = c1
		dfn = c2
		d0 = [(fdd(x, y, 0, 1) - df0) / h[0]]
		dn = [(dfn - fdd(x, y, n-2, 1)) / h[-1]]
		d = 6 * np.array(d0 + [fdd(x, y, i-1,2 ) for i in range(1, n-1)] + dn)
	else:
		mu = np.array([1] + [(h[i] / (h[i] + h[i+1])) for i in range(n-2)] + [0])
		lam = 1 - mu
		ddf0 = c1
		ddfn = c2
		d0 = [2 * ddf0]
		dn = [2 * ddfn]
		d = np.array(d0 + [6 * fdd(x, y, i-1,2 ) for i in range(1, n-1)] + dn)
	hm = H(x, mu, lam)
	m = np.linalg.solve(hm, d)
	return get_s(t, x, y, h, m)