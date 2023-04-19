if __name__ == "__main__":
    with open('file1.txt', 'r+') as f1, open('file2.txt', 'r+') as f2, open('file3.txt', 'r+') as f3:
        for line1 in f1:
            line2 = f2.readline()
            num1 = [int(x) for x in line1.split()]
            num2 = [int(x) for x in line2.split()]
            result = [str(x + y) for x, y in zip(num1, num2)]
            f3.write(' '.join(result)+'\n')
            # [f3.write(x + "\n") for x in result]








