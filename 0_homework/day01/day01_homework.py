# 실습 1
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4
number1 = 1
number2 = 3
add_number = number1 + number2

print('%d + %d = %d' % (number1, number2, add_number))


# 정리
number1 = 1
number2 = 3
add_number = number1 + number2
formatting = '%d + %d = %d' % (number1, number2, add_number)
#  '%d + %d = %d' % (number1, number2, add_number) 은 문자열이기 때문에 formatting에 넣어 정리

print(formatting)



# 실습 2
# 아래 메세지를 format 함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !

python = '파이썬'
django = '장고'
react = '리액트'
formatting = 'Hello {}, Python is fantastic !\nHello {}, Django is fantastic !\nHello {}, React is fantastic !'.format(python, django, react)

print("=" * 20)
print(formatting)


# 정리
python_kor, python_eng = '파이썬', 'Python'
django_kor, django_eng = '장고', 'Django'
react_kor, react_eng = '리액트', 'React'
# 클래스 안에는 함수가 있음

# 자동으로 해당 순서에 값이 반영된다.
python_formatting = 'Hello {}, {} is fantastic !'.format(python_kor, python_eng)

# 값에 할당된 번호를 작성하면 해당 값이 반영된다.
django_formatting = 'Hello {0}, {1} is fantastic !'.format(django_kor, django_eng)

# 값에 이름을 붙이면 해당 이름에 있는 값이 반영된다
react_formatting = 'Hello {kor}, {eng} is fantastic !'.format(kor=react_kor, eng=react_eng)
# python_formatting ... > 자료구조

print(python_formatting, django_formatting, react_formatting, sep='\n')
# \n은 제어문자




# 실습 3
# 포맷 스트링을 써서 해보기
# 아래 메세지를 format 함수를 사용하여 출력한다.
# Hello 파이썬, Python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !

python = '파이썬'
django = '장고'
react = '리액트'

print("=" * 20)
print(f'Hello {python}, Python is fantastic !')
print(f'Hello {django}, Django is fantastic !')
print(f'Hello {react}, React is fantastic !')
print("=" * 20)

# 정리
python_kor, python_eng = '파이썬', 'Python'
django_kor, django_eng = '장고', 'Django'
react_kor, react_eng = '리액트', 'React'

python_formatting = f'Hello {python_kor}, {python_eng} is fantastic !'
django_formatting = f'Hello {django_kor}, {django_eng} is fantastic !'
react_formatting = f'Hello {react_kor}, {react_eng} is fantastic !'

print(python_formatting, django_formatting, react_formatting, sep='\n')