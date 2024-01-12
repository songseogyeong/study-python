import json

# price에서 숫자 사이에 _(언더바)는 개발자를 위한 것으로 출력 시 함께 출력되지 않는다
# data는 dict 타입
data = {'name': '책', 'price': 25_000, 'stock': 55}
# dict의 목적은 서버 간 데이터 교환

# dict와 json은 다르다
# json은 반드시 ""쌍따옴표를 사용
print(data)
# 결과 값: {'name': '책', 'price': 25000, 'stock': 55}

# dict를 json으로 변환
# dumps 시 자동으로 joson형식으로 변경된다
json_data = json.dumps(data)
print(json_data)
# 결과 값: {"name": "\ucc45", "price": 25000, "stock": 55}
# \ucc45 는 유니코드 = cc45번째 확인

# 아스키코드 1바이트
# 영어, 숫자 밖에 없음
# 전구 8개로 표현 가능

# 유니코드 2바이트
# 한국어, 아랍어 등은.. 유니코드

# ensure_ascii: 한글을 유니코드가 아닌 원본으로 출력 (기본이 Ture, Ture 시 유니코드가 나온다)
# ensure_ascii=False 시 유니코드가 아닌 원본으로 나오게 한다
json_data = json.dumps(data, ensure_ascii=False)
print(json_data)
# 결과 값: {"name": "책", "price": 25000, "stock": 55}

# indent: 보기 좋게 바꿔주며, 전달한 값은 들여쓰기 공백 개수
json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data)
# 결과 값:
# {
#     "name": "책",
#     "price": 25000,
#     "stock": 55
# }

# loads: json을 dict로 변환
data_dict = json.loads(json_data)
print(data_dict)
# 결과 값: {'name': '책', 'price': 25000, 'stock': 55}

