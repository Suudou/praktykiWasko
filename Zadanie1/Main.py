digits = []
digit = input("Podaj cyfrę aby zakończyć wpisz 'k'")
print(digits)

while digit!="k":
    if digit.isnumeric() :
        digits.append(digit)
        digit = input("Podaj cyfrę aby zakończyć wpisz 'k'")
        print(digit)


print(digits)
