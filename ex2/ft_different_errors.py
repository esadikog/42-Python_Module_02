def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        10/0
    elif (operation_number == 2):
        open("test.txt")
    elif (operation_number == 3):
        "hello" + 5
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("\n=== Garden Error Types Demo ===\n")
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        finally:
            print()
    print("All error types tested successfully!")
    print("=== End of Program ===\n")


if __name__ == "__main__":
    test_error_types()
