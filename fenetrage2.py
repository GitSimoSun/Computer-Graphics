#coding: utf_8


import numpy as np
import matplotlib.pyplot as plt


fig, (ax1, ax2) = plt.subplots(1,2)

def point(x, y):
	return (x, y)

def polygone(*args):
	return (args)

def droite(a, b, c):
	return (a, b, c)

def droite_p(p1, p2):
	if p1[0] == p2[0]:
		return droite(1, 0, -p1[0])
	m = (p2[1] - p1[1]) / (p2[0] - p1[0])
	return droite(m, -1, p1[1] - m * p1[0])

def inter(d1, d2):
	det = (d1[0] * d2[1]) - (d2[0] * d1[1])
	detx = (d1[1] * d2[2]) - (d2[1] * d1[2])
	dety = (d1[2] * d2[0]) - (d2[2] * d1[0])
	return point(round(detx / det, 2), round(dety / det, 2))

def plot_line(ax, p1, p2, c):
	if p1[0] != p2[0]:
		pente = (p2[1] - p1[1]) / (p2[0] - p1[0])
		x = np.linspace(min(p1[0], p2[0]), max(p1[0], p2[0]), 1000)
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

def pos(p, p1, p2):
	expr = (p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0])
	return expr

def clipping(poly, p1, p2):
	print(poly)
	n = len(poly)
	s = list()
	d1 = droite_p(p1, p2)
	for i in range(n):
		k = (i+1) % n
		d2 = droite_p(poly[i], poly[k])
		if (pos(poly[i], p1, p2) > 0) and (pos(poly[k], p1, p2) > 0) :
			s.append(poly[k])
		elif (pos(poly[i], p1, p2) <= 0) and (pos(poly[k], p1, p2) > 0):
			s.append(inter(d1, d2))
			s.append(poly[k])
		elif (pos(poly[i], p1, p2) > 0) and (pos(poly[k], p1, p2) <= 0):
			s.append(inter(d1, d2))		
	return tuple(s)

def sutherland_hodgman(ax1, ax2, poly1, poly2):
	#plots config
	pymax = max(max(poly1, key = lambda tup : tup[1])[1], max(poly2, key = lambda tup : tup[1])[1]) + 1
	pymin = min(min(poly1, key = lambda tup : tup[1])[1], min(poly2, key = lambda tup : tup[1])[1]) - 1
	pxmax = max(max(poly1, key = lambda tup : tup[0])[0], max(poly2, key = lambda tup : tup[0])[0]) + 1
	pxmin = min(min(poly1, key = lambda tup : tup[0])[0], min(poly2, key = lambda tup : tup[0])[0]) - 1
	ax1.set_xlim([pxmin, pxmax])
	ax2.set_xlim([pxmin, pxmax])
	ax1.set_ylim([pymin, pymax])
	ax2.set_ylim([pymin, pymax])

	#before
	plot_polygone(ax1, poly1, 'b')
	plot_polygone(ax1, poly2, 'r')
	n = len(poly1)
	for i in range(n):
		k = (i+1) % n
		poly2 = clipping(poly2, poly1[i], poly1[k])
	#after
	plot_polygone(ax2, poly2, 'r')
	plot_polygone(ax2, poly1, 'b')
	

if __name__ == '__main__':
	#poly1 = polygone((15, 15), (15, 20), (20, 20), (20, 15))
	#poly2 = polygone((10,15), (20,25), (30,20))
	poly1 = polygone((0,2), (7,1), (7,5), (3, 6))
	poly2 = polygone((0,3), (6,3), (1,5))
	sutherland_hodgman(ax1, ax2, poly1, poly2)
	plt.show()