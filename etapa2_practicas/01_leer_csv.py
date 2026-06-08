import pandas as pd
df = pd.read_csv("precios_esios.csv", sep=";")
print(df.head())
print(df.info())
print(df.columns)
print("Precio medio:", df["value"].mean())
print("Precio máximo:", df["value"].max())
print("Precio mínimo:", df["value"].min())
