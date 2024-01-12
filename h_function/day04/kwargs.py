# keyword arguments
# print(1, 2, sep='\n')
#1, 2가 패킹, sep부분이 키워드

def introduce(**intro):
    print(intro)
    print(type(intro))
    print(f'name: {intro["name"]}')

info_dict = {
    'name': '한동석'
}

introduce(name='한동석')
introduce(**info_dict)


# 주문 총 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs):
    total = 0
    for i in args:
        total += i

    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')


order_info(3000, 2000, 1000, name='한동석')



# 실습1
# 국어, 영어, 수학 점수의 평균 구하기
# kwargs를 사용
def score_info(**score):
    total = 0
    for score in score:
        total = score % len(score)
    return total

print(score_info(kor = 90, eng = 80, math = 70))

# 실습1 정리1
def average(**kwargs):
    kor = kwargs['kor']
    eng = kwargs['eng']
    math = kwargs['math']
    return (kor + eng + math) / 3


print(average(kor=100, eng=30, math=22))



실습2
국어, 영어, 수학 점수의 평균 구하기
사용자가 원하는 자리수(round)에서 반올림해준다.
자리수를 받지 않았다면, 기본값을 리턴한다.
def average(**kwargs):
    kor = kwargs['kor']
    eng = kwargs['eng']
    math = kwargs['math']
    return (kor + eng + math) / 3

ave_result = average(kor=100, eng=30, math=22)
result = f'{ave_result:.2f}'
print(result)

정리2
def average(**kwargs):
    kor, eng, math = kwargs.get('kor'), kwargs.get('eng'), kwargs.get('math')
    total = kor + eng + math
    avg = total / 3

    if "round" in kwargs:
        return round(avg, kwargs['round'])

    return avg

print(average(kor=100, eng=30, math=22, round=3))

반드시 key와 함께 사용하고자 할 때에는 매개변수의 시작을 *로 한다.
def average(*, kor, eng, math):
    return (kor + eng + math) / 3


print(average(kor=100, eng=30, math=22))



# ''' ''' 사용
# ''' + enter + ''' 시 자동으로 정보를 입력할 수 있는 칸이 나옴
# 주문 총 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs):
    '''
    주문 총 가격과 주문한 회원의 정보 출력
    :param args: 주문 가격들
    :param kwargs: 회원의 정보
    '''
    total = 0
    for i in args:
        total += i

    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')


help(order_info)


++==
# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# packing으로 제작하기
# ※ 추가로 사용자에게 국어, 영어, 수학 뿐만 아니라 추가로 입력받은 모든 점수를 합하여 출력

def get_total(*scores):  # 반드시 받아야하는 매개 변수는 packing 앞에 작성한다.
    total = 0


    for score in scores:
        total += score

    return total


# print(type(scores))
message = '합산할 정수 입력: '
score = map(int, input(message).split(', '))
result = get_total(*score)
print(result)