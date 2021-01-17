import requests as rq
from bs4 import BeautifulSoup as bs

from album import Album


def check(name1, name2):
	return name1 in name2 or name2 in name1

def kkbox_search(album_name='房間裡的大象', artist_name='持修'):
	'''Given album name and artist name, return candidate album links'''
	url =  'https://www.kkbox.com/tw/tc/search.php?'
	params = {	'word': 	f'{album_name}+{artist_name}',
				'search':	 'album'						}
	r = rq.get(url, params=params)
	s = bs(r.text, 'html.parser')
	c = s.find_all('div', class_='height-wrap')
	ret = []
	for _ in c:
		link = 'https://www.kkbox.com' + _.h3.a['href']
		# returned album name
		abn = _.h3.a.text.strip()
		# returned artist name
		atn = _.find('span', class_='name').text.strip()

		if check(album_name, abn) and check(artist_name, atn):
			ret.append(Album(abn, atn, link))

	return ret


result = kkbox_search('')
print(result)
