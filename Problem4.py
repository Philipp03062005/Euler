def ispalindrome(number):
	return number == int(str(number)[::-1])

result = 0
for num1 in range(999, 700, -1):
	for num2 in range(999, 700, -1):
		if ispalindrome(num1 * num2):
			if num1 * num2 > result:
				result = num1 * num2
print (result)
