# # 모양 문제 (상속 예제)
# # 1. 부모 클래스: 모양
# # 메서드: 각 모서리의 갯수
# # 삼각형
# # 사각형
# # 오각형
# # 육각형
#
# class Shape:
#     def __init__(self, name, corner):
#         self.name = name
#         self.corner = corner
#
#     def corner(self):
#
#
# # 각 자식 클래스에 상속, 값 오버라이딩
# # 2.각 도형의 크기 구하기 메소드 추가(변의 길이는 입력받기)
# class Size:
#     def __init__(self, name, corner, high, leght):
#         super().__init__(name, corner)
#         self.high = high
#         self.leght = leght
#
#     def three_corners(self):
#         result = (self.hight * self.leght) / 2
#         return result
#
#




# ------------------------------------------------------------------------
# - 기본 출연료: 100000원
# - 기본 출연 시간: 1시간
# - 1시간 초과 당 : 50000원

# TV 프로그램
class Program:
    default_pay = 100000
    default_hour = 1
    add_pay = 50000

    # 1. 프로그램 이름,  유형(예능, 다큐 등..), 방송 분량(시간 단위), 출연자 수
    def __init__(self, name, type, hour=1):
        self.name = name
        self.type = type
        self.hour = hour
        self.cast_count = 0

    # 2. TV 프로그램 정보 출력 메소드
    def print_info(self):
        print(self.name, self.type, self.hour, self.cast_count)

#출연자
class Cast:

    # 1. 이름, 나이, 직업(코미디언, 가수, 배우 등..), 출연료, 출연프로그램
    def __init__(self, name, age, job, program, pay):
        self.name = name
        self.age = age
        self.job = job
        self.program = program
        self.pay = pay
        # 2. 출연자가 추가될 때 마다 출연자 수 1증가
        self.program.cast_count +=1

    # 3. 방송 분량에 따른 출연료 계산 메소드 정의
    def pay(self):
        self.pay += Program.default_pay + (self.program.hour * Program.add_pay)
        # cost = Program.default_pay
        # if Program.hour > Program.default_hour:
        #     cost += Program.default_pay + (self.program.hour * Program.add_pay)
        # return cost

    def print_info(self):
        print(self.name, self.age, self.job, self.pay)

    # 4. 출연자는 인당 1개의 프로그램에만 참여할 수 있음

program = Program('라디오스타', '예능', 2)
cast = Cast('정재현', '28', '가수', program)

program.print_info()
cast.print_info()




# # -----------------------------
# # 부모 클래스: 책
# # 자식 클래스: 만화책, 문제집
#
# # 만화책
# # 추가 인자 - 장르
# # 메소드 - 챕터 수를 입력받고, 전체 페이지 수에 따른 챕터 하나 당 페이지 수 구하기
# # 각 챕터의 페이지 수는 모두 같으며, 결과를 정수형으로 반환
#
# # 문제집
# # 추가 인자 - 과목
# # 메소드 - 공부한 페이지 수를 입력받고, 남은 페이지 수 구하기
# # 단, 남은 페이지 수는 다음에 이 메소드를 또 호출할 경우 이어서 적용됨
# # 그리고 만약 끝까지 다 풀었을 경우, 과목 이름 + "~문제집을 다 풀었다!" 메세지 출력'
#
# # 부모 클래스: 책
# class Book:
#     # 페이지수
#     def __init__(self, page):
#         self.page = page
#
# # 자식 클래스: 만화책, 문제집
#
# # 만화책
# # 추가 인자 - 장르
#
# class Comic(Book):
#     def __init__(self, page, name, chapter):
#         super().__init__(page)
#         self.chapter = chapter
#         self.name = name
#         self.chapter_page = 0
#
#     # 메소드 - 챕터 수를 입력받고, 전체 페이지 수에 따른 챕터 하나 당 페이지 수 구하기
#     # 각 챕터의 페이지 수는 모두 같으며, 결과를 정수형으로 반환
#     def chapter_page(self):
#         # 전체 페이지 / 챕터수 = 챕터 하나 당 페이지 수 구하고 chapter_page에 값 넣기
#         # int로 형변환
#         self.chapter_page += int(self.page / self.chapter)
#         return self.chapter_page
#
#     def print_info(self):
#         print(self.name, self.page, self.chapter, self.chapter_page)
#
# Comic.print_info()
#
# # 문제집
# # 추가 인자 - 과목
# # 메소드 - 공부한 페이지 수를 입력받고, 남은 페이지 수 구하기
#
# # 그리고 만약 끝까지 다 풀었을 경우, 과목 이름 + "~문제집을 다 풀었다!" 메세지 출력'
# class workbook(Book):
#     def __init__(self, page, name, study):
#         super().__init__(page)
#         self.page = page
#         self.name = name
#         self.study_page = study
#
#     def study_page(self):
#         self.study_page += self.page - self.study
#         if self.study_page == 0:
#             print(f'{name} 문제집을 다 풀었다!')
#
#     # 단, 남은 페이지 수는 다음에 이 메소드를 또 호출할 경우 이어서 적용됨
#     @classmethod
#     def other_page(cls):
#


