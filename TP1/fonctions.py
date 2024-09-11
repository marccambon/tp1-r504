def puissance(a,b):
	try:
		a = int(a)
		b = int(b)
	except ValueError:
		raise TypeError("Seul les entiers sont autorisés")   	
	return a**b

