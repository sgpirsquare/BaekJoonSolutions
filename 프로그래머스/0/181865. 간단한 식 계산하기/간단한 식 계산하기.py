def solution(binomial):
    calculus = list(binomial.split())
    a = int(calculus[0])
    b = int(calculus[2])
    op = calculus[1]
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b