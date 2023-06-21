import json
import requests
import tkinter as tk
# 1 funkcja zwraca liste nazw miast
# 2 funkcja zwraca dane do miasta -> https://danepubliczne.imgw.pl/api/data/synop/station/jeleniagora ma zmieniać
# link dla odpowiedniego miasta
# drugi plik zrobić klase która ma pola i wartosci do pól, __str__
# trzeci plik zrobić 2 mainy jeden na intera drugi na web
# commity!
url = "https://danepubliczne.imgw.pl/api/data/synop"
response = requests.get(url)
data = json.loads(response.text)
#choice = input("wpisz nazwę miasta\n")
#formatted_in = choice.lower().capitalize()
'''
for city in data:
    if city['stacja'] == formatted_in:
        for key, value in city.items():
            print(key, ":", value)'''
cities = []
for dictionary in data:
    city = dictionary.get('stacja')
    cities.append(city)
#print(cities)


def pop():
    weather_info = tk.Label(root,text="Brawo").pack()


root = tk.Tk()
root.geometry("400x200")
clicked = tk.StringVar()

drop = tk.OptionMenu(root, clicked, *cities)
drop.pack()


for city in data:
    if city['stacja'] == clicked:
        for key, value in city.items():
            print(key, ":", value)

my_button = tk.Button(root, text="Wyświetl pogodę",command=pop).pack()


root.mainloop()