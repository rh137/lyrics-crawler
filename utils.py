import requests as rq
from bs4 import BeautifulSoup as bs

from album import Album
from song import Song


KKBOX_DOMAIN_NAME = 'https://www.kkbox.com'

def check(name1, name2):
	return name1 in name2 or name2 in name1


def kkbox_search(searching_album_name='房間裡的大象', searching_artist_name='持修'):
	'''Given album name and artist name, return candidate albums'''
	url =  'https://www.kkbox.com/tw/tc/search.php?'
	params = {	'word': 	f'{searching_album_name}+{searching_artist_name}',
				'search':	 'album'						}
	r = rq.get(url, params=params)
	s = bs(r.text, 'html.parser')
	c = s.find_all('div', class_='height-wrap')
	ret = []
	for _ in c:
		album_link = KKBOX_DOMAIN_NAME + _.h3.a['href']
		album_name = _.h3.a.text.strip()
		artist_name = _.find('span', class_='name').text.strip()

		if  check(album_name, searching_album_name)\
			and check(artist_name, searching_artist_name):
			ret.append(Album(album_name, artist_name, album_link))

	return ret


def crawl_songs(album):
	'''crawl songs into a given Album object'''
	r = rq.get(album.link)
	soup = bs(r.text, 'html.parser')
	songs = soup.find_all('tr', class_='song-item')
	for s in songs:
		song_title_a = s.find('a', class_='song-title')
		song_name = song_title_a.text.strip()
		song_link = KKBOX_DOMAIN_NAME + song_title_a['href']
		album.songs.append(Song(album._title, album._artist, song_name, song_link)) 


def crawl_lyrics(song):
	'''crawl lyrics into a given Song object; store the lyrics as files'''
	r = rq.get(song.link)
	s = bs(r.text, 'html.parser')
	lyrics = s.find('p', class_='lyrics').text
	song.lyrics = lyrics
	song.store_lyrics()


result = kkbox_search('')
print(result)

crawl_songs(result[0])
print(result[0].songs)

for s in result[0].songs:
	crawl_lyrics(s)
