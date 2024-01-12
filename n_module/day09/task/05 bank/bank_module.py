from bank import *

def check(*, key: str, value: str) -> dict:
    # 저장소(DB)에서 각 은행 정보를 가져온 뒤
    for bank in Bank.banks:
        # 각 회원의 정보를 가져온다.(그래서 반복문 두번)
        for user in bank:
            # 전달 받은 키워드(key)로 회원의 정보를 value와 같은지 검사한다.
            if user[key] == value:
                # 만약 해당 회원을 찾았다면, 회원의 전체 정보를 리턴한다.
                return user

    # 해당 회원을 찾지 못했다면, None을 리턴한다.
    return None

class Bank:
    # 은행의 개수
    total_count = 3
    # 은행의 개수만큼 저장공간을 확보해 준다.
    # 은행의 개수만큼 반복문으로 저장공간 확보
    banks = [[] for i in range(total_count)]

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # 각 회원의 object 필드에는 필드의 주소 값이 담긴다.
        # self는 할당한 주소의 주소 값
        # classmethod에서 dict값으로 저장했기 때문에 주소값을 사용할 수 있도록 지정한 것
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    # 어떤 은행에서 개설하는 지 bank_choice로 전달 받는다.
    # 개설에 필요한 모든 회원정보는 **kwargs로 한 번에 받는다.
    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        # 회원이 어떤 은행에서 개설하는지 알 수 없다.
        # 전달 받은 bank_choice를 통해 정확히 은행을 선택할 수 있게 된다.
        # [ShinHan, KookMin, KaKao] > 저장 하는 저장소
        # [bank_choice - 1] 접근 하는 것
        # (**kwargs) 생성자 호출을 위해 소괄호로 묶어서 호출
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # 은행 DB에 고객의 정보를 담을 때, dict 타입으로 변환해서 담는다.
        # check 함수에서 원하는 key로 회원의 정보를 찾기 위해서 dict 타입으로 변환
        cls.banks[bank_choice - 1].append(user.__dict__)
        # 개설된 회원 정보를 리턴한다.
        return user

    # self에 접근하는 메소드가 아니기 때문에,
    # staticmethod 데코레이터를 붙여서 사용한다.
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        # check 함수에서 전달할 key와 value를 전달한다.
        return check(key='account_number', value=account_number)

    @staticmethod
    def check_phone(phone: str) -> dict:
        # check 함수에서 전달할 key와 value를 전달한다.
        return check(key='phone', value=phone)

    def deposit(self, money: int):
        self.money += money

    def withdraw(self, money: int):
        self.money -= money

    def balance(self):
        return self.money

    # 객체를 출력하면 __str__()가 실행되기 때문에,
    # 편하고 빠르게 회원 정보를 확인할 수 있다.
    # 재정의를 하지 않으면 __repr__ 실행
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):
    # Overrding
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)


class KookMin(Bank):
    # Overrding
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))


class KaKao(Bank):
    # Overrding
    def balance(self):
        self.money //= 2
        return super().balance()