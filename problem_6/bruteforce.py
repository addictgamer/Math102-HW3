
import math
import sympy

foundCounterexample = False

for n in range (1, 100):
	p = [1]
	p.extend([i for i in sympy.sieve.primerange(2, n+1)]) # all possible primes <= n

	# For every prime in list p, loop through all whole numbers less than or equal to the square root of n
	a = 0
	formulaWorks = False
	while a <= math.sqrt(n):
		for prime in p:
			if (prime + a*a == n):
				formulaWorks = True
				#print("For the positive integer ", n, ": p = ", prime, " and a = ", a, " (thus a^2 = ", a*a, ")")
				print(str(n) + " = " + str(prime) + " + " + str(a) + "^2 = " + str(prime) + " + " + str(a*a))
				break
		if (True == formulaWorks):
			break
		else:
			a += 1
	
	if (False == formulaWorks):
		print(n, " is just such a number for which this formula fails!")
		foundCounterexample = True
		break


if (False == foundCounterexample):
	print("Could not find any counterexamples :(")
