import praw
import config

rBot = config.create()

subreddit = rBot.subreddit('manga')


favoriteMangas = ['legend of the northern blade', 'one punch man']

for submission in subreddit.hot(limit=10):
    for manga in favoriteMangas:
        if manga in submission.title.lower():
            print('Title: ' + submission.title)
            print('URL: ' + submission.url)
            print('---------------------------')
            break


    