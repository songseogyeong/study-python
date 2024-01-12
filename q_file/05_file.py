# 절대 경로: 대한민국 서울시 강남구 역삼동 123-123 103동 203호
# 어떤 위치에 있든 상관 없이 찾아갈 수 있는 경로
# C:/a/b, D:/user/ted,....
# 처음부터 찾아 가는 경로

# 상대 경로 : 직진해서 좌회전 후 오른쪽 건물
# 현재 위치에 따라 변경 되는 경로
# ./ : 현재 경로
# (예시) ./scr/images
# ../: 이전 경로(뒤로가기)
# (예시) ../../a/b


# 파일 생성하기
# 상대경로 앞에 ./ 가 생략됨
# 운영체제에 맞게 인코딩을 해줘야지 글씨가 안깨져 나옴
file = open('food.txt', 'w', encoding='utf-8')
# open('w') 하면 안에 있는 바이트를 다 0으로 만들고 가져오기 때문에
# 안에 있는 내용이 다 날라감
# 들어갈 내용 작성
file.write('부대찌개\n')
# 파이썬은 write를 하면 플로시가 됨
file.write('햄버거\n')
# 파일 닫기
file.close()
# close로 닫아주지 않으면, 파일이 계속 열려있어서 이름 수정 같은 게 안됨


# 파일 추가하기
# 파일이 있으면 추가로 입력
# 파일이 없으면 파일 새로 생성 후 입력
file = open('food.txt', 'a', encoding='utf-8')
file.write("피자\n")
file.close()


# 파일 읽기
file = open('food2.txt', 'r')
# 결과 값: FileNotFoundError

예제1
try:
    file = open('food.txt', 'r', encoding='utf-8')
    print(file.readlines())
    # 결과 값: ['부대찌개\n', '햄버거\n', '피자\n']
    for i in range(4):
        print(file.readline(), end='')
        # 결과 값:
        # 부대찌개
        # 햄버거
        # 피자

    line = None
    while line != '':
        line = file.readline()
        print(line, end='')
        # 결과 값:
        # 부대찌개
        # 햄버거
        # 피자

except FileNotFoundError:
    print('경로를 다시 확인해 주세요.')

# with문은 객체를 쓰고 file이라는 별칭에 담는다
# with문은 exit부분에서 자동으로 close가 됐기 때문에
# with를 사용하면, 자동으로 file이 close된다.
with open('food.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())
