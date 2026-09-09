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


def water_plant(plant_name: str) -> None:
    if (plant_name.capitalize() == plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:

    print("\n=== Garden Watering System ===\n")
    test_inputs = ["Tomato", "lettuce", "Carrots"]
    try:
        print("\nTesting valid plants...")
        print("Opening watering system")
        for i in test_inputs:
            water_plant(i.capitalize())
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system")

    try:
        print("\nTesting invalid plants...")
        print("Opening watering system")
        for i in test_inputs:
            water_plant(i)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")
    print("=== End of Program ===")


if __name__ == "__main__":
    test_watering_system()
