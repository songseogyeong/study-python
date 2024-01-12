# 내부 API에 random이라는 module이 있다
# random module의 별칭은 r로 둔다
import random as r

# randint(시작값, 끝값)
# 1~10까지 중 랜덤한 값 1개
r.randint(1, 10)
print(r.randint(1, 10))

# 확률
# 1. list 선언
# 10단위 확률
단위 = 10
rating = [0] * 단위
확률 = 30

# 2. 확률을 계산해서 해당 자리에 1 대입
# 확률 // 10 = 3
for i in range(확률 // 10):
    # 3번째 자리까지 1을 넣는다
    # 0번째 = 1 ... 2번째 = 1,  3번째 = 0
    # list는 0부터 시작되니까 3번째하면 0~2번째까지임
    rating[i] = 1

# 0~0 - 1
# 30% 확률
# 10개 중 1은 3개 있기 때문에, 1이 나올 확률은 30%이다
if rating[r.randint(0, len(rating) - 1)] == 1:
    print('강화 성공')

# 확률
# 1. list 선언
# 1 > 100
# 10 > 10
단위 = 10
단위_dict = {1: 100, 10: 00}
rating = [0] * 단위_dict[단위]
확률 = 30

# 2. 확률을 계산해서 해당 자리에 1 대입
# 확률 // 10 = 3
for i in range(확률 // 10):
    # 3번째 자리까지 1을 넣는다
    # 0번째 = 1 ... 2번째 = 1,  3번째 = 0
    # list는 0부터 시작되니까 3번째하면 0~2번째까지임
    rating[i] = 1

# 0~0 - 1
# 30% 확률
# 10개 중 1은 3개 있기 때문에, 1이 나올 확률은 30%이다
if rating[r.randint(0, len(rating) - 1)] == 1:
    print('강화 성공')

# 70%확률로 뭘 할 거면 else 사용하기


# 컴퓨터는 난수를 만들 수 없다.
