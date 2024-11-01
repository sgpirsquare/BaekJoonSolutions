a = int(input())
b = int(input())
c = int(input())
dishs = {a, b, c}
for dish in dishs:
    if max(dishs) > dish > min(dishs):
        print(dish)