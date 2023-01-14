import praw
import config
import eMail.py

#initialize bot related variables
rBot = config.create()
subreddit = rBot.subreddit('manga')
my_list = ['Telework Yotabanashi', 'Senpai ga Uzai Kouhai no Hanashi ']
favoriteMangas = list(map(str.lower, my_list))
title = ""
my_dict = {}

def goThroughSub():
#go through submissions 
    for submission in subreddit.hot(limit=25):
        for manga in favoriteMangas:
            if manga in submission.title.lower():
                if '[DISC]' in submission.title:
                    if submission.title not in my_dict:
                        my_dict[submission.title] = submission.url
                        break
def goThroughCom():
    #go through comments
    for comment in subreddit.stream.comments():
        if "add" in comment.body:
            text = comment.body
            start = text.index("add") + 4
            if "!" in comment.body:
                end = text.index("!")
                title = text[start:end].strip()
                if title not in my_list:
                    my_list.append(title)



