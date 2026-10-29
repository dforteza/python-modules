# Resumen de POO en Python

*Resumen de `poo_aptes.py`. Todos los ejemplos usan la misma clase `Plant`.*

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

- **QUÉ ES:** un dato **propio de cada objeto**.
- **CREACIÓN:** con `self.atributo = valor`, normalmente en `__init__`.
- **ACCESO:** a través del objeto: `rose.height`.

### Atributo de clase

- **QUÉ ES:** un dato **compartido por todos los objetos** de la clase.
- **CREACIÓN:** en el cuerpo de la clase, fuera de los métodos: `total = 0`.
- **ACCESO:** a través de la clase: `Plant.total`.

**Imagen:** la clase es el **molde** y cada objeto es una **galleta**. El atributo de clase está escrito en el molde; el de instancia, en cada galleta.

### No confundir: parámetro y atributo

- `name` es un **parámetro**: una variable local de `__init__` que desaparece cuando el método termina.
- `self.name` es un **atributo de instancia**: se guarda en el objeto y sigue ahí después.

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

Un **método** es una función definida dentro de una clase.

Hay 3 tipos. Cuál usar depende de **qué necesita tocar el método**: el objeto, la clase o nada.

### Método de instancia

- **QUÉ ES:** trabaja con **un objeto concreto**.
- **DECORADOR:** ninguno.
- **PRIMER PARÁMETRO:** `self` (el objeto).
- **ATR. PERMITIDOS:** de instancia y de clase.
- **ACCESO:** a través del objeto: `rose.grow()`.

### Método de clase

- **QUÉ ES:** trabaja con **la clase**, es decir, con lo que comparten todos los objetos.
- **DECORADOR:** `@classmethod`.
- **PRIMER PARÁMETRO:** `cls` (la clase).
- **ATR. PERMITIDOS:** solo de clase.
- **ACCESO:** a través de la clase: `Plant.count()`.

### Método estático

- **QUÉ ES:** una **utilidad** relacionada con la clase que no toca ni el objeto ni la clase.
- **DECORADOR:** `@staticmethod`.
- **PRIMER PARÁMETRO:** ninguno automático.
- **ATR. PERMITIDOS:** ninguno, solo lo que le pases por parámetro.
- **ACCESO:** a través de la clase: `Plant.cm_to_m(200)`.

**Pregunta para elegir:** ¿qué necesita el método?

- Un objeto concreto → **de instancia**.
- La clase entera → **de clase**.
- Nada, solo sus parámetros → **estático**.

### Ejemplo

```python
class Plant:
    total = 0

    def __init__(self, name, height):
        self.name = name
        self.height = height
        Plant.total += 1

    def grow(self):                # de instancia: toca ESA planta
        self.height += 1

    @classmethod
    def count(cls):                # de clase: toca lo compartido
        return cls.total

    @staticmethod
    def cm_to_m(cm):               # estático: solo usa su parámetro
        return cm / 100


rose = Plant("Rose", 25)
oak = Plant("Oak", 200)

rose.grow()
print(rose.height)          # 26
print(Plant.count())        # 2
print(Plant.cm_to_m(200))   # 2.0
```

---

## 3. Herencia y polimorfismo

La **herencia** permite crear una clase **hija** a partir de una clase **madre**.

### Clase hija

- **QUÉ ES:** una clase que recibe **todo** lo de la madre: atributos y métodos.
- **SINTAXIS:** la madre entre paréntesis: `class Flower(Plant):`.
- **EFECTO:** la hija puede **añadir** cosas nuevas y **sobrescribir** las que ya tiene.

### super()

- **QUÉ ES:** la **clase madre**, vista desde dentro de la hija.
- **SINTAXIS:** `super().__init__(name, height)` o `super().show()`.
- **EFECTO:** ejecuta el método de la madre, así la hija no repite su código.

### Sobrescritura

- **QUÉ ES:** la hija define un método **con el mismo nombre** que uno de la madre.
- **SINTAXIS:** `def grow(self):` dentro de la hija.
- **EFECTO:** el objeto hija usa **su** versión, no la de la madre.

### Polimorfismo

- **QUÉ ES:** el **mismo método** se comporta distinto según la clase del objeto.
- **SINTAXIS:** `for plant in garden: plant.grow()`.
- **EFECTO:** cada objeto ejecuta la versión de su clase, sin preguntar cuál es.

