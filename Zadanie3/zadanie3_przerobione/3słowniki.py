import os
#__file__
input_folder = "/Users/l.sudol/PycharmProjects/lsudol/Zadanie3/files"
output_folder = "/Users/l.sudol/PycharmProjects/lsudol/Zadanie3/res/results.txt"

dir_list = os.listdir(input_folder)
lines_list = []
lines_dic = {}
numbers = {}

for filename in dir_list:
    file_path = os.path.join(input_folder, filename)
    lines = []
    lines_list.append(lines)
    with open(file_path, 'r+') as file:

        for i, line in enumerate(file):
            if i not in lines_dic.keys():
                lines_dic[i] = {}
            for j, num in enumerate(line.split()):
                if j not in lines_dic[i].keys():
                    lines_dic[i][j] = 0
                lines_dic[i][j] += float(num)

with open(output_folder, 'w') as file:
    for line in sorted(lines_dic.keys()):
        file.write(" ".join([str(lines_dic[line][column]) for column in sorted(lines_dic[line].keys())]) + '\n')






