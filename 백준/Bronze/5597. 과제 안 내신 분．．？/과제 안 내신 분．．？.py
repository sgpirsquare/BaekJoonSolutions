set_1 = [x for x in range(1, 31)]
set_2 = []
for i in range(28):
    set_2.append(int(input()))
diff = sorted(list(set(set_1) - set(set_2)))

print(diff[0])
print(diff[1])