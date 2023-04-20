if __name__ == "__main__":
    with open('file1.txt', 'r+') as f1, open('file2.txt', 'r+') as f2, open('file3.txt', 'r+') as f3:
        if len(f1.readlines()) >= len(f2.readlines()):
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
                print("nic")
