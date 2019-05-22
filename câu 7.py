S = open('D:/a.txt', 'r')
lc = 0
for line in S:
    for S in range(0, len(line)):
        if (line[S] == '\n'):
            lc += 1
print("Số dòng trong file là: ", lc)