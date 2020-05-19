import praw, re, requests, time, os, json
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('REDDIT_KEY')
client_secret= os.getenv('REDDIT_SECRET')

class Rbot:
    
    def __init__(self, subreddit):
        client_id = os.getenv('REDDIT_KEY')
        client_secret= os.getenv('REDDIT_SECRET')
        print(client_id)
        self.reddit = praw.Reddit(client_id=client_id, 
                    client_secret=client_secret,
                    user_agent='<console:reddit_bot:0.0.1 (by /u/saltlampafficionado)>')
        self.subreddit = subreddit

    def getPosts(self, number_posts):

        hot_posts = self.reddit.subreddit(self.subreddit).hot(limit=number_posts)

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
                
                path = "./posts/"+file_name[:-4]
                
                try:
                    os.mkdir(path)
                    with open(os.path.join(path, 'image.jpg'), 'wb') as f:
                        f.write(r.content)
                    #Save post info into directory
                    post_data = {}
                    post_data['author'] = str(post.author)
                    post_data['title'] = str(post.title)

                    with open(os.path.join(path, 'data.txt'), 'w') as f:
                        json.dump(post_data, f)
                except:
                    print(f"Creattion of the directory failed ({url})")

