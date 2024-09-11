def puissance(a,b):
	try:
		a = int(a)
		b = int(b)
	except ValueError:
		raise TypeError("Seul les entiers sont autorisés")   	
	
	valeur=a

	for i in range(1,abs(b)):
		valeur *=a

	return valeur
			


