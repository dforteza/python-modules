# Resumen de POO en Python

*Apuntes de POO (pm-01 · Code Cultivation; ABC en pm-06). Todos los ejemplos usan la misma clase `Plant`.*

## Índice

1. [Atributos: de instancia y de clase](#1-atributos-de-instancia-y-de-clase)
2. [Métodos: de instancia, de clase y estáticos](#2-métodos-de-instancia-de-clase-y-estáticos)
3. [Herencia y polimorfismo](#3-herencia-y-polimorfismo)
4. [Encapsulación](#4-encapsulación)
5. [Clases abstractas](#5-clases-abstractas)
6. Métodos dunder *(pendiente)*

---

## 1. Atributos: de instancia y de clase

Un **atributo** es un dato que guarda una clase o un objeto.

### Atributo de instancia

- **QUÉ ES:** un dato **PROPIO DE CADA OBJETO**.
- **CREACIÓN:** con `self.atributo = valor`, normalmente en `__init__`.
- **ACCESO:** a través del objeto: `rose.height`.

### Atributo de clase

- **QUÉ ES:** un dato **COMPARTIDO POR TODOS** los objetos de la clase.
- **CREACIÓN:** en el cuerpo de la clase, fuera de los métodos: `total = 0`.
- **ACCESO:** a través de la clase: `Plant.total`.

**Mantra:** *`self.x` → CADA OBJETO EL SUYO; `Clase.x` → UNO PARA TODOS.*

### No confundir

- **Parámetro y atributo:** `name` es una variable local de `__init__` y desaparece al terminar el método; `self.name` se guarda en el objeto.
- **Anotación y atributo:** `name: str` en el cuerpo de la clase SOLO ANOTA EL TIPO (para mypy) y no crea nada; `name: str = "Unknown"` sí crea un atributo de clase. Por eso `Plant().show()` en pm-01 ex1, sin asignar antes `name`, da `AttributeError`.

### Ejemplo

```python
class Plant:
    total = 0                      # atributo de clase

    def __init__(self, name, height):
        self.name = name           # atributo de instancia
        self.height = height       # atributo de instancia
        Plant.total += 1


rose = Plant("Rose", 25)
oak = Plant("Oak", 200)

print(rose.height)   # 25  -> cada objeto tiene el suyo
print(oak.height)    # 200
print(Plant.total)   # 2   -> uno solo, compartido
```

---

## 2. Métodos: de instancia, de clase y estáticos

Un **método** es una función dentro de una clase. El tipo depende de QUÉ NECESITA TOCAR: el objeto, la clase o nada.

| | De instancia | De clase | Estático |
|---|---|---|---|
| **TOCA** | UN OBJETO concreto | LA CLASE | NADA, solo sus parámetros |
| **DECORADOR** | ninguno | `@classmethod` | `@staticmethod` |
| **PRIMER PARÁMETRO** | `self` (el objeto) | `cls` (la clase) | ninguno |
| **ACCESO** | `rose.grow()` | `Plant.anonymous()` | `Plant.is_older_than_year(400)` |

**Mantra:** *¿OBJETO? `self`. ¿CLASE? `cls`. ¿NADA? ESTÁTICO.*

### No confundir: `cls(...)`

- `cls(...)` LLAMA AL CONSTRUCTOR y CREA UN OBJETO (no una clase): es lo mismo que `Plant(...)`.
- `cls` es LA CLASE DESDE LA QUE LLAMAS: `Flower.anonymous()` intentaría crear una `Flower` (y fallaría, porque `Flower` también necesita `color`).

### Ejemplo (pm-01 ex6)

```python
@staticmethod
def is_older_than_year(days: int) -> bool:     # no usa self ni cls
    return (days > 365)

@classmethod
def anonymous(cls) -> "Plant":                 # constructor alternativo
    return (cls("Unknown plant", 0.0, 0))      # = Plant("Unknown plant", 0.0, 0)
```

---

## 3. Herencia y polimorfismo

La **herencia** crea una clase **hija** que RECIBE TODOS LOS MÉTODOS de la **madre**: `class Flower(Plant):`.

### Ampliar: con `super()`

- **QUÉ ES:** la hija ejecuta el método de la madre y AÑADE LO SUYO.
- **SINTAXIS:** `super().show()` y debajo lo nuevo.
- **CUÁNDO:** cuando quieres lo de la madre y algo más (`Vegetable.age()`: cumple el día y +1 de nutrición).

### Sustituir: sin `super()`

- **QUÉ ES:** la hija define un método con el mismo nombre y el de la madre NO SE EJECUTA.
- **SINTAXIS:** `def grow(self):` en la hija, sin `super()`.
- **CUÁNDO:** cuando la hija lo hace de una forma completamente distinta.

### Polimorfismo

- **QUÉ ES:** la misma llamada ejecuta LA VERSIÓN DE LA CLASE DE CADA OBJETO.
- **SINTAXIS:** `for plant in garden: plant.show()`.
- **CUÁNDO:** para tratar igual a objetos de clases distintas.

**Mantra:** *CON `super()` AMPLÍAS; SIN `super()` SUSTITUYES.*

### No confundir: `__init__` también sigue la regla

- Hija SIN `__init__` → hereda el de la madre.
- Hija CON `__init__` → lo sustituye. Si no llama a `super().__init__()`, NO SE CREAN LOS ATRIBUTOS DE LA MADRE y `show()` da `AttributeError: ... no attribute '_name'`.

### No confundir: `self` en código del padre

- `self.Stats()` está escrito en `Plant.__init__`, pero al crear un `Tree` SELF ES EL `Tree` → se crea `Tree.Stats`.
- **Mantra:** *`self.X` SE BUSCA EN LA CLASE DEL OBJETO, AUNQUE EL CÓDIGO ESTÉ EN EL PADRE.*
- mypy no ejecuta el código y creería que es `Plant.Stats`; por eso en `Tree` va `_stats: "Tree.Stats"`.

### Ejemplo (pm-01 ex5)

```python
class Vegetable(Plant):
    def __init__(self, name, height, age, growth_rate, harvest_season):
        super().__init__(name, height, age, growth_rate)  # la madre crea lo común
        self._harvest_season = harvest_season              # la hija añade lo suyo
        self._nutritional_value = 0

    def age(self):
        super().age()                   # AMPLÍA: cumple el día...
        self._nutritional_value += 1    # ...y suma nutrición
```

---

## 4. Encapsulación

La **encapsulación** consiste en PROTEGER LOS ATRIBUTOS para que no se cambien sin control (por ejemplo, con una altura negativa).

### Niveles de acceso

| Nivel | Sintaxis | Desde fuera |
|---|---|---|
| Público | `self.height` | se lee y se cambia libremente |
| Protegido | `self._height` | funciona igual: es SOLO UN AVISO ("no lo toques") |
| Privado | `self.__height` | Python lo RENOMBRA a `_Plant__height` (name mangling) |

### Getters y setters

- **QUÉ ES:** métodos que dan acceso CONTROLADO al atributo; el setter VALIDA antes de cambiarlo.
- **SINTAXIS:** `def get_height(self):` y `def set_height(self, height):`.
- **CUÁNDO:** siempre que un valor pueda ser inválido (en pm-01 ex4, la altura y la edad negativas).

### `@property`

- **QUÉ ES:** un getter y un setter que se usan COMO UN ATRIBUTO, sin paréntesis.
- **SINTAXIS:** `@property` encima de `def height(self)` y `@height.setter` encima de `def height(self, value)`.
- **CUÁNDO:** fuera de 42, o cuando el subject lo autorice (en pm-01 no lo estaba).

**Mantra:** *`_` AVISA, `__` RENOMBRA, EL SETTER PROTEGE. En Python NADA ES PRIVADO.*

### No confundir: name mangling

- `rose.__height = -5` no da error, pero CREA UN ATRIBUTO NUEVO; el de verdad (`_Plant__height`) no cambia.
- `rose._Plant__height = -5` SÍ lo cambia.

### Ejemplo (pm-01 ex4)

```python
def set_height(self, height: float) -> None:
    if self._validate(height, "height"):      # el setter valida...
        self._height = height                 # ...y solo entonces cambia
    else:
        print("Height update rejected")


rose.set_height(-5)     # → Height update rejected (protegido por el setter)
rose._height = -5       # → funciona: el _ no lo impide
```

---

## 5. Clases abstractas

Una **clase abstracta** es un **molde incompleto**: obliga a sus hijas a tener ciertos métodos, sin implementarlos ella.

### Clase abstracta

- **QUÉ ES:** una clase que **solo sirve como madre**; no se pueden crear objetos de ella.
- **SINTAXIS:** hereda de `ABC`: `class Plant(ABC):`.
- **EFECTO:** `Plant()` → `TypeError` **al crear** el objeto.

### Método abstracto

- **QUÉ ES:** un método que la madre **declara** pero **no implementa**; es una obligación para las hijas.
- **SINTAXIS:** `@abstractmethod` encima, y el cuerpo vacío con `pass`.
- **EFECTO:** toda hija que **no** lo implemente sigue siendo abstracta.

### Clase hija concreta

- **QUÉ ES:** una hija que implementa **todos** los métodos abstractos de la madre.
- **SINTAXIS:** `class Flower(Plant):` y dentro `def water_needs(self):` con su código.
- **EFECTO:** ya se pueden crear objetos: `Flower("Rose")`.

### No confundir: cuándo salta el error

- El `TypeError` salta **al crear** el objeto, no al llamar al método.
- Le pasa a la madre abstracta **y** a cualquier hija que no implemente todos los métodos abstractos.
- La madre sí puede tener métodos **normales** que usen los abstractos (`show()` usa `water_needs()`); cada hija aporta su versión.

### Ejemplo

```python
from abc import ABC, abstractmethod


class Plant(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def water_needs(self):        # obligación para las hijas
        pass

    def show(self):               # método normal que usa el abstracto
        print(f"{self.name}: {self.water_needs()}L/week")


class Flower(Plant):
    def water_needs(self):
        return 2


class Tree(Plant):
    def water_needs(self):
        return 20


garden = [Flower("Rose"), Tree("Oak")]
for plant in garden:
    plant.show()
# Rose: 2L/week
# Oak: 20L/week

# Plant("Fern")               -> TypeError: Plant es abstracta
```
