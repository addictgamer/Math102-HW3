
import math
import sympy

for n in range (1, 100):
	prime = n*n - 2

	if sympy.isprime(prime):
		print("One prime is: ", prime, ", produced by n = ", n)


# print("Here are all the nums: ")
# num_composite = 0
# for i in range(4297, 4328):
# 	#print(i)
# 	if sympy.isprime(i) == False:
# 		num_composite += 1
# 		print (i, " is composite")
# 	else:
# 		print (i, "is prime")

# print("Num composite: ", num_composite)
