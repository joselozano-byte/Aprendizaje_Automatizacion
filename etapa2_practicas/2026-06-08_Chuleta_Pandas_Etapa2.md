# Chuleta pandas — Etapa 2

Referencia rápida de los comandos de pandas vistos hasta ahora.
Ampliar este archivo a medida que avance la etapa.

---

## Concepto clave: un nombre debe existir antes de usarse

Python solo conoce un nombre si se ha creado antes en el código, y lo
lee de arriba abajo. Si se usa un nombre que aún no existe, se detiene
con `NameError`. Hay tres formas de crear un nombre, misma lógica:

- Variable: `edad = 61`
- Función propia: `def clasificar(precio):`
- Librería importada: `import pandas as pd`

Por eso `import pandas as pd` va en la primera línea: crea el nombre
`pd` antes de que ninguna otra línea lo necesite.

`import` no crea pandas, lo **trae** a tu programa. El `as pd` es solo
un apodo corto, convención universal (no obligatorio, pero todos lo usan).

---

## 1. Importar (siempre lo primero)

```python
import pandas as pd
```

Crea el nombre `pd` y trae la librería.

## 2. Cargar datos

```python
df = pd.read_csv("archivo.csv", sep=";")
```

Lee un CSV. `sep=";"` indica separador punto y coma (habitual en
archivos españoles). El resultado se guarda por convención en `df`.

## 3. Mirar los datos recién cargados

| Comando        | Qué hace                                         | ¿Paréntesis? |
|----------------|--------------------------------------------------|--------------|
| `df.head()`    | Primeras 5 filas                                 | Sí (función) |
| `df.shape`     | Dimensiones (filas, columnas)                    | No (atributo)|
| `df.columns`   | Nombres de las columnas                          | No (atributo)|
| `df.info()`    | Resumen completo: dimensiones, tipos, no nulos   | Sí (función) |

## 4. Seleccionar una columna

```python
df["value"]
```

Extrae la columna entera por su nombre (corchetes y comillas).

## 5. Calcular sobre una columna numérica

```python
df["value"].mean()   # media
df["value"].min()    # mínimo
df["value"].max()    # máximo
```

Se encadena el cálculo detrás de la columna.

---

## Funciones vs atributos

- **Funciones** llevan paréntesis porque ejecutan una acción:
  `head()`, `mean()`, `min()`, `max()`, `info()`.
- **Atributos** NO llevan paréntesis porque son una propiedad que el
  objeto ya tiene: `shape`, `columns`.

Poner `df.shape()` con paréntesis da error.

## 6. Agrupar por día y calcular el spread

Para agrupar por día completo (no por hora), se extrae la fecha del
datetime con `.dt.date`. Es el equivalente diario de `.dt.hour`.

```python
df["dia"] = df["datetime"].dt.date
```

Crea una columna nueva con solo la fecha (sin la hora).

### groupby + max / min por grupo

```python
maximo_por_dia = df.groupby("dia")["value"].max()
minimo_por_dia = df.groupby("dia")["value"].min()
```

Estructura: `df.groupby("columna_grupo")["columna_calculo"].max()`.
Devuelve una Serie con el `dia` como índice y el valor calculado.

### Restar dos Series con el mismo índice

```python
spread_diario = maximo_por_dia - minimo_por_dia
```

Pandas resta elemento a elemento porque ambas Series comparten el
índice (`dia`). No hace falta bucle: la resta se alinea sola por índice.
El resultado es el spread (oscilación max-min) de cada día.

---

## Principio: el nombre de la variable debe decir la verdad

Si una variable agrupa por día, no la llames `precio_por_hora_max`.
El nombre es documentación: debe describir lo que contiene, no de dónde
se copió. `maximo_por_dia` se entiende solo; `precio_por_hora_max`
agrupando por día engaña a quien lo lea (incluido tú dentro de 6 meses).

---

## Lectura de negocio (RPI): el spread diario

El spread diario replica la herramienta Excel de análisis de RPI.
Mide la oscilación de precio dentro de cada día:

- Spread alto = mucho margen entre comprar barato y vender caro =
  más valor para almacenamiento y flexibilidad hidráulica.
- El spread crece de invierno a primavera/verano: más solar hunde
  el mínimo de mediodía mientras la punta de tarde se mantiene alta.
- El PV vende en el mínimo (mediodía); el spread cuantifica el dinero
  que el PV deja de capturar por no poder desplazar producción a la tarde.

---

## Pendiente para el próximo ejercicio

Resumir la serie del spread: `.mean()`, `.max()`, `.min()` sobre
`spread_diario` para obtener estadísticos. Más adelante, introducir
`pathlib` para que el script encuentre el CSV sin depender de la
carpeta desde la que se ejecuta (resuelve el `FileNotFoundError` de hoy).
---


