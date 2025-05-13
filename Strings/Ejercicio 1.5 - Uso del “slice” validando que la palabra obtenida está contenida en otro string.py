gases_nobles = "Helio, Neón, Argón, Kriptón, Xenón, Radón, Oganesón"
texto = "Hello, Aurelio"
texto2 = "Hello, Matías"

slice1 = texto[:2] + texto[-3:]
slice2 = texto2[:2] + texto2[-3:]

print(f"La palabra se encuentra dentro de los gases nobles: {slice1.lower() in gases_nobles.lower()}")
print(f"La palabra se encuentra dentro de los gases nobles: {slice2.lower() in gases_nobles.lower()}")