instalaciones = [
    {"cliente": "Citania", "tecnologia": "agua", "potencia": 120},
    {"cliente": "Acme", "tecnologia": "viento", "potencia": 85},
    {"cliente": "Beta", "tecnologia": "fotovoltaica", "potencia": 200},
    {"cliente": "Delta", "tecnologia": "viento", "potencia": 40},
]
def tamano_instalacion(potencia):
    if potencia > 100:
        return "grande"
    else:
        return "pequeña"
potacc = 0

for instalacion in instalaciones:
    cliente = instalacion["cliente"]
    tecnologia = instalacion["tecnologia"]
    potencia = instalacion["potencia"]
    tamano = tamano_instalacion(potencia)
    print(f"Cliente: {cliente}, Tecnologia: {tecnologia}, Potencia: {potencia} kW, Tamaño: {tamano}")
    potacc = potacc + potencia
print("Potencia total acumulada:", potacc, "kW")
print("Número de instalaciones:", len(instalaciones))
with open("informe.txt", "w") as archivo:
    for instalacion in instalaciones:
        cliente = instalacion["cliente"]
        tecnologia = instalacion["tecnologia"]
        potencia = instalacion["potencia"]
        tamano = tamano_instalacion(potencia)
        archivo.write(f"Cliente: {cliente}, Tecnologia: {tecnologia}, Potencia: {potencia} kW, Tamaño: {tamano}\n")
    archivo.write(f"Potencia total acumulada: {potacc} kW\n")
    archivo.write(f"Número de instalaciones: {len(instalaciones)}\n")


