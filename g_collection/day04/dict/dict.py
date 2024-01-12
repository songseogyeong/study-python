student = {
    "name": "한동석",
    "email": "tedhan1204@gmail.com"
}

print(student['name'])
# 결과 값: 한동석

# print(student['phone'])
# 결과 값: 오류


# get()
# get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# default 값이 없을 때에는 None을 가져온다.

# get을 써서 studnet에 있는 name을 가져온다
print(student.get('name'))
# 결과 값: 한동석

# get을 써서 studnet에 있는 phone을 가져온다
print(student.get('phone'))
# 결과 값: None
# 오류가 나지 않고 None 값이 나옴

# phone 값을 가져오는데, 만약 없으면 뒤 값을 default 값으로 설정한다.
print(student.get('phone', '01012341234'))

# name' key 값이 이미 있기 때문에, 아래의 코드는 '수정'이다.
# student에 name 이 있으면 수정 없으면 추가한다
student['name'] = '홍길동'
print(student)

# 'phone' key 값이 없기 때문에, 아래의 코드는 '추가'이다.
student['phone'] = '01012341234'
print(student)

# student 안에 email이 있으면 수정
if 'email' in student:
    student['email'] = 'hgd1234@gmail.com'

# 없으면 추가
else:
    student['email'] = 'hgd1234@gmail.com'

print(student)
# 결과 값: {'name': '홍길동', 'email': 'hgd1234@gmail.com', 'phone': '01012341234'}

my_dict = {
    1: "한동석",
    "two": "20살",
    False: [10, 20, 30],
    "row": [
        {"name": "ted", "age": 40},
        {"name": "jack", "age": 30},
        {"name": "john", "age": 20}
    ]
}

# 실습 1
# row에 있는 회원 3명의 정보를 모두 출력
# my_dict에 있는 row 값을 모두 출력
print(my_dict["row"])
# 결과 값: [{'name': 'ted', 'age': 40}, {'name': 'jack', 'age': 30}, {'name': 'john', 'age': 20}]

print(my_dict.get('row'))
# 결과 값: [{'name': 'ted', 'age': 40}, {'name': 'jack', 'age': 30}, {'name': 'john', 'age': 20}]

# my_dict에 row라는 키 값이 있으면
if 'row' in my_dict:
    # my_dict에 'row'가 있는지 확인, 있으면 어떤 타입인지 확인
    # print(type(my_dict['row']))
    # my_dict에 row라는 키 값이 있으면 data에 담아준다
    for data in my_dict['row']:
        # data의 name, data의 age를 문자열로 출력한다.
        print(f'{data["name"]}, {data["age"]}')


# 실습2 1번
# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면, 짝수만 출력하고
# '홀수'를 입력하면, 홀수만 출력한다.
# dict를 사용한다.
number_dict에
number_dict = {
    # '홀수'라는 키 값이 있다
    # 밸류 값은 5번 반복하는 값을 i에 담아주고 i를 * 2를 한 뒤 1을 더해준다.
    # 0 * 2 = 0 + 1 = 1
    # 1 * 2 = 2 + 1 =3 ... 홀수 값
    '홀수' : [i * 2 + 1 for i in range(5)],
    # '짝수'라는 키 값이 있다
    # 밸류 값은 5번 반복하는 값을 i에 담아주고 i에 1을 더하고 * 2를 곱해준다.
    #
    '짝수' : [(i + 1) * 2 for i in range(5)]
}

# print(number_dict[input('짝수 혹은 홀수: ')])
print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ')])))

# 실습2 2번
number_dict = {
    True : [i * 2 + 1 for i in range(5)],
    False : [(i + 1) * 2 for i in range(5)]
}

# str 형변환 이유: 형변환을 하지 않으면 정수끼리 연산됨
print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ') == '홀수'])))


# 예제1
student = {
    "name": "한동석",
    "email": "tedhan1204@gmail.com"
}

# key 분리
print(list(student.keys()))

# value분리
(print(list(student.values())))

# item 분리
# 한 쌍 씩 튜플로 가져옴!
print(list(student.items()))
# list 안에 튜플이 있어서 각 값을 key와 value에 담아 출력
for key, value in student.items():
    print(key, value)