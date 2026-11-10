import sys


def stream_management(argv: list[str]) -> None:
    if len(argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
        print(
            f"[STDERR] Error opening file '{filename}': {error}",
            file=sys.stderr)
        return

    # TRANSFORM: '#' al final de cada línea
    new_content: str = ""
    for line in content.splitlines():
        new_content += line + '#' + '\n'

    # MOSTRAR EL CONTENIDO TRANSFORMADO
    print()
    print("Transform data:")
    print("---")
    print()
    print(new_content, end="")
    print()
    print("---")

    # SAVE FILE
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip("\n")
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
        print(
            f"[STDERR] Error opening file '{new_filename}': {error}",
            file=sys.stderr)
        print("Data not saved.")


if __name__ == "__main__":
    stream_management(sys.argv)
