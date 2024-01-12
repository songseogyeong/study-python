# 수정
# 외부 파일에 있는 내용을 담아주는 변수
content = ""
with open('food.txt', 'r', encoding='utf-8') as file:
    line = None
    # 전체 내용을 한 줄 씩 읽어오기
    while line != '':
        # 한 줄을 line에 담기
        line = file.readline()
        # 담은 내용이 찾고 있는 햄버거일 경우
        # 가져오는 값 자체가 \n이 들어가기 때문에 잊지말고 써주기
        if line == '햄버거\n':
            # content에 치킨으로 변경해서 담기
            content += '치킨\n'
            continue
        # 수정 대상이 아닌 줄은 그대로 content에 담기
        content += line

    # 수정 완료된 문자열 값 확인
    print(content)

# 기존의 내용을 수정 완료된 문자열로 덮어쓰기
with open('food.txt', 'w', encoding='utf-8') as file:
    file.write(content)

# 원본 파일의 내용 확인
with open('food.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))