# isinstance
# 타입 검사 시 사용한다.

class A:
    pass

class B(A):
    pass


a = A()
b = B()

# a는 A타입인지 확인
print(isinstance(a, A))
# 결과 값: True

# b는 B타입인지 확인
print(isinstance(b, B))
# 결과 값: True

# b는 A타입인지 확인
print(isinstance(b, A))
# 결과 값: True
# 모든 자식은 부모 타입이다.

# 부모는 절대 자식 타입이 될 수 없다
print(isinstance(a, B))
# 결과 값: False
# 부모는 자식의 타입을 호출하지 않기 때문에 False

