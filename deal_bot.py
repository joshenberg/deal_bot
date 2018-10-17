import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("frugalmalefashion")
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))


keys = ["common projects", "cp ", "acne", "naked and famous", "naked & famous", "margiela", "uniqlo", "red wing", "norse",
        "bonobos", "patagonia", "ray ban"]

for submission in subreddit.stream.submissions():

    if any(keyword in submission.title.lower() for keyword in keys) and submission.id not in posts_replied_to:

        submission.reply("Check this out /u/senor_procrastinator")
        posts_replied_to.append(submission.id)

        print("Title: ", submission.title)
        print("Score: ", submission.score)
        print("URL: ", submission.url)
        print("---------------------\n")



with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")