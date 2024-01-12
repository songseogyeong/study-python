# 중복이 없고, 순서가 없다.
# 중복값 입력 시 들어가지 않음
# 순서가 없다는 건 = 값을 가져올 수 없음
# 있냐 없냐를 검사
world_set = {'korea', 'america', 'japan', 'china'}
# 중괄호에 값이 ,(콤마)로 연결되어 있으면 set이다.
print(type(world_set))
# 결과 값: <class 'set'>
print(len(world_set))
# 결과 값: 4
# print(world_set[1])
# 결과 값: 오류
# set에서 값을 가져오고 싶으면 list로 형변환하기
world_set.add('korea')
print(world_set)
# 결과 값: {'japan', 'korea', 'china', 'america'}
# 중복된 값은 처리가 안 됨
# set은 출력이 안되는데 출력이 되는 이유
# set 자료구조를 떠나서 다른 자료구조로 형변환을 한 뒤, 하나씩 값을 가져와서 ,(콤마)로 연결을 하고 중괄호로 감싸준 것
# set은 자료가 있는지 없는지를 검사하기 위한 목적이지, 값을 가져오기 위한 목적이 아님

# 중복을 제거할 때 효과적이다.
data = [1, 1, 3, 2, 3, 4, 1, 4]
print(list(set(data)))
# 결과 값: [1, 2, 3, 4]
# 아스키 코드 합으로 정렬이 됨
# 여기서 set으로 중복을 제거한다
# 실무 예시 > set으로 문상 일련번호 중복검사 가능

