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

    def set_age(self, age: int) -> int:
        if age >= 0:
            self._age = + age
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


class Flower(Plant):
    def __init__(self, name: str, plant_type: str = "", height: float = 0,
                 age: int = 0, color: str = "", bloom: bool = False) -> None:
        super().__init__(name, plant_type, height, age)
        self._color: str = color
        self._bloom: bool = bloom

    def bloom(self) -> None:
        self._bloom = True
        Flower.show(self)

    def show(self) -> None:
        Plant.show(self)
        print(f"Color : {self._color}")
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, plant_type: str = "",
                 height: float = 0, age: int = 0,
                 trunk_diam: float = 0) -> None:
        super().__init__(name, plant_type, height, age)
        self._trunk_diam = trunk_diam

    def shade(self) -> None:
        if self._trunk_diam and self._height:
            print(f"Tree {self._name} now produces a shade of "
                  f"{round(self._height, 1)}cm long and "
                  f"{round(self._trunk_diam, 1)}cm wide.")
        else:
            print(f"Tree {self._name} produces no shade")

    def show(self) -> None:
        Plant.show(self)
        print(f"Trunk diameter: {round(self._trunk_diam, 1)}")


class Vegetable(Plant):
    def __init__(self, name: str, plant_type: str = "", height: float = 0,
                 age: int = 0, harv_season: str = "",
                 growth_rate: float = 0.0, nutr_val: float = 0,
                 nutr_growth_rate: float = 0,) -> None:
        super().__init__(name, plant_type, height, age)
        self._harv_season = harv_season
        self._growth_rate = growth_rate
        self._nutr_val = nutr_val
        self._nutr_growth_rate = nutr_growth_rate

    def age(self, days: int) -> None:
        self._age = Plant.set_age(self, self._age + days)
        self.grow(days)

    def grow(self, days: int) -> None:
        height_increase: float = days * self._growth_rate
        self._height = Plant.set_height(self, self._height + height_increase)
        self._nutr_val = + height_increase * self._nutr_growth_rate

    def show(self) -> None:
        Plant.show(self)
        print(f"Harvest season: {self._harv_season}")
        print(f"Nutritional value: {round(self._nutr_val)}")


def main() -> None:
    plant1 = Flower("Rose", "Flower", 15.0, 10, "red", False)
    plant2 = Tree("Oak", "Tree", 200.0, 365, 5.0)
    plant3 = Plant("Cactus", "", -2, 90)
    plant4 = Flower("Sunflower", "Flower", 80.0, -45, "variable", True)
    plant5 = Tree("Fern", "Tree", 15.0, 120)
    plant6 = Vegetable("Tomato", "Vegetable", 5.0, 10, "April", 2.1, 0, 0.4761)
    plants = [plant1, plant2, plant3, plant4, plant5, plant6]
    print("=== Garden Plant Types ===")
    for i in plants:
        if isinstance(i, Flower):
            print("=== Flower")
            Flower.show(i)
            print(f"[asking the {i._name} to bloom]")
            Flower.bloom(i)
        elif isinstance(i, Tree):
            print("=== Tree")
            Tree.show(i)
            print(f"[asking the {i._name} to produce shade]")
            Tree.shade(i)
        elif isinstance(i, Vegetable):
            print("=== Vegetable")
            Vegetable.show(i)
            print("[make tomato grow and age for 20 days]")
            Vegetable.age(i, 20)
            Vegetable.show(i)

