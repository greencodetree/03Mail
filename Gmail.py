import smtplib
from email.mime.text import MIMEText

sendEmail = ""    #보내는 구글 이메일 주소
recvEmail = ""       #받는 이메일 주소
password = ""             #구글 비밀번호

smtpName = "smtp.gmail.com" #smtp 서버 주소
smtpPort = 587 #smtp 포트 번호

text = "This is a test mail"    #메일 내용
msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

msg['Subject'] ="Test mail" #메일 제목
msg['From'] = sendEmail 
msg['To'] = recvEmail
print(msg.as_string()) #전송을 위해 전용함수 as_string 으로 텍스트 형태로 변환

s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
s.starttls() #TLS 보안 처리
s.login( sendEmail , password ) #로그인
s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환해야 합니다.
s.close() #smtp 서버 연결을 종료합니다.