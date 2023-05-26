import re
import random

print("Wpisz wzór AdXdhYdlZrC")
text = input("pisz:\n")
pattern = r"(.)d(.)dh(.)dl(.)r(.)"
# AdXdhYdhZrC

match = re.match(pattern, text)
if match:
    a = match.group(1)
    X = match.group(2)
    Y = match.group(3)
    Z = match.group(4)
    C = match.group(5)

    print("A:", A)
    print("X:", X)
    print("Y:", Y)
    print("Z:", Z)
    print("C:", C)
else:
    print("nie znaleziono wzoru")
def roll_dice(dice):
    return random.randint(1, dice)

dice = int(input("Podaj ilość ścian kostki: "))

while dice <= 0:
    print("Ilość ścian musi być większa od zera.")
result = roll_dice(dice)
print("Wyrzucono:", result)