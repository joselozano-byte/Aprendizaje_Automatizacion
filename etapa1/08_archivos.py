energias = ["agua", "viento", "fotovoltaica"]
with open("energias.txt", "w") as archivo:
    for energia in energias:
        archivo.write("Tecnologia: " + energia + "\n")
with open("energias.txt", "r") as archivo:
    print(archivo.read())
