
"""
Hasta ahora creaba los objetos son comprobarlos, ahora recurre
a set_height y set_age comprobando previamente su valor postitivo
El subject pide la creación de get_age() y get height() pero yo
no los necesito ya que el __init__ llama e set(height o age) devolviendo
mensajes si son negativos (y ponerlos a 0 ya que en el subject 
permite no variarlos o dejar a default) tanto y al crearlos como
al alterarlos (set) y logro sacarlo en 45 lineas claras en vez de 63.
"""
class Plant:
    """
    los atributos de Plant los antecedo de _ (p.ej. _name _age)
    es una convención que alerta que ese atributo de los objetos
    no debe alterarse sin más sino a traves de de métodos, asi
    _age = -5 no se "debería hacer" se debe alterar a traves de set_age(age)
    """
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
        print(f"{self._name}: {round(self._height, 1)}cm, end=""")
        print(f"{self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", -2, 90)
    plant4 = Plant("Sunflower", 80.0, -45)
    plant5 = Plant("Fern", 15.0, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]
    print(f"\nTotal plants: {len(plants)}")


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