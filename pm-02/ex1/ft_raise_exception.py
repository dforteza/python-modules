MIN_TEMP = 0
MAX_TEMP = 40


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > MAX_TEMP:
        raise ValueError(f"{temp}°C is too hot for plants (max {MAX_TEMP}°C)")
    if temp < MIN_TEMP:
        raise ValueError(f"{temp}°C is too cold for plants (min {MIN_TEMP}°C)")
    return (temp)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    for temp_str in ["25", "abc", "100", "-50"]:
        print(f"\nInput data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
