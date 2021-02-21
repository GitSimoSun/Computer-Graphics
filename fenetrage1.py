#coding: utf_8


import numpy as np
import matplotlib.pyplot as plt


def rect(xmin, xmax, ymmin, ymax):
	return (xmin, xmax, ymmin, ymax)

def droite(a, b, c):
	return (a, b, c)

def droite_p(p1, p2):
	if p1[0] == p2[0]:
		return droite(1, 0, -p1[0])
	m = (p2[1] - p1[1]) / (p2[0] - p1[0])
	return droite(m, -1, p1[1] - m * p1[0])

def code(p, r):
	c = [0,0,0,0]
	c[0] = 0 if p[1] <= r[3] else 1
	c[1] = 0 if p[1] >= r[2] else 1
	c[2] = 0 if p[0] <= r[1] else 1
	c[3] = 0 if p[0] >= r[0] else 1
	return c

def produit_logique(c1, c2):
	c = np.array(c1) * np.array(c2)
	return list(c)

def inter(d1, d2):
	det = (d1[0] * d2[1]) - (d2[0] * d1[1])
	detx = (d1[1] * d2[2]) - (d2[1] * d1[2])
	dety = (d1[2] * d2[0]) - (d2[2] * d1[0])
	return (round(detx / det), round(dety / det))

def plot_line(ax, p1, p2, c):
	if p1[0] != p2[0]:
		pente = (p2[1] - p1[1]) / (p2[0] - p1[0])
		x = np.arange(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
		y = p1[1] + pente * (x - p1[0])	
		ax.plot(x, y, c)
	else:
		ymin = min(p1[1], p2[1])
		ymax = max(p1[1], p2[1])
		ax.vlines(p1[0], ymin, ymax, c)
	

def cohen_sutherland(ax1, ax2, p1, p2, r):
	#plots config
	pymax = max(p1[1], p2[1], r[3]) + 1
	pymin = min(p1[1], p2[1], r[2]) - 1
	pxmax = max(p1[0], p2[0], r[1]) + 1
	pxmin = min(p1[0], p2[0], r[0]) - 1
	ax1.set_xlim([pxmin, pxmax])
	ax2.set_xlim([pxmin, pxmax])
	ax1.set_ylim([pymin, pymax])
	ax2.set_ylim([pymin, pymax])
	#before
	plot_line(ax1, p1, p2, 'r')
	plot_line(ax1, (r[0], r[3]), (r[1], r[3]), 'b')
	plot_line(ax1, (r[0], r[2]), (r[1], r[2]), 'b')
	plot_line(ax1, (r[1], r[3]), (r[1], r[2]), 'b')
	plot_line(ax1, (r[0], r[3]), (r[0], r[2]), 'b')

	ds = droite_p(p1, p2)
	dh = droite_p((r[0], r[3]), (r[1], r[3]))
	db = droite_p((r[0], r[2]), (r[1], r[2]))
	dd = droite_p((r[1], r[3]), (r[1], r[2]))
	dg = droite_p((r[0], r[3]), (r[0], r[2]))
	c1 = code(p1, r)
	c2 = code(p2, r)
	zero = [0, 0, 0 , 0]
	while produit_logique(c1, c2) == zero and not(c1 == zero and c2 == zero):
		c = c1 if c1 != zero else c2
		if c[0] == 1:
			i = inter(ds, dh)
		elif c[1] == 1:
			i = inter(ds, db)
		elif c[2] == 1:
			i = inter(ds, dd)
		elif c[3] == 1:
			i = inter(ds, dg)
		if c == c1:
			p1 = i
			c1 = code(i, r)
		else:
			p2 = i
			c2 = code(i, r)
	#after
	if produit_logique(c1, c2) == zero:
		plot_line(ax2, p1, p2, 'r')
	plot_line(ax2, (r[0], r[3]), (r[1], r[3]), 'b')
	plot_line(ax2, (r[0], r[2]), (r[1], r[2]), 'b')
	plot_line(ax2, (r[1], r[3]), (r[1], r[2]), 'b')
	plot_line(ax2, (r[0], r[3]), (r[0], r[2]), 'b')
	
