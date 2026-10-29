# Funciones en Python

*Apuntes de funciones (teoría: `ut4_funciones`). Ejemplos con la planta de pm-01.*

## Índice

1. [Parámetros](#1-parámetros)

---

## 1. Parámetros

Los parámetros son las variables que recibe una función. Hay CUATRO TIPOS y SIEMPRE VAN EN ESTE ORDEN: `def f(a, b=10, *args, **kwargs)`.

### Posicional

- **QUÉ ES:** un parámetro OBLIGATORIO que se rellena por posición.
- **SINTAXIS:** `def plant(name):`.
- **CUÁNDO:** para los datos sin los que la función no tiene sentido.

### Por defecto

- **QUÉ ES:** un parámetro OPCIONAL; si no lo pasas, toma su valor por defecto.
- **SINTAXIS:** `def plant(name, height=0.0):`.
- **CUÁNDO:** para un valor que casi siempre es el mismo (`growth_rate=0.8`).

### `*args`

- **QUÉ ES:** recoge los posicionales QUE SOBRAN en una **TUPLA**.
- **SINTAXIS:** `def plant(name, *args):`.
- **CUÁNDO:** cuando no sabes cuántos valores te van a pasar.

### `**kwargs`

- **QUÉ ES:** recoge los argumentos con nombre QUE SOBRAN en un **DICCIONARIO**.
- **SINTAXIS:** `def plant(name, **kwargs):`.
- **CUÁNDO:** cuando no sabes qué opciones con nombre te van a pasar.

**Mantra:** *OBLIGATORIOS, OPCIONALES, LOS QUE SOBRAN SIN NOMBRE (tupla), LOS QUE SOBRAN CON NOMBRE (dict).*

### No confundir

- **Al definir y al llamar:** al DEFINIR, el orden es obligatorio (un parámetro por defecto delante de uno posicional da `SyntaxError`). Al LLAMAR con nombre (`height=5.0, name="Cactus"`), el orden da igual.
- **Los nombres `args` y `kwargs`** son una convención: lo que importa son los asteriscos. `*` crea una tupla y `**` un diccionario.

### Ejemplo

```python
def plant(name, height=0.0, *args, **kwargs):
    print(name, height, args, kwargs)


plant("Rose")                                       # Rose 0.0 () {}
plant("Oak", 200.0)                                 # Oak 200.0 () {}
plant("Rose", 25.0, "red", "big", season="spring")  # Rose 25.0 ('red', 'big') {'season': 'spring'}
plant(height=5.0, name="Cactus")                    # Cactus 5.0 () {}
```

---
