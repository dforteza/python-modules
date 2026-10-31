import sys


def archive_creation(argv: list[str]) -> None:
    if len(argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    # READ FILE
    try:
        f = open(filename, "r")
        content = f.read()
        f.close()

        print("---")
        print()
        print(content, end="")
        print()
        print("---")
        print(f"File '{filename}' closed.")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    # TRANSFORM: '#' at the end
    new_content: str = ""
    for line in content.splitlines():
        new_content += line + '#' + '\n'

    # DISPLAY NEW_CONTENT
    print()
    print("Transform data:")
    print("---")
    print()
    print(new_content, end="")
    print()
    print("---")

    # SAVE FILE
    new_filename = input("Enter new file name (or empty): ")
    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        f = open(new_filename, "w")
        f.write(new_content)
        f.close()
        print(f"Data saved in file '{new_filename}'.")
    except OSError as error:
        print(f"Error opening file '{new_filename}': {error}")


if __name__ == "__main__":
    archive_creation(sys.argv)
