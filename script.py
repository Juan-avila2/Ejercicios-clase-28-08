#Autor: Juan Felipe Avila Rodriguez

# Esto es una prueba para novatos

#1

texto = input("escriba un numero del 1 al 10")
print(texto)

#2 Tablas de multiplicar

numero_str = input("escriba un numero")

numero = int(numero_str)

a = 1

while a < 11:
	resultado = a * numero
	print(resultado)
	a += 1


#3 Factorial

factorial_str = input("escriba un numero")

factorial = int(factorial_str)


resultado = 1

while factorial > 0:
	resultado *= factorial
	factorial -= 1

print(resultado)
