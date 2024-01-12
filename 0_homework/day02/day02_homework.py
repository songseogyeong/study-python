# # if문
# # 점수를 입력 받은 뒤, 학점을 출력하기
message = '점수를 입력하세요: '
score = int(input(message))

a = 100 >= score >= 90
b = score >= 80
c = score >= 70
d = score >= 60
f = 60 > score >= 0

result = ''

if a:
    result = f'{score}점은 A학점입니다.'
elif b:
    result = f'{score}점은 B학점입니다.'
elif c:
    result = f'{score}점은 C학점입니다.'
elif d:
    result = f'{score}점은 D학점입니다.'
elif f:
    result = f'{score}점은 F학점입니다.'
else:
    result = '잘못 입력하셨습니다.'

print(result)



# for문
# 입력 받은 숫자를 n번 반복해서 한 줄로 보여주기
message1 = '숫자를 입력하세요: '
message2 = '반복 횟수를 입력하세요: '
number1 = int(input(message1))
number2 = int(input(message2))

for i in range(number2):
    print(number1, end=' ')

print('\n')


# while문
# 사용자에게 문구와 반복 횟수를 입력받아 한 줄로 출력하기
message1 = '정수 입력: '
message2 = '반복할 문구 입력: '
number = int(input(message1))
input_message = input(message2)

count = 0
while count != number:
    print(input_message, end=' ')
    count += 1


# while

