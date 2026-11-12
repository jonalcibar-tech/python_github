class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height ,1)}cm, {self.age} days old")

    def grow(self, growth) -> None:
        self.height += growth

    def get_older(self, time) -> None:
        self.age += time

    def week_growth_sim(self, rate) -> None:
        # simulate a growth of a plant in a week
        print("=== Garden Plant Growth ===")
        Plant.show(self)
        for day in range(1, 8, 1):
            Plant.grow(self, rate)
            Plant.get_older(self, 1)
            print(f"=== Day {day} ===")
            Plant.show(self)
        print(f"Growth this week: {round(rate*7, 1)}cm")


def main():
    # simulate a growth of a plant in a week
    plant1 = Plant("Rose", 20, 30)
    Plant.week_growth_sim(plant1, 0.8)


if __name__ == "__main__":
    main()

"""
Exercise2
ft_plant_growth

Directory: ex2/
Files to Submit: ft_plant_growth.py
Authorized: print(), range(), round()

The garden manager wants to simulate plant growth over time. You need to track how
plants change and provide operations to modify their state.
Requirements:
• Reuse your Plant class from Exercise 1
• Plants need to be able to grow() and age() on their own (i.e., these will be methods
of the class)
• Simulate a week of growth for a plant, then access the data in the class to get the
final height and display the total week increase.
• Consider how the plant should change over time when using grow() and age().
Different plants can evolve differently.

Your program should show a plant changing over time, and a summary at the end of the
week. Think about giving your plants behaviors that will drive grow() differently.

Code Cultivation Object-Oriented Garden Systems

Example:
$> python3 ft_plant_growth.py
=== Garden Plant Growth ===
Rose: 25.0cm, 30 days old
=== Day 1 ===
Rose: 25.8cm, 31 days old
=== Day 2 ===
Rose: 26.6cm, 32 days old
=== Day 3 ===
Rose: 27.4cm, 33 days old
=== Day 4 ===
Rose: 28.2cm, 34 days old
=== Day 5 ===
Rose: 29.0cm, 35 days old
=== Day 6 ===
Rose: 29.8cm, 36 days old
=== Day 7 ===
Rose: 30.6cm, 37 days old
Growth this week: 5.6cm

There are multiple possible approaches to handle this. You can implement it the way you
want, adding attributes to the Plant class, parameters to the methods in the class, etc.
"""