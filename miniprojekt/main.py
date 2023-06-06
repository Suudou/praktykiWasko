if __name__ == "__main__":
    import re
    import random


    class Dice:
        def __init__(self, sides):
            self.sides = sides

        def roll(self):
            return random.randint(1, self.sides)


    def parse_roll_pattern(pattern):
        match = re.match(r"(\d+)d(\d+)(h(\d+))?(l(\d+))?(r(\d+))?([\+\-\*\/])?(\d+)?", pattern)
        if match:
            num_rolls = int(match.group(1))
            sides = int(match.group(2))
            high_drop = int(match.group(4)) if match.group(4) else 0
            low_drop = int(match.group(6)) if match.group(6) else 0
            reroll = int(match.group(8)) if match.group(8) else 0
            sign = match.group(9) if match.group(9) else None
            number = int(match.group(10)) if match.group(10) else 0
            return num_rolls, sides, high_drop, low_drop, reroll, sign, number
        else:
            return None


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


    def reroll_dice(results, reroll,sides):
        for i in range(len(results)):
            if results[i] == reroll:
                dice_choice = input(f"Przerzucić wynik {results[i]}? (tak/nie): ")
                if dice_choice.lower() == "tak":
                    dice = Dice(sides)
                    results[i] = dice.roll()
        return results


    def drop_high_low(results, high_drop, low_drop):
        if high_drop > 0:
            results = sorted(results, reverse=True)[high_drop:]
        if low_drop > 0:
            results = sorted(results)[low_drop:]
        return results


    def simulate_rolls(pattern):
        parsed_pattern = parse_roll_pattern(pattern)
        if parsed_pattern:
            num_rolls, sides, high_drop, low_drop, reroll, sign, number = parsed_pattern

            results = roll_dice(num_rolls, sides)
            print("Wyniki rzutów:", results)

            results = reroll_dice(results, reroll, sides)
            print("Wyniki po przerzucie:", results)

            results = drop_high_low(results, high_drop, low_drop)
            print("Wyniki po odrzuceniu:", results)

            if sign:
                results = do_operation(sign, results, number)

            print("Suma wyników:", results)
        else:
            print("Nieprawidłowy wzór.")


    roll_pattern = input("Podaj wzór rzutu kością (np. '2d6h1l1r3'): ")
    simulate_rolls(roll_pattern)
