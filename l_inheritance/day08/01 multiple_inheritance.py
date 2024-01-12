# 다중 상속
# 파이썬은 다중상속을 지원한다.
# 하지만, 여러 부모를 상속 받았을 때, 동일한 이름의 필드가 겹치면
# 자식에서 사용할 때 혼란을 야기한다.
# 이 때에는 mro()를 사용하여 접근 순서를 확인할 수 있으나,
# 자식에서 재정의한 뒤, 사용하는 것이 오히려 낫다.
# 다중 상속은 다양한 모호성을 발생시키기 때문에 되도록 피하는 것이 좋다.

class A:
    pass

class B(A):
    def print_info(self):
        print('B')

class C(A):
    def print_info(self):
        print('C')

# 다중 상속의 문제점
# B와 C랑 연결되어 있지 않은데, D에서 부모를 한 번에 받고 print_info를 출력하면
# print_info라는 게 어디에 있는 걸 가져오는지 몰라서
# 좌측에 있는 값을 가져온다
class D(B, C):
    pass

# mro()는 접근 순서를 보여준다
print(D.mro())
# 결과 값: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# object는 모든 class가 받는 값. 출력 시 무조건 함께 나옴.

D().print_info()
# 결과 값: B

# 다중 상속에서 부모 값을 받을 때 아래 처럼 사용
class D(C, B):
    def __init__(self):
        # C.super().__init__(self)
        C.__init__(self)
        # B.super().__init__(self)
        B.__init__(self)

D().print_info()
# 결과 값: C
# C가 왼쪽에 먼저와서 C 값 출력