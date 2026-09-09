def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_inputs = ["25", "abc"]

    for value in test_inputs:
        print(f"Input data is '{value}'")
        try:
            response = input_temperature(value)
            print(f"Temperature is now {response}°C")
        except ValueError as error:
            print("Caught input_temperature error: ", error)
        finally:
            print()


if __name__ == "__main__":
    print("\n=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
    print("=== End of Program ===\n")
