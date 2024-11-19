import sys

lines = []
for i in range(8):
    lines += [list(sys.stdin.readline())]

count = 0

for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        if lines[i][j] == "F":
            count += 1

for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        if lines[i][j] == "F":
            count += 1


print(count)
