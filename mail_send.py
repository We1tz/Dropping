import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
smtp_server = 'smtp.antidropping.ru'
smtp_port = 587
smtp_username = 'admin2281337@antidropping.ru'
smtp_password = 'r$U3q#V7&fW3x%'
from_email = 'admin2281337@antidropping.ru'
to_email = 'kripersam1@gmail.com@gmail.com'
characters = string.ascii_letters + string.digits
pin_code = ''.join(random.choice(characters) for _ in range(4))
subject = 'Код подтверждения регистрации(antidropping.ru)'
body = ('Здравствуйте,\n\nВаш код: {}\n\nС уважением, \nКоманда FoxProof').format(pin_code)
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, msg.as_string())
    print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка при отправке письма: {e}")
finally:
    server.quit()