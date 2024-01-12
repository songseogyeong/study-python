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