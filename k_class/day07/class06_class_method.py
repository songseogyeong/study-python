# class Car:
#     wheel = 4
#
#     # 클래스 메소드는 cls(클래스)를 받아야 한다.
#     @classmethod
#     def change_wheel(cls):
#         cls.wheel = 6
#
#     # 이렇게 써도 되나, 스테틱 메소드를 쓰는 게 더 좋음

# static 메소드와 class 메소드의 공통점
# 객체가 아닌, 클래스로 접근해서 사용한다.

# static 메소드와 class 메소드의 차이점
# static 메소드는 전체 객체를 대상으로 실행할 문장을 작성하는 데에 목적을 두지만,
# class 메소드는 위의 목적과 생성자를 wrapping하는 목적도 가지고 있다.
# 이 때, cls는 클래스를 받는 매개 변수이다(cls는 객체나 생성자가 아닌 클래스 그 자체이다).

class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    @classmethod
    def translate_to_eng(cls, brand, color, price):
        if color == '빨간색':
            color = 'red'

        # 생성자를 호출한 것
        return cls(brand, color, price)

car = Car.translate_to_eng('Benz', '빨간색', 15000)
# car = Car('Benz', '빨간색', 15000)
print(car.color)

# @classmethod, @staticmethod
# method로 객체화를 함
# 공통점: 클래스로 직접 접근해서 사용할 수 있는 메소드
# 차이점: 스테틱 메소드는 내가 하고 싶은 거 쓰면됨(공통으로 하고 싶은거) 객체들을 한 번에 처리 하고 싶은ㄱ ㅓ
# 클래스는 내가 만든 생성자를 쓰지 않고 내가 만든 클래스 메소드로 호출(객체화를 함)
# 클래스 메소드로 객체화하면, 놓칠 수 있는 부분이 잡혀진다>랩핑
# 생성자를 클래스 메소드가 감싼 느낌

