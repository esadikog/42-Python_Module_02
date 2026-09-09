class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.message = message
        super().__init__(self.message)


def test_garder_errors() -> None:
    print("\n=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError Without Message")
    try:
        raise PlantError()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting PlantError With Message")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError Without Message")
    try:
        raise WaterError()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting WaterError With Message")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting GardenError Without Message")
    try:
        raise GardenError()
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nTesting GardenError For PlantError")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nTesting GardenError For WaterError")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("\nAll custom error types work correctly!")
    print("=== End of Program ===")


if __name__ == "__main__":
    test_garder_errors()
