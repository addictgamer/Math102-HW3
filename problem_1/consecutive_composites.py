import math
import sympy

def consecutiveComposites(num):
	num_consecutive = 0
	while sympy.isprime(num) == False:
		num_consecutive += 1
		num += 1
	return num_consecutive

for i in range(2, 100):
	#prime = math.factorial(i) + 1
	prime = sympy.primorial(i, nth=False) + 1
	#print("primorial of " + str(i) + " = " + str(prime))
	#if isPrime(prime):
	if sympy.isprime(prime):
		print("i " + str(i) + " passed")

		#Now find how many consecutive composites there are.
		# num_consecutive = 0
		# composite = prime + 1
		# while sympy.isprime(composite) == False:
		# 	num_consecutive += 1
		# 	composite += 1
		num_consecutive = consecutiveComposites(prime+1)
		
		print("Found " + str(num_consecutive) + " consecutive composite numbers after ", i, "#+1")

		if (num_consecutive > 40):
			print ("There are at least 40 consecutive composite numbers after ", prime, ", which is ", i, "# + 1")
			#print("Found " + str(num_consecutive) + " consecutive composite numbers.")

print("Consecutive prime numbers after 31#+1+32 = ", consecutiveComposites(sympy.primorial(31, nth=False)+1+32), " and that number is: ", sympy.primorial(31, nth=False)+1+32)