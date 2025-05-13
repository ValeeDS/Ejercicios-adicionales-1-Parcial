def es_palindromo(texto):
	return texto == texto[::-1]

print(es_palindromo("radar"))    # Imprime: True
print(es_palindromo("python"))   # Imprime: False
print(es_palindromo("reconocer")) # Imprime: True