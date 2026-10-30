import random

ACHIEVEMENTS = ["Crafting Genius", "World Savior", "Master Explorer",
                "Collector Supreme", "Untouchable", "Boss Slayer",
                "Strategist", "Unstoppable", "Speed Runner", "Survivor",
                "Treasure Hunter", "First Steps", "Sharp Mind",
                "Hidden Path Finder"]


def gen_player_achievements() -> set[str]:
    count = random.randint(3, 8)
    res = set(random.sample(ACHIEVEMENTS, count))
    return (res)


def display(players: list[tuple[str, set[str]]]) -> None:
    for name, achievements in players:
        print(f"Player {name}: {achievements}")


def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    # Assign and print player and its achievements
    print()
    players = [("Alice", gen_player_achievements()),
               ("Bob", gen_player_achievements()),
               ("Charlie", gen_player_achievements()),
               ("Dylan", gen_player_achievements())]
    display(players)
    print()

    # DISTINCT: All different achievements
    distinct = set()
    for name, achievements in players:
        distinct = distinct.union(achievements)
    print(f"All distinct achievements: {distinct}")
    print()

    # COMMON: All common achievements between players
    common = players[0][1]
    for name, achievements in players:
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")
    print()

    # ONLY: player_achievements - distinct(all - this player)
    for name, achievements in players:
        others = set()
        for other_name, other_achievements in players:
            if other_name != name:
                others = others.union(other_achievements)
        only = achievements.difference(others)
        print(f"Only {name} has: {only}")
    print()

    # MISSING: All achievements - player_achievements
    all = set(ACHIEVEMENTS)
    for name, achievements in players:
        missing = all.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    achievement_tracker()
