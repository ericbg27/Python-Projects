def CountPrimes(num):
	primeCounter = 0

	if num == 2:
		primeCounter += 1
		return primeCounter
	elif num > 2 and num <= 4:
		primeCounter += 2
		return primeCounter
	elif num > 4 and num <= 6:
		primeCounter += 3
		return primeCounter

	primeCounter += 3

	for i in range(7, num+1, 2):

		j = 5
		w = 2

		isPrime = True

		if i % 3 == 0:
			isPrime = False
		else:
			while True:
				if i % j == 0:
					isPrime = False
					break

				j += w
				w = 6 - w

				if(j*j > i):
					break

		if isPrime == True:
			print(i)
			primeCounter += 1

	return primeCounter

print("test: " + str(CountPrimes(100)))