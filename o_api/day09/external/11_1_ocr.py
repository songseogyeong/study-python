# https://ocr.space/OCRAPI
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true
# https://api.ocr.space/parse/imageurl?apikey=[내 API 키]&url=[가져올 url]&language=[인식할 언어]&isOverlayRequired=true
# apikey=
# url=
# language=

# requests 모듈이 없다고 나오면 requests를 드레그하면 아래 나오는 창에 깔 수 있도록 나올 거임
import requests

url = 'https://api.ocr.space/parse/imageurl?apikey=[api키 입력]&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
# requests > 요청, get() > 방식, 주소창
# 나는 이런 방식으로 요청을 할거야
response = requests.get(url)
response.raise_for_status()

# 위 페이지를 요청을 하면 아래에서 나옴
# 리턴 값임
result = response.json()
print(result)
# 결과 값: {'ParsedResults': [{'TextOverlay': {'Lines': [{'LineText': '사람은 완벽할 수 없고', 'Words': [{'WordText': '사람은', 'Left': 136.0, 'Top': 167.0, 'Height': 25.0, 'Width': 73.0}, {'WordText': '완벽할', 'Left': 217.0, 'Top': 167.0, 'Height': 26.0, 'Width': 72.0}, {'WordText': '수', 'Left': 297.0, 'Top': 168.0, 'Height': 25.0, 'Width': 24.0}, {'WordText': '없고', 'Left': 330.0, 'Top': 167.0, 'Height': 26.0, 'Width': 48.0}], 'MaxHeight': 26.0, 'MinTop': 167.0}, {'LineText': '완벽할 필요도 없다.', 'Words': [{'WordText': '완벽할', 'Left': 137.0, 'Top': 220.0, 'Height': 26.0, 'Width': 73.0}, {'WordText': '필요도', 'Left': 218.0, 'Top': 220.0, 'Height': 26.0, 'Width': 71.0}, {'WordText': '없다.', 'Left': 298.0, 'Top': 220.0, 'Height': 26.0, 'Width': 52.0}], 'MaxHeight': 26.0, 'MinTop': 220.0}, {'LineText': '삶을 너무 보채지 말자.', 'Words': [{'WordText': '삶을', 'Left': 137.0, 'Top': 273.0, 'Height': 25.0, 'Width': 48.0}, {'WordText': '너무', 'Left': 194.0, 'Top': 273.0, 'Height': 25.0, 'Width': 47.0}, {'WordText': '보채지', 'Left': 248.0, 'Top': 273.0, 'Height': 26.0, 'Width': 69.0}, {'WordText': '말자.', 'Left': 329.0, 'Top': 273.0, 'Height': 26.0, 'Width': 53.0}], 'MaxHeight': 26.0, 'MinTop': 273.0}, {'LineText': '완벽하지 않은 것들이', 'Words': [{'WordText': '완벽하지', 'Left': 137.0, 'Top': 325.0, 'Height': 26.0, 'Width': 92.0}, {'WordText': '않은', 'Left': 243.0, 'Top': 325.0, 'Height': 26.0, 'Width': 46.0}, {'WordText': '것들이', 'Left': 297.0, 'Top': 325.0, 'Height': 26.0, 'Width': 68.0}], 'MaxHeight': 26.0, 'MinTop': 325.0}, {'LineText': '아름답다.', 'Words': [{'WordText': '아름답다.', 'Left': 138.0, 'Top': 378.0, 'Height': 26.0, 'Width': 100.0}], 'MaxHeight': 26.0, 'MinTop': 378.0}], 'HasOverlay': True, 'Message': 'Total lines: 5'}, 'TextOrientation': '0', 'FileParseExitCode': 1, 'ParsedText': '사람은 완벽할 수 없고\r\n완벽할 필요도 없다.\r\n삶을 너무 보채지 말자.\r\n완벽하지 않은 것들이\r\n아름답다.\r\n', 'ErrorMessage': '', 'ErrorDetails': ''}], 'OCRExitCode': 1, 'IsErroredOnProcessing': False, 'ProcessingTimeInMilliseconds': '984', 'SearchablePDFURL': 'Searchable PDF not generated as it was not requested.'}
print(type(result))
# 결과 값: <class 'dict'>

# ParsedResults의 0번째 방에 접속해서 ParsedText라는 key의 value 값을 가져온다
print(result['ParsedResults'][0]['ParsedText'])

# AI는 컴파일 언어로 사용이 불가능하다.(학습 때문에)