
# ya estoy diciendo que el valor inicial de day es 0 y retorna nada (None)
# esto es para 
def ft_count_harvest_recursive(day: int = 0) -> None:
    if not day:
        harvest_day: int = int(input("Days until harvest: "))
        day += 1
    while day <= harvest_day:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")


def main():
    ft_count_harvest_recursive()


if __name__ == "__main__":
    ft_count_harvest_recursive()