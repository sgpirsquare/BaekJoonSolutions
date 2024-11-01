while True:
    n = input()
    reverse_n = []

    if int(n) == 0:
        break
    elif n == n[::-1]:
        print("yes")
        # if n[i] != n[-i - 1]:
    else:
        print("no")
