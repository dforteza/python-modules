import importlib


reagents = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
]
flag = False

print("REAGENT STATUS: Loading reagents...")
print("Checking dependencies:")

for name, description in reagents:
    try:
        modulo = importlib.import_module(name)
        print(f"[OK] {name} ({modulo.__version__}) - {description}")
    except ModuleNotFoundError:
        print(f"[MISSING] {name}")
        print(f"  pip: pip install {name}")
        print(f"  Poetry: poetry add {name}")
        flag = True

print("pip installs packages directly, "
      "while Poetry manages project dependencies.")

if not flag:
    print("All reagents present and accounted for.")
