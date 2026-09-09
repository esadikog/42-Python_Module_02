def input_temperature(temp: str) -> int:
    message: str
    celc: int = int(temp)

    if (celc >= 0 and celc <= 40):
        return celc
    if (celc > 0):
        message = f"{celc}°C is too hot for plants (max 40°C)"
    else:
        message = f"{celc}°C is too cold for plants (min 0°C)"
    raise Exception(message)


def test_temperature() -> None:
    test_inputs = ["25", "abc", "100", "-50"]

    for input in test_inputs:
        print(f"Input data is '{input}'")
        try:
            input_temperature(input)
            print(f"Temperature is now {input}°C")
        except Exception as error:
            print("Caught input_temperature error: ", error)
        finally:
            print()


if __name__ == "__main__":
    print("\n=== Garden Temperature ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
    print("=== End of Program ===\n")
