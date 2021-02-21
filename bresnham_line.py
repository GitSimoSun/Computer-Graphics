from math import *
import numpy as np



def droite_bresenham(Ax, Ay, Bx, By):
	
	data = []

	#les cas des octants (1-5) (2-6) (4,8) (3,8) sont symetriques il suffit donc de changer les cordonnées 
	if (Bx < Ax) or (By < Ay):
		Ax , Bx = Bx, Ax
		Ay , By = By, Ay

	
	Δx = Bx - Ax
	Δy = By - Ay
	pente  = Δy / Δx

	def position(x,y, Δx, Δy):
		return Δy*(x-Ax)-Δx*(y-Ay)


	Δx = abs(Δx)
	Δy = abs(Δy)	
	

	#on determine l'ordre d'incrementation pour les cordonnees selon l'octant correspond
	xinc = 1 if Bx > Ax else -1
	yinc = 1 if By > Ay else -1

	#début:
	x = Ax
	y = Ay

	if (abs(pente) < 1):
		md = (2 * (Δy - Δx))
		ma = (2 * Δy)
		C = 2 * Δy - Δx
		for i in range(min(Ax, Bx), max(Ax, Bx) + 1):
			data.append((x, y))
			if(C>=0):
			 	x += xinc 
			 	y += yinc 
			 	C += md
			else:
				x += xinc 
				C += ma	
	else:
		md = (2 * (Δx - Δy))
		ma = (2 * Δx)
		C = 2 * Δx - Δy
		for i in range(min(Ay, By), max(Ay, By) + 1):
			data.append((x, y))
			if(C>=0):
			 	x += xinc 
			 	y += yinc 
			 	C += md
			else:
				y += yinc 
				C += ma

	return data