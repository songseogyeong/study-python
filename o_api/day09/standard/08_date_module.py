# datetime은 내부 API
import datetime

# 현재 날짜
# 뭔가를 새롭게 등록할 때 사용함..회원가입

now = datetime.date.today()
print(now)
# 결과 값: 2024-01-10

now = datetime.datetime.today()
print(now)
# 결과 값: 2024-01-10 13:39:08.853202
# 2024-01-10 13:37:44.375394 실제 저장된 데이터
# 실제 저장된 데이터 형식과 출력하는 데이터 형식이 다르다

# now도 객체이기 때문에 연결해서 더 쓸 수 있음
print(now.year)
# 결과 값: 2024
print(now.month)
# 결과 값: 1
print(now.day)
# 결과 값: 10
print(now.hour)
# 결과 값: 13

# 이런 건 외울 수 없음
# 구글링해서 그때마다 찾기

# 지정된 날짜
date = datetime.datetime(2024, 1, 1, 12, 0, 0)
print(date)
# 결과 값: 2024-01-01 12:00:00
