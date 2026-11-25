class Plant:

    def __init__(self, name: str, plant_type: str = "",
                 height: float = 0, age: int = 0) -> None:
        self._name: str = name
        self._plant_type: str = plant_type
        self._height: float = height
        self._age: int = age

    def set_height(self, height: float = 0.0) -> float:
        if height >= 0:
            self._height = height
            print(f"{self._name} height updated: {self._height}cm")
            return (self._height)
        else:
            print("Error, height can't be negative. Set to 0.0")
            return (0.0)

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")
        
class Flower(Plant):
    def __init__(self, name: str, plant_type: str = "", height: float = 0,
                 age: int = 0, color: str = "", bloom: bool = False) -> None:
        super().__init__(name, plant_type, height, age)
        self._color: str = color
        self._bloom: bool = bloom
        self._seeds_number = None # Placeholder until the flower blooms

    def bloom(self) -> None:
        self._bloom = True
        Flower.append(self._seeds_number) = Seed(self._name)
        Flower.show(self)

    def show(self) -> None:
        Plant.show(self)
        print(f"Color : {self._color}")
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
            print(f"Seeds: {Seed._seeds_number}")
        else:
            print(f"{self._name} has not bloomed yet")
            

class Seed(Flower):
    def __init__(self, name: str, seeds_number: int = 42) -> int:
        super().__init__(name, plant_type = None, height = None, age = None, color = None, bloom = None) -> None:
        self._seeds_number = seeds_number
        return(seeds_number)

    #def get_seeds_number() -> int:
    #    return(_seeds_number)


def main() -> None:
    plant4 = Flower("Sunflower", "Flower", 80.0, -45, "yellow", False)
    Flower.bloom(plant4)
    
if __name__ == "__main__":
    main()