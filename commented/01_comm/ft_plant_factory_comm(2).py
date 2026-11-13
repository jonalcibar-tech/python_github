class Plant:
    """aquí, en vez de crear una lista fuera de la clase Plants, la
    hacemos dentro de la clase, "plants: list = []" appending cada nuevo objeto creado 
    por el _init_ a la lista plants mediante Plant.plants.append(self)
    """
    plants: list = []

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.plants.append(self)

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self, growth: float) -> None:
        self.height += growth

    def get_older(self, time: int) -> None:
        self.age += time


def main() -> None:
    Plant("Rose", 25.0, 30),
    Plant("Oak", 200.0, 365),
    Plant("Cactus", 5.0, 90),
    Plant("Sunflower", 80.0, 45),
    Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    for i in Plant.plants:
        print("Created: ", end="")
        Plant.show(i)


if __name__ == "__main__":
    main()
