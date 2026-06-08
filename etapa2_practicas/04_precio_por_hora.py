import pandas as pd
df = pd.read_csv("precios_esios.csv", sep=";")
df["datetime"] = pd.to_datetime(df["datetime"], utc=True)
df["datetime"] = df["datetime"].dt.tz_convert("Europe/Madrid")
print(df.info())
df["hora"] = df["datetime"].dt.hour
print(df.head())
precio_por_hora = df.groupby("hora")["value"].mean()
print(precio_por_hora)