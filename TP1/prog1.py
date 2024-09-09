#print("Hello, World!")
#while True:
#    Number=int(input("Saisissez le nombre dont vous voulez connaire le carré:"))
#    print(Number*Number);
import fonctions as f


a=input("Saisissez un nombre: ")
b=input("Saisissez un second nombre: ")

if not type(a) is int:
    raise TypeError("Seul les entiers sont autorisés")
or type(b) is not int:
    raise TypeError("Seul les entiers sont autorisés")
else print(f.puissance(a,b));
