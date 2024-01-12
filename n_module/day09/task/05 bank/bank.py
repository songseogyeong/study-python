from bank_module import *
from message_module import *

if __name__ == '__main__':
    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        # 나가기
        if bank_choice == 4:
            break

        # 메뉴의 번호 이외의 번호를 입력 시 밑으로 내려가지 못하게 막아준다(continue)
        # len은 은행이 늘어나면 일일이 수를 수정해줘야해서 len으로 몇개인지 자동 계산
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))
            # 은행 메뉴로 돌아가기
            if menu_choice == 6:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    # None은 False 값이지만, 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.
                    if Bank.check_account_number(account_number) is None:
                    # 아래처럼도 사용이 가능하지만, 직관성이 중요해서 is None이라고 표기해 준다.(가독성 up)
                    # if not Bank.check_account_number(account_number) :
                        break

                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break

                money = int(input(money_message))

                # 계좌가 개설된다.
                # 어떤 은행에서 개설했는지를 bank_choice에 담아서 전달한다.
                # open_account()는 회원의 정보를 **kwargs로 받기 때문에 모두 풀어서 전달해 준다.
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone, password=password, money=money)

                # 재정의한 __str__()이 사용되고, 회원의 전체 정보를 확인한다.
                print(user)

            # 입금
            elif menu_choice == 2:
                account_number = input(account_number_message)
                # 계좌번호 검색 결과가 user에 담긴다
                user = Bank.check_account_number(account_number)
                # 개설한 은행에서만 입금 가능
                # 해당 회원을 찾았다면,
                if user is not None:
                    # 비밀번호를 검사한다
                    if user['password'] == input(password_message):
                        # 신한은행 회원인지 검사한다
                        if isinstance(user.get('object'), ShinHan):
                            # 현재 선택된 은행이 신한은행이 아니라면,
                            if bank_choice != 1:
                                # 신한은행 회원은 신한은행에서만 입금이 가능하다고 안내해 준다.
                                print('개설한 은행에서만 입금 서비스를 사용하실 수 있습니다.')
                                # 입금 서비스를 이용하지 못하도록 막아준다.
                                continue

                            # 입금 서비스
                            deposit_money = int(input(deposit_message))
                            # 계좌 개설 시 담아놓은 self(객체)를 통해 메소드를 접근한다.
                            # 객체는 현재 dict타입이라.. 담아놓은 self객체를 통해 접근
                            user['object'].deposit(deposit_money)

                else:
                    print(error_message)

            # 출금
            elif menu_choice == 3:
                print('들어옴')
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        # 출금액을 입력 받는다.
                        withdraw_money = int(input(withdraw_message))
                        # 로그인한 회원의 은행이 국민은행 이라면,
                        # 국민은행은 출금 수수료가 50%이기 때문에, 잔액 검사 시 1.5를 곱해준다.
                        # 타 은행이면 수수료가 없다(1을 곱하기)
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            user['object'].withdraw(withdraw_money)
                            continue
                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                print('들어옴')
                phone = input(phone_message)
                user = Bank.check_phone(phone)
                if user is not None:
                    if user['password'] == input(password_message):
                        while True:
                            account_number = input(account_number_message)
                            if Bank.check_account_number(account_number) is None:
                                break
                        # 새롭게 설정한 계좌 번호로 등록 한다.
                        # 계좌를 개설할 때 __dict__로 저장했다.
                        # 이 때, __dict__를 수정하는 것 보다, 객체로 접근해서 바꾸는 것이 안전하다.
                        # 결국, __dict__도 self를 받아서 만들어진 객체이므로, 뿌리인 self로 접근하는 것이 좋다
                        # self를 받아와서 안에있는 필드를 dict로 만든거임
                        # dict로 접근해도 self로 감
                        # dict에서 바꾸면 거쳐서 변경되기 때문에 애당초에 self로 접근해서 값을 변경하는게 안전하다는 뜻
                        user.get('object').account_number = account_number
                        # 잘 되면 아래 print(오류메세지)가 출력되면 안되기 때문에 continue로 막아준것!
                        continue


                    print('핸드폰 번호 혹은 비밀번호를 다시 확인해 주세요.')

                # account_number = input(account_number_message)
                # user = Bank.check_account_number(account_number)
                # if user is not None:
                #     if user['password'] == input(password_message):
                #         user['account_number'] = input(account_number_message)
                #         continue

                else:
                    print(error_message)

            else:
                print(error_message)
