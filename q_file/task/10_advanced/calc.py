# 사용하는 메일 모듈을 기준으로 경로를 작성해야 한다.
from log import log_time

class Calculator:
    def __init__(self, number: int):
        self.oper = None
        self.number = number

    def calc(self, other, oper, error_code=""):
        oper_number = {'+': 0, '-': 1, '*': 2, '/': 3}
        self.oper = oper
        operations = [self.__add__, self.__sub__, self.__mul__, self.__floordiv__]
        return operations[oper_number[oper]](other, error_code=error_code)

    @log_time
    def __add__(self, other, **kwargs):
        return self.number + other

    @log_time
    def __sub__(self, other, **kwargs):
        return self.number - other

    @log_time
    def __mul__(self, other, **kwargs):
        return self.number * other

    @log_time
    # floor는 소수점 버림
    # 몫만 나옴
    def __floordiv__(self, other):
        # 몫과 나머지 모두 구현
        return self.number // other, self.number % other