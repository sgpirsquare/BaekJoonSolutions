univ_w = []
univ_k = []
for _ in range(10):
    univ_w.append(int(input()))
for _ in range(10):
    univ_k.append(int(input()))
print(sum(sorted(univ_w)[-3:]), sum(sorted(univ_k)[-3:]))