# 실습 1번
# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

# taxi class 생성
class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self, money, distance):
        self.money = money
        self.distance = distance

    def calculate_fare(self):
        cost = Taxi.default_fare
        if self.distance > Taxi.default_distance:
            cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km

        return cost

    def get_change(self):
        return self.money - self.calculate_fare()


taxi = Taxi(20000, 1)
print(taxi.calculate_fare(), taxi.get_change())

taxi = Taxi(30000, 10)
print(taxi.calculate_fare(), taxi.get_change())



# 실습 2번
# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화 한다.

# 1. 거리에 따른 요금 계산 메소드 정의
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달 받는다)
# 3. 거리에 따른 잔돈 계산 메소드 정의

class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self):
        # 위에 값을 못 받게(초기화) 하기 위해 아래에만 작성
        # 승객이 타고 난 이후에 거리와 요금을 계산할 거기 때문에 여기에는 안 넣어줌
        self.income = 0

    def calculate_fare(self, money, distance):
        cost = Taxi.default_fare
        # 매개변수로 받은 거기 때문에 self없이 distance만 작성
        if distance > Taxi.default_distance:
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km

        self.income += cost

        # 잔돈을 계산하기 위해 return

        # 잔돈부터 계산 x
        # closure로 넣는 이유:  잔돈은 앞에 있는 로직을 실행하고 나서 구할 수 있는 거기 때문에
        def get_change():
            return money - cost

        # 두개의 리턴을 해야하니까 tuple로 묶어서 보냄
        return cost, get_change()


taxi = Taxi()
print(taxi.calculate_fare(20000, 1))
print(taxi.calculate_fare(30000, 10))
print(taxi.income)
