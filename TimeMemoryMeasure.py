import time

# 외부 모듈 psutil 설치해야 함
import psutil
import os

# 시작 시간과 메모리 사용량 측정
start_time = time.time()
process = psutil.Process(os.getpid())  # 현재 프로세스 정보 가져오기
start_memory = process.memory_info().rss  # 시작 메모리 (bytes)

# 예제 코드: 측정하고자 하는 코드 블록
# 아래 부분에 실행하고자 하는 코드를 넣으세요
arr = list(range(10**6, 0, -1))
arr.sort()

# 종료 시간과 메모리 사용량 측정
end_time = time.time()
end_memory = process.memory_info().rss  # 종료 시 메모리 (bytes)

# 실행 시간과 사용 메모리 계산
elapsed_time = (end_time - start_time) * 1000  # ms 단위로 변환
used_memory = (end_memory - start_memory) / 1024  # KB 단위로 변환

print(f"실행 시간: {elapsed_time:.2f} ms")
print(f"사용 메모리: {used_memory:.2f} KB")
