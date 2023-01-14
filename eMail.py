import smtplib
from email.message import EmailMessage
import config

#email info
user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

def create_body(my_dict):
    body = "Here is What has Updated!: \n\n"
    for key in my_dict:
        body += key + "\n" + my_dict[key] + "\n\n"
    return body

def set_mail(email_body):
    msg = EmailMessage()
    msg['Subject'] = 'New Manga Chapters Found!'
    msg['From'] = user
    msg['To'] = rec
    msg.set_content(email_body)
    return msg

def send(msg):
#sending email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)
