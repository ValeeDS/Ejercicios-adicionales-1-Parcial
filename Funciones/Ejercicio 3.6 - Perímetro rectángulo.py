def calcular_perimetro(base, altura):
	perim = 2 * (base + altura)
	if base == 0 or altura == 0:
		return 0
	elif perim > 0:
		return perim
	else:
		return "El perímetro del rectángulo no puede ser negativo"

perimetro_1 = calcular_perimetro(5,4)
perimetro_2 = calcular_perimetro(3,-3)
perimetro_3 = calcular_perimetro(0,20)

print(perimetro_1) # Imprime: 18
print(perimetro_2) # Imprime: El perímetro del rectángulo no puede ser negativo
print(perimetro_3) # Imprime: 0
