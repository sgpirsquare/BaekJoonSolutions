N = int(input())

dice_sum = []

for _ in range(N):
    dice1, dice2, dice3, dice4 = map(int, input().split())
    dices_list = sorted([dice1, dice2, dice3, dice4])
    dices_set = set(dices_list)

    if len(dices_set) == 1:
        dice_sum.append(50000 + dice1 * 5000)

    elif len(dices_set) == 4:
        dice_sum.append(max(dices_set) * 100)

    elif len(dices_set) == 2 and dices_list[1] != dices_list[2]:
        dice_sum.append((dices_list[0] + dices_list[3]) * 500 + 2000)

    elif len(dices_set) == 2 and dices_list[0] != dices_list[1]:
        dice_sum.append(dices_list[3] * 1000 + 10000)

    elif len(dices_set) == 2 and dices_list[2] != dices_list[3]:
        dice_sum.append(dices_list[0] * 1000 + 10000)

    elif len(dices_set) == 3 and dices_list[0] == dices_list[1]:
        dice_sum.append(dices_list[0] * 100 + 1000)

    elif len(dices_set) == 3 and dices_list[1] == dices_list[2]:
        dice_sum.append(dices_list[1] * 100 + 1000)

    elif len(dices_set) == 3 and dices_list[2] == dices_list[3]:
        dice_sum.append(dices_list[2] * 100 + 1000)


print(max(dice_sum))