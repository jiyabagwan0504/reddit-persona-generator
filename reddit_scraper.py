import praw

# Connect to Reddit
reddit = praw.Reddit(
    client_id="kYNuMs_5YQem7vIKU5yarw",
    client_secret="1yGTWP7XWdw4WA0QVBdi3JBbjpXe5Q",
    user_agent="script:reddit.persona:v1.0 (by /u/Independent_Day6367)"
)

# Extract username from URL
profile_url = "https://www.reddit.com/user/kojied/"
username = profile_url.strip('/').split("/")[-1]
redditor = reddit.redditor(username)

# Gather comments and posts
print(f"\n Fetching info for Reddit user: {username}\n")

comments = []
posts = []

for comment in redditor.comments.new(limit=10):
    comments.append(f" {comment.body}\n[Subreddit: {comment.subreddit}]\n")

for post in redditor.submissions.new(limit=5):
    posts.append(f" {post.title}\n{post.selftext}\n[Subreddit: {post.subreddit}]\n")

# Combine into single text
all_text = f"REDDIT USER: {username}\n\n"
all_text += "===== USER COMMENTS =====\n\n" + "\n".join(comments)
all_text += "\n\n===== USER POSTS =====\n\n" + "\n".join(posts)

# Save to file
filename = f"{username}_raw.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"\n Combined data saved to {filename}")
