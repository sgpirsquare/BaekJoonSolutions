while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    isTriangle = a + b > c and b + c > a and c + a > b
    set_Isosceles = {a, b, c}
    if isTriangle is False:
        print("Invalid")
    elif a == b == c and a * b * c != 0:
        print("Equilateral")
    elif len(set_Isosceles) == 2:
        print("Isosceles")
    else:
        print("Scalene")