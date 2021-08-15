def isprime(number):
	if number % 2 == 0:
		return False 
	for dividor in range(3, int(number ** 0.5) + 1, 2):
		if number % dividor == 0:
			return False 
	return True

number = 600851475143
for dividor in range(3, int(number ** 0.5) + 1, 2):
	if number % dividor == 0 and isprime(dividor):
		while  number % dividor == 0:
			number //= dividor
		result = dividor
print(result)
