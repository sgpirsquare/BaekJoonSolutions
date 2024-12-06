def even_odd(a):
    if int(a % 2 == 0):
        return print("even")
    else:
        return print("odd")


N = int(input())
for _ in range(N):
    integer = int(input())
    even_odd(integer)
