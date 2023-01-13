import praw
import config
import emaill

rBot = config.create()
subreddit = rBot.subreddit('manga')

favoriteMangas = ['legend of the northern blade', 'one punch man', 'boku no kokoro no yabai yatsu']

urls = []

for submission in subreddit.hot(limit=10):
    for manga in favoriteMangas:
        if manga in submission.title.lower():
            if '[DISC]' in submission.title:
                print('Title: ' + submission.title)
                urls.append(submission.url)
                break











    