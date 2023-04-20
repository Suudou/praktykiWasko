if __name__ == "__main__":
    end_list = []
    # lista ostateczna, z przekonwertowanymi wartosciami
    input_list = input("Podaj cyfry oddzielone spacją")
    if not input_list:
        print("Avg = 0")
        exit()
    # dziele liste spacjami i zapisuje ja w nowej liscie
    digits = input_list.split()
    for digit in digits:
        # zamieniam przecinki na kropki, żeby złapał float
        digit = digit.replace(",", ".")
        # próbuje zmienic na float, jesli sie nie udaje czyli jest litera lub inny znak to ignoruje
        try:
            end_list.append(float(digit))
        except ValueError:
            pass
        # wyjatek 0/0
        if len(digits) == 0:
            avg = 0
            print(avg)
    avg = sum(end_list)/len(end_list)
    print(avg)
