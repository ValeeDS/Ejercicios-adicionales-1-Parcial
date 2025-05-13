def verificar_positividad(num):
	if num > 0:
		return f"El número {num} es positivo."
	elif num < 0:
		return f"El número {num} es negativo."
	else:
		return f"El número es cero."

print(verificar_positividad(5))   # Imprime: El número 5 es positivo.
print(verificar_positividad(-3))  # Imprime: El número -3 es negativo.
print(verificar_positividad(0))   # Imprime: El número es cero.