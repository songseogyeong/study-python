comprehension (컴프리헨션 : (어떤 뜻을) 내포[포함])
직역 = 이해력
숨어있는 의미를 이해
어디 안에 들어가있는 문법 ..! 안쪽에다 작성하는 문법이구나~를 알면됨
반복하거나 특정 조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법

# list comprehension
# [표현식 for 항목 in iterator (if조건)]
number_list = [1, 2, 3, 4]
result_list = [num * 3 for num in number_list]
print(result_list)
# number_list(4번) 만큼 반복하는 걸 num에다 넣고
# num을 끄집어내서 사용

number_list = [1, 2, 3, 4]
# [6, 12]
result_list = [number * 3 for number in number_list if number % 2 == 0]
# 1번 for number in number_list
# number_list를 number에 넣고
# 2번 if number % 2 == 0
# 짝수만 출력
# 3번  number * 3
# 표현
print(result_list)

[표현식 if 조건 else 표현식 for 항목 in iterator]
[삼항연산자 for number in number_list]

삼항 연산자
10 if 10 > 9 else 9
true 10, false면 9
그래서 두개의 값만 갖게됨!

number_list = [1, 2, 3, 4]
result_list = [number * 3 if number % 2 == 0 else number for number in number_list]
# number_list가 number 안에 들어가고 number 값을 사용할 수 있음~
# if 조건식이 참이면
# 앞의 표현식을 사용 ~ 거짓이면 else 표현식을 사용!
print(result_list)

# 실습 1
# 아래의 list에서 '양수'만 추출한 뒤 새로운 list에 담기
number_list = [10, 20, 30, -20, -3, 50, -70]
result_list = [sorted(number) if number > 0 else number for number in number_list]
print(result_list)

# 실습1 정리
number_list = [10, 20, 30, -20, -3, 50, -70]
result_list = [number for number in number_list if number > 0]
print(result_list)


# 실습2
# n개의 0으로만 채워진 list
message = 'list의 수를 입력하세요: '
length = int(input(message))

list = [0] * length
print(list)

# 실습 2 정리
# 위에 한 코드가 더 좋음~! 오예~
message = '생성할 list의 칸 수: '
length = int(input(message))
result_list = [0 for i in range(length)]
# i만큼의 0을 생성한다라고 생각하면 됨!!!
print(result_list)



# 실습3
# 제곱(a ** 2)의 결과가 10보다 큰 결과만 담은 list
number_list = [1, -2, 3, -4, 5]

result_list = [number for number in number_list if number ** 2 > 10]
print(result_list)


# 실습4
# 0~9까지 중 3의 배수만 담은 list
number_list = []

for i in range(10):
    number_list.append(i)
print(number_list)

result_list = [number for number in number_list if number % 3 == 0 and number > 0]
print(result_list)

# 실습4 정리
result_list = [i for i in range(10) if i % 3 == 0]
print(result_list)