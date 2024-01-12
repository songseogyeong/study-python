def discount(*args, **kwargs):
    coupon, count = kwargs.get('coupon'), kwargs.get('count')
    return [int(args[i] - args[i] * coupon/100) if i < count else args[i] for i in range(len(args))]

print(discount(2000, 4000, 5000, coupon=50, count=2))