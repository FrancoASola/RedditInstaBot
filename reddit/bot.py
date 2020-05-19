import praw, re, requests, time, os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('REDDIT_KEY')
client_secret= os.getenv('REDDIT_SECRET')

reddit = praw.Reddit(client_id=client_id, 
            client_secret=client_secret,
            user_agent='<console:reddit_bot:0.0.1 (by /u/saltlampafficionado)>')

subreddit = 'battlestations'

hot_posts = reddit.subreddit(subreddit).hot(limit=10)

for post in hot_posts:
    print(post.url)

