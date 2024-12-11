pledge = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]
N = int(input())
answer = 0
for _ in range(N):
    text = input()
    if text in pledge:
        answer += 1

if answer == N:
    print("No")
else:
    print("Yes")