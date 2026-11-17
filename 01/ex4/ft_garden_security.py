class Plant:

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self.name: str = (name)
        print(f"\nPlant created: {self.name}")
        self.height: float = self.set_height(height)
        self.age: int = self.set_age(age)

    def set_height(self, height: float = 0.0) -> float:
        if height < 0:
            print("Error, height can't be negative")
            height = 0
        print(f"Height updated: {height}cm")
        return (height)

    def set_age(self, age: int) -> int:
        if age < 0:
            print("Error, age can't be negative")
            age = 0
        print(f"Age updated: {age} days")
        return (age)

    def get_height(self) -> None:
        print(f"{self.name} height: {round(self.height, 1)}cm")

    def get_age(self) -> None:
        print(f"{self.name} age: {self.age} days old")

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


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
