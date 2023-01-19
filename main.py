import praw
import config
import eMail
import threading 
import time

#initialize bot related variables
my_list = ["Naruto"]
favoriteMangas = [title.lower() for title in my_list]


def favorite_title(sub):
    title = ""
    new_list = []
    processed_comments = []
    for comment in sub.stream.comments(skip_existing=False):
        if comment.id not in processed_comments:
            if "add" in comment.body:
                text = comment.body
                start = text.index("add") + 4
                if "manga" in comment.body:
                    end = text.index("manga")
                    title = text[start:end].strip()
                    if title.lower() not in favoriteMangas:
                        new_list.append(title.lower())
                        processed_comments.append(comment.id)
    favoriteMangas.extend(new_list)
    print("manga list right now")
    print(my_list)
    print("processed comment id")
    print(processed_comments)
    return favoriteMangas


def main():
    rBot = config.create()
    subreddit = rBot.subreddit('manga')
    sub = rBot.subreddit('testingMyStuffCode')
    title_list = favorite_title(sub)
    while True:
        for submission in sub.stream.submissions(skip_existing=True):
            for manga in title_list:
                if manga in submission.title.lower():
                    if '[DISC]' in submission.title:
                        body = eMail.create_body(submission, rBot)
                        msg = eMail.set_mail(body)
                        eMail.send(msg)
        
main()