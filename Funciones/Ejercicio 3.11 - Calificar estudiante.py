def calificar_estudiante(nota):
	letra = "F"
	if nota >= 90:
		letra = "A"
	elif nota >= 80:
		letra = "B"
	elif nota >= 70:
		letra = "C"
	elif nota >= 60:
		letra = "D"
	
	return letra

print(calificar_estudiante(95))  # Imprime: A
print(calificar_estudiante(82))  # Imprime: B
print(calificar_estudiante(70))  # Imprime: C
print(calificar_estudiante(65))  # Imprime: D
print(calificar_estudiante(45))  # Imprime: F