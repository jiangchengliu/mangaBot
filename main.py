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
my_list = ['legend of the northern blade', 'one punch man', 'Telework Yotabanashi', 'Senpai ga Uzai Kouhai no Hanashi ']
favoriteMangas = list(map(str.lower, my_list))
my_dict = {}

for submission in subreddit.hot(limit=10):
    for manga in favoriteMangas:
        if manga in submission.title.lower():
            if '[DISC]' in submission.title:
                print('Title: ' + submission.title)
                print('URL: ' + submission.url)
                my_dict[submission.title] = submission.url
                break

body = "Here is What has Updated!: \n\n"
for key in my_dict:
    body += key + "\n" + my_dict[key] + "\n\n"


msg = EmailMessage()
msg['Subject'] = 'New Manga Chapters Found!'
msg['From'] = user
msg['To'] = rec
msg.set_content(body)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(user, password)
    smtp.send_message(msg)