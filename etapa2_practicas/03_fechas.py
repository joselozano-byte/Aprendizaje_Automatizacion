import pandas as pd
df = pd.read_csv("precios_esios.csv", sep=";")
df["datetime"] = pd.to_datetime(df["datetime"], utc=True)
print(df.info())
df["hora"] = df["datetime"].dt.hour
print(df.head())
