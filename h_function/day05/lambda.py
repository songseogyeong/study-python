# 람다(lambda): 이름이 없는 함수(익명함수), 일회성
# lambda 매개변수, ...: 리턴값

# 일반 함수
def add(number1, number2):
    return number1 + number2

# 익명 함수
lambda number1, number2 : number1 + number2

# 값을 다 불러옴(사용하는 것)
add()

# 코드가 어디있는지 주소값 자체
add

# 사용예시
print(list(map(lambda number: number + 2, [1, 2, 3, 4])))
# 결과 값: [3, 4, 5, 6]
# 리턴 값 없으면 람다 안 씀!


# 실습1
# 아래의 list의 각 요소에 2를 곱하여 변경
datas = [2, 4, 6, 8]

# map은 뒤에 있는 요소가 앞에 있는 함수에 적용되도록 사용
# lambda라는 익명함수에 있는 매개변수 number에 datas의 값의 요소가 하나하나 들어감
# 그래서 return으로 number + * 를 해주면
# 2*2, 4*2 ... 이런식으로 됨
# 나온 값은 list에 다시 담아서 출력
print(list(map(lambda number: number * 2, datas)))
# 결과 값: [4, 8, 12, 16]


# 실습2
# 각 경로 앞에 '/app'를 붙여준다.
# '/app/game', '/app/news', '/app/fashion', '/app/ranking'
urls = ['/game', '/news', '/fashion', '/ranking']

print(list(map(lambda url: '/app' + url, urls)))
# 결과 값: ['/app/game', '/app/news', '/app/fashion', '/app/ranking']

# 실습2 정리
print(list(map(lambda url: f'/app{url}', urls)))

# filter(function, iterator)
# 1~10까지 중 짝수만 출력
print(list(filter(lambda number: number % 2 == 0, [i + 1 for i in range(10)])))

# ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
# 'game' 서비스를 제공하는 경로 찾기
urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']

print(list(filter(lambda url: url.split('/')[-1] == 'game', urls)))