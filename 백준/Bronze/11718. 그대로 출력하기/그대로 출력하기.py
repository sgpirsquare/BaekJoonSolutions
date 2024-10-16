import sys
# 이게 된다고?? 너무 구석진 거 아닌가..음...
# sys.stdin. 까지는 파일객체랑 같은 역할을 한다. EOF(End of File)
user_input = sys.stdin.read()
print(f"{user_input}")

'''
# 요런 풀이도 있고 와..한줄에 끝내다니
print(open(0).read())

# 아래 풀이도 꽤 보인다.
while True:
  try:
    a = input()
    print(a)
  except:
    break    
'''
