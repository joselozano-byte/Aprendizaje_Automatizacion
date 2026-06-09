# Chuleta de sintaxis básica — Python

Repaso de los signos y conceptos básicos vistos hasta ahora.
Pensada para tener abierta en VS Code junto al código.
Ampliar a medida que avance el curso.

---

## Concepto raíz: un nombre debe existir antes de usarse

Python lee el código de arriba abajo y solo conoce un nombre si se ha
creado antes. Usar un nombre que aún no existe da `NameError`.

Tres formas de crear un nombre, misma lógica:

- Variable: `edad = 61`
- Función propia: `def clasificar(precio):`
- Librería importada: `import pandas as pd`

Por eso el `import` va siempre en la primera línea.

---

## Los signos, uno a uno

### Comillas `" "` — marcan texto

Lo que va entre comillas es texto (`str`). Lo que no, es un número o un
nombre de la programación.

```python
nombre = "Jose"      # texto
edad = 61            # número (sin comillas)
```

- `"61"` es texto; `61` es número. No son lo mismo.
- Sirven comillas dobles `"` o simples `'`, pero hay que abrir y cerrar
  con la misma.
- Cuidado con las comillas tipográficas (curvas) del Mac: dan error.
  Deben ser rectas.

### Paréntesis `( )` — ejecutan una acción (funciones)

Marcan que algo **se ejecuta**. Dentro van los datos que entran
(argumentos), aunque a veces estén vacíos.

```python
print("hola")            # ejecuta print, le entra "hola"
df["value"].mean()       # ejecuta mean, no necesita argumentos
df.info()                # vacíos, pero obligatorios para ejecutar
```

Regla clave (funciones vs atributos):
- CON paréntesis = función, ejecuta una acción: `head()`, `mean()`, `info()`
- SIN paréntesis = atributo, dato que el objeto ya tiene: `shape`, `columns`

`df.shape()` con paréntesis da error. `df.shape` sin ellos, correcto.

### Corchetes `[ ]` — seleccionar / acceder

Para entrar a un elemento concreto por su nombre o su posición.

```python
energias[0]          # primer elemento de una lista (se cuenta desde 0)
df["value"]          # la columna llamada "value"
df["datetime"].dt.hour
```

En pandas, el nombre de la columna va entre corchetes Y comillas:
`df["value"]`.

### Coma `,` — separa elementos

Separa argumentos dentro de un paréntesis, o elementos de una lista.

```python
print("Edad:", edad)                 # separa dos cosas a imprimir
pd.read_csv("archivo.csv", sep=";")  # separa argumentos
lista = ["agua", "viento", "sol"]    # separa elementos
```

Ojo: en los números de Python el decimal es punto, no coma: `52.65`.

### Dos puntos `:` — abren un bloque

Al final de un `def`, `if`, `else`, `for`. Lo que sigue va dentro del
bloque y se escribe sangrado.

```python
def clasificar(precio):
    if precio > 50:
        return "caro"
    else:
        return "barato"
```

Olvidar los dos puntos es un error muy frecuente.

### Punto y coma `;`

En Python NO se usa al final de las líneas (a diferencia de otros
lenguajes). Cada instrucción va en su propia línea, sin nada al final.

Donde sí aparece en este curso es DENTRO de las comillas, como dato:
el separador de los CSV españoles.

```python
df = pd.read_csv("precios_esios.csv", sep=";")
```

Ahí el `;` no es código: es el carácter que separa columnas en ese
archivo.

### Punto `.` — encadena: "de esto, hazme aquello"

Conecta un objeto con algo que le pertenece (su función o su atributo).

```python
df.head()                  # de df, dame las primeras filas
df["value"].mean()         # de la columna value, su media
df["datetime"].dt.hour     # de la fecha, su hora
```

Se lee de izquierda a derecha como una cadena de pertenencia.

### Espacios y sangría (indentación)

La sangría (4 espacios al principio de la línea) NO es estética: define
qué está dentro de un bloque. Lo sangrado bajo un `def`/`if`/`for`
pertenece a ese bloque; lo no sangrado queda fuera.

