answer_number=0

while True:
    try:
        sentence=input()
        answer_number+=1
    except EOFError:
        break
        
print(answer_number)