# 맥북은 아래의 명령어를 반드시 작성한다
# ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.10/etc/openssl

import smtplib
# ssl은 보안 설정할 때 쓰는 module
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# port 번호는 고정
port = 587
# 주소 형식
smtp_server = "smtp.gmail.com"
# 보내는 사람 이메일
sender_email = "보내는 사람 이메일"
# 받는 사람 이메일
receiver_email = "받는 사람 이메일"
# 비밀번호(앱 비밀번호)
# 1회용 비밀번호
password = "앱 비밀번호"
# 메세지
message = "<h1>내용</h1>"

msg = MIMEText(message, 'html')
data = MIMEMultipart()
data.attach(msg)

context = ssl.create_default_context()
# 이 영역 안에서만 서버로 접근
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, data.as_string())
