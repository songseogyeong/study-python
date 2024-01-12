# 전역 변수(global variable)
# 어떤 지역 밖에 선언된 변수
# 여러 함수에서 공유해야 하는 값이 있을 경우 사용
# (예시)
data = 10

# 지역 변수(local variable)
# 어떤 지역 안에 선언된 변수
# (예시)
def test():
    # 데이터 선언, test안에서 선언됐기 때문에 지역변수임!
    data = 10

# 전역변수
# 모든영역에서 사용 가능
count = 0

def inrease():
    # print(count)
    # 밖에 있는 count랑 안에 있는 count는 다름
    # 지역변수
    # count = 0
    # global을 붙이면 전역변수를 사용할 수 있음
    global count
    # 지역에서 전역변수를 수정하려면 global 키워드를 사용한다.
    count += 1

inrease()
print(count)


# ----------------------------------------------------

data = [1, 2, 3]
# 데이터를 변경하면 global을 사용해야 하는데
# 데이터를 수정하면 global을 사용하지 않아도됨!

global data
data = [3, 4, 5]
# 데이터 자체 주소값을 바꾸는 거기 때문에 global 사용

data[0] = 10
# 데이터 주소값으로 접근해서 값을 바꾸는 거기 때문에 global사용할 필요 없음