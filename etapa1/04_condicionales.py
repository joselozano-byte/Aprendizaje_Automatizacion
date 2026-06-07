potencias = [120, 85, 200, 40]
for potencia in potencias:
    if potencia > 100:
        print("Instalacion Grande:", potencia)
    elif potencia > 50 and potencia <= 100:    
        print("Instalacion Mediana:", potencia)
    else:
        print("Potencia baja:", potencia)