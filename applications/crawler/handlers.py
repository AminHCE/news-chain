import feedparser
from datetime import datetime

from django.utils.timezone import make_aware

from .models import News, Agency


def agency_crawler(agency):
    title_tag = agency.title_tag
    link_tag = agency.link_tag
    pub_date_tag = agency.pub_date_tag

    feed = feedparser.parse(agency.rss)
    for post in feed.entries:
        pub_date = make_aware(datetime.strptime(post[pub_date_tag], '%a, %d %b %Y %H:%M:%S %Z'))

        News.objects.get_or_create(title=post[title_tag],
                                   link=post[link_tag],
                                   pub_date=pub_date,
                                   agency=agency)


def common_crawler():
    agencies = Agency.objects.all()

    for agency in agencies:
        agency_crawler(agency)
