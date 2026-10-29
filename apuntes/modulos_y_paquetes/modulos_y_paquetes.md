# Módulos y paquetes en Python

*Apuntes de módulos y paquetes (pm-05 · The Codex). Ejemplos sacados de los ejercicios de los módulos.*

## Índice

1. [Entornos virtuales: `venv`](#1-entornos-virtuales-venv)
2. [Ejecutar o importar: `__name__`](#2-ejecutar-o-importar-__name__)

---

## 1. Entornos virtuales: `venv`

Un **venv** es una CARPETA CON SU PROPIO PYTHON Y SUS PROPIOS PAQUETES, separada del Python del sistema.

### Chuleta

| Para qué | Comando |
|---|---|
| Crear | `python3 -m venv ~/venv42` |
| Activar | `source ~/venv42/bin/activate` |
| Salir | `deactivate` |
| Instalar paquetes | `pip install flake8 mypy` |
| Ver qué tiene instalado | `pip list` |
| Comprobar qué Python usas | `which python3` (si sale `~/venv42/...`, estás dentro) |
| Guardar la lista de paquetes | `pip freeze > requirements.txt` |
| Reinstalarla en otro sitio | `pip install -r requirements.txt` |
| Borrarlo | `deactivate` y luego `rm -rf ~/venv42` |
| Sin venv (plan B) | `pip install --user flake8 mypy` |

**Mantra:** *EL VENV NO VIAJA; VIAJA LA LISTA (`requirements.txt`).*

### No confundir

- **Copiar el venv frente a recrearlo:** el venv guarda RUTAS ABSOLUTAS (`/home/dforteza/...`), así que en otra máquina no funciona. Se crea uno nuevo y se instala desde `requirements.txt`.
- **`deactivate` frente a borrar:** `deactivate` solo sale del venv; la carpeta sigue ahí y la próxima vez basta con `source`.

### Ejemplo: corregir en el campus

```bash
python3 -m venv ~/venv42 && source ~/venv42/bin/activate
pip install flake8 mypy             # solo la primera vez
flake8 .                            # desde la carpeta del evaluado
mypy ex*/*.py
deactivate
```

---

## 2. Ejecutar o importar: `__name__`

`__name__` es una VARIABLE QUE PYTHON RELLENA SOLO e indica cómo se está usando el archivo.

### Ejecutar directamente

- **QUÉ ES:** `python3 ft_garden_intro.py` → `__name__` vale `"__main__"`.
- **SINTAXIS:** `if __name__ == "__main__":` → el `if` es verdadero y se ejecuta `main()`.
- **CUÁNDO:** para probar el archivo por sí solo.

### Importar

- **QUÉ ES:** `import ft_garden_intro` → `__name__` vale `"ft_garden_intro"` (el nombre del módulo).
- **SINTAXIS:** el mismo `if` es falso y `main()` NO SE EJECUTA.
- **CUÁNDO:** cuando otro archivo solo quiere usar tus funciones o clases.

**Mantra:** *EJECUTAS → `"__main__"` → CORRE; IMPORTAS → SU NOMBRE → NO CORRE.*

### Ejemplo

```python
def main() -> None:
    print("=== Welcome to My Garden ===")


if __name__ == "__main__":      # solo si lanzas este archivo
    main()
```

---
