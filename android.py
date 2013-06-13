#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import __main__
import datetime
import codecs
import sys
import os

urls = {
	'top_paid_in_games': 'https://play.google.com/store/apps/category/GAME/collection/topselling_paid?start=%(start)d&num=24',
	"top_free_in_games": 'https://play.google.com/store/apps/category/GAME/collection/topselling_free?start=%(start)d&num=24'
}
rank = 1

d = datetime.datetime.today()
date_str = d.strftime('%Y%m%d%H%M')

def get():
	for key in urls.keys():
		parse_rank(urls[key], key)

def parse_rank(url, name):
	file_name = name + '_' + date_str + '.txt'
	file_path = os.path.join(os.path.dirname(__file__), 'dist', 'android', file_name)
	file = codecs.open(file_path, 'w', 'utf-8')
	print('parse ' + name + " start...")
	for i in range(20):
		sys.stdout.write('\r page %d parsing...' %(i))
		response = urllib2.urlopen(url % {'start': i * 24})
		html = response.read()
		parse_page(file, html)

	print("")
	file.close()
	__main__.rank = 1

def parse_page(file, html):
	soup = BeautifulSoup(html)
	aTags = soup.findAll('a')
	for tag in aTags:
		if 'class' in tag.attrs:
			if 'title' == tag['class'][0]:
				try:
					file.write('%d,%s' % (__main__.rank, tag['title']))
				except UnicodeEncodeError:
					file.write('Encode Error')
				file.write('\n')
				__main__.rank += 1

if __name__ == '__main__':
	get()
