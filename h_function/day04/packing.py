# unpacking : 값을 풀어서 적는 것
def get_total(number1, number2, number3):
    return number1 + number2 + number3

# packing : 값을 묶어서 적는 것
# 패킹에 *형식으로 전달되면 튜플로 이해하면됨> 왜? 값을 수정하면 X
# 묶어서 받음
def get_total(*numbers):
    # 외부에서 전달받은 값들이 numbers(튜플)에 저장된다.
    # 그래서 타입을 프린트로 확인해봄
    print(type(numbers))
    total = 0
    # 튜플이라 인덱스로 접근
    for number in numbers:
        total += number

    return total


# # 여러개의 값을 콤마를 구분하여 전달한다.
# total = get_total(1, 2, 3, 4, 5)
# print(total)

# 여러개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫번째 방에 통채로 들어가게 된다.
# 즉, 결과는 다음과 같다 ([1, 2, 3, 4, 5],)
numbers = [1, 2, 3, 4, 5]
total = get_total(numbers)
print(total)

# 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다.
numbers = [1, 2, 3, 4, 5]
# numbers의 값을 *묶어서 가져옴
total = get_total(*numbers)
print(total)

# 실습1
# 국어, 영어, 수학 점수를 전달 받은 뒤 총점을 출력하는 함수
# packing으로 제작하기
def get_total(*score):
    total = sum(score)

    print(total)

get_total(90, 90, 90)

# 실습1 정리 1
def get_total(*score):
    total = 0
    for score in score:
        total += score
    return total

print(get_total(90, 90, 90))


# 실습1 정리 2
def get_total(name, *score): # 반드시 받아야 하는 매개변수는 packing 앞에 작성한다
    # 패킹은 무조건 마지막에 작성
    print(name + '님')

    total = 0
    for score in scores:
        total += score
    return total

scores = [100, 40, 50]
print(get_total('한동석', *scores))


실습2
문자열에서 'A'가 몇 개 있는지 검사하는 함수
packing으로 제작하기
def get_count(*target):
    return len(i for i in target if i == 'A')

print(get_count('ABC', 'AAA'))


# 실습2 정리1
def get_count_of_A(*strs):
    return [str.count("A") for str in strs]

print(get_count_of_A("ABC", "AAB", "AAA"))

# 실습2 정리2
def get_count_of_A(*strs):
    count = 0
    counts = []
    for str in strs:
        for s in str:
            if s == "A":
                count += 1
        counts.append(count)
        count = 0
    return counts

print(get_count_of_A("ABC", "AAB", "AAA"))