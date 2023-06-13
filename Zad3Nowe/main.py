import os

input_folder = "C:/Users/l.sudol/PycharmProjects/lsudol/Zad3Nowe/files"
output_folder = "D:/PROGRAMY/pythonprogramy/3/res"
dir_list = os.listdir(input_folder)
lines_list = []

res_list = []

for filename in dir_list:
    file_path = os.path.join(input_folder, filename)
    lines = []
    lines_list.append(lines)
    with open(file_path, 'r+') as f:
        for line in f:
            number = [int(x) for x in line.split()]
            lines.append(number)

#Tworzę tablicę z 0 wielkości najdłuższego pliku

longest_file = len(max(lines_list, key=len))
zero_list = [[] for _ in range(longest_file)]
print(zero_list)

'''for line in longest_file:
    zero_list.append([])
    for number in line:
        zero_list[-1].append(0)'''
print(lines_list)
temp_list = []
for file in lines_list:
    print(file, "plik")
    print(zero_list, "lista startowa")
    print(list(zip(zero_list, file, )), "zipy linijek ........................")
    for line1, line2 in zip(zero_list, file):
        print(list(zip(line1, line2)), "zipy liczb w linijkach")
        result = [x + y for x, y in zip(line1, line2)]
        print(result, "dodanie każdej z cyfr")
        temp_list.append(result)
        zero_list = temp_list
        print(zero_list, "wynikowa lista")



'''for inner_list in lines_list:
    for i in range(len(inner_list)):
        for j in range(len(inner_list[i])):
            if j >= len(res_list):
                res_list.append([inner_list[i][j]])
                print(inner_list[i][j])
            else:
                res_list[j].append(inner_list[i][j])'''
#for inner_list in lines_list:
#res_list = [list(elements) for elements in zip(*inner_list)]

print(res_list)







