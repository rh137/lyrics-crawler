import os

class Song:
	def __init__(self, album, artist, title, link):
		self.__album = album
		self.__artist = artist
		self.__title = title
		self.link = link
		self.lyrics = ''
	
	def store_lyrics(self):
		file_name = './lyrics/' + str(self).replace('/', '[slash]') + '.txt'
		print(file_name)
		if not os.path.isfile(file_name):
			with open(file_name, 'w') as f:
				f.write(self.lyrics)
	
	def title(self):
		return self.__title
	
	def from_(self):
		if 'kkbox' in self.link: return 'kkbox'
		if 'mojim' in self.link: return 'mojim'

	def __repr__(self):
		return f'{self.__title}_{self.__artist}_{self.__album}'
