# 핸드폰도 찾고 계좌번호도 찾아야해서 key, value 다 써주기
# 로그인 처럼 써주기
def check(*, key: str, value: str) -> dict:
    for bank in Bank.banks:
        for user in bank:
            # user의 키 값을 가져와서 해당하는 value 값인지 확인
            # 아래서 객체를 dict 타입으로 설정했기 때문에 key값을 list처럼 넣어도됨
            if user[key] == value:
                return user

    return None


# 은행
class Bank:
    total_count = 3
    # 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
    banks = [[] for i in range(total_count)]

    # 예금주, 계좌번호(중복 없음), 핸드폰번호(중복 없음), 비밀번호, 통장잔고
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    # 사용자가 어떤 은행을 선택했는지에 따른 객체 생성

    # 계좌 개설
    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        # 객체화 하기
        bank = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # 고객의 정보(객체)를 dict으로 변경해서 넣기
        cls.banks[ank_choice - 1].append(bank.__dict__)
        # 생성자 대신 사용하기 때문에 return 값을 bank로 담아주기
        return bank

    # 중복 검사는 전역 check 메소드를 사용해서 찾기

    # 계좌 중복 검사
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        # 리턴 값은 dict가 되거나 none이 됨
        return check(key='account_number', value=account_number)

    # 핸드폰 번호 중복 검사
    @staticmethod
    def check_phone(phone: str) -> dict:
        return check(key='phone', value=phone)


    # 입금
    def deposit(self, money: int):
        self.money += money


    # 출금
    def withdraw(self, money: int):
        self.money -= money

    # 잔액 조회
    def balance(self):
        return self.money

    # 한번에 조회할 수 있도록 재정의
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'

# 은행은 3개를 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.

# 신한
# 입금 시 수수료 50%
class ShinHan(Bank):
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)

# 국민
# 출금 시 수수료 50%
class KookMin(Bank):
    def withdraw(self, money: int):
        money *= 1.5
        # 실수가 되기 때문에 int로 형변환
        super().withdraw(int(money))

# 카카오
# 잔액조회 재산 반토막
class KaKao():
    def balance(self):
        self.money //= 2
        return super().balance()

# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        while True:
            # 서비스 메뉴
            menu_choice = int(input(owner_message))
            if menu_choice == 5:
                break

            # 개설
            if menu_choice == 1:
                # owner_message = "예금주: "
                # account_number_message = "계좌번호: "
                # phone_message = "핸드폰 번호: "
                # password_message = "비밀번호(4자리): "
                # money_message = "예치금: "


# 주소를 넣을 수 있는 공간 = None
# 그래서 None은 반드시 is로 넣어야됨 (== 안됨)

# ----------------------------------------------------------------------------------------------------------------------
#     while True:
#         # 은행 메뉴
#         bank_choice = int(input(bank_menu))
#
#         if 0 < bank_choice < 4:
#             while True:
#                 # 서비스 메뉴
#                 service_choice = int(input(menu))
#
#                 # 개설
#                 if service_choice == 1:
#                     pass
#
#                 # 입금
#                 elif service_choice == 2:
#                     pass
#
#                 # 출금
#                 elif service_choice == 3:
#                     pass
#
#                 # 잔액
#                 elif service_choice == 4:
#                     pass
#
#                 # 은행 선택 메뉴로 돌아가기
#                 elif service_choice == 5:
#                     break
#
#                 # 에러 메세지
#                 else:
#                     print(error_message)
#
#         # 나가기
#         elif bank_choice == 4:
#             break
#
#         # 에러 메세지
#         else:
#             print(error_message)