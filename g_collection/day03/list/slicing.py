# 인덱스 슬라이싱
animals = ['dog', 'dog', 'cat', 'bird', 'fish']

# list[inclusive_start = 0 : exclusive_end = len(list)] -> list
# 왼쪽이 시작 인덱스 오른쪽이 끝나는 인덱스
print(animals[0])
print(animals[0:3])
# 0부터 3번째까지 보여줘 0, 1, 2 출력
print(animals[1:4])
print(animals[:2])
print(animals[2:])

# list[inclusive_start = 0 : exclusive_end = len(list) : step = 1]
food = ['noodle', 'meat', 'bread', 'chicken']
print(food[:3:2])
print(food[2::2])
# 반복문이랑 유사..
# 시작 : 몇 번째까지 : 몇씩?
# step은 거의 사용하지 않음! 메모리를 많이 소모한다.


# 역순 출력
print(food[::-1])

# 실습1
number_list = list(range(1, 11))
print(number_list)

# [1, 3, 5, 7, 9]
print(number_list[::2])

# [6, 5, 4, 3, 2]
print(number_list[5:0:-1])
# 마지막 값은 포함하지 않기 때문에 0으로 둬야함!

# [2, 4, 6]
print(number_list[1:6:2])

# [2, 3, 4, 5, 6, 7]
print(number_list[1:7])

# --------------------------------------------------------------------------
animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['panda', 'giraffe']

animals[1:2] = zoo
# [1:2] = [1]
# 자리에 있던 dog은 대체가 됨
print(animals)

animals.insert(animals.index('dog') + 1, 'giraffe')
# 기존에 있던 값이 날라가지 않음
# dog 있는자리 +1 만큼 뒤에 붙음
print(animals)

animals.insert(animals.index('dog') + 1, zoo)
# 리스트 통으로 넣고 싶으면 insert하면됨
print(animals)


# 실습2
# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']

animals[2:3] = ['whale']
print(animals)

animals.insert(animals.index('dog') + 1, 'hamster')
animals.insert(2, 'fish')
print(animals)


# 실습2 정리
animals = ['dog', 'dog', 'cat', 'bird']

del animals[animals.index('cat')]
# animals.remove('cat')
print(animals)

animals[-2: -3: -1] = ['whale']
print(animals)

animals.insert(animals.index('dog' + 1), 'fish')
print(animals)

animals.insert(animals.index('dog' + 1), 'hamster')
print(animals)

animals[1:3] = ['hamster', 'fish', 'dog']
print(animals)