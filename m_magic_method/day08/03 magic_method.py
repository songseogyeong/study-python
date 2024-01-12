# 예제 1
class Magic:
    pass

print(Magic())
# 결과 값: <__main__.Magic object at 0x00000162BCA6CBB0>
print(Magic().__repr__())
# repr은 자동으로 사용되고, 재정의 x
# 결과 값: <__main__.Magic object at 0x00000162BCA6CBB0>


# 예제2
# __repr__ 뒤에 뭔가 추가하고 싶을 땐 __str__() 로 재정의 해준다.
class Magic:
    def __str__(self):
        return f'{self.__repr__()}, __repr__ 사용됨'

# 객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
print(Magic().__repr__())
# 결과 값: <__main__.Magic object at 0x00000162BCA6CBB0>

# 만약 해당 클래스에서 __str__()을 재정의했다면, __repr__()가 아닌 __str__()이 사용된다.
print(Magic().__str__())
# 결과 값: <__main__.Magic object at 0x000002BBC893BFD0>, __repr__ 사용됨

# 따라서, 생략해서 작성하면 __str__()이 붙게된다.
print(Magic())
# 결과 값: <__main__.Magic object at 0x000002BBC893BFD0>, __repr__ 사용됨


# 예제 3
class Magic:
    def __init__(self, name):
        self.name = name

    # 초기화된 필드를 확인하고자 할 때 사용한다
    def __str__(self):
        return f'name: {self.name}'

magic = Magic('magic')
print(magic)
# 결과 값: name: magic


# 예제 4
class Student:
    def __init__(self, score):
        self.score = score

    # other은 Student라는 type
    def __add__(self, other):
        # other로 다른 객체를 받은 것
        return self.score + other.score

std1 = Student(30)
std2 = Student(50)

# std1.score + std2.score
# 위 값을 아래 처럼 재정의를 통해 사용 가능
total = std1.__add__(std2)
print(total)
# 결과 값: 80

# total = std1.__add__(std2)
# 연산자를 사용해도 재정의된 메소드로 사용된다
total = std1 + std2
print(total)
# 결과 값: 80

# 이런 식으로 재정의 하지 않고 바로 사용가능
# class 객체를 dict로 변환해서 출력
# 작업 편리함
print(std1.__dict__)
# 결과 값: {'score': 30}

# dict 타입의 std1 객체에 있는 'score'의 값을 __getitem__을 사용해 가져오기
print(std1.__dict__.__getitem__('score'))
# 결과 값: 30

# [1, 2, 3]에서 2번째에 있는 값을 get
print([1, 2, 3].__getitem__(2))
# 결과 값: 3

print([1, 2, 3].__contains__(0))
# 결과 값: False

print(std1 == std2)
# 결과 값: False


# 예제 5 ★중요
class Student:
    def __init__(self, score, number):
        self.score = score
        self.number = number

    # other은 Student라는 type
    def __add__(self, other):
        # other로 다른 객체를 받은 것
        return self.score + other.score

    # self는 나 other은 다른 곳에서 들어온 것
    # 주소비교>타입비교> 값비교 순서로 하기(효율)
    def __eq__(self, other):
        # 두개 주소가 같은지 비교
        if self.__repr__() == other.__repr__():
            print('들어옴')
            # return을 만나면 종료되기 때문에 else를 사용하지 않고 if 사용한 것!
            return True

        # 타입 비교
        # isinstance(객체, 타입(=class명)): 전달한 객체가 전달한 타입일 경우 Ture, 아니면 False
        if isinstance(other, Student):
            # 값 비교
            return self.number == other.number

        # 위 if가 모두 아니면 False
        return False

std1 = Student(30)
# std2 = Student(50)

# 아래처럼 되면, 주소 값이 같아짐
std2 = std1

print(std1 == std2)
# 결과 값: False