### No confundir: sobrescribir y ampliar

- **Sobrescribir:** la hija **sustituye** el método de la madre (`Tree.grow()`).
- **Ampliar:** la hija llama a `super()` y **añade** lo suyo (`Flower.show()`).
- `__init__` es un método más y sigue la misma regla:
  - Si la hija **no** tiene `__init__`, **hereda** el de la madre (`Tree`).
  - Si la hija **sí** tiene `__init__`, lo **sobrescribe**; si no llama a `super().__init__()`, el objeto se queda sin los atributos de la madre.

### Ejemplo

*`Plant` reducida a lo necesario para este tema.*

```python
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1

    def show(self):
        print(f"{self.name}: {self.height}cm")


class Flower(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)   # la madre crea name y height
        self.color = color               # la hija añade lo suyo

    def show(self):                      # AMPLÍA: madre + lo suyo
        super().show()
        print(f"  color: {self.color}")


class Tree(Plant):
    def grow(self):                      # SOBRESCRIBE: sustituye
        self.height += 5


garden = [Plant("Fern", 10), Flower("Rose", 25, "red"), Tree("Oak", 200)]
for plant in garden:                     # POLIMORFISMO
    plant.grow()
    plant.show()
# Fern: 11cm
# Rose: 26cm
#   color: red
# Oak: 205cm
```

---

## 4. Encapsulación

La **encapsulación** consiste en **proteger los atributos** para que no se cambien desde fuera sin control (por ejemplo, una altura negativa).

### Atributo público

- **QUÉ ES:** un atributo sin protección.
- **SINTAXIS:** sin guion bajo: `self.height`.
- **DESDE FUERA:** se lee y se cambia libremente: `rose.height = -5`.

### Atributo protegido

- **QUÉ ES:** un atributo que **no se debería** tocar desde fuera. Es solo una **convención**.
- **SINTAXIS:** un guion bajo: `self._height`.
- **DESDE FUERA:** funciona igual (`rose._height = -5`); Python no lo impide.

### Atributo privado

- **QUÉ ES:** un atributo que Python **renombra** para que sea difícil de alcanzar desde fuera.
- **SINTAXIS:** dos guiones bajos: `self.__height`.
- **DESDE FUERA:** `rose.__height` da `AttributeError`.

### Getters y setters

- **QUÉ ES:** métodos que dan acceso **controlado** al atributo; el setter **valida** antes de cambiarlo.
- **SINTAXIS:** `def get_height(self):` y `def set_height(self, value):`.
- **DESDE FUERA:** `rose.get_height()` y `rose.set_height(30)`.

### @property

- **QUÉ ES:** getter y setter que **se usan como un atributo** normal, sin paréntesis.
- **SINTAXIS:** `@property` encima del getter y `@height.setter` encima del setter; los dos se llaman igual, `height`.
- **DESDE FUERA:** `rose.height` y `rose.height = 30`; por debajo se ejecutan los métodos.

### No confundir: name mangling

- Dentro de la clase, Python renombra `__height` a `_Plant__height`. A esto se le llama **name mangling**.
- **Leer** `rose.__height` → `AttributeError`, porque con ese nombre no existe.
- **Escribir** `rose.__height = -5` → no da error, pero crea un atributo **nuevo** que no tiene nada que ver con el de la clase.
- **Escribir** `rose._Plant__height = -5` → sí cambia el de la clase.
- **Conclusión:** en Python **nada es privado de verdad**. La protección real la dan los getters y setters que validan.

### Ejemplo

*`Plant` reducida a lo necesario para este tema.*

```python
class Plant:
    def __init__(self, name, height):
        self.name = name          # público
        self.__height = height    # privado

    @property
    def height(self):             # getter: rose.height
        return self.__height

    @height.setter
    def height(self, value):      # setter: rose.height = 30
        if value < 0:
            raise ValueError("height must be positive")
        self.__height = value


rose = Plant("Rose", 25)
rose.height = 30              # pasa por el setter, que valida
print(rose.height)            # 30
print(rose._Plant__height)    # 30  -> name mangling: se puede alcanzar
# rose.height = -5            -> ValueError
# print(rose.__height)        -> AttributeError
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
