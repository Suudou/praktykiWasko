import os
if __name__ == "__main__":
    input_folder = "/Users/l.sudol/PycharmProjects/lsudol/Zadanie3/files"
    output_folder = "/Users/l.sudol/PycharmProjects/lsudol/Zadanie3/files2"
    # create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r+') as f1, \
                    open(os.path.join(input_folder, 'a.txt'), 'r+') as f2, \
                    open(os.path.join(output_folder, filename), 'w') as f3:
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
                        f3.write(' '.join(result) + '\n')
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
                        f3.write(' '.join(result) + '\n')

