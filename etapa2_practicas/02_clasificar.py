import pandas as pd
df = pd.read_csv("precios_esios.csv", sep=";")
def clasificar_precio(precio):
    if precio < df["value"].mean():
        return "Bajo"
    else:
        return "Alto"
df["categoria"] = df["value"].apply(clasificar_precio)
print(df.head())
print(df["categoria"].value_counts())
