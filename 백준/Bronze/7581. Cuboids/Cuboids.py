while True:
    l, w, h, v = map(int, input().split())
    if l == 0 and w * h * v != 0:
        print(v // (w * h), w, h, v)
    elif w == 0 and l * h * v != 0:
        print(l, v // (l * h), h, v)
    elif h == 0 and l * w * v != 0:
        print(l, w, v // (l * w), v)
    elif v == 0 and l * w * h != 0:
        print(l, w, h, l * w * h)
    elif l == 0 and w == 0 and h == 0 and v == 0:
        break