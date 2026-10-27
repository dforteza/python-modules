class Plant:
    name: str
    height: float
    days: int
    growth_rate: float

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days += 1


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    rose.growth_rate = 0.8

    print("=== Garden Plant Growth ===")
    rose.show()
    start = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()
    print(f"Growth this week: {round(rose.height - start, 1)}cm")


if __name__ == "__main__":
    main()
