def dias_a_horas_con_fracciones(dias):
	horas = "Número erróneo de días ingresados"
	if dias >= 0:
		horas = int(dias * 24)

	return horas

horas_1 = f"{dias_a_horas_con_fracciones(5)} horas"
horas_2 = f"{dias_a_horas_con_fracciones(2.5)} horas"
horas_3 = f"{dias_a_horas_con_fracciones(0)} horas"
horas_4 = f"{dias_a_horas_con_fracciones(-4)} horas"

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 60 horas
print(horas_3) # Imprime: 0 horas
print(horas_4) # Imprime: Número erróneo de días ingresados