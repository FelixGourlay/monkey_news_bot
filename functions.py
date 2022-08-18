import datetime
from itertools import islice

from dateutil import parser
from pygooglenewsscraper import GoogleNews


def time_until_next_reset(dt=None, target=5):
    """messing with datetime to get a value (could be 1 line)"""
    if dt is None:
        dt = datetime.datetime.now()

    val = ((target - dt.hour - 1) * 60 * 60) + ((60 - dt.minute - 1) * 60) + (60 - dt.second)

    if val < 0:
        return 86400 + val
    else:
        return val


def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(islice(iterable, n))


def get_article_list(keyword, days=1):
    """ returns Google News results for the keyword search in the time span given"""
    gn = GoogleNews(keyword=keyword)

    raw_news = gn.get_raw_news()

    news = gn.parse_news(html=raw_news.text)

    ret_articles = {}

    for k, v in news.items():
        x = parser.parse(v['date'])
        now = datetime.datetime.now()
        delta = now - x
        if delta.days <= days:
            ret_articles[k] = v

    return ret_articles


def clean_up(articles):
    """takes the list of news, returns 4 items that don't come from chimp report or talk about monkey pox"""
    article_list = []
    i = 0

    for k, v in articles.items():
        if 'chimpreports.com' in v['publisher']:
            pass
        if 'pox' in v['title']:
            pass
        else:
            pass
            if i <= 3:
                article_list.append(v)

    return article_list


def get_chimp_news(search_term):
    raw_list = get_article_list(search_term)
    cleaned_list = clean_up(raw_list)

    return take(4, cleaned_list)
