import string
if __name__ == "__main__":

    def convert(lst):
        keys = lst
        dictionar = {key: 0 for key in keys}
        return dictionar


    sentence = input("podaj ciąg znaków \n ")
    x = string.ascii_lowercase
    dic = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    dictionary = convert(dic)
    for element in sentence:
        if element in dictionary:
            dictionary[element] += 1
    for key, value in dictionary.items():
        print(key, "-", value, " \n ")


