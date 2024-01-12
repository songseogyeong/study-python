# client_id = PwsfI8GDesraXQ8m6QQ1
# client_secret = gbkc7eSajZ
# https://openapi.naver.com/v1/papago/n2mt

# 요청 예시
# H는 헤더
# curl "https://openapi.naver.com/v1/papago/n2mt" \
# -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
# -H "X-Naver-Client-Id: PwsfI8GDesraXQ8m6QQ1" \
# -H "X-Naver-Client-Secret: gbkc7eSajZ" \
# -d "source=ko&target=en&text=만나서 반갑습니다." -v

import urllib.request
import json

client_id = "PwsfI8GDesraXQ8m6QQ1"
client_secret = "gbkc7eSajZ"
encoding_text = urllib.parse.quote("보고싶어, 사랑해")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

# loads는 json을 dict타입으로 변경
if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response['message']['result']['translatedText'])
    # 결과 값: I miss you. I love you


# 설정에 따라 안 되거나
# 보안이 강한 컴퓨터에서 안 될 수 있다
# 보안을 꺼주는 방법
# import ssl
# ssl._create_default_https_context =
# ssl._create_unverified_context