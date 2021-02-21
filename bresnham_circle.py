import matplotlib.pyplot as plt


def circle(rayon):
    pk = 3 - (2 * rayon)
    pts = set()
    x = 0
    y = rayon
    while x <= y:
        pts.add((x,-y))
        pts.add((y,-x))
        pts.add((y,x))
        pts.add((x,y))
        pts.add((-x,y))        
        pts.add((-y,x))
        pts.add((-y,-x))
        pts.add((-x,-y))
        if pk < 0:
            pk = pk + (4 * x) + 6
        else:
            pk = pk + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1
    return pts