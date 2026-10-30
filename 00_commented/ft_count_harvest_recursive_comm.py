
# ya estoy diciendo day :int (que day es un entero) esto es
# "type hint" (pistas de tipo) no es necesario pero se lee mejor el código.
# Que el valor inicial de day es 0 y que no retorna nada -> None (tambien type hint)
def ft_count_harvest_recursive(day: int = 0) -> None:
    if not day:
        harvest_day: int = int(input("Days until harvest: ")) #tengo que hacer int(input("Da.., para poder comprobar luego con <=
        day += 1
    while day <= harvest_day:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")

#para comprobar la función, si el nombre del archivo pasado a interprete python3 coincide con __name__
#ejecuta función como main
if __name__ == "__main__":
    ft_count_harvest_recursive()