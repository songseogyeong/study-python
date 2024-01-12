number = 15
# % 모듈러스(mod)
if number % 3 == 0:
    print(f'{number}는 3의 배수입니다')
if number % 5 == 0:
    print(f'{number}는 5의 배수입니다')

# number가 양수인지, 음수인지, 0인지 검사
number = 1

if number == 0:
    print(f'{number}는 0입니다.')
if number == number > 0:
    print(f'{number}는 양수입니다.')
if number == number < 0:
    print(f'{number}는 음수입니다.')


# 정리
number = 1

positive_condition = number > 0
negative_condition = number < 0
zero_condition = number == 0

if positive_condition:
    print(f'{number}는 양수입니다.')
elif negative_condition:
    print(f'{number}는 음수입니다.')
else:
    print(f'{number}는 음수입니다.')

# 실습
# 나이를 입력받은 후 미성년자인지 검사
message = '나이를 입력하세요: '
age = int(input(message))

adult_condition = age > 19

if adult_condition:
    print('성인입니다.')
else:
    print('미성년자입니다.')

#
message = '나이를 입력하세요: '
age = int(input(message))
condition = 0 < age < 20

if condition:
    print('미성년자입니다.')

#
message = '나이를 입력하세요: '
age = int(input(message))
condition = 0 < age < 20
error_condition = age <= 0

if condition:
    print('미성년자입니다.')
elif error_condition:
    print('잘못 입력하셨습니다')
else:
    print('성인입니다.')


# 실습
# 두 정수를 입력받은 후 대소비교 진행
message = '두 정수를 입력하세요: '
ex_massage = 'ex)3, 5'
num1, num2 =  map(int, input(message + '\n' + ex_massage + '\n').split(', '))

condition1 = num1 > num2
condition2 = num1 < num2

if condition1:
    print(f'{num1}이 더 크다.')
elif condition2:
    print(f'{num2}이 더 크다.')
else:
    print(f'{num1}과 {num2}는 같다.')


# 실습 정리
message = '두 정수를 입력하세요: '
ex_massage = 'ex)3, 5'
num1, num2 =  map(int, input(message + '\n' + ex_massage + '\n').split(', '))

if num1 > num2:
    print(f'{num1}이 더 크다.')
elif num1 != num2:
    print(f'{num2}이 더 크다.')
else:
    print(f'{num1}과 {num2}는 같다.')


# print 정리하기
message = '두 정수를 입력하세요: '
ex_massage = 'ex)3, 5'
num1, num2 =  map(int, input(message + '\n' + ex_massage + '\n').split(', '))
# 선언할 때 넣을 값을 모를 경우 초기값을 넣어준다.
# 정수: 0
# 실수: 0.0
# 문자열: '' 또는 ""
# 불린: False


result_message = ''
# 어떤 값이 들어갈지 모르기 때문에 '' <초기값을 넣어준다 = 초기화


# 일괄처리란
# 각 분기별로 결과를 처리하지 않고
# 모든 분기 종료 후 한번에 처리하는 것을 의미한다.

if num1 > num2:
    result_message = f'{num1}이 더 크다.'
elif num1 != num2:
    result_message = f'{num2}이 더 크다.'
else:
    result_message = f'{num1}과 {num2}는 같다.'

print(result_message)