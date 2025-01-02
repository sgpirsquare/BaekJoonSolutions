sentence = input()
sen_length = len(sentence)
for i in range((sen_length - 1) // 10 + 1):
    print(sentence[i * 10 : (i + 1) * 10])