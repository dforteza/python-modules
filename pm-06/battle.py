from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    a = factory1.create_base()
    b = factory2.create_base()
    print(a.describe())
    print(" vs.")
    print(b.describe())
    print(" fight!")
    print(a.attack())
    print(b.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    test_factory(flame)
    print()
    test_factory(transform)
    print()
    test_battle(flame, transform)
