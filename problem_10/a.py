
import math
import sympy

def h(n):
	return 103*n*n - 3945*n + 34381

for i in range(0, 100):
	n = h(i)
	if (False == sympy.isprime(n)) and (n >= 0):
		print("h(" + str(i) + ") = " + str(n) + " fails this!")
		break
