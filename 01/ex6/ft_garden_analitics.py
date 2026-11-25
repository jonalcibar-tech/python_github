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

    @staticmethod
    def older_than_year(days):
        if days > 365:
            print (f"Is {days} days more than a year? -> True")
        else:
            print (f"Is {days} days more than a year? -> False")


class Statistics(Plant):
    def __init__(self, grow_calls : int = 0, age_calls : int = 0,
                 show_calls: int =0) -> None:
        pass
        
        

class Flower(Plant):
    def __init__(self, name: str, plant_type: str = "", height: float = 0,
                 age: int = 0, color: str = "", bloom: bool = False) -> None:
        super().__init__(name, plant_type, height, age)
        self._color: str = color
        self._bloom: bool = bloom
        self._seeds_number = None # Placeholder until the flower blooms

    def bloom(self) -> None:
        self._bloom = True
        self._seeds_number = Seed(self._name)
        Flower.show(self)

    def show(self) -> None:
        Plant.show(self)
        print(f"Color : {self._color}")
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
            print(f"Seeds: {Seed.get_seeds_number()}")
        else:
            print(f"{self._name} has not bloomed yet")

class Seed(Flower):
    def __init__(self, name: str, seeds_number: int = 42) -> None:
        super().__init__(name)
        self._seeds_number = seeds_number

    def get_seeds_number() -> int:
        return(self._seeds_number)


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


class Anonymous(Plant):
    def __init__(self, name: str = "Anonymous", plant_type: str = "",
                 height: float = 0, age: int = 0) -> None:
        super().__init__(plant_type, height, age)
        Plant.show(self)


def main() -> None:
    plant1 = Flower("Rose", "Flower", 15.0, 10, "red", False)
    plant2 = Tree("Oak", "Tree", 200.0, 365, 5.0)
    plant3 = Plant("Cactus", "", -2, 90)
    plant4 = Flower("Sunflower", "Flower", 80.0, -45, "yellow", True)
    plant5 = Tree("Fern", "Tree", 15.0, 120)
    plant6 = Vegetable("Tomato", "Vegetable", 5.0, 10, "April", 2.1, 0, 0.4761)
    plants = [plant1, plant2, plant3, plant4, plant5, plant6]
    print("Garden statistics")
    print("=== Check year.old ===")
    Plant.older_than_year(30)
    Plant.older_than_year(400)
    Flower.bloom(plant4)



if __name__ == "__main__":
    main()

    """
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
"""

"""
ft_garden_analytics

Directory: ex6/
Files to Submit: ft_garden_analytics.py
Authorized: super(), print(), range(), round(), staticmethod(),
classmethod()

Enhance your classes from the previous exercise to display analytics. You will need to
handle complex data relationships, use nested components and inheritance chains.
Requirements:
• Create a static method for the Plant class that checks if a specific age given as a
parameter is older than a year.
• Create a class method that allows you to create an “anonymous” plant directly
when you do not yet have all the information.
• Create a Seed class that inherits from Flower, and holds the number of seeds once
the flower has bloomed. The show() method must be improved accordingly.
• Each Plant has an internal system, implemented as a nested class, that holds
statistical data: number of grow() calls, number of age() calls, number of show()
calls. Encapsulation is required, as well as a display function.
• Trees need an extra piece of statistical data: number of produce_shade() calls.
• Finally, create a unique function, not part of any class, that displays statistics for
any kind of plant.

Note: the decorator syntax is also accepted for static and class
methods

19

Code Cultivation Object-Oriented Garden Systems

Example:
$> python3 ft_garden_analytics.py
=== Garden statistics ===
=== Check year-old
Is 30 days more than a year? -> False
Is 400 days more than a year? -> True
=== Flower
Rose: 15.0cm, 10 days old
Color: red
Rose has not bloomed yet
[statistics for Rose]
Stats: 0 grow, 0 age, 1 show
[asking the rose to grow and bloom]
Rose: 23.0cm, 10 days old
Color: red
Rose is blooming beautifully!
[statistics for Rose]
Stats: 1 grow, 0 age, 2 show
=== Tree
Oak: 200.0cm, 365 days old
Trunk diameter: 5.0cm
[statistics for Oak]
Stats: 0 grow, 0 age, 1 show
0 shade
[asking the oak to produce shade]
Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
[statistics for Oak]
Stats: 0 grow, 0 age, 1 show
1 shade
=== Seed
Sunflower: 80.0cm, 45 days old
Color: yellow
Sunflower has not bloomed yet
Seeds: 0
[make sunflower grow, age and bloom]
Sunflower: 110.0cm, 65 days old
Color: yellow
Sunflower is blooming beautifully!
Seeds: 42
[statistics for Sunflower]
Stats: 1 grow, 1 age, 2 show
=== Anonymous
Unknown plant: 0.0cm, 0 days old
[statistics for Unknown plant]
Stats: 0 grow, 0 age, 1 show
"""