dia_1 = "Martes"
dia_2 = "Domingo"
dia_3 = "Octodia"

dias_lab = "lunes, martes, miércoles, jueves, viernes"
fin_sem = "sábado, domingo"

if dia_1.lower() not in dias_lab and dia_1.lower() not in fin_sem:
	print(f"El día {dia_1} no es válido")
elif dia_1.lower() in dias_lab:
	print(f"El día {dia_1} es un día laborable")
elif dia_1.lower() in fin_sem:
	print(f"El día {dia_1} es un día de fin de semana")

if dia_2.lower() not in dias_lab and dia_2.lower() not in fin_sem:
	print(f"El día {dia_2} no es válido")
elif dia_2.lower() in dias_lab:
	print(f"El día {dia_2} es un día laborable")
elif dia_2.lower() in fin_sem:
	print(f"El día {dia_2} es un día de fin de semana")

if dia_3.lower() not in dias_lab and dia_3.lower() not in fin_sem:
	print(f"El día {dia_3} no es válido")
elif dia_3.lower() in dias_lab:
	print(f"El día {dia_3} es un día laborable")
elif dia_3.lower() in fin_sem:
	print(f"El día {dia_3} es un día de fin de semana")