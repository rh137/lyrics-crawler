import requests as rq
from bs4 import BeautifulSoup as bs
import re

import album
import song

from utils import Thesaurus

MOJIM_DOMAIN_NAME = 'https://mojim.com/'


def mojim_search(searching_album_name='房間裡的大象', searching_artist_name='持修'):
	if searching_artist_name in Thesaurus.keys():
		searching_artist_name = Thesaurus[searching_artist_name]
	search_artist_url = f'{MOJIM_DOMAIN_NAME}{searching_artist_name}.html?t1'
	r = rq.get(search_artist_url)
	s = bs(r.text, 'html.parser')
	c = s.find_all('ul', class_='mxsh_ulz')
	# candidate artists
	li = []
	for _ in c:
		li += _.find_all('li')
	
	ret = []
	FOUND = False
	for _ in li:
		if FOUND: break
		artist_url = MOJIM_DOMAIN_NAME[:-1] + _.a['href']
		artist_name = _.a['title'].rsplit(' ', 1)[0]
		r = rq.get(artist_url)
		s = bs(r.text, 'html.parser')
		album_titles = s.find_all('span', class_='hc1')[1:]
		for span in album_titles:
			try:
				album_name = span.a.text.strip()
			except:
				continue
			if album_name in searching_album_name or searching_album_name in album_name:
				album_link = MOJIM_DOMAIN_NAME[:-1] + span.a['href']
				ret.append(album.Album(album_name, artist_name, album_link))
				FOUND = True
				break
	return ret


if __name__ == '__main__':
	mojim_search()

