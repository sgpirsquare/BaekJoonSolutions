n = int(input())
for _ in range(n):
    password_9 = input()
    if len(password_9) >= 6 and len(password_9) <= 9:
        print("yes")
    else:
        print("no")
