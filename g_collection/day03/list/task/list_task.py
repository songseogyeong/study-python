# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "과일가게"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ''
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

# while True:
#     search1 = int(input(menu))
#     result = ''
#
#     if search1 == 1:
#         add_item = input(append_message)
#         add_list = add_item.split()
#
#         if add_list == name_list:
#             result = (append_error_message)
#             break
#
#         elif add_list != name_list:
#             name_list.append(add_list[0])
#             price_list.append(int(add_list[1]))
#             result = f'{add_list[0]}, {add_list[1]}원 상품이 추가 되었습니다.'
#             break
#
#     elif search1 == 2:
#         search_result = input(search_menu)
#         if search_result == 1:
#             update_result = input(search_name_message_for_update)
#             if update_result != name_list:
#                 result = update_error_message
#                 break
#
#             elif update_result == name_list:
#                 update_result2 = input(update_message)
#                 update_list = update_result2.split()
#
#                 if
#
#         elif search_result == 2:
#         else:
#             result = '잘 못 입력하셨습니다.'
#             break
#
#     elif search1 == 3:
#         result = delete_message
#     elif search1 == 5:
#         result = f'{search_name_message}{name_list}\n{search_price_message}{price_list}'
#     elif search1 == 6:
#         break
#     else:
#         result = ('잘못 입력하셨습니다.')
#         break
#
# print(result)
# print(name_list)
# print(price_list)

# 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
while True:
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자)
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지 않는다면,
        if newn_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위해 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 사용자에게 수정할 상품명을 입력 받는다.
        name = input(search_name_message_for_update)
        # 익력한 상품명이 name_list에 있다면,
        if name in name_list:
            # 새로운 상품명과 새로운 가격을 입력 받고
            new_name, new_price = input(update_message).split()
            # 새로운 상품명이 name_list에 없다면(중복이 안 된다면)
            if new_name not in name_list:
                # 인덱스 = name_list에 원래있던 상품명의 인덱스 번호를 찾고
                index = name_list.index(name)
                # 해당 인덱스에 새로운 상품명과 가격으로 값을 변경한다.
                name_list[index], price_list[index] = new_name, new_price
                # 오류 메세지를 출력하지 않기 위해 즉시 다음 반복으로 skip
                continue
            else:
                # 상품명이 중복된다면 오류 메세지 출력
                result_message = update_error_message2
        else:
            # 상품명이 없다면 오류 메세지 출력
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 사용자에게 삭제할 상품명을 입력 받는다
        name = input(delete_message)
        # name_list에 입력한 상품명이 있다면
        if name in name_list:
            # ame_list에 있는 상품명의 인덱스 번호를 인덱스에 담아두고
            index = name_list.index(name)
            # * name의 인덱스 번호를 조회해서 pirce를 삭제하는 건데,
            # * name먼저 삭제하면 pirce 순서가 조회가 불가능
            # * 그래서 위 처럼 name 값을 저장해 주고 삭제해 주기!
            # name_list에서 해당하는 인덱스 번호에 있는 값을 지우고
            del name_list[index]
            # price_list에서 해당하는 인덱스 번호에 있는 값을 지운다
            del price_list[index]
            # 오류 메세지를 출력하지 않기 위해 즉시 다음 반복으로 skip
            continue
        else:
            # 사용자가 입력한 상품명이 없다면 에러 메세지를 출력한다.
            result_message = delete_error_message


    # 검색
    elif choice == 4:
        # 상품명으로 검색할지 가격으로 검색할지 입력받는다
        choice = int(input(search_menu))

        # 상품명으로 검색
        # 사용자가 상품명으로 검색한다고 하면,
        if choice == 1:
            # 상품명을 입력받는다
            name = input(search_name_message)
            # name_list에 상품명이 있다면
            if name in name_list:
                # name_list의 상품명 인덱스 번호를 인덱스에 담고
                index = name_list.index(name)
                # 해당하는 인덱스 번호의 값을 출력한다
                print(f'{name_list[index]}, {price_list[index]}')
                # 오류 메세지를 출력하지 않기 위해 즉시 다음 반복으로 skip
                continue

            else:
                # 사용자가 입력한 상품명이 없다면 오류 메세지를 출력한다.
                result_message = search_name_error_message

        # 가격으로 검색
        # 사용자가 가격으로 검색한다고 하면
        elif choice == 2:
            # 사용자에게 가격의 값을 입력 받고 문자열을 정수로 형변환한다.
            price = int(input(search_price_message))
            # 오차 범의를 0.5씩 두기 위해
            # 가격에 0.5를 곱해 최솟값을 구하고
            min = price * 0.5
            # 가격에 1.5를 곱해 최댓값을 구한다
            max = price * 1.5
            # price_list를 price에 담아주는데 이 pirce는 최솟값보다 크거나 같고, 최댓값보다 작거나 같다
            # 그리고 이 price는 i에 담고 i의 인덱스 번호를 구하고 result_index에 선언해 준다.
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]

            # result_indexd의 길이가 0과 같지 않으면
            if len(result_index) != 0:
                # result_index(인덱스 번호)를 i에 담고
                for i in result_index:
                    # name_list, price_list에서 해당하는 인덱스 번호의 값을 출력한다
                    print(f'{name_list[i]}, {price_list[i]}')
                    # 오류 메세지를 출력하지 않기 위해 즉시 다음 반복으로 skip
                    continue

        else:
            # 1, 2번 외 값을 입력한 경우 오류 메세지 출력
            result_message = search_error_message


    # 검색
    elif choice == 5:
        # name_list의 길이가 0과 같다면(값없음)
        if len(name_list) == 0:
            # 에러 메세지를 출력한다
            result_message = no_item_message
        else:
            # name_list의 길이 만큼 반복해서 name_lise의 모든 값을 출력한 뒤, i에 담는다.
            for i in range(len(name_list)):
                # name_list와 price_list의 모든 값을 출력한다
                print(f'{name_list[i]}, {price_list[i]}')
                # 오류 메세지를 출력하지 않기 위해 즉시 다음 반복으로 skip
                continue
    # 성공했을 때 컨티뉴를 써놔야 아래 있는 print(result_message) 오류 메세지가 출력되지 않음!


    # 나가기
    elif choice == 6:
        # 6을 선택하면 탈출
        break

    else:
        # 다른 값을 입력하면 오류 메세지 출력 후
        result = ('잘못 입력하셨습니다.')
        # 탈출
        break

# 에러 메세지 일괄처리
print(result_message)
# 혹시 모를 사항에 대비해서 메세지 값 초기화 하기
result_message = ""

print(name_list)
print(price_list)

# 코드짜고 출력해보고 버그가 있나 없나 확인하는 걸 디버깅(하나하나 뜯어보는 거)이라고 한다.