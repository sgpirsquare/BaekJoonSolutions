word_text = list(input())
alphabets_number = [[-1] for _ in range(97, 123)]
for i in range(97, 123):
    for j in range(len(word_text)):
        if chr(i) == word_text[j]:
            alphabets_number[i - 97] += [j]
result_number = [0 for _ in range(97, 123)]

for i in range(len(alphabets_number)):
    if len(alphabets_number[i]) == 1:
        result_number[i] = -1
    else:
        result_number[i] = alphabets_number[i][1]

print(*result_number)
