number1, number2 = input().split()
n1, n2=number1[::-1], number2[::-1]
print(n1 if n1 > n2 else n2)
