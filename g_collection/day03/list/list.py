# animals = ['dog', 'cat', 'bird', 'fish']
# #animals에 dog의 주소값이 담겨있음!
#
# print(animals)
# # 원래대로라면 animals에 dog의 주소값이 담겨있기 때문에 주소값이 나와야 하는데
# # ['dog', 'cat', 'bird', 'fish'] 이 나옴
# # 뭔가 다른 코드가 숨어있는 거임
#
# print(type(animals))
#
#
# # 인덱스로 접근
# # 인덱스는 시작 주소를 담고있기 때문에 0번부터 시작한다.
# print(animals[1])
# print(animals[2])
#
#
# # 음수 인덱스 가능(가장 마지막 순서대로 앞으로 이동한다)
# print(animals[-1])
# # leg -1 해서 마지막 값을 가져옴
# # # 4개가 있으니 -1해서 3번째를 가져오는 거임 = fish
# # print(animals[-2])
# # # 글에서 첫 글은 1 이고 최신글로 갈 수록 숫자가 커짐
# # # 그래서 최신순으로 보고 싶을 때는 음수를 쓰는게 좋음
# #
# #
# # # leng()
# # print(len(animals))
# #
# #
# # # append()
# # # 어펜드는 무조건 마지막에 붙는다.
# # animals.append("hamster")
# # print(len(animals))
# # print(animals)
# #
# # animals.append("cat")
# # print(animals)
# # # list는 중복 값을 허용한다.
# #
# #
# # # insert()
# # animals.insert(1, "dog")
# # print(animals)
# #
# #
# # # remove()
# # animals.remove('fish')
# # print(animals)
# #
# #
# # # del()
# # # del(animals[1]) 둘 다 가능~!
# # del animals[1]
# # print(animals)
# #
# #
# # # clear()
# # # animals.clear()
# # # print(animals)
# #
# #
# # # index()
# # print(animals.index('bird'))
# # # print(animals.index('tiger')) # #오류코드 tiger이 없음
# #
# #
# # # 수정
# # # animals[animals.index('bird')] = 'Lion'
# # # 대괄호에는 인덱스 번호만 들어갈 수 있는데,
# # # 저 안에 연산이 되어 있음
# # # 저 연산 자체가 인덱스 번호가 된다는 뜻
# #
# # index = animals.index('bird')
# # animals[index] = 'Lion'
# # print(animals)
# #
# #
# # # 그 외
# # animals = ['dog', 'cat', 'bird', 'fish']
# # print(animals * 2)
# # # 안에 있는 요소가 두번 나옴!
# #
# # print("dog" in animals)
# # print("tiger" in animals)
# # # 위에서는 없는 걸 찾으면 오류가 났는데 이건 오류가 안남! False 값이 나옴
# #
# #
# # for i in animals:
# #     print(i)
# #
# # for animals in animals:
# #     print(animals)
#
# # -------------------------------------------------------------------------------------
# # # 실습1
# # # 1~90까지 list에 담고 출력
# # number = []
# #
# # for i in range(90):
# #     number.append(i+1)
# # print(number)
# #
# #
# # # 실습 1 정리
# # number_list = [0] * 90
# #
# # for i in range(len(number_list)):
# #     number_list[i] = i + 1
# # print(number)
#
#
# # # 실습2
# # # 1~100까지 중 짝수만 list에 담고 출력
# # number = list()
# #
# # for i in range(100):
# #     if i % 2 == 0 :
# #         number.append(i)
# #     print(number)
#
#
# # 실습2 정리
# # number_list = [0] *50
# #
# # for i in range(len(number_list)):
# #     number_list[i] =(i + 1) * 2
# # print(number_list)
#
#
# # 실습3
# # 1~10까지 list에 담은 후 짝수만 출력
# # number_list = []
# #
# # for i in range(10):
# #     number_list.append(i+1)
# # print(number_list)
# #
# # for i in range(len(number_list)):
# #     if number_list[i] % 2 == 0:
# #         print(number_list[i])
# #
# # even_list = []
# #
# # for i in range(len(number_list)):
# #     if number_list[i] % 2 == 0:
# #         even_list.append(number_list[i])
# #
# # print(even_list)
#
#
# # 실습 4
# # 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# # 1. 두 번째 회원의 이름 수정
# # 2. 마지막 회원 삭제
# names = ['song', 'jea', 'min', 'hyeun']
#
# index = names.index('jea')
# names[index] = 'jung'
# print(names)
#
# del names[-1]
# print(names)
#
#
# # 실습4 정리
# names = ['한동석', '홍길동', '이순신', '장보고']
#
# # 1.
# names[1] = '서경덕'
# print(names)
#
# # 2
# # names.remove(names[-1])
# # print(names)
#
# del names[-1]
# print(names)

# list 안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
# number_list는 2칸짜리임!
number_list[0][0]
# 주소값 안에 주소값이 있기 때문에 number_list에서 값까지 두번 접근해야함
# 치환하여 접근 대괄호[]
# 넘버리스트의[첫번째 주소값][두번째 주소값]

length = len(number_list) * len(number_list[0])
# 길이 = 2칸 * 3

# for i in range(length):
#     print(number_list[i // 3][i % 3])

# number_list의 길이를 반복하고 반복한 값을 i에 담는다
for i in range(len(number_list)):
    # i의 값이 담겨있는 number_list의 길이를 반복해서 j에 넣어준다.
    for j in range(len(number_list[i])):
        # number_list i와 j를 출력한다.
        print(number_list[i][j])

#number_list에는 지금 값이 2
# i 에는 값이 2번 반복 된 것이 들어감~
# j에는 값이 3번 반복되는게 들어감
# 6
