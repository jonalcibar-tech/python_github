class Plant:

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name: str = (name)
        print(f"{self._name}")
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


class Flower(Plant):
    def __init__(self, name: str, height: float = 0, age: int = 0,
                 color: str = "", bloom: bool = False) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._bloom: bool = bloom

    def bloom(self):
        self._bloom = True
        Plant.show(self)

    def show(self) -> None:
        Plant.show(self)
        print("Color : {self._color}")
        if self._bloom:
             print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float = 0, age: int = 0,
                 trunk_diam: float = 0) -> None:
        super().__init__(name, height, age)
        self._trunk_diam = trunk_diam

    def shade(self) -> None:
        if self._trunk_diamm & self._height:
            print(f"Tree {self._name} now produces a shade of "
                  f"{round(self._height, 1)}cm long and "
                  f"{round(self._trunk_diamm, 1)}cm wide.")

    def show(self) -> None:
        Plant.show(self)
        print(f"Trunk diameter: {round(self._trunk_diam, 1)}")

class Vegetable(Plant):
    def __init__(self, name: str, height: float = 0, age: int = 0,
                 harv_season: str = "", nutr_val: float = 0, 
                 nutr_growth_rate: float = 0,
                 nutr_day_rate: float = 0)-> None:
        super().__init__(name, height, age)
        self._harv_season = harv_season
        self._nutr_val = nutr_val
        self._nutr_growth_rate = nutr_growth_rate
        self._nutr_day_rate = nutr_day_rate
    
    def age(self, days: int) -> None:
        self._age = Plant.set_age(self, self._age + days)
        self._nutr_val =+ days * self._nutr_day_rate     
        
    def grow(self, growth: float) -> None:
        self.set_height = Plant.set_height(self, self._height + growth)
        self._nutr_val =+ growth * self._nutr_growth_rate
        
    def show(self) -> None:
        Plant.show (self)
        print(f"Harvest season: {self._harv_season}")
        print(f"Nutritional value: {self._nutr_val}")


def main() -> None:
    plant1 = Flower("Rose", 15.0, 10, "red", False)
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant3 = Plant("Cactus", -2, 90)
    plant4 = Flower("Sunflower", 80.0, -45, "variable", True)
    plant5 = Plant("Fern", 15.0, 120)
    plant6 = Vegetable("Tomato", 5.0, 10, "April", 0, 2.1, 1)
    plants = [plant1, plant2, plant3, plant4, plant5, plant6]
    print("=== Garden Plant Types ===")
    Vegetable.show(plant6)
    Vegetable.age(plant6, 20)
    Vegetable.grow(plant6, 20)
    Vegetable.show(plant6)

if __name__ == "__main__":
    main()

"""""
The garden now needs to handle different types of plants: flowers, trees, and vegetables.
Each type has unique characteristics but inherits common plant features from its parent
category.
Requirements:
• Start with your Plant class from the previous exercise, which holds the common
features (name, height, and age)
• Create specialized types: Flower, Tree, and Vegetable
• Each specialized type should inherit the basic plant features
• Flower needs: a color attribute and ability to bloom()
• Tree needs: a trunk_diameter attribute and the ability to produce_shade()
• Vegetable needs: a harvest_season and a nutritional_value attributes
• When creating specialized plants, call the parent methods from inside your new
class using super(). It can be applied to any method, including __init__()
• A call to show() on a specialized class needs to print the standard Plant output
and the extra characteristics of your specialized plant. Your method override can
re-use the already existing code in the parent.
• Create at least one instance of each plant type; make the flower bloom; make the
nutritional value start from 0, then increase when the vegetable’s age() and grow()
methods are called.

17

Code Cultivation Object-Oriented Garden Systems

• Avoid duplicating common plant code across different specialized types.
• No need to validate the new attributes in the three new classes.

Example:
$> python3 ft_plant_types.py
=== Garden Plant Types ===
=== Flower
Rose: 15.0cm, 10 days old
Color: red
Rose has not bloomed yet
[asking the rose to bloom]
Rose: 15.0cm, 10 days old
Color: red
Rose is blooming beautifully!
=== Tree
Oak: 200.0cm, 365 days old
Trunk diameter: 5.0cm
[asking the oak to produce shade]
Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
=== Vegetable
Tomato: 5.0cm, 10 days old
Harvest season: April
Nutritional value: 0
[make tomato grow and age for 20 days]
Tomato: 47.0cm, 30 days old
Harvest season: April
Nutritional value: 20

How are you handling the common features shared by all plant types?
It is advised to avoid repeating the same code in the different
classes to handle these common features.
"""