class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self, growth: float) -> None:
        self.height += growth

    def get_older(self, time: int) -> None:
        self.age += time


def main() -> None:
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)
    # y creo una lista para que pueda iterar
    plants = [plant1, plant2, plant3, plant4, plant5]
    print("=== Plant Factory Output ===")
    for i in plants:
        print("Created: ", end="") # end="" significa imprime a continuación
        Plant.show(i)
        """ No valdría print(f"Created: {Plant.show(i)} porque print(f llama
         primero a la función show() que ya imprime la planta y luego como
        show() devuelve None imprime Created: None"""

if __name__ == "__main__":
    main()

