import sys


def command_quest(av: list[str]) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {av[0]}")
    if len(av) > 1:
        print(f"Arguments received: {len(av[1:])}")
        i = 1
        while i < len(av):
            print(f"Argument {i}: {av[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(av)}")


if __name__ == "__main__":
    command_quest(sys.argv)
