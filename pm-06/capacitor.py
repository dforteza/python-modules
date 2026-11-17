from ex3 import Creature, TransformCapability, TransformCreatureFactory


def test_capability(creature : Creature, label : str) -> None:
    print(f" {label}:")
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


if __name__ == "__main__":
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()
    test_capability(factory.create_base(), "base") # Shiftling
    test_capability(factory.create_evolved(), "evolved")
