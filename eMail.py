import smtplib
from email.message import EmailMessage
import config

#email info
user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

def create_body(submission, bot):
    discuss = bot.config.reddit_url + submission.permalink
    body = "Update!: \n"
    body += submission.title + "\n\n" + submission.url + "\n\n" + discuss + "\n\n"
    return body

def set_mail(email_body):
    msg = EmailMessage()
    msg['Subject'] = 'New Chapter Found!'
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
        print("done!")