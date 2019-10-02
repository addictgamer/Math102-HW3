
import math
import sympy

a = [i for i in sympy.sieve.primerange(2, 10000000)]

#print("a = " + str(a))


for i in range (1, len(a)):
	num_composites = a[i] - a[i-1]
	#print("Number of composites between ", a[i], " and ", a[i-1], " is ", num_composites)

	if num_composites == 31:
		print("Found 30 consecutive composites! Between: ", a[i-1], " and ", a[i])
		#break


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
