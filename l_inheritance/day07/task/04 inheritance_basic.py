# 인간(부모)
# 이름(name), 나이(age)

# 걷기(walk) → 메소드
# '두 발로 걷습니다' 출력

# 원숭이(자식)
# 이름, 나이, 동물원 이름(소속)

# 걷기(walk) → 메소드
# '두 발로 걷습니다', '네 발로 걷습니다' 출력


# 인간(부모)
class Person:
    # 이름(name), 나이(age)
    # name: str, age: int → 주석(옵션) 같은 느낌으로 작성해 주는 것
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 걷기(walk) → 메소드
    # '두 발로 걷습니다' 출력
    def walk(self):
        print('두 발로 걷습니다')

# 원숭이(자식)
# 이름, 나이, 동물원 이름(소속)
class Monkey(Person):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo

    # 걷기(walk) → 메소드
    # '두 발로 걷습니다', '네 발로 걷습니다' 출력
    def walk(self):
        super().walk()
        print('네 발로 걷습니다')

p = Person('송서경',25)
p.walk()

m = Monkey('몽키', 5, '동물원')
m.walk()