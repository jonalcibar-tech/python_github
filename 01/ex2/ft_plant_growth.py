class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self, growth: float) -> None:
        self.height += growth

    def get_older(self, time: int) -> None:
        self.age += time

    def week_growth_sim(self, rate: float) -> None:
        # simulate a growth of a plant in a week
        print("=== Garden Plant Growth ===")
        self.show()
        for day in range(1, 8):
            self.grow(rate)
            self.get_older(1)
            print(f"=== Day {day} ===")
            self.show()
        print(f"Growth this week: {round(rate*7, 1)}cm")


def main() -> None:
    # simulate a growth of a plant in a week
    plant1 = Plant("Rose", 20, 30)
    Plant.week_growth_sim(plant1, 0.8)


if __name__ == "__main__":
    main()
