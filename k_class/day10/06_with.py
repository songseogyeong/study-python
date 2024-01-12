# new 할당자, init 생성자
# with문을 쓰면 왜 자동으로 close?
class NameCard:
    def print_info(self, name):
        print(name)


    def __enter__(self):
        print('enter')
        # self를 리턴해야 주소 값이 들어가서 값을 출력할 수 있음
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def __del__(self):
        print('del')

with NameCard() as name_card:
    name_card.print_info('한동석')

with문은 enter부터 씀
그리고 exit함 가장 마지막에 실행되어야 하는 코드를 작성
del는 소멸자