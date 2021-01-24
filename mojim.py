import requests as rq
from bs4 import BeautifulSoup as bs
import re

import album_class
import song_class

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
				ret.append(album_class.Album(album_name, artist_name, album_link))
				FOUND = True
				break
	return ret


def mojim_crawl_songs(album):
	r = rq.get(album.link)
	s = bs(r.text, 'html.parser')
	c = s.find_all('span', class_='hc3')
	for _ in c:
		songs = _.find_all('a')
		for song in songs:
			if  '專輯歌曲' in song['title']\
				or ('提供' in song['title'] and '謝謝您' in song['title']):
				continue
			else:
				song_name = song.text.strip()
				song_link = MOJIM_DOMAIN_NAME[:-1] + song['href']
				print(song_name, song_link, flush=True)

				album.songs.append(song_class.Song(album.title(), album.artist(), song_name, song_link))
				


if __name__ == '__main__':
	ret = mojim_search('藍寶石', '濁水溪公社')
	mojim_crawl_songs(ret[0])
	print(ret[0].songs)
