datos = ["120", "85", "abc", "200"]
for dato in datos:
    try:
        numero = int(dato)
        print("Numero:", numero)
    except ValueError:
        print("Error: No es un numero valido:", dato)
        