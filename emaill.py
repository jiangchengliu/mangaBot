import smtplib
import config
import main

user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

def send_email():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        for url in main.urls:
            smtp.sendmail(user, rec, url)
