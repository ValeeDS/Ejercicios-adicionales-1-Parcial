def calcular_area(base,altura):
	area = base * altura
	if area >= 0:
		return area
	else:
		return "El área del rectángulo no puede ser negativa"

area_1 = calcular_area(5,4)
area_2 = calcular_area(3,-3)
area_3 = calcular_area(0,20)

print(area_1) # Imprime: 20
print(area_2) # Imprime: El área del rectángulo no puede ser negativa
print(area_3) # Imprime: 0