class Student:
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math



    # self를 쓰지 않을 때는 매개 변수에서 self를 지워도 됨
    # 모든 학생들에게 공통적으로 적용하기 때문에 객체로 접근하지 않아도됨(한번에 문장을 실행하자!)
    @staticmethod
    # 데코레이터가 먼저 실행
    # 해당 함수가 전달
    def print_start_time_of_study():
        # 객체로 접근하는 게 아님
        # 객체로 접근할 필요가 없으면 데코레이터로 메소드로 선언
        print('9시 땡')
        Student.status = '공부 중'

hen = Student(0, 0, 0)
hong = Student(0, 0, 0)
print(Student.status)

Student.print_start_time_of_study()
print(Student.status)

