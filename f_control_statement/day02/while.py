# 이름 10번 츨략
count = 0
while count != 10:
    print('한동석')
    count += 1

print(count)
# 위는 비효율적! 반복횟수를 알면 while문 보다 for문이 좋음

# 실습
# 사용자가 입력한 정수가 몇 자리수인지 출력
# 1. 사용자에게 정수를 입력 받는다.
# 2. 입력받은 정수의 각 자릿수를 센다.
# 3. 자리수를 출력한다.
# 힌트: 몫과 나머지

# message1 = '입력한 정수가 몇 자리수인지 출력\n'
# message2 = '정수: '
# num = int(input(message1 + message2))
#
# result = ''
#     while num != 0:
#         print(str(num))


# 실습 정리
message = '정수 입력: '
number = int(input(message))
count = 0

while number != 0:
    number = number // 10
    count += 1

print(count)
# 넘버가 0과 같지 않으면 반복
# 넘버를 10으로 몫을 나누ㅓ
# 한번 나누면 카운트가 올라감
# 0 같으면 탈출되는데 탈출되기 전까지 반복(카운트 횟수 올라감)

# if, while, for 문 문제 만들기 숙제

message = '정수 입력: '
number = int(input(message))
count = None

while number != 0:
    number = number // 10
    count += 1

print(count)