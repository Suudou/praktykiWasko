import os
input_folder = "/Users/l.sudol/PycharmProjects/lsudol/Zadanie3/files"
output_folder = "/Users/l.sudol/PycharmProjects/lsudol/Zadanie3/res"
dir_list = os.listdir(input_folder)
print(dir_list[0])
paf = os.path.join(input_folder, dir_list[0])
#print(paf)
'''with open(os.path.join(input_folder, dir_list[0]),'r') as temp1:
    cont = temp1.read()
with open("/Users/l.sudol/PycharmProjects/lsudol/Zadanie3/res/temp_res", 'w') as temp2:
    temp2.write(cont)'''

for element in dir_list[1:]:
    file1 = os.path.join(input_folder, dir_list[0])
    file_path = os.path.join(input_folder, element)
    print(file_path)
    with open(file1, 'r+') as f1,\
            open(file_path, 'r+') as f2, \
            open(os.path.join(output_folder, "results.txt"), 'w') as f3:
            print(f1.read())
            if len(f1.readlines()) >= len(f2.readlines()):
                f1.seek(0)
                f2.seek(0)
                for line1 in f1:
                    line2 = f2.readline()
                    num1 = [int(x) for x in line1.split()]
                    num2 = [int(x) for x in line2.split()]
                    if len(num1) > len(num2):
                        diff = len(num1) - len(num2)
                        for i in range(diff):
                            num2.append(0)
                    else:
                        diff = len(num2) - len(num1)
                        for i in range(diff):
                            num1.append(0)
                    # print(num1, num2)
                    # print(list(zip(num1, num2)))
                    result = [str(x + y) for x, y in zip(num1, num2)]
                    f1.write(' '.join(result) + '\n')
            else:
                f1.seek(0)
                f2.seek(0)
                for line2 in f2:
                    line1 = f1.readline()
                    num1 = [int(x) for x in line1.split()]
                    num2 = [int(x) for x in line2.split()]
                    if len(num1) > len(num2):
                        diff = len(num1) - len(num2)
                        for i in range(diff):
                            num2.append(0)
                    else:
                        diff = len(num2) - len(num1)
                        for i in range(diff):
                            num1.append(0)
                    result = [str(x + y) for x, y in zip(num1, num2)]
                    f1.write(' '.join(result) + '\n')

