#!/usr/bin/env python3
import feedparser
from pprint import pprint

feedURLs = ["https://www.youtube.com/feeds/videos.xml?user=2veritasium"]

feeds = []
feeds.append(feedparser.parse(feedURLs[0]))

for feed in feeds:
    for title, post in feed.items():
        if title == "bozo":
            continue
        print(title)
        # print(type(title)) # str
        # print(type(post)) # list

        # pprint(post)

        for video in post:
            # pprint(video)
            for name, element in video.items():
                pprint(name)
                pprint(element)
            break
        break
