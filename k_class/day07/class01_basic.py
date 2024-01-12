class Car:
    # 생성자 안에서 선언하지 않고 class에서 바로 선언함 = 생성자 안에 선언하는 것과 다름
    # 바로 선언 시 모든 객체가 공유하는 변수
    # car라는 타입이 모두 유하는 객체
    # 생성자로 선언 시 일일히 필드에 들어가서 변경해야 하지만
    # 바로 선언 시 객체에 일괄로 처리 가능
    # 객체로 직접 접근하는 것이 아니라 class로 접근
    # car.wheel로 접근
    # 정적 변수(static variable) > 고정되어 있음. 객체별로 수정하는 게 아님!
    # 생성자에 올라가는 게 아님(생성자에 의존하지 않음)
    wheel = 4

    def __init__(self, brand='', color='', price=0):
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_stop(self):
        print(self.brand + '시동 꺼짐')

# 생성자에 값 전달
mom_car = Car('Benz', 'Black', 15000)
daddy_car = Car('BMW', 'Blue', 8800)

mom_car.engine_start()
daddy_car.engine_start()

# 정적 변수는 아래 처럼 쓰지 않고
# print(mom_car.wheel)
# print(daddy_car.wheel)

# 아래 처럼 씀
# 어차피 모든 객체가 공유 받는 값인데.. 헷갈리게 객체마다 확인할 필요 없이 class로 접근해서 확인하는 게 효율
print(Car.wheel)

Car.wheel = 6
print(mom_car.wheel)


# # 실습
# # 변수로 여러번 선언하면 비효율적이라 list를 사용해서 한번에 선언하기
# # class명만 써도 내부적으로 값을 할당할 수 있음
# # car라는 자료형이 두개가 필요해서 2개 생성
# cars = [Car, Car]
# # cars의 0번째 방에 소괄호를 붙여서 생성자를 호출
# mom_car = cars[0]()
# daddy_car = cars[1]()
# print(mom_car, daddy_car, sep='\n')
# # 결과 값:
# # <__main__.Car object at 0x0000019C338D75E0>
# # <__main__.Car object at 0x0000019C338D7EB0>
# # mom_car와 daddy car의 주소 값이 다르다는 것을 알 수 있음
#
# # # 원래 아래처럼 해줘야 하는데 위처럼 한 번에 선언한거임
# # mom_car = Car
# # daddy_car = Car
