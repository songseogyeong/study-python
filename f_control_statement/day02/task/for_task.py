# 실습1
# 1~15까지 출력
for i in range(15):
    print(i + 1)


# 실습2
# 30~1까지 출력
for i in range(30):
    print(30 - i)


# 실습3
# 1~100까지 중 홀수만 출력
for i in range(1, 100, 2):
    print(i)

for i in range(50):
    print(i * 2 + 1)

# for i in range(100):
    count = i + 1
    if count % 2 != 0:
        print(count)


# 실습4
# 1~10까지 합 출력
total = 0

for i in range(10):
    i = i + 1
    total = total + i

print(total)


# 실습4 정리
total = 0
for i in range(10):
    total += i + 1

print(total)


# 실습5
# 1~n까지 합 출력
message1 = '정수를 입력하세요: '
num =  int(input(message))
sum = 0

for i in range(num):
    i = i + 1
    sum = sum + i

print(sum)

# 실습5 정리
message1 = '1~n까지의 합'
message2 = 'n: '
end = int(input(message1 + '\n' + message2))

total = 0
for i in range(end):
    total += i + 1

print(total)



# 3 4 5 6 3 4 5 6 3 4 5 6 출력
for i in range(12):
    print(i % 4 + 3, end=' ')
# i % 4
# 0 % 4 = 0 + 3 = 3
# 1 % 4 = 1 + 3 = 4
# 2 % 4 = 2 + 3 = 5
# 3 % 4 = 3 + 3 = 6
# 4 % 4 = 0 + 3 = 3
# .... 반복

# '1,235,500' 를 1235500으로 출력
data = '15,235,500'
# 문자열이기 때문에 순서가 있음
result = ""
for i in data:
    if i != ',':
        result += i

result = int(result)
print(result)

