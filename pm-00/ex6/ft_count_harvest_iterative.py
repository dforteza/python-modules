def ft_count_harvest_iterative() -> None:
    n: int = int(input("Days until harvest: "))
    for i in range(1, n + 1):
        print("Day", i)
    print("Harvest time!")
