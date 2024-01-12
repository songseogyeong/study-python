# input은 통으로 문자열임
name = input("이름: ")

# 문자열끼리만 연결(+)가 가능하다
# 2 + 1 = 3 으로 +가 연산
# '안' + '녕' = 안녕 으로 +가 연결
data = 3
print('안' + str(data))

# # 실습
name = input("이름: ")
formatting = f'{name}님 환영합니다'

print(formatting)


# 실습 1
# 제 이름은 ???, 키는 ???cm 입니다.
name = input("이름: ")
height = input("키: ")
formatting = f'제 이름은 {name}, 키는 {height}cm 입니다.'

print(formatting)


# 실습2
# 두 정수를 입력받은 후 곱셈 결과 출력
number1 = input('첫번째 숫자 입력: ')
number2 = input('두번째 숫자 입력: ')
formatting = int(number1) * int(number2)

print(formatting)


# 실습 2 정리1
number1, number2 = map(int,input('두 정수를 입력하세요\nex)1, 3\n').split(','))
print(number1 * number2)
# map을 쓰는 이유? 바꾸기 위해 사용
# map에 첫번째로 전달되는 곳에는 반드시 함수가 들어감
# 각각의 원소(뒤에 있는 거!)를 앞에 있는 함수로 적용시킴 = 형변환


# 실습 2 정리2
message1 = '첫 번째 정수'
message2 = '두 번째 정수'

number1 = int(input(message1))
number2 = int(input(message2))
result = number1 * number2

formatting = f'{number1} * {number2} = {result}'

print(formatting)


# split
print('A, B, C'.split(','))


# 변수와 리스트의 개수를 맞춰야함
number1, number2 = input('두 정수: ').split(',')

print(number1, number2)


# map
# map(각각 어떻게 바꿀 것인가, [내용])
message = '두 정수를 입력하세요'
example_message = '예) 1, 3'
number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
result = number1 * number2
formatting = f'{number1} * {number2} = {result}'

print(formatting)


# 실습1
# 현재 시간을 입력하고 시와 분으로 분리하여 출력
message = '현재 시간을 입력하세요\n'
example_message = '예) 13:00\n'

num1, num2 = map(int, input(message + example_message).split(':'))
result_message1 = f'현재 시간은 {num1}시'
result_message2 = f'현재 시간은 {num2}분'
formatting = result_message1 + '\n' + result_message2

print(formatting)


# 실습1 정리
message = '현재 시간'
time = input(message)
hours, minuts = time.split(':')
formatting = f'{hours}시 {minutes}분'

print(formatting)


# 실습2
# 핸드폰 번호를 -(하이픈)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
massage = '전화번호를 입력하세요\n'
example_message = '010-0000-0000\n'

num1, num2, num3 = map(int, input(massage + example_message).split('-'))
result_message1 = f'첫 번째 전화번호는 {num1}'
result_message2 = f'두 번째 전화번호는 {num2}'
result_message3 = f'세 번째 전화번호는 {num3}'
formatting = result_message1 + '\n' + result_message2 + '\n' + result_message3

print(formatting)


# 실습2 정리
massage = '핸드폰 번호: '
num1, num2, num3 = input(message).split('-')
formatting = f'통신사: {num1}\n앞번호: {num2}\n뒷번호: {num3}\n]}'

print(formatting)


# 실습3
# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
massage = '이름과 나이를 입력해 주세요\n'
example_message = '홍길동, 20\n'

num1, num2 = map(int, input(massage + example_message).split(', '))
num3 = str(num1)
formatting = f'{num3}님의 나이는 {num2}살'

print(formatting)


# 실습3 정리
massage = '이름과 나이를 입력하세요'
example_message = '예) 홍길동 20'

name, age = input(massage + \n + example_message + \n).split(' ')
formatting = f'{name}님의 나이는 {age}살'

print(formatting)


# 실습4
# 3개의 정수를 입력 받은 뒤 덧셈 결과 출력
message = '3개의 정수를 입력하세요\n'
example_message = '예) 1, 3, 5\n'
num1, num2, num3 = map(int, input(message + example_message).split(', '))
result= (num1 + num2) + num3
formatting = f'{num1} +  {num2} + {num3} = {result}'

print(formatting)


# 실습4
message = '3개의 정수를 입력해 주세요.'
example_message = '예)1/2/3'

num1, num2, num3 = map(int, input(message + '\n' + example_message + '\n').split())
result = num1 + num2 + num3

formatting = f'{num1} +  {num2} + {num3} = {result}'
print(formatting)
