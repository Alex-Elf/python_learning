#https://ru-static.z-dn.net/files/d31/c63358f04dbb610c2702fff577957814.bmp
import math

def D(a, b, c):
	return b*b - 4*a*c
def Quad_eq(a, b, c):
	
	if a == 0:
		if b == 0:
			if c == 0:
				return 'INF'
			else:
				return None
		else:
			x = -(c/b)
			print(x)
			return x
	else:
		d = D(a,b,c)
		if d > 0:
			d = math.sqrt(d)
			x1 = (-b-d)/(2*a)
			x2 = (-b+d)/(2*a)
			return (x1, x2)
		else:
			if d == 0:
				x = -b/(2*a)
				return x
			else:
				return None