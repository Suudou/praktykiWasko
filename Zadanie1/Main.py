if __name__ == "__main__":
    end_list = []
    #lista ostateczna, z przekonwertowanymi wartosciami
    input_list = input("Podaj cyfry oddzielone spacją")
    digits = input_list.split() #dziele liste spacjami i zapisuje ja w nowej liscie
    for digit in digits:
        digit = digit.replace(",", ".") #zamieniam przecinki na kropki, żeby złapał float
        try: #próbuje zmienic na float, jesli sie nie udaje czyli jest litera lub inny znak to ignoruje
            end_list.append(float(digit))
        except ValueError:
            pass
        if len(digits) == 0: #wyjatek 0/0
            avg = 0
            print(avg)
    avg = sum(end_list)/len(end_list)
    print(avg)
