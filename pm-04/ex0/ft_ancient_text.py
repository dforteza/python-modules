import sys


def ancient_text(av: list[str]) -> None:
    if len(av) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = av[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    # READ FILE
    try:
        f = open(filename, "r")
        content = f.read()

        print("---")
        print()
        print(content)
        print()
        print("---")
        print(f"File '{filename}' closed.")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")


if __name__ == "__main__":
    ancient_text(sys.argv)
