import smtplib
import config

user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

def send_email(list):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        for url in list: 
            smtp.sendmail(user, rec, url)
            
