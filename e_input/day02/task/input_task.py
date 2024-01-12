# 실습1
# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
message = '이메일: '
id, domain = input(message).split('@')
formatting = f'아이디: {id}\n도메인: {domain}'

print(formatting)


'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm

    round(값, 원하는 자리수)
'''

message = '야드 값과 인치 값을 입력하세요'
ex_message = '10 10'

num1, num2 = map(float, input(message + '\n' + ex_message + '\n').split(' '))
result =  str(num1 * 91.44) + '\n' + str(num2 * 2.54)

print(result)


#실습2 정리
yard_message = 'yard 입력: '
inch_message = 'inch 입력: '
yard = float(input(yard_message))
inch = float(input(inch_message))

yard_to_cm = round(yard * 91.44, 2)
inch_to_cm = round(inch * 2.54, 2)

yard_formatting = f'{yard} yard는 {yard_to_cm}cm'
inch_formatting = f'{inch} inch는 {inch_to_cm}cm'

print(yard_formatting, inch_formatting, sep='\n')
