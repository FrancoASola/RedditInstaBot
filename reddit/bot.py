import praw, re, requests, time, os, json
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('REDDIT_KEY')
client_secret= os.getenv('REDDIT_SECRET')

reddit = praw.Reddit(client_id=client_id, 
            client_secret=client_secret,
            user_agent='<console:reddit_bot:0.0.1 (by /u/saltlampafficionado)>')

subreddit = 'battlestations'

print()

hot_posts = reddit.subreddit(subreddit).hot(limit=10)

for post in hot_posts:
    url = post.url
    print(url)


    file_name = url.split('/')
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".jpg" 
    
    if file_name != ".jpg":
        # Make new directory and save image
        r = requests.get(url)
        
        path = "../posts/"+file_name[:-4]
         
        try:
            os.mkdir(path)
        except:
            print(f"Creattion of the directory failed ({url})")

        with open(os.path.join(path, file_name), 'wb') as f:
            f.write(r.content)

        #Save post info into directory
        author = post.author
        title = post.title
        print(author, title)