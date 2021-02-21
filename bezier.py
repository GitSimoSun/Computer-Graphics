#coding: utf_8

import pandas as pd
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def C(i, n):
	return factorial(n) / (factorial(i) * factorial(n-i))

def B(i, n):
	t = symbols('t')
	return C(i, n) * t**i * (1 - t)**(n - i)

def Q_bezier(p):
	if len(p[0]) == 2:
		q = np.array([0, 0])
	else:
		q = np.array([0, 0, 0])
	n = len(p)
	for i in range(n):
		q = q + p[i] *  B(i, n-1)
	return q

def plot_line(ax, p1, p2, c):
	ax.scatter(p1[0], p1[1], c='y')
	ax.scatter(p2[0], p2[1], c='y')
	ax.annotate(f'{p1[0], p1[1]}', (p1[0], p1[1]))
	ax.annotate(f'{p2[0], p2[1]}', (p2[0], p2[1]))
	if p1[0] != p2[0]:
		pente = (p2[1] - p1[1]) / (p2[0] - p1[0])
		x = np.arange(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
		y = p1[1] + pente * (x - p1[0])	
		ax.plot(x, y, c)
	else:
		ymin = min(p1[1], p2[1])
		ymax = max(p1[1], p2[1])
		ax.vlines(p1[0], ymin, ymax, c)

def generate_from_file(file):
	df = pd.read_csv(file, sep= ',')
	records = df.to_records(index=False)
	p = np.array(records.tolist())
	return tuple(p)