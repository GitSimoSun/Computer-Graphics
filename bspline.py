#coding: utf_8


import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def N(i, j, t, T):
	if j == 0:
		if (T[i] <= t < T[i+1]) and (T[i] <= t < T[i+1]):
			return 1
		return 0
	first = last = 0
	if (T[i + j] - T[i]) != 0:
		first = (t - T[i]) * N(i, j-1, t, T) / (T[i + j] - T[i])
	if (T[i + j + 1] - T[i + 1]) != 0:
		last = (T[i + j + 1] - t) * N(i + 1, j-1, t, T) / (T[i + j + 1] - T[i + 1])
	return first + last

def S_abspline(p, k, t):
	if len(p[0]) == 2:
		s = np.array([0, 0])
	else:
		s = np.array([0, 0, 0])
	n = len(p)
	m = k + n + 1
	#knots
	T = [0] * k + [i / (m - 2*k -1) for i in range(m - 2*k)] + [1] * k
	for i in range(n):
		s = s + N(i, k, t, T) * p[i]
	return s

def plot_line(p1, p2, c):
	plt.scatter(p1[0], p1[1], c='y')
	plt.scatter(p2[0], p2[1], c='y')
	plt.annotate(f'{p1[0], p1[1]}', (p1[0], p1[1]))
	plt.annotate(f'{p2[0], p2[1]}', (p2[0], p2[1]))
	if p1[0] != p2[0]:
		pente = (p2[1] - p1[1]) / (p2[0] - p1[0])
		x = np.arange(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
		y = p1[1] + pente * (x - p1[0])	
		plt.plot(x, y, c)
	else:
		ymin = min(p1[1], p2[1])
		ymax = max(p1[1], p2[1])
		plt.vlines(p1[0], ymin, ymax, c)


if __name__ == '__main__':

	p = np.array([(2.5, 1), (1, 4), (3, 9), (6, 7.5), (5, 4), (7, 1), (9, 3), (8, 8)])
	#p = np.array([(2.5, 1, 0), (1, 4, 0), (3, 9, 0), (6, 7.5, 0), (5, 4, 0), (7, 1, 0), (9, 3, 0), (8, 8, 0)])
	#p = np.array([(1,0), (1,1), (-1,1), (-1,0), (-1,-1), (1,-1), (1,0)])
	#p = np.array([(0, 1), (1, 1), (3, 4), (4, 2), (5, 3), (6, 4), (7, 3)])
	'''
	df = pd.read_csv("data.csv", sep= ',')
	records = df.to_records(index=False)
	p = np.array(records.tolist())'''
	n = len(p)
	d = len(p[0])
	if d == 2:
		fig, ax1 = plt.subplots()
		for i in range(n -1):
			k = (i+1)
			plot_line(p[i], p[k], 'r')
		t = np.linspace(0, 1, 1000, endpoint = False)
		x = [S_abspline(p, 2, k)[0] for k in t]
		y = [S_abspline(p, 2, k)[1] for k in t]
		ax1.plot(x, y, 'b')
		ax1.spines['left'].set_position('zero')
		ax1.spines['right'].set_color('none')
		ax1.yaxis.tick_left()
		ax1.spines['bottom'].set_position('zero')
		ax1.spines['top'].set_color('none')
		ax1.xaxis.tick_bottom()
		plt.show() 
	else:
		fig = plt.figure()
		ax = fig.add_subplot(projection='3d')
		t = np.linspace(0, 1, 3000, endpoint = False)
		result = np.array([S_abspline(p, 2, k) for k in t])
		X = [r[0] for r in result]
		Y = [r[1] for r in result]
		Z = [r[2] for r in result]
		x = np.reshape(X, (50, 60))
		y = np.reshape(Y, (50, 60))
		z = np.reshape(Z, (50, 60))
		ax.plot_wireframe(x,y,z)
		plt.show()