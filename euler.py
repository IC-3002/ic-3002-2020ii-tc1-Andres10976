def e_cuadratica(n):
	result = 1
	for i in range(1, n+1):
		fact = 1
		for i in range(1,i+1): 
			fact = fact * i 
		result += 1/fact
	return result


def e_lineal(n):
	result = 1
	fact=1
	for i in range(1, n+1):
		fact= fact * i
		result += 1/fact
	return result
