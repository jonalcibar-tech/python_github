class Plant:

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name: str = (name)
        print(f"\nPlant created: {self._name}")
        self._height: float = self.set_height(height)
        self._age: int = self.set_age(age)

    def set_height(self, height: float = 0.0) -> float:
        if height >= 0:
            print(f"{self._name} height updated: {height}cm")
            return (height)
        print("Error, height can't be negative. Set to 0.0")
        return (0.0)

    def set_age(self, age: int) -> int:
        if age >= 0:
            print(f"{self._name} age updated: {age} days")
            return (age)
        print("Error, age can't be negative. Set to 0")
        return (0)

    def get_height(self) -> None:
        print(f"{self._name} height: {round(self._height, 1)}cm")

    def get_age(self) -> None:
        print(f"{self._name} age: {self._age} days old")

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, ", end="")
        print(f"{self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", -2, 90)
    plant4 = Plant("Sunflower", 80.0, -45)
    plant5 = Plant("Fern", 15.0, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]
    print(f"\nTotal plants: {len(plants)}")


if __name__ == "__main__":
    main()
