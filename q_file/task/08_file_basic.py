# 고등어를 참치로 수정하기

content = ""
with open('fish.txt', 'r', encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.readline()
        if line == '고등어\n':
            content += '참치\n'
            continue
        content += line

    print(content)

with open('fish.txt', 'w', encoding='utf-8') as file:
    file.write(content)

with open('fish.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))