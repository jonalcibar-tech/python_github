class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
"""
Exercise 1: Garden Data Organizer

Exercise1
ft_garden_data

Directory: ex1/
Files to Submit: ft_garden_data.py
Authorized: print()

The community garden needs to track multiple plants with their information. You need
to store and display data for several plants efficiently.
Each plant has:
• A name
• Height in centimeters
• Age in days
Create a program that manages data for at least 3 different plants and displays their
information in an organized way.
Required: You must create a Plant class that serves as a model for any plant, rather
than handling each one individually. All plants will be described using the same at-
tributes, or characteristics: a name, a height, and an age. For each plant, the class will
be instantiated, then the attributes will be set to their specific values. You can use the
name you want for each attribute.
You will create a show() method in the class to display the plant information.
Example:
$> python3 ft_garden_data.py
=== Garden Plant Registry ===
Rose: 25cm, 30 days old
Sunflower: 80cm, 45 days old
Cactus: 15cm, 120 days old

9

Code Cultivation Object-Oriented Garden Systems

How are you currently storing plant information? There are multiple
ways to do this. What challenges might arise with more plants? In
the next exercises, you may eventually need to make your approach
evolve.

If you have already worked with Python programming or object-oriented
programming in the past, you will probably go directly for an
advanced solution. In this case, you may find the next exercises
****************************************************************
Yo hubiese preferido iterar solo poniendo show()
pero para ello tendría que crear una lista demtro de la clase, 

class Plant:
    all_plants = []
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

        # Añadimos el objeto recién creado a la lista
        Plant.all_plants.append(self)
en la que cada vez que la llamo para crear un objeto hace un append a la lista
y luego para imprimir itera dentro de la lista imprimiendo cada self pero ¡OJO 
QUE HABRIA QUE CREAR UN METODO DE CLASE classmethod

    @classmethod    
    def show(cls):
        print("=== Garden Plant Registry ===")

        for plant in cls.all_plants:
            print(f"Name: {plant.name}")
            print(f"Height: {plant.height}")
            print(f"Age: {plant.age}")

y en el main bastaría con poner:
Plant.show()
"""