```python
def clasificar(precio):
    return "caro"      # sangrado -> dentro de la función
print("fin")           # sin sangrar -> fuera
```

VS Code suele sangrar solo tras los dos puntos. Verificarlo.

---

## Funciones vistas hasta ahora

### De Python (vienen de serie)
| Función      | Qué hace                                  |
|--------------|-------------------------------------------|
| `print(...)` | Muestra algo en pantalla                  |
| `type(...)`  | Dice de qué tipo es un dato               |
| `int(...)`   | Convierte a número entero                 |
| `float(...)` | Convierte a número decimal                |
| `str(...)`   | Convierte a texto                         |
| `len(...)`   | Cuenta elementos de una lista             |
| `sum(...)`   | Suma los elementos de una lista           |

### De pandas (requieren `import pandas as pd`)
| Comando                          | Qué hace                                | ¿Paréntesis? |
|----------------------------------|-----------------------------------------|--------------|
| `pd.read_csv("f.csv", sep=";")`  | Lee un CSV                              | Sí           |
| `pd.to_datetime(col, utc=True)`  | Convierte texto a fecha real            | Sí           |
| `df.head()`                      | Primeras 5 filas                        | Sí           |
| `df.info()`                      | Resumen: filas, tipos, no nulos         | Sí           |
| `df.shape`                       | Dimensiones (filas, columnas)           | No (atributo)|
| `df.columns`                     | Nombres de columnas                     | No (atributo)|
| `df["col"]`                      | Selecciona una columna                  | No (corchetes)|
| `df["col"].mean()`               | Media de la columna                     | Sí           |
| `df["col"].min()` / `.max()`     | Mínimo / máximo                         | Sí           |
| `df["col"].value_counts()`       | Cuenta cuántos hay de cada valor        | Sí           |
| `df["col"].apply(funcion)`       | Aplica una función propia a cada valor  | Sí           |
| `df["fecha"].dt.hour`            | Extrae la hora de una columna de fechas | No (atributo)|
| `df["fecha"].dt.tz_convert(...)` | Cambia la zona horaria                  | Sí           |
| `df.groupby("col")["otra"].mean()`| Agrupa y promedia por grupo            | Sí           |

---

## Métodos propios (cómo definir una función)

```python
def clasificar(precio):       # def, nombre, argumento, dos puntos
    if precio > 50:
        return "caro"         # return marca lo que sale
    else:
        return "barato"
```

Como `y = f(x)`: entra un valor (`precio`), una regla lo transforma,
sale un resultado (`return`).

- `.apply(clasificar)` -> el nombre SIN paréntesis: se la das a pandas
  para que la ejecute él una vez por fila.
- Usar `.apply()` solo para lógica PROPIA. Si pandas ya tiene la
  operación directa (como `.dt.hour`), usar esa: es más simple y rápida.

---

## Errores frecuentes ya vistos (y qué significan)

| Error                                   | Causa habitual                              |
|-----------------------------------------|---------------------------------------------|
| `NameError: name 'pd' is not defined`   | Falta `import pandas as pd` al principio    |
| `command not found: import`             | Se escribió código Python en la Terminal    |
| `No such file or directory`             | Ejecutas desde la carpeta equivocada (`cd`) |
| `ModuleNotFoundError: No module named`  | La librería no está instalada en ese equipo |
| `Mixed timezones detected`              | Falta `utc=True` en `pd.to_datetime`        |
| `'Timestamp' object has no attribute 'dt'` | Usar `.dt` sobre un valor suelto, no columna |

---

## Recordatorio de flujo (no es Python, es Terminal/Git)

```
cd ~/Aprendizaje_Automatizacion/etapa2_practicas   # situarse
source ../.venv/bin/activate                        # activar entorno
python3 archivo.py                                  # ejecutar
git pull      # al empezar (traer lo del otro Mac)
git add .     # preparar cambios
git commit -m "mensaje sin tildes ni ñ"
git push      # al terminar (subir)
```
