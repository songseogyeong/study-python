# 실습 1 클로저 만들기
user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},
]

# 추가
# 회원 번호는 자동 증가한다.
number = 5

# set_user함수 선언, 사용 시 매개 변수 입력
def set_user():

    # insert함수를 선언하고 매개변수를 name으로 받기
    def insert(name):
        # 클로저에서도 전역 변수 global 사용 가능
        # 전역 변수 number를 global을 통해 연결
        global number
        # user_info에 name의 value 값을 추가하면, number가 1씩 증가
        number += 1
        user_info.append({'number': number, 'name': name})


    # 목록
    # select_all 함수 선언, 모든 값을 조회하기 때문에 매개변수 비워두기(특정한 키 값으로 조회하는 게 아님)
    def select_all():
        # user_info를 리턴 값으로 지정해서 select_all 자체가 user_info가 됨
        # select_all를 print하면 user_info가 그대로 출력
        return user_info


    # 조회(번호로 조회)
    # select를 함수로 선언하고 number를 매개 변수로 받음
    def select(number):
        # user_info를 user에 넣어서 가져오는데,
        # user(=user_info)에서 'number' 키 값의 value가 매개변수 number인 값만 가져오고
        # 이 결과 값을 user의 return 값으로 받는다

        for user in user_info:
            if user['number'] == number:
                return user
        # user를 못찾았을 때 return값이 {}가 된다
        return {}


    # 수정(번호로 이름 수정)
    def update(**kwargs):
        '''

        :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
        '''
        select(kwargs.get('number'))['name'] = kwargs.get('name')


    # 삭제(번호로 삭제)
    def delete(number):
        del user_info[user_info.index(select(number))]

    return {'insert': insert, 'select_all': select_all, 'select': select, 'update': update, 'delete': delete}

user_service = set_user()
# 아래는 주소값, 주소값에 접근해서 안에 있는 소스 코드를 읽을 거임

# 추가 사용
user_service.get('insert')('han')
# insert() <하면 어디 서비스에 접속해 있는지 모르기 때문에 user_service.get('insert') 이렇게 풀어줌

# 전체 조회 사용
print(user_service.get('select_all')())

# 조회 사용
# select에서 6번 조회
print(user_service.get('select')(6))

# 업데이트 사용
print(user_service.get('update')(number=6, name='song'))
print(user_service.get('select')(6))


# delete 사용
print(user_service.get('delete')(6))
print(user_service.get('select')(6))


# ----------------------------------------------------------------------------------------------------------------------
# 실습2
post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]


# 전역변수
number = 5

def post():

    # 추가(조회수는 전달받지 않고 기본값 0으로 설정)
    def insert(**kwargs):
        '''

        :param kwargs: {'title': '게시글 제목', 'content': '게시글 내용', 'file': '파일의 경로'},
        :return:
        '''
        global number
        number += 1
        post = {
            'number': number,
            'title': kwargs.get('title'),
            'content': kwargs.get('content'),
            'file': kwargs.get('file'),
            'read_count': 0
        }
        post_info.append(post)


    # 목록(최신순으로 조회)
    def select_all():
        return post_info[::-1]


    # 조회(번호로 조회, 조회수 1 증가)
    def read(number):
        post = select(number)
        post['read_count'] += 1
        return post


    def select(number):
        for post in post_info:
            if post['number'] == number:
                return post

        return {}


    # 수정(번호로 정보 수정)
    def update(**kwargs):
        post = select(kwargs.get('number'))
        post['title'] = kwargs.get('title')
        post['content'] = kwargs['content']
        post['file'] = kwargs.get('file')


    # 삭제(번호로 삭제)
    def delete(number):
        del post_info[post_info.index(select(number))]

    return {'insert': insert, 'select_all': select_all, 'read': read, 'select': select, 'update': update, 'delete': delete}


# insert(title='테스트 제목6', content='테스트 내용6', file='')
# print(select_all())
# print(read(5))
# print(read(5))
# print(read(5))
# post = read(5)
# post['title'] = '수정된 제목'
# update(**post)
# print(read(5))
# delete(5)
# print(select_all())

post_service = post()
post_service.get('insert')('테스트 제목7')
print(post_service.get('select')(7))

# ----------------------------------------------------------------------------------------------------------------------
def post(*args):
    number = 5

    for post_info in args:
        number += 1
        product['number'] = number

    # 추가
    def insert(**kwargs):
        global number, args
        number += 1

        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},