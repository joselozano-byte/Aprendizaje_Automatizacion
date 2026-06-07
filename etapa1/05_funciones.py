def clasificacion_potencia(potencia):
    if potencia > 100:
        return "Instalacion Grande"
    elif potencia > 50 and potencia <= 100:    
        return "Instalacion Mediana"
    else:
        return "Potencia baja"
    
potencias = [120, 85, 200, 40]

for potencia in potencias:
    print(potencia, "->", clasificacion_potencia(potencia))
