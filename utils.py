import requests as rq
from bs4 import BeautifulSoup as bs

from album import Album
from song import Song


KKBOX_DOMAIN_NAME = 'https://www.kkbox.com'

def check(name1, name2):
	return name1 in name2 or name2 in name1

def kkbox_search(album_name='房間裡的大象', artist_name='持修'):
	'''Given album name and artist name, return candidate albums'''
	url =  'https://www.kkbox.com/tw/tc/search.php?'
	params = {	'word': 	f'{album_name}+{artist_name}',
				'search':	 'album'						}
	r = rq.get(url, params=params)
	s = bs(r.text, 'html.parser')
	c = s.find_all('div', class_='height-wrap')
	ret = []
	for _ in c:
		link = KKBOX_DOMAIN_NAME + _.h3.a['href']
		# returned album name
		abn = _.h3.a.text.strip()
		# returned artist name
		atn = _.find('span', class_='name').text.strip()

		if check(album_name, abn) and check(artist_name, atn):
			ret.append(Album(abn, atn, link))

	return ret

def crawl_songs(album):
	'''Given album, return song names and links in the album'''
	r = rq.get(album.link)
	soup = bs(r.text, 'html.parser')
	songs = soup.find_all('tr', class_='song-item')
	for s in songs:
#		song_data = s.find('td', class_='song-data')
		song_title_a = s.find('a', class_='song-title')
		song_name = song_title_a.text.strip()
		song_link = KKBOX_DOMAIN_NAME + song_title_a['href']
		album.songs.append(Song(song_name, song_link)) 


result = kkbox_search('')
print(result)

crawl_songs(result[0])
print(result[0].songs)
