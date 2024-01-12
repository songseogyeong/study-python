# # 개발자는 CRUD 한다
#
# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
#
# # # 추가
# # # 초보자용 예제
# # def insert(*, number, name):
# #     '''
# #
# #     :param number: 회원 번호
# #     :param name: 회원 이름
# #     '''
# #     # 수정은 user_info = []가 되어야 한다.
# #     # 그래서 아래는 수정이 아닌 사용이고 global을 사용하지 않아도 된다.
# #     user_info.append({'number': number, 'name': name})
# #
# # insert(number=6, name='hong')
# # print(user_info)
#
# # 회원 번호는 자동 증가한다.
# number = 0
#
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': name})
#
#
# # 목록
# def select_all():
#     return user_info
#
#
# # 조회(번호로 조회)
# def select(number):
#     for user in user_info:
#         if user['number'] == number:
#             return user
#     return {}
#
#
# # # 수정(번호로 이름 수정)
# # def update(*, name, number):
# #     global user_info
# #     user_info[number] = [{'name': name}]
# #     # user_info[{'number': number, 'name': name}]
# #
# # update(number=6, name='jea')
# # print(user_info)
#
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#     '''
#     # print(select(kwargs.get('number'))['name'])
#     # print(kwargs.get('name'))
#     select(kwargs.get('number'))['name'] = kwargs.get('name')
#
# updata(number=1, name='han')
# print(select_all())
#
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]
#
# delete(1)
# print(select_all())
# insert(name='hong')

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]


# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
# 전역변수
# 현재 게시글이 5개가 있으므로 number = 0을하지 않고 number = 5
number = 5

# insert 함수에 매개변수 넣어주고 read_count의 초기 값을 0으로 두기
def insert(title, content, file, read_count=0):
    # 전역변수 number를 지역변수로 가져오기
    global number
    # number에 카운트 +1씩 해주기
    number += 1
    # post_info에 추가[{키 값(매개변수 뭔지 표시): 입력값}]
    post_info.append({'number': number, 'title': title, 'content': content, 'file': file, 'read_count': read_count})

# 추가할 내용 작성
insert(title='테스트 제목6', content='테스트 내용6', file='/usr/post/file/img006.png')
# post_info 출력
print(post_info)

# 추가 정리
number = 5
# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
# insert 함수에 kwargs라는 매개값을 주
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

print(select_all())



# 조회(번호로 조회, 조회수 1 증가)
def select(number):
    for view in post_info:
        view['read_count'] += 1 #분리해 주는 게 좋음! 조회 후 삭제 수정이 일어나는데 버그가 일어날 수 있어서...
        # 만약 그 포스트 넘버랑 넘버랑 같으면
        if view['number'] == number:
            # 그 포스트가 필요해
            return view
    # return 시 none이 나올 수 있도록 해줌
    return {}

print(select(1))
print(select(1))

# 조회 정리
def read(number):
    post = select(number)
    post['read_count'] += 1
    return post

def select(number):
    for post in post_info:
        if post['number'] == number:
            return post

    return {}



# 조회 함수 로직 그대로 복붙한 다음, 조회수 증가시키는 부분만 삭제
# 위에서 만든 검색 함수를 수정, 삭제 함수 내에서 사용
# 두 함수 모두 검색한 다음, 그 반환 값을 가지고 로직을 실행하는 거라서
# 공통 기능을 함수로 만들어서 빼기?


# 수정(번호로 정보 수정)
def updata(number):
    for view in post_info:
        view[number] = [{'title': title, 'content': content, 'file': file}]
        if view['number'] == number:
            return view
    return {}

updata(number=6, title='제목 수정', content='내용 수정', file='파일 수정')
print(post_info)

 # 수정 정리
def update(**kwargs):
    post = select(kwargs.get('number'))
    # 직접 '타이틀'이라는 주소로 접근을 해서 '타이틀'값을 가져옴
    post['title'] = kwargs.get('title')
    post['content'] = kwargs['content']
    post['file'] = kwargs.get('file')

# 수정하는 페이지로 접근
post = read(5)
# 타이틀만 수정
post['title'] = '제목 수정'
# 형식이 딕셔너리이기 때문에 **을 붙여서 형식을 맞춰줘야함
updata(**post)

# 삭제(번호로 삭제)
def delete(number):
    del post_info[post_info.index(select(number))]


insert(title='테스트 제목6', content='테스트 내용6', file='')
print(select_all())
print(read(5))
print(read(5))
print(read(5))
post = read(5)
post['title'] = '수정된 제목'
update(**post)
print(read(5))
delete(5)
print(select_all())
