scales = list(map(int, input().split()))

ascending = [i for i in range(1, 9)]
descending = [i for i in range(8, 0, -1)]

if scales == ascending:
    print("ascending")
elif scales == descending:
    print("descending")
else:
    print("mixed")