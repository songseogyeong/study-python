for i in range(1, 11, 1):
    print(f'{i + 1}. 한동석')

for i in range(1, 11):
    print(f'{i}. 한동석')

for i in range(10, 0, -1):
    print(f'{i}. 한동석')

# 실습
# 1~10까지 출력해보기
for i in range(10):
   print(f'{i + 1}')

for i in range(10):
    print(f'{10-i}. 한동석')

# 실습
# 1~10까지 중 3까지만 출력
for i in range(10):
    print(i + 1)
    if i == 2:
        break
# break 아래에 print 쓰면 2까지 반복하고 탈출해서 3이 안 나옴!

# 1~10까지 중 4를 제외하고 출력
for i in range(10):
    if i == 3:
        continue
    print(i + 1)
# continue 코드가 특정 조건일 때 실행X
# print는 컨티뉴 아래에다 작성
# 10번 반복하는데 4번째가 컨티뉴로 빠진것~
