import praw
import config
import eMail
import threading 

#initialize bot related variables
rBot = config.create()
subreddit = rBot.subreddit('manga')
sub = rBot.subreddit('testingMyStuffCode')
my_list = ["ayakashi triangle", "cockroa-chan"]
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

def goThroughCom(sub, list):
    global my_list
    for comment in sub.stream.comments():
        found_add = False
        if "add" in comment.body:
            text = comment.body
            start = text.index("add") + 4
            if "manga" in comment.body:
                end = text.index("mangaBot")
                title = text[start:end].strip()
                if title not in my_list:
                    my_list.append(title)
                    found_add = True
        if found_add:
            break
        
print(my_list)

comments_thread = threading.Thread(target=goThroughCom, args=(sub, my_list))
comments_thread.start()

body = eMail.create_body(my_dict)
msg = eMail.set_mail(body)
eMail.send(msg)
my_dict.clear()



