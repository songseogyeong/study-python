# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

# PartTimer class 생성:
class PartTimer:
    # '모든 직원'에 공통적으로 적용되는 내용
    # - 시급
    pay_of_hour = 10000
    # - 직원수
    total_of_part_timers = 0

    # '각 직원'별로 적용되는 내용
    def __init__(self, nickname, address='청담동'):
        # - 별명
        self.nickname = nickname
        # - 근무지(기본값: '청담동')
        self.address = address
        # - 급여 총액(초기값: 0, 생성자로 초기화 불가능)
        self.total_money = 0
        # 객체 생성 시 직원수 +1 씩 증가
        # self로 받으면 각 객체가 1씩만 받음
        PartTimer.total_of_part_timers +=1

    # 직원 급여 계산
    # '근무 시간 + 상여금'에 따른 직원 급여 계산
    # '상여금'은 지정 하지 않으면 0 으로 처리
    def calculate_money(self, hour, bonus=0):
        # 지금 받을 돈
        # total_money는 함수에 있는 값
        total_money = PartTimer.pay_of_hour * hour + bonus
        # 그동안 받은 돈
        # total_money는 생성자에 있는 값(영역이 다름)
        self.total_money += total_money

        return total_money

ryan = PartTimer('라이언')
neo = PartTimer('네오', '역삼동')

print(ryan.total_money, ryan.nickname, ryan.address)
# 결과 값: 0 라이언 청담동
result = ryan.calculate_money(8, 10000)
print(ryan.total_money, ryan.nickname, ryan.address)
# 결과 값: 90000 라이언 청담동
