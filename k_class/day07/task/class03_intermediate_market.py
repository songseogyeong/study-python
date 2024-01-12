# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.

# 손님
# 이름, 나이, 할인율, 잔액

# 상품
class Product:
    # 상품명, 가격
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 상품의 정보를 print()로 출력하는 함수
    def product_info(self):
        print(self.product, self.price)

# product_list = [Product, Product]
# apple_product = product_list[0]('apple', 1000)
# banana_product = product_list[1]('banana', 3000)
#
# apple_product.product_info()
# banana_product.product_info()


# 손님
# 손님을 먼저해야 쉽다. 마켓에서 손님을 받아야 하기 때문
class Customer:
    # 이름, 나이, 할인율, 잔액
    def __init__(self, name, age, discount=0, money=0):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money

# 마켓
class Market:
    # 상품, 재고
    # 상점을 먼저 열고
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    # 손님이 오면 그 때 팔기
    def sell(self, customer):
        # 판매 시 손님의 할인율을 적용하여 판매한다.
        customer.money -= self.product.price * (1 - customer.discount * 0.01)
        # 손님 한 명에게 한 개의 상품을 판매한다.
        self.stock -= 1

product = Product('사과', 3000)
customer = Customer('한동석', 20, 30, money=10000)
market = Market(product, 40)
market.sell(customer)

print(market.stock)
print(customer.money)






