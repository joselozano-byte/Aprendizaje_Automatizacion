instalacion = {"cliente": "Citania", "tecnologia": "hydro", "potencia": 20}

def describir(instalacion):
    return f"Cliente: {instalacion['cliente']}, Tecnologia: {instalacion['tecnologia']}, Potencia: {instalacion['potencia']} kW"

print(describir(instalacion))

instalacion["año"] = 2026
print(instalacion)
