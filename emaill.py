import smtplib
import config

user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(user, password)

    msg = 'hello'


    smtp.sendmail(user, rec, msg)
