class A:
    def __init__(self, name):
        # A class에는 부모 필드가 없기 때문에 오브젝트의 init을 비워둔다
        super().__init__()
        self.name = name
        print('부모 생성자')

    def print_intro(self):
        print('A')


class B(A):
    # self = B
    def __init__(self, name):
        # super = 부모 객체
        # super() = A()
        # 부모에 있는 name을 전달을 해줘야함(여기서 초기화하게끔)
        super().__init__(name)
        print('자식 생성자')

    def add(self, number1, number2):
        return number1 + number2

    # 다형성(이름은 하나인데 형태가 다양하다)
    # 재정의 되었기 때문에 'B'값만 나오게 됨
    def print_intro(self):
        print('B')

    # super로 부모 주소값을 붙이면
    # 부모 값 뒤에 추가로 붙는다
    def print_intro(self):
        # 부모의 메소드를 그대로 사용하고자 할 때(선택 사항)
        # 안 붙이면... 그냥 재정의되어서 부모의 메소드가 사용이 안됨
        super().print_intro()
        # 자식의 메소드에서 추가할 내용 작성
        print('B')

# 자식 생성자는 부모의 생성자를 가장 먼저 호출한다
b = B('한동석')
print(b.name)
# 자식에서 없으면 부모필드로 접근해서 찾음
b.print_intro()
print(b.add(1,2))

# 부모 생성자가 할당 다른 곳에 자식 필드가 할당이 됨
# 부모의 주소값은 super이 갖고 자식의 주소 값은 self가 갖음

a = A('홍길동')
a.print_intro()