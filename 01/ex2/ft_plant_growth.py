class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

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
