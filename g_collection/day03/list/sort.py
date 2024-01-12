# 정렬
number_list = [5, 4, 6, 1, 3]

# 1. sort(): 원본이 그대로 변경됨
# 원본을 수정했기 때문에 좋지 않음
# 그래서 sort는 꼭! 필요할 때만 사용
number_list.sort()
print(number_list)

number_list.sort(reverse=True)
print(number_list)
# print에도 옵션이 있듯이 sort에도 revers라는 옵션이 있음
# 기본적으로 sort는 False, reverse = True를 넣어서 내림차순 정렬

# 2. sorted(): 원본은 유지되고 새로운 list가 만들어짐
# 프린트처럼 사용하고 솔티드에다가 넘버리스트를 전달해주는 식!
# 원본을 건들이지 않음~
sorted_list = sorted(number_list)
# sorted 자체가 새로운 list
# 그래서 앞에다가 변수를 선언해서 사용
print(number_list)
print(sorted_list)

sorted_list = sorted(number_list, reverse=True)
print(number_list)
print(sorted_list)

print(sorted('ABC'))