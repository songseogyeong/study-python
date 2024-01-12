# # set_key안에 set_value 함수 선어
# def set_key(key):
#     # 지역변수
#     formatting = ''
#
#     # 클로저: 함수 안에 함수 선언
#     def set_value(value):
#         # 아래는 사용이 아니라 수정을 했기 때문에 global 같은 nonlocal을 사용해서 formatting을 연결
#         # read는 그냥해도 됨 writing하려면 global함수 써야함
#         nonlocal formatting
#         formatting = f'{key}: {value}'
#         # set_value(value) = formatting이라는 리턴 값 설정
#         return formatting
#
#     # set_key(key) = set_value라는 리턴 값 설정
#     return set_value
#
# # '이름'은 set_key에 들어감
# set_name = set_key('이름')
# # 클로저 함수
# # set_value에 들어감
# formatting = set_name('한동석')
#
# print(formatting)
# # 결과 값: 이름: 한동석
#
# formatting = set_key('이름')('한동석')
# print(formatting)
#
#
# # 실습 1
# # '나이: 00살'
# def set_key(key):
#     formatting = ''
#
#     # 클로저
#     def set_value(value):
#         nonlocal formatting
#         formatting = f'{key}: {value}'
#         return formatting
#
#     return set_value
#
# set_name = set_key('이름')
# formatting_name = set_name("한동석")
# print(formatting_name)
#
# # '나이: 00살'
# set_name = set_key('나이')
# formatting_age = set_name("20살")
# print(formatting_age)
#
# print(f'{formatting_name}\n{formatting_age}')


# # 실습2
# # 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# # 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# # 함수1. "name, 전달받은 이름"
# # 함수2. "전달받은 주제, 전달받은 요약"
# # 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# # 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# # 구분점은 각 함수에서 전달받는다.
#
# # set_topic이라는 함수에 kwargs를 매개변수로 받기
# def set_topic(**kwargs):
#     # result = 0
#     # 만약 lwargs가 name이라는 key에 값으로 들어가면,
#     if 'name' in kwargs:
#         # 클로저 함수를 다시 선언 매개변수 sep의 초기 값은 ', '
#         def set_format(sep=', '):
#             # formatting 변수 선언 = f'name{구분점} {kwargs에서 가져온 name값}'
#             formatting = f'name{sep}{kwargs.get("name")}'
#             # set_format() = formatting 리턴 값을 받아줌
#             return formatting
#         # result에 set_format 함수를 담기
#         # set_format에는 리턴값이 formatting이니까
#         # kwargs가 name이라는 키 값에 들어가면 formatting형식으로 들어가게 되는 것
#         result = set_format
#
#     # 그게 아니라면,
#     else:
#         # 클로저 함수를 다시 선언 매개변수 sep의 초기 값은 ', '
#         def set_format(sep=', '):
#             # formatting 변수 선언 = f'{kwargs에서 가져온 topic 값}{구분점} {kwaargs에서 가져온 point값}'
#             formatting = f'{kwargs.get("topic")}{sep}{kwargs.get("point")}'
#             # set_format() = formatting 리턴 값을 받아줌
#             return formatting
#
#         # result에 set_format 함수를 담기
#         # set_format에는 리턴값이 formatting이니까
#         # kwargs가 name이라는 키 값에 들어가지 않으면 formatting형식으로 들어가게 되는 것
#         result = set_format
#
#     # set_format의 return 값을 받아 set_topic의 리턴 값으로 지정
#     return result
#
#
# print(set_topic(name='한동석')(': '))
# print(set_topic(topic='지구 온난화', point='오존층 파괴를 막기 위해 인간이 해야할 일')("\n"))


# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

# # 실습
# product_info = []
#
# # 상품 정보를 여러개 전달 받아 product info에 저장
# def set_product(name, price, number = 0):
#     global product_info
#     number += 1
#     add = product_info.append({'number': number, 'name': name, 'price': price})
#
#
# set_product(name='과자', price=3000)
# set_product(name='과일', price=5000)
# print(product_info)

# 정리
# args는 튜플인데 튜플 안에 딕셔너리 있음
# sete_product 함수에 매개 변수 값을 args를 모두 다 가져오기:
def set_product(*args):
    # 값 추가 시 number에 번호를 하나씩 증가해줘야 하기 때문에
    # number에 초기값 0을 둔다
    number = 0

    # 반복
    # args 값을 product에 넣을 때 마다
    for product in args:
        # number가 1씩 증가한다
        number += 1
        # number의 값은 product 속 'number' 키 값에 저장된다
        product['number'] = number

    # 추가
    # insert 함수를 선언후 kwargs(딕셔너리)를 매개변수로 받아옴
    def insert(**kwargs):
        nonlocal number, args
        number += 1

        # args에 통채로 다른 튜플을 넣음
        # 그래서 nonlocal에 args 넣어야함
        # 어펜트는 list에서 사용 튜플이라 연결해서 넣어줌
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},


    def update(**kwargs):
        # args는 사용임 args에서 받은 것들을 product에서 확인함
        for product in args:
            if product['number'] == kwargs.get('number'):
                product['name'] =kwargs.get('name')
                product['price'] = kwargs.get('price')
                break

    def select_all():
        return args

    # 딕셔너리로 전달해야 사용자가 정확하게 알 수 있음
    return {'insert': insert, 'update': update, 'select_all': select_all}

product = [
    {'name': '마우스', 'price': 5000},
    {'name': '키보드', 'price': 25000}
]

# product_service는 딕셔너리
# data= [1, 2, 3]
# print(*data)
# 앞에 *을 붙이면 리스트에 담겨져 있던 값이 각각 들어감
product_service = set_product(*product)
print(product)

product_service.get('insert')(name='모니터', price=8000)
print(product_service.get('select_all')())

product_service.get('update')(name='키보드', price=5000, number=2)
print(product_service.get('select_all')())




원래 함수 [1, 2, 3]
클로저 [[1, 2], [3]]
클로저[0]
클로저.get(0)