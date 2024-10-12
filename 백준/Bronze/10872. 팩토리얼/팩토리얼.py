n=input()
n=int(n)
a=1

if n == 0:
    print(a)
else:
    for i in range(n):
        a = a*(i+1)
    print(a)