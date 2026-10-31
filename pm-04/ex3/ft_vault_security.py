def secure_archive(filename: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, "r") as file:
                content = file.read()
            return (True, content)

        with open(filename, "w") as file:
            file.write(content)
        return (True, "Content successfully written to file")
    except OSError as error:
        return (False, str(error))


def vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", result[1]))


if __name__ == "__main__":
    vault_security()
