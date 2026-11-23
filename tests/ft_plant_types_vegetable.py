class Plant:

    def __init__(self, name: str, plant_type: str = "", height: float = 0, age: int = 0) -> None:
        self._name: str = (name)
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

    def set_age(self, age: int) -> int:
        if age >= 0:
            self._age =+ age
            print(f"{self._name} age updated: {self._age} days")
            return (self._age)
        else:
            print("Error, age can't be negative. Set to 0")
            return (0)

    def get_height(self) -> None:
        print(f"{self._name} height: {round(self._height, 1)}cm")

    def get_age(self) -> None:
        print(f"{self._name} age: {self._age} days old")

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")
class Vegetable(Plant):
    def __init__(self, name: str, plant_type: str = "", height: float = 0, age: int = 0,
                 harv_season: str = "", growth_rate: float = 0.0, nutr_val: int = 0, 
                 nutr_growth_rate: float = 0,) -> None:
        super().__init__(name, plant_type, height, age)
        self._harv_season: int = harv_season
        self._growth_rate: float = growth_rate
        self._nutr_val: int = (nutr_val)
        self._nutr_growth_rate: float = nutr_growth_rate
    
    def age(self, days: int) -> None:
        self._age = Plant.set_age(self, (self._age + days))
        self.grow(days)
        
    def grow(self, days: int) -> None:
        height_increase: float = days * self._growth_rate 
        self.set_height = Plant.set_height(self, self._height + height_increase)
        self._nutr_val =+  height_increase * self._nutr_growth_rate
        
    def show(self) -> None:
        Plant.show (self)
        print(f"Harvest season: {self._harv_season}")
        print(f"Nutritional value: {round(self._nutr_val)}")


def main() -> None:
    plant6 = Vegetable("Tomato", "Vegetable", 5.0, 10, "April", 2.1, 0, 0.4761)
    plants = [plant6]
    Vegetable.show(plant6)
    print("[make tomato grow and age for 20 days]")
    Vegetable.age(plant6, 20)
    Vegetable.show(plant6)

if __name__ == "__main__":
    main()