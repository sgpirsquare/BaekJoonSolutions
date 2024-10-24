n=int(input())
a=list(map(int,input().split()))

max=min= a[0]
for i in range(1,n):
    if a[i] > max:
        max=a[i]
for i in range(1,n):
    if a[i]< min:
        min=a[i]
print(min,max)