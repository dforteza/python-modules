class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 0.8) -> None:
        self._name: str = name
        self._growth_rate: float = growth_rate
        self._height: float = height if self._is_valid(height, "height") else 0
        self._age: int = age if self._is_valid(age, "age") else 0

    def _is_valid(self, value: float, field: str) -> bool:
        if value < 0:
            print(f"{self._name}: Error, {field} can't be negative")
            return False
        return True

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if self._is_valid(height, "height"):
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if self._is_valid(age, "age"):
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print("Age update rejected")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1


def main() -> None:
    print("=== Garden Security System ===")
    rose: Plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-1)

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
