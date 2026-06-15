import pandas as pd
df = pd.read_csv("precios_esios.csv", sep=";")
df["datetime"] = pd.to_datetime(df["datetime"], utc=True)
df["datetime"] = df["datetime"].dt.tz_convert("Europe/Madrid")
df["dia"] = df["datetime"].dt.date

maximo_por_dia = df.groupby("dia")["value"].max()
print(maximo_por_dia)
minimo_por_dia = df.groupby("dia")["value"].min()
print(minimo_por_dia)
spread_diario = maximo_por_dia - minimo_por_dia   
print(spread_diario)
