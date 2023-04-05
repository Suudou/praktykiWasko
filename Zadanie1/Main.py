digits = []
end_list = [] #lista ostateczna, z przekonwertowanymi wartosciami
input_list = input("Podaj cyfry oddzielone spacją")
digits = input_list.split() #dziele liste spacjami i zapisuje ja w nowej liscie
for digit in digits:
    digit = digit.replace(",",".") #zamieniam przecinki na kropki, żeby złapał float
    try: #próbuje zmienic na float, jesli sie nie udaje czyli jest litera lub inny znak to ignoruje
        end_list.append(float(digit))
    except ValueError:
        pass
    if len(digits) == 0: #wyjatek 0/0
        avg = 0
        print(avg)
avg = sum(end_list)/len(end_list)
print(avg)


''' moje notatki
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
