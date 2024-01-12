import copy
# copy라는 게 내장되어있어서 그냥 사용이 가능

datas = [1, 2, 3]
# dats와 datas_copy는 같은 주소 값을 공유하기 때문에 datas_copy를 하면 data의 값이 바뀜
# 그래서 얕은 복사를 하는 것
datas_copy = datas
# 얕은 복사는 기존 값을 복사해서 새롭게 만들어내는 것을 의미한다.
# 새로운 주소에 할당하기 때문에, 불변성이 보장된다.

# list안에 값만 나열되어있을 때 사용

datas = [1, 2, 3]
# copy파일 안에 copy라는 함수를 사용해서 datas를 복사
# data
datas_copy = copy.copy(datas)
# 주소를 비교하여 출력
print(datas is datas_copy)
# 결과 값: False

# datas_copy의 0을 바꿔도 dats와 dats_copy는 다른 주소값을 가지고 있기 때문에
# datas의 값이 바뀌지 않는다(불변성 보장)
datas_copy[0] = 10

print(datas)
# 결과 값: [1, 2, 3]
print(datas_copy)
# 결과 값: [10, 2, 3]


# 얕은 복사
datas = [1, 2, 3]
# 슬라이싱 디폴트 값이기 때문에 처음부터 끝까지
# 슬라이싱 자체가 얕은 복사를 지원함
datas_copy = datas[:]
datas_copy[0] = 10
print(datas)
print(datas_copy)


# 얕은 복사
# 얕은 복사 사용 시, 두번째 접근부터는 불변성이 보장되지 않는다.
datas = [1, [1, 2, 3], [4, 5, 6]]
datas_copy = copy.copy(datas)
datas_copy[0] = 10
print(datas)
print(datas_copy)

datas_copy[1][0] = 10
print(datas)
print(datas_copy)


# 깊은 복사 사용 시 , 깊은 접근까지 모두 불변성이 보장된다.
# 너무 깊은 구조에서 사용할 때에는, 메모리 소모량이 증가하기 때문에,
# 불변성이 보장될 필요가 없을 때에는 사용하지 않는 것이 좋다.

# 깊은 복사
datas = [1, [1, 2, 3], [4, 5, 6]]
datas_copy = copy.deepcopy(datas)
datas_copy[1][0] = 10
print(datas)
print(datas_copy)