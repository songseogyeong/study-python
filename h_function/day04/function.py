f(x) = 2x+1
def f(x):
    return 2 * x + 1

result = f(2)
print(result)

# 실습1
# 두 정수의 곱셈 함수
message = '두 정수를 입력하세요\n예시) 3, 7\n'
num1, num2 = (map(int, input(message).split(', ')))

def number():
    return num1 * num2

result = number()
print(result)


실습1 정리
def multiple(number1, number2):
    return number1 * number2


# 실습2
# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
message = '두 정수를 입력하세요\n예시)3, 7\n'
num1, num2 = map(int, input(message).split(', '))

# def number1():
#     number_result = num1 // num2
    return number_result

def number2():
    number_result = num1 % num2
    return number_result

result1 = number1()
result2 = number2()
formatting = f'몫: {result1}\n나머지: {result2}'

print(formatting)


# def number():
#     number_result = num1 / num2
#     return number_result
#
# result1 = number()
# print(result)

# 실습2 정리
# 여러개의 값을 받아올 때 튜플을 사용 함
def divide(number1, number2):
    if number2 != 0:
        return number1 // number2, number1 % number2
    return None


result = divide(10, 0)
if result:
    value, rest = result
    print(f'몫: {value}, 나머지: {rest}')
else:
    print('0으로 나눌 수 없습니다.')


# 실습3
# 1~10까지 print()로 출력하는 함수
def number():
    for i in range(10):
        print(i + 1)

number()

# 실습3 정리
def print_from1_to10():
    for i in range(10):
        print(i + 1, end=' ')

print_from1_to10()


# 실습4
# 이름을 n번 print()로 출력하는 함수
name_message = '이름을 입력하세요: '
name = input(name_message)
count_message = '반복 횟수를 입력하세요: '
count = int(input(count_message))
sum = 0

def count_name():
    for name in range(count):
    name = name + 1
    sum = sum + i

count_name()


# 실습4 정리
def print_name(name, count):
    for i in range(count):
        print(name)

print_name('송', 5)

# 실습5
# 1~n까지의 합을 구해주는 함수
def get_total_from1(end):
    total = 0
    for i in range(end):
        total += i + 1
    # 0 + 1 1
    # 1 + 1 2
    # 2 + 1 3
    # 6

    return total
    # 리턴을 사용하는 이유
    # 콘솔창에 표기가 되어야 하면 return을 작성하지 않고 print로 출력함
    # 콘솔창 표기가 필요하지 않으면 return을 작성
    # print하면 다른 곳에 사용이 불가, reuturn 시 값을 다른곳에 활용 가능

print(get_total_from1(3))


def get_total_form1(end):
    total = 0
    for i in range(end):
        total += i + 1

    print(total)

get_total_form1(5)

# 실습 6
# 1~100까지 중 n의 배수를 print()로 출력하는 함수
# 함수 선언(매개변수):
def print_time_from1_to100(time):
    # 100번을 반복한 값을 i에 담을 거임
    for i in range(100):
        # 만약 time이
        if (i + 1) % time == 0:
            print(i + 1)

print_time_from1_to100(3)


# 세 정수의 뺄셈 함수
def sub(number1, number2, number3):
    return number1 - number2 - number3

# 문자열을 입력 받고 원하는 문자의 개수를 구해주는 함수
def get_count_of_result(target, keyword):
    # return len([i for i in target if i == keyword])
    count = 0
    for i in target:
        if i == keyword:
            count += 1
        return count

'''
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는지 검사하고,
    만약 해당문자가 없으면 -1을 리턴하는 함수
'''
# 1
def find(target, keyword):
    for i in range(len(target)):
        if target[i] == keyword:
            return i
            break

    return -1

# 2
def find(target, keyword):
    result = -1
    for i in range(len(target)):
        if target[i] == keyword:
            result = ibreak

    return result

# 3
# 비효율적인 코드
    result = 0
    for i in range(len(target)):
        if target[i] == keyword:
            result = i
            break
        else:
            result = -1

    return result


data = 10
data = 20

# 위 값과 아래 값은 동일함~

def test():
    print(10)

def test():
    print(20)

test()
# 저장공간에 값이 입력되는 거라 tset에 20이 나온다는 걸 이해해야됨
