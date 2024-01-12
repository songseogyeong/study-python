# def order_info(*args, **kwargs):
#     # 튜플인 args의 값을 list로 형 변환
#     pay_list = list(args)
#     # 결과 값: [2000, 4000, 5000]
#     # coupon, count 값을 입력 받기
#     coupon, count = kwargs.get('coupon'), kwargs.get('count')
#
#     # pay_list에 있는 0번째 값~count(쿠폰개수)번째까지 출력
#     # print(pay_list[:count])
#     # 결과 값: [2000, 4000]
#     # cut에 할인율 적용 값 보내주기
#     cut = pay_list[:count]
#
#     # pay_list를 pay에 담고 pay의 0번째 값~count번째 값에 해당하면 할인율 적용해주기, 아니면 적용 X
#     result = [int(pay - (pay * (coupon / 100))) if cut == 0 else pay for pay in pay_list]
#
#     # 값 출력
#     print(result)
#
# order_info(2000, 4000, 5000, coupon=20, count=2)


# 정리
def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:
        return [
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            for i in
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None


help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=100)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')
