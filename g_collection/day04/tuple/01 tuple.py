# mutable : 변할 수 있는
# mutable은 비추천! 한 곳에서 바꾸면 모든 데이터가 다 바뀌기 때문이다.
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
# data_list2 과 data_list1 는 같은 주소값을 가지기 때문에 하나만 수정해도 같이 변경됨
data_list2[0] = 10
print(data_list1)
# 결과 값 = [10, 2, 3, 4]
print(data_list2)
# 결과 값 = [10, 2, 3, 4]

# list는 제한을 주는 목적이 아님
# 제한을 주고 싶으면 len, range 등으로 검사를 해야 함!

# immutable :  변할 수 없는
data_tuple1 = (1, 2, 3, 4)
# 구조는 list와 같음. 저장공간에 값을 넣고 저장공간의 주소값을 가짐
data_tuple2 = data_tuple1

# data_tuple2[0] = 10
# 결과 값: 오류
# 튜플은 데이터 값을 수정할 수 없다.

test = list(data_tuple2)
test[0] = 10
print(test)
# 결과 값 = [10, 2, 3, 4]
# tuple을 list로 변환하면 수정 가능
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1

data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)
# 결과 값: (1, 2, 3, 4, 5, 6)
print(data_tuple1)
# 결과 값: (1, 2, 3, 4)
# 튜플은 주소값을 공유하는 게 아니라 변경이 불가능하기 때문에 복사 후 값을 추가하는 식

datas = 1, 2
print(type(datas))
# 결과 값: <class 'tuple'>
print(datas[0])
# 결과 값: 1

ERROR_CODE = 1,
print(type(ERROR_CODE))
# 결과 값: <class 'tuple'>
# 상수는 대문자로 작성
# 값이 하나만 있어도 ,(콤마)만써주면 튜플임
# 소괄호 생략

# 외부에서 전달 받은 값은 튜플로 받고, 내가 외부로 보낼 때도 튜플로 보냄
# 값이 수정이 안 되기 때문에 신뢰가 감!