potencias = [120, 85, 200, 40, 150]

def es_grande(potencia):
    if potencia > 100:
        return True
    else:
        return False

grandes = 0
medianas = 0

for potencia in potencias:
    if es_grande(potencia):
        grandes = grandes + 1
    else:
        medianas = medianas + 1

print("Grandes:", grandes)
print("Medianas:", medianas)