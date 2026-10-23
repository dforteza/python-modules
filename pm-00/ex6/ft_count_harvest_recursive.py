def recursive(s: int, e: int) -> None:
    if (s == e):
        return
    print("Day", s)
    recursive(s + 1, e)


def ft_count_harvest_recursive() -> None:
    n: int = int(input("Days until harvest: "))
    recursive(1, n + 1)
    print("Harvest time!")
