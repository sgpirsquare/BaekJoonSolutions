while True:
    n = int(input())
    if n == -1:
        break
    div = [i for i in range(1, n) if n % i == 0]
    if sum(div) != n:
        print(f"{n} is NOT perfect.")
    else:
        rearr = []
        rearr += [n] + ["="]
        for i in range(len(div) - 1):
            rearr += [div[i]] + ["+"]
        rearr += [div[-1]]
        print(*rearr)