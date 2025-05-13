edad_adolescente = 14
edad_anciano = 66

edad_grupo = 0

if edad_adolescente <= 4:
	edad_grupo += 0
elif edad_adolescente <= 17:
	edad_grupo += 50
elif edad_adolescente <= 50:
	edad_grupo += 30
else:
	edad_grupo += 10

if edad_anciano <= 4:
	edad_grupo += 0
elif edad_anciano <= 17:
	edad_grupo += 50
elif edad_anciano <= 50:
	edad_grupo += 30
else:
	edad_grupo += 10

print(f"El costo de entrada para el grupo familiar es de: ${edad_grupo}")