from datetime import datetime, timedelta, timezone

LOCAL_TIMEZONE = datetime.now(timezone(timedelta(0))).astimezone().tzinfo


class VidKachel:
    def __init__(self, yt_videoid: str, media_thumbnail_url: str, yt_channelid: str, title: str, media_statistics_views: int, author: str, published: str) -> None:
        self.yt_videoid = yt_videoid
        self.media_thumbnail_url = media_thumbnail_url
        self.yt_channelid = yt_channelid
        self.title = title
        self.media_statistics_views = media_statistics_views
        self.author = author

        date_format: str = "%Y-%m-%dT%H:%M:%S%z"
        self.published = datetime.strptime(published, date_format).astimezone(LOCAL_TIMEZONE)

    def __repr__(self) -> str:
        return \
            "VidKachel: {" + \
            "\n    yt_videoid:\"" + self.yt_videoid + \
            "\"\n    media_thumbnail_url:\"" + self.media_thumbnail_url + \
            "\"\n    yt_channelid:\"" + self.yt_channelid + \
            "\"\n    title:\"" + self.title + \
            "\"\n    media_statistics_views:\"" + str(self.media_statistics_views) + \
            "\"\n    author:\"" + self.author + \
            "\"\n    published:\"" + str(self.published) + \
            "\n}"

    def views_in_thousands(self) -> str:
        return str(round(int(self.media_statistics_views)/1000, 2)) + "k views"

    def uploaded_ago(self) -> str:
        now = datetime.now(timezone(timedelta(0)))
        delta = now - self.published
        days = delta.days
        if days == 0:
            seconds = delta.seconds
            hours = seconds // (60*60)
            minutes = (seconds // 60) % 60
            return "today at " + str(hours).zfill(2) + ": " + str(minutes).zfill(2) + " on " + str(self.published.date())
        elif days > 10:
            return str(days) + " days ago on " + str(self.published.date())
        else:
            seconds = delta.seconds
            hours = seconds // (60*60)
            minutes = (seconds // 60) % 60
            return str(days) + " days ago, at " + str(hours).zfill(2) + ":" + str(minutes).zfill(2) + " on " + str(self.published.date())
