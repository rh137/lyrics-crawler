from kkbox import *
from mojim import *

def search(album_name, artist_name):
	ret = kkbox_search(album_name, artist_name)
	if len(ret) == 0:
		ret = mojim_search(album_name, artist_name)
	return ret

def crawl_songs(album):
	source_site = album.from_()
	if source_site == 'kkbox':
		kkbox_crawl_songs(album)
	elif source_site == 'mojim':
		mojim_crawl_songs(album)
	else:
		raise ValueError(f'[crawl_songs] {album.title()}: Source url is neither KKBOX nor MOJIM')

def crawl_lyrics(song):
	source_site = song.from_()
	if source_site == 'kkbox':
		kkbox_crawl_lyrics(song)
	elif source_site == 'mojim':
		mojim_crawl_lyrics(song)
	else:
		raise ValueError(f'[crawl_lyrics] {song.title()}: Source url is neither KKBOX nor MOJIM')
	
