a = 4
b = -5
c = 2

max = a
min = a

if b > max:
	max = b
if c > max:
	max = c
if b < min:
	min = b
if c < min:
	min = c

print(f"El número mayor es: {max}")
print(f"El número menor es: {min}")