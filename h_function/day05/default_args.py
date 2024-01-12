# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정할 수 있고, arg=value 로 작성한다.

def sub(number1, number2, number3, number4=0):
    return number1 - number2 - number3 - number4


result = sub(1, 2, 3)
print(result)
# 결과 값: -8


# 실습
# 이름을 전달받지 못하면 '익명'으로 대체하고,
# 나이를 전달받지 못하면 0으로 대체한다.
# def get_info(name, age):
#     return {}
# 만약 name만 packing하고 age는 안 하면 packing한 걸 뒤로 보내야함
# age, name='익명'
def get_info(name='익명', age=0):
    return {'name': name, 'age': age}

result = get_info('송', 20)
print(result)
# 결과 값: {'name': '송', 'age': 20}