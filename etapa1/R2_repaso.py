potencias = [120, 85, 200, 40, 150]
grandes = 0
medianas = 0
for potencia in potencias:
    if potencia > 100:
        grandes = grandes + 1
    else:
        medianas = medianas + 1
print("Total de potencias:", sum(potencias))
print("Grandes:", grandes)
print("Medianas:", medianas)
