def dias_a_horas(dias):
	horas = "Número erróneo de días ingresados"
	if dias >= 0:
		horas = dias * 24

	return horas

horas_1 = f"{dias_a_horas(5)} horas"
horas_2 = f"{dias_a_horas(0)} horas"
horas_3 = f"{dias_a_horas(-4)} horas"

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 0 horas
print(horas_3) # Imprime: Número erróneo de días ingresados
