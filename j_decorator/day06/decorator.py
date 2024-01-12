# datetime라는 모듈은 이미 만들어져 있는 모듈
import datetime

# loge_time => 데코레이터 이름
# 데코레이터를 붙인 함수가 original_function으로 들어옴
def log_time(original_function):
    print('log_time 들어옴')

    # 클로저 만들기
    def logging(*args):
        # 화면에 잘 들어왔나 확인
        print('logging 들어옴')
        print(args)
        # datetime모듈을 사용해서 현재시간 출력
        print(datetime.datetime.now())
        print('logging 함수 종료')
        # logging의 리턴 값은 original_funtion의 매개변수 값
        return original_function(*args)

    print('log_time 함수 종료')
    return logging

# add함수가 로그타임에 들어가고
# 내가 사용한 함수가 데코레이터로 전달?
@log_time
# 데코레이터를 붙여줄 함수 선언
# add라는 함수 선언 후 매개변수를 *args 값으로 받아옴
def add(*args):
    # args 값의 모든 합을 구하기 위해
    # total 변수 선언 후 초기 값 0을 두기
    total = 0
    # args의 값을 i에 담아
    # total + i를 반복
    # 0 + 1 = 1, ..., 0 + 3 = 3
    # 담긴 total 값은 1, 2, 3이고 모두 합하기 = 6
    for i in args:
        total += i

    # add(1, 2, 3)함수의 리턴 값은 total 값인 6이 된다
    return total

# add(1, 2, 3)의 결과 값은 6
result = add(1, 2, 3)
# result 출력
print(result)
# 결과 값: 6



# 평균을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다. args
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다. kwargs
# 총 합을 구하는 함수(=메인로직)를 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.

def average(original_function):
    def operate(*args, **kwargs):
        count = len(args)
        if count != 0:
            pass
        else:
            pass
        print("평균: ")


@average
def set_datas(*args, **kwargs):
    total = 0
    for i in args:
        total += 1

    return total

    # print("총 합: ")


result = set_datas(1, 2, 3, 4, 5)
print(result)
set_datas(total=100, count=5)


# 정리
def average(original_function):
    def operate(*args, **kwargs):
        count = len(args)
        if count != 0:
            total = 0
            for i in args:
                total += i

        else:
            total = kwargs.get('total')
            count = kwargs.get('count')

        print(f"평균: {total / count}")

        return original_function(*args, **kwargs)

    return operate


@average
def set_datas(*args, **kwargs):
    total = 0
    for i in args:
        total += i
    print(f"총 합: {total if total != 0 else kwargs.get('total')}")


set_datas(1, 2, 3, 4, 5)
set_datas(total=100, count=5)
