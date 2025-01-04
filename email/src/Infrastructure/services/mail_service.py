import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.Infrastructure.services.databaseService import insert_mail
from src.Infrastructure.services.logger import logger
from src.Infrastructure.configs.config import PSSWD,FROM_EMAIL

def send_email(email):
    smtp_server = "smtp.mail.ru"
    smtp_port = 25

    msg = MIMEMultipart()
    msg['From'] = email.mailFrom
    msg['To'] = email.mailTo
    msg['Subject'] = email.subject
    msg.attach(MIMEText(email.content, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(FROM_EMAIL,PSSWD)
        server.sendmail(FROM_EMAIL,email.mailTo,msg.as_string())
        server.quit()
        insert_mail(email)
        logger.info(f'Email sent to {email.mailTo}')
    except Exception as e:
        email.status= 'Провал'
        insert_mail(email)
# send_email(
#     subject="Тест сабджект",
#     body="test msg",
#     to_email=TO_EMAIL,
#     from_email=FROM_EMAIL,
#     psswd=PSSWD
# )