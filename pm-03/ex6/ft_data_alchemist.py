import random

PLAYERS = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john",
           "kevin", "Liam"]


def data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {PLAYERS}")

    capitalized: list[str] = [x.capitalize() for x in PLAYERS]
    print(f"New list with all names capitalized: {capitalized}")

    only_capitalized: list[str] = [x for x in PLAYERS if x[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")
    print()

    scores: dict[str, int] = {
        name: random.randint(1, 100) for name in capitalized}
    print(f"Score dict: {scores}")

    average: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores = {
        name: score for name, score in scores.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    data_alchemist()
