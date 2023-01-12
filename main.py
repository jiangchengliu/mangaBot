import praw
import config

rBot = config.create()

subreddit = rBot.subreddit('manga')

favoriteMangas = ['legend of the northern blade', 'one punch man']

urls = []

for submission in subreddit.hot(limit=10):
    for manga in favoriteMangas:
        if manga in submission.title.lower():
            if '[DISC]' in submission.title:
                print('Title: ' + submission.title)
                urls.append(submission.url)
                break

for url in urls:
    print(url)


    