a = int(input())
b = int(input())
c = int(input())
list_abc = list(str(a * b * c))
for i in range(10):
    suma = 0
    for j in range(len(list_abc)):
        if i == int(list_abc[j]):
            suma += 1
    print(suma)