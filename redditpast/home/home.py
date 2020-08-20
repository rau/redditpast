import requests
import praw
from flask import Blueprint, render_template
from pprint import pprint

home_bp = Blueprint(
    'home_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/')
@home_bp.route('/home/')
def home():
    x = requests.get(f"https://api.pushshift.io/reddit/search/submission/?size=2")
    posts = []
    rank = 1
    for post in x.json()['data']:
        posts.append({
            'title': post['title'],
            'url': post['url'],
            'score': post['score'],
            'num_comments': post['num_comments'],
            'rank': rank
        })
        rank += 1
    return render_template('index.html', posts=posts)

@home_bp.route('/faq/')
def faq():
    return render_template('faq.html')
