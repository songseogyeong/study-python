# 문자열 = 리스트
# print(list("ABC"))
# 원래는 A, B, C 다 따로임

# for i in "ABC":
#     print(i)

# upper(), lower()
# 영문이 다 대문자로 변경됨!
print("Apple123!@$".upper())
# 영문이 다 소문자로 변경됨!
print("Apple123!@$".lower())

# split()
data = "사과, 바나나, 파인애플, 포도, 복숭아"
print(data.split(sep=",", maxsplit=2))
# 구분점으로 구분을 할 건데, 최대 두개까지만 구분해라!
print("A B C D E F".split())
# 공백으로 구분하면 split() <에 굳이 공백 안 띄어두 됨~
print("A           B".split())
# 중간에 \n을 넣으면 구분점으로 사용할 수 있음
print("A        B".split(" "))
# split에 공백을 넣으면 공백을 문자열로 인식함
# 'A'(공백)' '(공백)' '(공백)'B'...

# join()
# 현재 시간을 알맞는 날짜 형식으로 바꿀 때 사용
# 10:15 를 [10, 15]로 변환해서 사용
print(":".join(['a', 'b', 'c']))
# 리스트가 :로 구분되어 문자열 값으로 출력된다!
print("".join(['a', 'b', 'c']))
# 리스트의 값을 원하는 구분점으로 연결할 때 사용!


# replace('기존 값', '새로운 값'
print("A b C d".replace(" ", ""))
# 공백을 찾아서 빈 문자열로 변경
print("안녕! 반가워~!".replace("!", "?"))
# 중복된 값을 처리할 때 replace를 사용해 처리한다

# strip(), lstrip(), rstrip() : 앞 뒤 공백을 제거할 때 보통 사용한다.
print("a        b      c         ".strip())
print("a        b      c         ".strip(" "))
print("apple".strip("a"))
print("apple".strip("ap"))
# a___a있을 때 왼쪽 a만 없애고 싶으면 lstrip(), 오른쪽 없애고 싶으면 rstrip()


# index() : 찾고자 하는 값이 없으면 오류가 발생한다.
print("ABC".index("A"))
# print("ABC".index("Z")) 오류
# 이거 없으면 큰일난다!!! 하면 index사용
# 인덱스는 없는 값을 검색하면 바로 오류가 나면서 프로그램이 꺼짐
# 그래서 만든게 find 아래로...


# find() : 찾고자 하는 값이 없으면 -1을 가져온다.
print("ABC".find("A"))
print("ABC".find("Z"))


# in: 값의 유무 검사
print("A" in "ABC")
print("Z" in "ABC")

# count() : 전달한 값이 몇 개 있는지 검사
print("fdsjfmsdlffjskfjdlkfjsdklfjadlkfjskldf".count("s"))

s = "189,000원"
# 위 값은 list값!
for i in s:
    if '0' <= i <= '9':
    # 대소비교 조건식에서 사용되면 문자열인 숫자가 정수로 변경된다.
    # 아스키 코드 '0' = 48, '1' = 49...
        print(i)

s = "189,000원"
print("".join([i for i in s if '0' <= i <= '9']))
# comprehension이기 때문에 리스트에 담긴 것
# 위에 작성한 코드랑 똑같음!
# join으로 리스트를 묶어서 출력