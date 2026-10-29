# Excepciones en Python

*Apuntes de excepciones (pm-02 · Garden Guardian). Ejemplos sacados de los ejercicios del módulo.*

## Índice

1. [Lanzar y capturar](#1-lanzar-y-capturar)
2. [Varios tipos de error](#2-varios-tipos-de-error)
3. [Excepciones propias](#3-excepciones-propias)
4. [Limpiar siempre: `finally`](#4-limpiar-siempre-finally)

---

## 1. Lanzar y capturar

Una **excepción** es un objeto error que sube por las llamadas hasta que alguien la captura. Si nadie la captura, aparece el traceback y el programa termina.

### Lanzar: `raise`

- **QUÉ ES:** `ValueError("msg")` **CREA** el objeto con tu mensaje y `raise` **LO LANZA**.
- **SINTAXIS:** `raise ValueError("msg")`.
- **CUÁNDO:** en la función que **DETECTA** el problema.

### Capturar: `try/except`

- **QUÉ ES:** si dentro del `try` salta un error de ese tipo, se ejecuta el `except`.
- **SINTAXIS:** `except ValueError as e:` (`e` es el mismo objeto que se lanzó).
- **CUÁNDO:** en la función que **DECIDE** qué hacer con el error.

**Mantra:** *QUIEN DETECTA, LANZA; QUIEN DECIDE, CAPTURA. El mensaje del `raise` ES el `{e}` del `except`.*

### No confundir

- **`ValueError("msg")` frente a `raise ValueError("msg")`:** el primero solo crea el objeto; el segundo además lo hace saltar.
- **Dentro y fuera del `try`:** dentro, el error salta al `except` y lo que quedaba del `try` no se ejecuta; fuera, el error sube hasta arriba y el programa termina.

### Ejemplo

```python
raise ValueError(f"{temp}°C is too hot")    # lanza (input_temperature)

except ValueError as e:                     # captura (test_temperature)
    print(f"Caught: {e}")                   # → Caught: 100°C is too hot
```

---

## 2. Varios tipos de error

Cada error tiene su **tipo** para que puedas tratar cada uno de una forma distinta.

### Un `except` por tipo

- **QUÉ ES:** varios `except` seguidos, cada uno con su propio plan B.
- **SINTAXIS:** `except ValueError as e:` / `except ZeroDivisionError as e:`.
- **CUÁNDO:** cuando cada error necesita un trato distinto.

### Un `except` para varios tipos

- **QUÉ ES:** un solo `except` que captura cualquier tipo de la tupla.
- **SINTAXIS:** `except (ValueError, TypeError) as e:` ⚠️ **CON PARÉNTESIS: ES UNA TUPLA**.
- **CUÁNDO:** cuando varios errores se tratan igual.

**Mantra:** *De arriba abajo, entra SOLO EL PRIMERO QUE ENCAJA.*

### Ejemplo

```python
try:
    garden_operations(1)                    # 10 / 0
except ValueError as e:                     # no encaja → se salta
    print(f"Caught ValueError: {e}")
except ZeroDivisionError as e:              # encaja → solo este
    print(f"Caught ZeroDivisionError: {e}")
```

---

## 3. Excepciones propias

Clases tuyas que heredan de `Exception`, para separar los errores de **TU DOMINIO** de los de Python y agruparlos por familia.

### Crear la excepción

- **QUÉ ES:** una clase hija de `Exception` (o de otra excepción tuya).
- **SINTAXIS:** `class PlantError(GardenError):` + `super().__init__(message)`.
- **CUÁNDO:** cuando el error es de tu programa y no encaja en uno de Python.

### Capturar por familia

- **QUÉ ES:** `except Padre` captura también a todos sus hijos (un `PlantError` **ES** un `GardenError`).
- **SINTAXIS:** `except GardenError as e:`.
- **CUÁNDO:** cuando todos los errores de la familia se tratan igual.

**Mantra:** *EL HIJO ES UN PADRE; `except` DEL MÁS ESPECÍFICO AL MÁS GENERAL.*

### No confundir

- **Orden de los `except`:** si pones `except GardenError` encima de `except PlantError`, el de abajo no se ejecuta nunca (código muerto).
- **`super().__init__(message)`:** le pasa el mensaje a `Exception`. Sin él, `PlantError("x")` sigue imprimiendo `x`, pero `PlantError()` imprime vacío porque se pierde el mensaje por defecto.

### Ejemplo

```python
class GardenError(Exception):               # padre (familia)
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)           # el mensaje llega a Exception


class PlantError(GardenError):              # hijo
    ...


try:
    raise PlantError("The tomato plant is wilting!")
except GardenError as e:                    # el padre coge al hijo
    print(f"Caught GardenError: {e}")
```

---

## 4. Limpiar siempre: `finally`

Bloque que se ejecuta **SIEMPRE**, justo antes de salir del `try`, para cerrar recursos (archivos, conexiones, el riego) aunque haya un error.

### `finally`

- **QUÉ ES:** el último bloque del `try`, que se ejecuta salgas como salgas.
- **SINTAXIS:** `try: ...` / `except ...: ...` / `finally: ...`.
- **CUÁNDO:** para cerrar o liberar algo que abriste en el `try`.

**Mantra:** *Salgas por donde salgas, ANTES PASAS POR EL `finally`.*

### No confundir: las formas de salir

- **Sin error:** termina el `try` → `finally`.
- **Error capturado con `return`:** `except` → llega al `return` → `finally` → vuelve a quien llamó.
- **Error sin capturar:** `finally` → el error **SUBE** a quien llamó (si nadie lo captura, aparece el traceback).

### Ejemplo

```python
def test_watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)                  # "lettuce" → PlantError
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return                                  # antes de volver a main...
    finally:
        print("Closing watering system")        # ...se ejecuta esto
```

---
