import praw
import config
import eMail
import threading 
import time

#initialize bot related variables
my_list = ["Please Go Home, Akutsu-san!", "Dandadan"]
favoriteMangas = list(map(str.lower, my_list))
title = ""
my_dict = {}
processed_comments = []

def send_email():
    body = eMail.create_body(my_dict)
    msg = eMail.set_mail(body)
    eMail.send(msg)

def check_for_updates(submission):
    if submission.title not in my_dict:
        return True

def favorite_title(comment):
    if comment.id not in processed_comments:
        if "add" in comment.body:
            text = comment.body
            start = text.index("add") + 4
            if "manga" in comment.body:
                end = text.index("manga")
                title = text[start:end].strip()
                if title not in my_list:
                    my_list.append(title)
                    processed_comments.append(comment.id)  
    
def main():
    rBot = config.create()
    subreddit = rBot.subreddit('manga')
    sub = rBot.subreddit('testingMyStuffCode')

    for submission in subreddit.hot(limit=25):
        for manga in favoriteMangas:
            if manga in submission.title.lower():
                if '[DISC]' in submission.title:
                    if check_for_updates(submission):
                        my_dict[submission.title] = submission.url
                        send_email()
            for comment in submission.comments.list():
                favorite_title(comment)
    for comment in subreddit.stream.comments(skip_existing=True):
            favorite_title(comment)

main()