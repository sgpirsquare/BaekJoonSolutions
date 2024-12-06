N = int(input())

for _ in range(N):
    sentence = input()
    if sentence[-1] != ".":
        print(sentence + ".")
    else:
        print(sentence)