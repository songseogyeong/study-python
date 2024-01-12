# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

# import re
#
# # 1. 전체 문자 조회
# with open('alice.txt', 'r', encoding='utf-8') as file:
#     # 문자열로 만들기
#     not_string = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', file.read())
#     # 2. 알파벳 검사
#     string = not_string.split()
#     # 3. 대소문자 구분없이 비교
#     result = list(map(lambda string: string.lower(), string))
#
# key_number = {}
#
# # 4. 글자수 2개 이상인 단어 카운트
# for i in result:
#     # 글자수가 2개 이상인 i의 값이면
#     if len(i) >= 2:
#         # dict의 key 값에 글자수가 2개 이상인 i이 값을 넣고
#         # i의 값을 가져오는데, 문자를 더할 수도 없고 i를 그대로 가져오면 key값과 value 값이 똑같기 때문에
#         # i를 0으로 만들어준다음 반복문에서 같은 값이면 하나씩 value를 증가
#         key_number[i] = key_number.get(i, 0) + 1
#
# print(key_number)
#
# # 5. 빈도수 100회 이상인 단어만 카운트
# if key_number >= 100:
#     print(key_number)


# 정리
with open('alice.txt', 'r', encoding='utf-8') as file:
    # file을 문자열로 읽어와서 소문자로 변환
    content = file.read().lower()

temp = []
# 각각의 단어를 character에 넣음
for character in content:
    # a~z 사이면
    if 'a' <= character <= 'z':
        # temp에 담기
        temp.append(character)
    # 아니면
    else:
        # 공백으로 담기
        temp.append(" ")

# 조인해서 문자열로 담기
content = "".join(temp)

# 2개 이상의 단어만 들어감
words = [
    word
    for word in content.split()
    if len(word) > 1
]

# 딕셔너리 선언
result = {}
# 월즈에는 2개 이상의 단어만 들어감
# 각각의 단어를 월드
for word in words:
    # result 딕셔너리에 키가 있는지 없는지 확인
    if result.get(word) is not None:
        # 있으면 동일 key 값의 value를 하나씩 증가
        result[word] += 1

    # 없으면 키 값 추가하고 value는 하나로 두기
    else:
        result[word] = 1

print(result)

# 100개 걸러주기
result = {
    word: result[word]
    for word in result
    # result 딕셔너리의 키값의 value가 100이상?
    if result[word] >= 100
}

print(result)

# dict vaule 값 가져오는 함수가 get
sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
    print(key, result[key])
