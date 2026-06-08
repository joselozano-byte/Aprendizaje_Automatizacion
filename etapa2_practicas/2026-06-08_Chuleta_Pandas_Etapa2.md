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

---

## Pendiente para el próximo ejercicio

Convertir la columna `datetime` (ahora texto / `str`) a fecha real
para poder agrupar por día y por hora. Aparecerá el cambio de huso
horario (+01:00 invierno / +02:00 verano) en los datos de REE.
