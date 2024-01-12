number = int(input('정수를 입력하세요.'))
# 정수가 아닌 다른 값을 입력하면 튕김
print('반드시 실행되어야 하는 문장')
# ValueEorror 라는게 메모리에 할당이 됐는데 값을 저장할 공간이 없어 강제 종료됨

try:
    number = int(input('정수를 입력하세요.'))

# except에서 ValueError 타입 검사를 하고 타입이 ValueError 이면 e라는 객체에 담는 것
except ValueError as e:
    print('정수만 입력해 주세요')

print('반드시 실행되어야 하는 문장')


# 예제1
# print(10 / 0)

try:
    print(10 / 0)

except ZeroDivisionError as e:
    print(e)
    # 결과 값: division by zero
    # 모든 에러들은 str을 재정의함
    # 그래서 주소 값이 안 나오고 문자열이 나옴
    print('0으로 나눌 수 없습니다')
    # 결과 값: 0으로 나눌 수 없습니다


# 예제 2
try:
    print(10 / 0)

except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')


# 예제3
# 가장 아래다가 씀
try:
    print(10 / 0)

except :
# except Exception:
# except 뒤에 Exception가 숨어 있음
# Exception은 모든 에러의 부모
    print('0으로 나눌 수 없습니다')


# 예제 4
datas = [1, 2, 3]

# datas의 인덱스 번호는 2까지 밖에 없기 때문에 에러
datas[3]
# 결과 값: IndexError 에러

try:
    datas[3]

# 위 오류는 IndexError 에러인데, ValueError를 받음 그래서 처리 불가
except ValueError:
    pass

finally:
    print('반드시 실행되어야 하는 문장')


# 예제 5
try:
    datas[3]

# except는 여러번 사용이 가능하다
except ValueError:
    pass

except IndexError:
    print('인덱스를 확인해 주세요!')

finally:
    print('반드시 실행되어야 하는 문장')

# 예제 5
try:
    datas[3]

# except는 여러번 사용이 가능하다
except ValueError:
    pass

except IndexError:
    print('인덱스를 확인해 주세요!')

# 오류가 발생하지 않았을 때
else:
    # try에 작성한 문장에서 오류가 발생하지 않는다면 실행된다.
    print('오류가 없어요!')


finally:
    print('반드시 실행되어야 하는 문장')


# 예제 6
# 근데 위 처럼 else를 사용하지 않아도 되는 이유가
# 오류가 없으면 try아래 바로 오류가 없다고 출력하게 하면 된다
try:
    datas[2]
    # 위의 문장에서 오류가 발생하지 않는다면 실행된다.
    print('오류가 없어요!')

# except는 여러번 사용이 가능하다
except ValueError:
    pass

except IndexError:
    print('인덱스를 확인해 주세요!')

finally:
    print('반드시 실행되어야 하는 문장')

#  -----------------------------------------------------------------------------------------------
오류확인
datas : {'A': 1}
print(datas['B'])
# 결과 값: NameError

# 에제 1
nickname = input('닉네임: ')
if nickname == '멍청이':
    # 오류가 나는 상황이 아닌데 오류처리를 하고 싶으면 raise 사용
    raise RuntimeError
    # 결과 값: RuntimeError


# 예제 2
# Exception을 부모 class로 받아서 BadWordError라는 class 생성:
class BadWordError(Exception):
    # class는 __str__으로 재정의:
    def __str__(self):
        # "비속어는 사용할 수 없습니다."를 리턴 값을 받음
        # Exception이 오류 값으로 들어가기 때문에 오류 발생 시
        return "비속어는 사용할 수 없습니다."

# 비속어를 검색할 수 있는 함수 선언 후 message를 매개 변수로 받기
def check_bad_word(message):
    # 만약 message에 '멍청이'라는 단어가 있으면
    if '멍청이' in message:
        # BadWordError라는 오류가 되도록 한다
        raise BadWordError

# input을 사용해 사용자 채팅을 입력하도록 하고, 입력한 값은 chat 변수를 선언하여 담는다
chat = input('채팅: ')

# 오류가 발생할 수 있는 문장 작성
try:
    # chat에서 받은 문자를 check_bad_word 함수로 비속어 검수
    check_bad_word(chat)
    # 오류가 없다면 chat 그대로 출력
    print(chat)
# 오류 발생 시 BadWordError를 실행
# BadWordError는 별칭을 e로 받는다:
except BadWordError as e:
    # 오류 발생 후 e 출력
    print(e)
# check_bad_word(chat)
# 비속어가 없으면 chat이 출력
