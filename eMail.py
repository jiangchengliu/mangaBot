import smtplib
from email.message import EmailMessage
import config

#email info
user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

def create_body(submission, bot):
    body = "Update!!!: \n\n"
    body += submission.title + "\n" + submission.url + bot.config.reddit_url + "\n" + submission.permalink + "\n\n"
    return body

def set_mail(email_body):
    msg = EmailMessage()
    msg['Subject'] = 'New Chapters Found!'
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