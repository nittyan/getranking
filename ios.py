#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import datetime
import codecs
import os
import __main__


d = datetime.datetime.today()
date_str = d.strftime('%Y%m%d%H%M')
rank = 1

urls = {
    'iTunes_Store_Games_Top_Free':
    ('http://itunes.apple.com/jp/rss/'
        'topfreeapplications/limit=300/genre=6014/xml'),
    'iTunes_Store_Games_Top_Paid':
    ('http://itunes.apple.com/jp/rss/'
        'toppaidapplications/limit=300/genre=6014/xml'),
    'iTunes Store Top Sales':
    ('http://itunes.apple.com/jp/rss/'
        'topgrossingapplications/limit=300/genre=6014/xml')
}


def get():
    for key in urls:
        parse_rank(urls[key], key)


def parse_rank(url, name):
    print('parse ' + name + ' start...')
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read())
    entries = soup.findAll('entry')
    file_name = name + "_" + date_str + ".txt"
    file_path = os.path.join(
        os.path.dirname(__file__), 'dist', 'ios', file_name)
    file = codecs.open(file_path, 'w', 'utf-8')
    for entry in entries:
        file.write('%d,%s' % (__main__.rank, entry.find('title').text))
        file.write('\n')
        __main__.rank += 1

    file.close()
    __main__.rank = 1


if __name__ == "__main__":
    get()
