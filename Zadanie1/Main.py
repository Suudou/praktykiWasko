digits = []
input_list = input("Podaj cyfry oddzielone spacją")
digits = input_list.split()
for digit in digits:
    digit = digit.replace(",",".")
    try:
        digits.append(float(digit))
    except ValueError:
        pass
    if len(digits) == 0:
        return 0
    return avg = sum(digits)/len(digits)
print(avg)




'''
    if digit.isnumeric() : #sprawdza czy jest cyfrą
        digits.append(float(digit))
        digit = input("Podaj cyfrę aby zako`+ńczyć wpisz 'enter'")
        print(digit)
        
    else :                  #ignoruje jeśli nie jest cyfrą
        digit = input("Podaj cyfrę aby zakończyć wpisz 'enter'")
print(digits)

summary = sum(digits)
print(summary)
'''

#avg = summary/len(digits)
#print(avg)
#jesli w stringu znajdzie . albo , to zapisuje go jako float
#i wczesniej zmienic , na . replace
#  digits.append(float(digit))
#try !!!
