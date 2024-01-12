# 대게 선언은 아래처럼 함
a = 10
b = 20
c = 30

print(a, b, c, sep=', ')


# 여러개의 변수를 한 줄에 선언 1
# 성능이 올라감
a = 10; b = 20; c = 30

print(a, b, c, sep=', ')


# 여러개의 변수를 한 줄에 선언 2
a, b, c = 10, 20, 30
print(a, b, c, sep=', ')
# 튜플 때문에 가능
# (a, b, c = 100, 200, 300) > 소괄호 생략된 것


# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)


# 방법 1
a = 11
b = 33

temp = a
a = b
b = temp

print(a, b)
a=b
b=a
# 하면 a랑 b둘 다 33 나오니까 temp라는 새로운 선언
# a=b 하면 a값이 33으로 변경되니까, a값인 11을 temp에 저장해준다고 생각하면 됨


# 방법 2
# a는 b값인 33이 되고, b는 a값인 11이 되고
a = 11
b = 33

a, b = b, a
print(a, b)


# 동적 바인딩
# int
a = 10
print(type(a))

# float
a = 10.5
print(type(a))

# str
a = 'A'
print(type(a))

# str
a = "ABC"
print(type(a))

# list
# 변수는 하나만 들어갈 수 있음
# 대괄호는 리스트
a = ['A', 'B', 'C']
print(type(a))

# dict
a = {'A': 1, 'B': 2, 'C': 3}
print(type(a))

# bool
a = True
a = 5 > 2
print(type(a))
True = 1 = 참
False = 0 = 거짓


# 변수명 주의사항
age = 10
print(type(age))

number = 10.5
print(type(number))

center = 'A'
print(type(center))

data = "ABC"
print(type(data))

course = ['A', 'B', 'C']
print(type(course))

Level = {'A': 1, 'B': 2, 'C': 3}
print(type(Level))

condition = True
condition = 5 > 2
print(type(condition))


# 서식문자
name = '한동석'
print("이름 : %s" % name)

name = '한동석'
print("이름 : %s" % 'ABC')
가능!

# 5의 경우에는 5의 앞자리가 홀수인 경우에 올림을 하고 짝수인 경우에 버림을 하여 짝수로 만들어 준다.
# 예를 들어 53.45는 53.4로, 32.75는 32.8로 반올림한다.
# 이를 오사오입(round-to-nearest-even) 이라고 한다.
name = '한동석'
age = 20
height = 157.55
height2 = 157.45

print("이름 : %s" % name)
print("나이 : %d" % age)
print("키 : %f" % height)
print("키 : %.1f" % height)
print("키 : %.1f" % height2)
# %f하면 소수점 6자리까지 나오고 7자리부터 정확 X
# % + . + 원하는 소수점 자릿수 + f

name = '한동석'
age = 20
height = 157.55
height2 = 157.45

print("이름 : %s\n나이 : % d살\n키: %.1fcm" % (name, age, height))


# -------------------------------

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4
number1 = 1
number2 = 3
add_number = number1+number2

print('{} + {} = {}'.format(number1, number2, add_number))

# -------------------------------

# format 함수
name = '홍길동'
age = 80
height = 156.26

print('이름 : {}\n나이 : {}\n키 : {}'.format(name, age, height))


# 문자열로 연산해서 딱 작성한 자릿수까지나옴
# 그래도 첫번째 자릿수까지 쓰고 싶다면 :.숫자f
name = '홍길동'
age = 80
height = 156.26

print('이름 : {}\n나이 : {}\n키 : {:.1f}'.format(name, age, height))


# 리스트
# 리스트의 순서를 작성, 리스트는 0부터 시작
name = '홍길동'
age = 80
height = 156.26

print('이름 : {0}\n나이 : {1}\n키 : {2:.1f}'.format(name, age, height))


# 딕셔너리
# 키 값을 정해줌
name = '홍길동'
age = 80
height = 156.26

print('이름 : {name}\n나이 : {age}\n키 : {height:.1f}'.format(name=name, age=age, height=height))

# -------------------------------
# format은 전체가 문자열 값
name = '홍길동'
age = 80
height = 156.26

formatting1 = '이름 : {}\n나이 : {}\n키 : {:.1f}'.format(name, age, height)
formatting2 = '이름 : {0}\n나이 : {1}\n키 : {2:.1f}'.format(name, age, height)
formatting3 = '이름 : {name}\n나이 : {age}\n키 : {height:.1f}'.format(name=name, age=age, height=height)

print(formatting1)
print(formatting2)
print(formatting3)

# -------------------------------
name = '한동석'
age = 20
height = 157.55

print("=" * 20)
formatting = "이름 : %s\n나이 : % d살\n키: %.1fcm" % (name, age, height)
print(formatting)
print("=" * 20)

# -------------------------------
# 실습
# 아래 메세지를 format 함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic
# Hello 장고, Django is fantastic
# Hello 리액트, React is fantastic

python = '파이썬'
django = '장고'
react = '리액트'

print('Hello {}, Python is fantastic\nHello {}, Django is fantastic\nHello {}, React is fantastic'.format(python, django, react))

# -------------------------------

# format string
name = '한동석'
age = 20
height = 157.55

# round(실수값, 반올림 자리수)
print(f'이름 : {name}')
print(f'나이 : {age}살')
print(f'키 : {round(height, 1)}cm')

# -------------------------------
# 실습 - F스트링을 써서 해보기
# 아래 메세지를 format 함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !
# -------------------------------

python = '파이썬'
django = '장고'
react = '리액트'

print(f'Hello {python}, Python is fantastic !')
print(f'Hello {django}, Django is fantastic !')
print(f'Hello {react}, React is fantastic !')