#!/usr/bin/env python3
import feedparser
from flask import Flask
from flask import render_template
from pprint import pprint

feedURLs = ["https://www.youtube.com/feeds/videos.xml?user=2veritasium"]

feeds = []
feeds.append(feedparser.parse(feedURLs[0]))

kacheln = []

for feed in feeds:
    for title, post in feed.items():
        if title == "bozo":
            continue
        print(title)
        # print(type(title)) # str
        # print(type(post)) # list

        # pprint(post)

        kacheln.append(post)
        # for video in post:
        #     # pprint(video)
        #     for name, element in video.items():
        #         pprint(name)
        #         pprint(element)
        #     break
        break


app = Flask(__name__)


# def url_for(where, filename):
#     return filename


@app.route('/')
def index():
    return render_template('hello.html', kacheln=kacheln, int=int, round=round)


@app.route('/hello')
def hello():
    return 'Hello, World'
