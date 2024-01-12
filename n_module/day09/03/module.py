# calc_add 모듈을 사용
# calc_add 모듈에 있는 내용을 사용할 수 있음
import calc_add
# import calc.calc_sub as sub
# 패키지에 있는 거 사용하고 싶으면 패키지 명부터 작성해서 연결하고 모듈명 작성하기
# 단, 패키지에 있는 것을 사용하고 싶으면 별칭을 주기
# form에 있는 모듈에서 improt 뭘쓸래
from calc.calc_sub import sub
# clac 패키지에 calc모듈의 *(모든 것)을 연결
from calc.calc import *

# 해당 모듈을 사용해라:
if __name__ == '__main__':
    # import calc_add로 add함수를 사용해서 필드에 값을 넣고 연산
    print(calc_add.add(2, 3))
    # 결과 값: 5

    # import calc.calc_sub
    # print(calc.calc_sub.sub(10, 5))
    # import calc.calc_sub as sub
    # 별칭을 설정했기 때문에 sub 모듈안에 sub 함수 사용한다고만 표기 가능
    # print(sub.sub(10, 5))
    # 결과 값: 5

    # 모듈에서 sub 필드를 사용한다고해서 sub 함수만 작성해서 값을 입력해도 바로 써짐
    # from calc.calc_sub import sub
    print(sub(10,5))
    # 결과 값: 5
    print('=' * 20)
    c = Calculator(10, 5)
    print(c.add())
    print(c.sub())