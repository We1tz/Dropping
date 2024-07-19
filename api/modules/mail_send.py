import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from api.config import smtp_server, smtp_port, smtp_username, smtp_password, from_email


def send_password_mail(data):
    email = data[0]
    code = data[1]

    to_email = f'{email}'

    subject = 'Foxproof | Письмо восстановления пароля'

    body = (f"""Здравствуйте, это Ваше письмо восстановления пароля.

        Ваш новый пароль: {code}

        С уважением FoxProof""")

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


def send_register_mail(data):
    email = data[0]
    to_email = f'{email}'

    subject = 'Foxproof | Письмо для регистрации на сайте'

    confirmation_url = data[1]

    body = (f"""Здравствуйте, это Ваше письмо для подтверждения регистрации на сайте.

        Перейдите по следующей ссылке для подтверждения регистрации: {confirmation_url}

        С уважением, FoxProof""")

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
