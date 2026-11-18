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


class Type(Plant):
    def __init__(self, name: str, height: float = 0, age: int = 0
                 plant_type: str) -> None:
    super.__init__(name, height, age)
    self._plant_type: str = type


class Flower(Type):
    def _init_(self, name, color, bloom = False) -> None:
        super.__init__(name)
        self._color: str = color
        self._bloom: bool = bloom


class Tree(Type):
    def _init_(self, name, shade) -> None:
        super.__init__(name)
        self.shade: float= ()


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", -2, 90)
    plant4 = Plant("Sunflower", 80.0, -45)
    plant5 = Plant("Fern", 15.0, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]

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