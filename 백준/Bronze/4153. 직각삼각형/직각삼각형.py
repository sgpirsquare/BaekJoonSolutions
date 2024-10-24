while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break

    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("right")
    else:
        print("wrong")
