import praw
import config
import smtplib
from email.message import EmailMessage

#email info
user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

rBot = config.create()
subreddit = rBot.subreddit('manga')
my_list = ['legend of the northern blade', 'one punch man', 'Telework Yotabanashi',]
favoriteMangas = list(map(str.lower, my_list))
urls = []

for submission in subreddit.hot(limit=10):
    for manga in favoriteMangas:
        if manga in submission.title.lower():
            if '[DISC]' in submission.title:
                print('Title: ' + submission.title)
                print('URL: ' + submission.url)
                urls.append(submission.url)
                break

body = "List of Urls: \n"
for url in urls:
    body += url + "\n"

msg = EmailMessage()
msg['Subject'] = 'New Manga Chapters Found!'
msg['From'] = user
msg['To'] = rec
msg.set_content(body)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(user, password)
    smtp.send_message(msg)