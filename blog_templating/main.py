from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

posts_objects = []
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
for blog_post in all_posts:
    posts_objects.append(Post(blog_post["id"], blog_post["title"], blog_post["subtitle"], blog_post["body"]))


@app.route('/')
def home():
    return render_template("index.html", posts=posts_objects)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    required_post = None
    for post in posts_objects:
        if post.post_id == post_id:
            required_post = post
            break
    return render_template("post.html", post_content=required_post)


if __name__ == "__main__":
    app.run(debug=True)
