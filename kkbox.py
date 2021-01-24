import requests as rq
from bs4 import BeautifulSoup as bs
import re

import album_class
import song_class


KKBOX_DOMAIN_NAME = 'https://www.kkbox.com'


Thesaurus = {
	"蘇聖育Organ 3樂團": "Shen Yu Su",
	"JSheon": "J.Sheon",
	"熊仔 & 豹子膽": "熊仔&豹子膽",
	"LEO37 & SOSS": "LEO37+SOSS",
	"焦安溥": "張懸",
	"福爾摩沙任務爵士樂團 Mission Formosa": "福爾摩沙任務爵士樂團",
	"舒米恩．魯碧": "舒米恩",
	"Miss Ko 葛仲珊": "葛仲珊",
	"阿洛˙卡力亭˙巴奇辣": "Ado",
	"陳修澤": "那我懂你意思了",	
	"袁興緯": "",
	"林生祥": "生祥",
	}



def _check(name1, name2):
	n1, n2 = name1.lower().replace(' ', ''), name2.lower().replace(' ', '')
	if n1 in n2 or n2 in n1: return True
	n2 = name2.lower().replace(' & ', '與').replace(' ', '')
	if n1 in n2 or n2 in n1: return True
	n1 = ''.join(re.split('\W|_', n1))
	n2 = ''.join(re.split('\W|_', n2))
	if n1 in n2 or n2 in n1: return True
	if name2 in Thesaurus.keys():
		n2_ = Thesaurus[name2].lower()
		print(name1, name2, n2_)
		if n1 in n2_ or n2_ in n1:
			print('n1')
			return True
	return False


def kkbox_search(searching_album_name='房間裡的大象', searching_artist_name='持修'):
	'''Given album name and artist name, return candidate albums'''
	url =  'https://www.kkbox.com/tw/tc/search.php?'
	if searching_artist_name in Thesaurus.keys():
		searching_artist_name = Thesaurus[searching_artist_name]
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
		
		if '搶先聽' in album_name: continue

		if  _check(album_name, searching_album_name)\
			and _check(artist_name, searching_artist_name):
			ret.append(album_class.Album(album_name, artist_name, album_link))

	return ret


def kkbox_crawl_songs(album):
	'''crawl songs into a given Album object'''
	r = rq.get(album.link)
	soup = bs(r.text, 'html.parser')
	songs = soup.find_all('tr', class_='song-item')
	for s in songs:
		song_title_a = s.find('a', class_='song-title')
		song_name = song_title_a.text.strip()
		song_link = KKBOX_DOMAIN_NAME + song_title_a['href']
		album.songs.append(song_class.Song(album.title(), album.artist(), song_name, song_link)) 


def kkbox_crawl_lyrics(song):
	'''crawl lyrics into a given Song object; store the lyrics as files'''
	r = rq.get(song.link)
	s = bs(r.text, 'html.parser')
	try:
		lyrics = s.find('p', class_='lyrics').text
	except:
		lyrics = ''
	song.lyrics = lyrics




if __name__ == '__main__':
	result = kkbox_search('失物之城', '許哲珮')
	print(result)
	
	if len(result) == 1:
		crawl_songs(result[0])
		print(result[0].songs)

		for s in result[0].songs:
			crawl_lyrics(s)
