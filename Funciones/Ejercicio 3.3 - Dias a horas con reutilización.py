def dias_a_horas_con_fracciones(dias):
	horas = "Número erróneo de días ingresados"
	if dias >= 0:
		horas = int(dias * 24)

	return horas

horas_1 = dias_a_horas_con_fracciones(5)
horas_2 = dias_a_horas_con_fracciones(2.5)
horas_3 = dias_a_horas_con_fracciones(0)
horas_4 = dias_a_horas_con_fracciones(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 60 horas
print(horas_3) # Imprime: 0 horas
print(horas_4) # Imprime: Número erróneo de días ingresados