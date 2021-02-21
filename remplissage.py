#coding: utf_8

import pandas as pd
import numpy as np
from collections import defaultdict as dd
import math


def polygone(*args):
	return (args)

def plot_line(ax, p1, p2, c):
	if p1[0] != p2[0]:
		pente = (p2[1] - p1[1]) / (p2[0] - p1[0])
		x = x = np.linspace(min(p1[0], p2[0]), max(p1[0], p2[0]), 1000)
		y = p1[1] + pente * (x - p1[0])	
		ax.plot(x, y, c)
	else:
		ymin = min(p1[1], p2[1])
		ymax = max(p1[1], p2[1])
		ax.vlines(p1[0], ymin, ymax, c)
	
def plot_polygone(ax, poly, c):
	n = len(poly)
	for i in range(n):
		k = (i+1) % n
		plot_line(ax, poly[i], poly[k], c)

def scanLine(edge_table,y_min,y_max):
	output = []
	active_edge = []
	for curr_y in range(y_min,y_max+1):
		i=0
		while i<len(active_edge):
			if active_edge[i][2]==curr_y:
				active_edge.pop(i)
			else:
				i+=1
		for e in range(len(active_edge)):
			if e%2: active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.floor(active_edge[e][1]);
			else:	 active_edge[e][1]+=active_edge[e][3];active_edge[e][0]=math.ceil(active_edge[e][1]);
		active_edge+=edge_table[curr_y]
		active_edge.sort()
		for cur in range(0,len(active_edge)-1,2):
			for x in range(int(active_edge[cur][0]),int(active_edge[cur+1][0])+1):
				output.append((x, curr_y))

	return output

def filling(poly):
	vert = list(poly)
	vert+=[vert[0]]
	edge_table =dd(list)
	for i in range(len(vert)-1):
		x,y,x1,y1 =*vert[i],*vert[i+1]
		if y>y1:
			x,y,x1,y1 =x1,y1,x,y 
		if y==y1:
			continue
		else:	
			slope_inv = (x1-x)/(y1-y)
				 
		edge_table[y].append([x,x,y1,slope_inv])

	y_max = max(v[1] for v in vert)
	y_min = min(v[1] for v in vert)

	return scanLine(edge_table,y_min,y_max)

def generate_from_file(file):
	df = pd.read_csv(file, sep= ',')
	records = df.to_records(index=False)
	p = np.array(records.tolist())
	return tuple(p)


#poly = polygone((6, 1), (7, 1), (9, 2), (10, 5), (6, 7), (5, 7), (3, 6), (4, 3))