import praw
import config
import smtplib
from email.message import EmailMessage
from praw.models import Message

#email info
user = config.EMAIL_USER
password = config.PASSWORD
rec = config.RECEIVE_USER

#initialize bot related variables
rBot = config.create()
subreddit = rBot.subreddit('manga')
subreddit2 = rBot.subreddit('testingMyStuffCode')
my_list = ['muscle exorcism', 'Telework Yotabanashi', 'Senpai ga Uzai Kouhai no Hanashi ']
favoriteMangas = list(map(str.lower, my_list))
title = ""
my_dict = {}

#go through submissions 
for submission in subreddit.hot(limit=25):
    for manga in favoriteMangas:
        if manga in submission.title.lower():
            if '[DISC]' in submission.title:
                if submission.title not in my_dict:
                    my_dict[submission.title] = submission.url
                    break

#go through comments
for comment in subreddit2.stream.comments():
    if "add" in comment.body:
        text = comment.body
        start = text.index("add") + 4
        if "!" in comment.body:
            end = text.index("!")
            title = text[start:end].strip()
        if title in my_list:
            comment.reply("already in the list!")
        my_list.append(title)

#create the email body content
body = "Here is What has Updated!: \n\n"
for key in my_dict:
    body += key + "\n" + my_dict[key] + "\n\n"

#set the layout of email 
msg = EmailMessage()
msg['Subject'] = 'New Manga Chapters Found!'
msg['From'] = user
msg['To'] = rec
msg.set_content(body)

#sending email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(user, password)
    smtp.send_message(msg)