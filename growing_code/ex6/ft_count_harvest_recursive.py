def ft_count_harvest_recursive(day: int = 0) -> None:
    if not day:
        harvest_day = int(input("Days until harvest: "))
        day += 1
    while day <= harvest_day:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")
