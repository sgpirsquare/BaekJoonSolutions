n, m = map(int, input().split())
mat_1 = []
mat_2 = []
for i in range(n):
    mat_1.append(list(map(int, input().split())))
for i in range(n):
    mat_2.append(list(map(int, input().split())))
for i in range(n):
    add_mat = []
    for j in range(m):
        add_mat.append(mat_1[i][j] + mat_2[i][j])
    print(*add_mat)
