import praw
import config
import eMail
import threading 
import time

#initialize bot related variables
my_list = ["One Punch man", "One Piece", "Ace of Diamond"]
favoriteMangas = list(map(str.lower, my_list))
processed_comments = []
processed_subs = []

def check_for_updates(submission):
    if submission.id not in processed_subs:
        processed_subs.append(submission.id)
        return True

def favorite_title(comment):
    title = ""
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

    for submission in sub.stream.submissions(skip_existing=True):
        for manga in favoriteMangas:
            if manga in submission.title.lower():
                if '[DISC]' in submission.title:
                    if check_for_updates(submission):
                        body = eMail.create_body(submission, rBot)
                        msg = eMail.set_mail(body)
                        eMail.send(msg)
            for comment in submission.comments.list():
                favorite_title(comment)
    for comment in sub.stream.comments(skip_existing=True):
            favorite_title(comment)

main()