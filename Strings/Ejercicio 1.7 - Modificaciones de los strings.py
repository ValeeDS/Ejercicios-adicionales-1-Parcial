texto = "Carlos tiene 19 años"
texto2 = "Felipe tiene 22 años"

texto_edad = int(texto[-7:-5]) + 1
texto2_edad = int(texto2[-7:-5]) + 1

print(f"{texto[:-7]}{texto_edad} años")

print(f"{texto2[:-7]}{texto2_edad} años")