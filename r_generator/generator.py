# 메모리 확인
import os
import psutil

# 프로그램은 미실행> 프로그램을 실행하면 프로세스(실행중인 프로그램을 프로세스라고 함)
# os.getpid() 내 컴의 고유 메모리를 가져오기
process_object = psutil.Process(os.getpid())
# 1024 = 1 바이트 나눈 거
memory_before = process_object.memory_info().rss / 1024 / 1024

data_list = [i ** 2 for i in range(10000)]
print(data_list)

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')
# 메모리 사용량을 봐도 데이터를 하나씩 가져오게 하는게 효율적이다
# ----------------------------------------------------------------------------------------------------------------------

memory_before = process_object.memory_info().rss / 1024 / 1024

data_generator = (i ** 2 for i in range(10000))
print(next(data_generator))

memory_after = process_object.memory_info().rss / 1024 / 1024
print(f'memory: {memory_before} -> {memory_after}')

# ----------------------------------------------------------------------------------------------------------------------

#
def increase(number: int = 0):
    while True:
        number += 1
        yield number
        # yield는 리턴의 기능을 가지고 있음
        # 이 기능은 next를 가지고 가져올 수 있음
        # yield 를 썼다는 건 increase 객체가 제너레이터라는 뜻

# 서버를 만들 때 요청에 대한 걸 제너레이터로 생성함
result = increase()
while True:
    data = input("Y/n >> ")
    if data == "Y":
        print(next(result))
    else:
        break