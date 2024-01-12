class A:
    def print_name(self, name):
        print(name)


#  객체화
a = A()
# a > 객체, A > 클래스
# A() >생성자, 함수x
print(a)
# 결과 값: <__main__.A object at 0x000002B97AAF75E0>
# 0x000002B97AAF75E0 → 주소 값


class A:
    def print_name(self, name):
        print(name)

#     # @
#     # new는 생성자
#     # 메모리에 필드 할당만해줌
#     #     def __init__(self):
#     #         pass
#     # init은 직접 처리하는 애 <근데 얘를 생성자라고도 함
#     # 실질적인 처리는 init
#
#     # new랑 init은 한 쌍이다
#     # 지우면 자동으로 생성됨
#         init은 필요한 변수 선언
#
#     def __init__(self, name):
#         pass
#
# a = A()
# print(a)
#
#
# #    def __init__(self, name):
# #         pass
# #
# # a = A()
# # print(a)
# # init에 name을 담고 프린트하면 오류가 남> 클래스에서 받은 값이 없어서
# # 근데 self만 남겨놓으면 오류가 안남, self는 자동으로 주소값을 가져오기 때문

        # 디폴트 값 넣기
        # 디폴트 값이 있는 건 안 들어갈 수도 있으니 뒤로 보내기
        def __init__(self, data1, data2, name='',):
            print(self)
            slef.data1 = data1
            self.data2 = data2
            self.name = name

        # def print_name(self, name):
        #     print(name)

        def print_name_(self):
            print(self.name)

# a = A()
a = A(10, 20, 'a')
# a주소값에 접근해서 data를 선언 지금은 a에 값이 없어도 파이썬은 동적이기 때문에 변수가 없으면 만들어짐
# a.data1 = 10
# a.data2 = 20
print(a.data1, a.data2)
# 있으면 수정, 없으면 추가가됨
# a.print_name('a')
# 공백으로 나옴... 결과 값
# 생성자 호출할 때 네임 정한 적 없음 그래서 빈문자열 생성됨
a.print_name()

# b = A()
b = A(100, 200, 'b')
print(b)
# b.data1=100
# b.data2=200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()


# ----------------------------------------------------------------------------------------------------------------------
class A:
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = super().__new__(cls)
        return obj

    def __init__(self, data1, data2, name=''):
        print('__init__')
        print(self)
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # def print_name(self, name):
    #     print(name)

    def print_name(self):
        print(self.name)

# a = A()
a = A(10, 20, 'a')
print(a)
# a.data1 = 10
# a.data2 = 20
print(a.data1, a.data2)
# a.print_name('a')
a.print_name()

# b = A()
b = A(100, 200, 'b')
print(b)
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()