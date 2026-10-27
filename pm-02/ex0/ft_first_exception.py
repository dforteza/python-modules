def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    for temp_str in ["25", "abc"]:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
