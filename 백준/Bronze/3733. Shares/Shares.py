import sys

lines = sys.stdin.readlines()

for line in lines:
    n, s = map(int, line.strip().split())
    print(s // (n + 1))