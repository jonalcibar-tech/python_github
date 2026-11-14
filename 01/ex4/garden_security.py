class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth: float = 0.0) -> None:
        if growth <0:
            print("grow value must be positive")
            return()
        self.height += growth

    def get_older(self, time: int = 0) -> None:
        if time < 0:
            print("time value must be positive")
            return()
        self.age += time

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]
    print("=== Plant Factory Output ===")
    for i in plants:
        print("Created: ", end="")
        Plant.show(i)


if __name__ == "__main__":
    main()

"""
Exercise4
ft_garden_security

Directory: ex4/
Files to Submit: ft_garden_security.py
Authorized: print(), range(), round()

The garden manager is concerned about data integrity. Some volunteers accidentally
corrupted plant data by setting invalid values (negative heights, impossible ages). You
need to create a secure system that protects and encapsulates sensitive data.
Requirements:
• Improve your Plant class in order to protect its data from corruption
• Provide controlled ways to modify plant data: set_height(), set_age()
• Provide safe ways to access plant data: get_height(), get_age()
• Ensure plant height cannot be negative through validation
• Ensure plant age cannot be negative through validation
• Print error messages from the class when invalid values are provided, leaving data
unchanged or creating the plant with default values
• Use encapsulation: prevent your class attributes from being used directly by using
the “protected” convention (not the mangling)

Consider how you might create a system that validates data before storing it, ensuring
data integrity.

15

Code Cultivation Object-Oriented Garden Systems

Example:
$> python3 ft_garden_security.py
=== Garden Security System ===
Plant created: Rose: 15.0cm, 10 days old
Height updated: 25cm
Age updated: 30 days
Rose: Error, height can't be negative
Height update rejected
Rose: Error, age can't be negative
Age update rejected
"""