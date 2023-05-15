import random

if __name__ == "__main__":
    # pobieram cyfrę z inputa, od razu generuję parę randomowych cyfr i dziele na tuple, bez zipowania
    list_lenght = int(input("Podaj długość listy:"))
    pairs = [(random.randint(1, 100), random.randint(1, 100)) for i in range(list_lenght)]
    print("Wylosowane pary:", pairs)

    # operacje
    operations = (
        ("suma:", lambda x, y: x + y),
        ("różnica:", lambda x, y: x - y),
        ("mnożenie:", lambda x, y: x * y),
        ("iloraz:", lambda x, y: x / y)
    )

    # tworzę listę, otwieram tuple(nazwa działania ( wykonane działanie dla każdej z podanych par ))
    results = [(operation[0], tuple(operation[1](x, y) for x, y in pairs)) for operation in operations]
    print(results)
