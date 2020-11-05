#!/usr/bin/env python3
import feedparser
from flask import Flask
from flask import render_template
from pprint import pprint
from models.vidKachel import VidKachel
from collections import defaultdict

feedURLs = ["https://www.youtube.com/feeds/videos.xml?user=2veritasium",
            "https://www.youtube.com/feeds/videos.xml?user=1veritasium"]

with open("yt.txt") as f:
    feedURLs = f.readlines()
feedURLs = [x.strip() for x in feedURLs]

feedURLs = feedURLs[0:200]  # hmm

feeds = []
for feedUrl in feedURLs:
    print(feedUrl)
    feeds.append(feedparser.parse(feedUrl))

kacheln = []

for feed in feeds:
    for title, element in feed.items():
        if title != "entries":
            continue
        # print("title: ", title)
        # print("type(title) ", type(title))  # str
        # print("type(element)", type(element))  # list

        # pprint(element)

        for video in element:
            try:
                vk = VidKachel(video["yt_videoid"], video["media_thumbnail"][0]["url"],
                               video["yt_channelid"], video["title"], video["media_statistics"]["views"], video["author"], video["published"])
                # print(vk)
                kacheln.append(vk)
            except Exception as e:
                pprint(video)
                # for name, element in video.items():
                #     print("element.name:", name, " : ", end="")
                #     pprint(element)
                print(video)
                pprint(e)
            # pprint(video)
            # break

print("len(kacheln) ", len(kacheln))
kacheln.sort(key=lambda x: x.published, reverse=True)

kacheln = kacheln[0:100]

app = Flask(__name__)


# def url_for(where, filename):
#     return filename


@app.route('/')
def index():
    return render_template('hello.html', kacheln=kacheln, int=int, round=round)


@app.route('/hello')
def hello():
    return 'Hello, World'
