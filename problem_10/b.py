
import math
import sympy

def k(n):
	return 36*n*n - 810*n + 2753

for i in range(0, 1000):
	n = k(i)
	if (False == sympy.isprime(n)) and (n >= 0):
		print("k(" + str(i) + ") = " + str(n) + " fails this!")
		break
