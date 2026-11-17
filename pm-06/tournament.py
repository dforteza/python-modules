from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (BattleStrategy, NormalStrategy, AggressiveStrategy,
                 InvalidStrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(0, len(opponents)):
            for j in range(i + 1, len(opponents)):
                # Create Creatures
                a = opponents[i][0].create_base()
                b = opponents[j][0].create_base()
                # Start battle
                print()
                print("* Battle *")
                print(a.describe())
                print(" vs.")
                print(b.describe())
                print(" now fight!")
                # Attack
                opponents[i][1].act(a)
                opponents[j][1].act(b)

    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def tournament() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle([(flame, normal), (transform, aggressive)])
    print()

    print("Tournament 1 (error)")
    print(" [ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle([(transform, aggressive), (flame, aggressive)])


if __name__ == "__main__":
    tournament()
