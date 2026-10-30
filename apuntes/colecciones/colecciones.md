# Colecciones en Python

*pm-03 · Data Quest. Solo lo fundamental y lo nuevo. Lo básico de listas y diccionarios (métodos, acceso, `get`…) está en `pythonbasics_git/01-fundamentos/tipos_datos/` (`listas.py`, `diccs.py`).*

## Índice

1. [sys.argv](#1-sysargv)
2. [Tuplas](#2-tuplas)
3. [Sets](#3-sets)
4. [Comprehensions](#4-comprehensions)
5. [Generadores](#5-generadores)

---

## 1. sys.argv

- **QUÉ ES:** la LISTA DE `str` con los argumentos de la terminal.
- **SINTAXIS:** `import sys` → `sys.argv[0]` es el programa; los argumentos reales son `sys.argv[1:]`.

### No confundir

- `argv[5]` fuera de rango da `IndexError`; `argv[5:]` da `[]` sin error.
- Todo llega como `str`: `"42"` hay que convertirlo con `int()` (y capturar `ValueError`).

---

## 2. Tuplas

- **QUÉ ES:** una lista INMUTABLE: una vez creada, no se cambia.
- **SINTAXIS:** `pos = (1.0, 2.5, 3.0)`; desempaquetar: `x, y, z = pos`.
- **CUÁNDO:** para datos fijos que van juntos (coordenadas, un par `(name, action)`).

### No confundir

- LA TUPLA LA HACE LA COMA, no los paréntesis: `(5)` es un `int`; `(5,)` es una tupla.
- Desempaquetar con un número distinto de variables da `ValueError`.

---

## 3. Sets

- **QUÉ ES:** una colección SIN ORDEN y SIN REPETIDOS.
- **SINTAXIS:** `set(lista)` o `{"a", "b"}`; vacío, SOLO `set()`.
- **CUÁNDO:** cuando importa qué hay, no el orden ni cuántas veces.

| Operación | Método | Con `a = {1, 2}`, `b = {2, 3}` |
|---|---|---|
| Unión (en alguno) | `a.union(b)` | `{1, 2, 3}` |
| Intersección (en los dos) | `a.intersection(b)` | `{2}` |
| Diferencia (en `a`, no en `b`) | `a.difference(b)` | `{1}` |

### No confundir

- `{}` es un DICT vacío; el set vacío es `set()`, y así se imprime.
- Acumular: la unión empieza en `set()`; la intersección, en el primer set (con `set()` saldría vacía).

---

## 4. Comprehensions

- **QUÉ ES:** un `for` + `append` en una línea: crea una colección nueva transformando y/o filtrando.
- **SINTAXIS:** lista `[expr for x in it if cond]` · dict `{k: v for x in it if cond}` · set `{expr for x in it}`.

### No confundir

- La expresión de delante TRANSFORMA; el `if` del final FILTRA.
- `for k in d` da solo claves; `for k, v in d.items()` da clave y valor.
- No admite `try/except`: si algo puede fallar, `for` normal.

---

## 5. Generadores

- **QUÉ ES:** una función con `yield` que devuelve los valores DE UNO EN UNO, cuando se le piden, sin guardarlos todos en memoria.
- **SINTAXIS:** `yield valor` dentro de la función; pedir el siguiente: `next(gen)`; o recorrerlo con `for x in gen:`.
- **CUÁNDO:** flujos largos o infinitos de datos.

Cómo funciona:

1. Llamar a la función NO ejecuta nada: devuelve un objeto generador.
2. Cada `next()` ejecuta hasta el siguiente `yield`, entrega el valor y SE PAUSA ahí.
3. El siguiente `next()` sigue justo después de ese `yield`, con las variables intactas.
4. Cuando la función termina, salta `StopIteration` (el `for` lo captura solo y para).

Type hint: `Generator[TipoQueEntrega, None, None]` (de `typing`).

### No confundir

- `return` termina la función; `yield` la PAUSA.
- `while True: yield ...` es un generador INFINITO: con `for` no acaba nunca; se usa con `next()` un número de veces.

### Ejemplo

```python
from typing import Generator


def countdown(n: int) -> Generator[int, None, None]:
    while n > 0:
        yield n
        n -= 1


gen = countdown(3)
print(next(gen))     # 3
print(next(gen))     # 2
for x in gen:        # 1   (sigue donde se quedó)
    print(x)
```
