def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(seed_type.capitalize(), "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
        #lo anterior sería otra forma de usar el print con print(f...
    elif unit == "area":
        print(seed_type.capitalize(), "seeds:", "covers", quantity, end=" ")
        print("square meters")
    else:
        print("Unknown unit type")

if __name__ == "__main__":
	ft_seed_inventory("tomatoes", 5, "grams")