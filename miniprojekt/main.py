
import re
import random


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

# wykonywanie operacji na wyniku


def do_operation(sign, results, number):
    x = sum(results)
    if sign == "+":
        return x + number
    elif sign == "-":
        return x - number
    elif sign == "*":
        return x * number
    elif sign == "/":
        return float(x // number)
    else:
        return x


def roll_dice(num_rolls, sides):
    results = []
    for _ in range(num_rolls):
        dice = Dice(sides)
        results.append(dice.roll())
    return results
# funkcja przelosowywująca wynik


def reroll_dice(results, reroll, sides):
    for i in range(len(results)):
        if results[i] == reroll:
            dice_choice = input(f"Przerzucić wynik {results[i]}? (tak/nie): ")
            if dice_choice.lower() == "tak":
                dice = Dice(sides)
                results[i] = dice.roll()
    return results

# funkcja odrzucająca wyniki najwyższe najniższe.


def drop_high_low(results, high_drop, low_drop):
    if high_drop > 0:
        results = sorted(results, reverse=True)[high_drop:]
    if low_drop > 0:
        results = sorted(results)[low_drop:]
    return results

# funkcja dopasowywująca dane z inputa


def simulate_rolls(pattern):
    match = re.match(r"(\d+)?(?:\((\d+)d(\d+)(h(\d+))?(l(\d+))?(r(\d+))?\))?([\+\-\*\/])?(\d+)?", pattern)
    if match:
        series_count = int(match.group(1)) if match.group(1) else 1 if not match.group(1) else 1
        num_rolls = int(match.group(2)) if match.group(2) else 1
        sides = int(match.group(3)) if match.group(3) else 6
        high_drop = int(match.group(5)) if match.group(5) else 0
        low_drop = int(match.group(7)) if match.group(7) else 0
        reroll = int(match.group(9)) if match.group(9) else 0
        sign = match.group(10) if match.group(10) else 1
        number = int(match.group(11)) if match.group(11) else 0

        results = []  # Inicjalizacja pustej tablicy wyników

        for _ in range(series_count):
            roll_results = roll_dice(num_rolls, sides)
            print("Wyniki rzutów:", roll_results)

            roll_results = reroll_dice(roll_results, reroll, sides)
            print("Wyniki po przerzucie:", roll_results)

            roll_results = drop_high_low(roll_results, high_drop, low_drop)
            print("Wyniki po odrzuceniu:", roll_results)
            results.append(roll_results)  # Dodanie wyników rzutów do tablicy wyników
            if sign:
                x = do_operation(sign, roll_results, number)
                print("Wynik po obliczeniach", x)

        for serie in results:
            summ = "suma: " + str(sum(serie))
            serie.append(summ)

        print("Wyniki końcowe:", results)  # Drukowanie ostatecznej tablicy wyników
    else:
        print("Nieprawidłowy wzór.")


if __name__ == "__main__":
    while True:
        roll_pattern = input("Podaj wzór rzutu kością (np. '2d6h1l1r3', enter rzuci kostką d6): \n"
                             "jeśli chcesz zakończyć działanie programu wpisz 'q' \n")

        if roll_pattern.lower() == "q":
            break
        simulate_rolls(roll_pattern)
