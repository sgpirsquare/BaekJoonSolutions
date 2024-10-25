money = int(input())
shopping = int(input())
sum = 0
for i in range(shopping):
    mon, shop = map(int, input().split())
    sum += mon * shop
if money == sum:
    print("Yes")
else:
    print("No")