def calcular_area(base,altura):
	area = base * altura
	if area >= 0:
		return area
	else:
		return "El área del rectángulo no puede ser negativa"

def calcular_perimetro(base, altura):
	perim = 2 * (base + altura)
	if base == 0 or altura == 0:
		return 0
	elif perim > 0:
		return perim
	else:
		return "El perímetro del rectángulo no puede ser negativo"

def informancion_del_rectangulo(base, altura):
	print(f"Rectángulo con base {base} y altura {altura}:")
	print(f"Área: {calcular_area(base, altura)}")
	print(f"Perímetro: {calcular_perimetro(base, altura)}")

informancion_del_rectangulo(5,4)