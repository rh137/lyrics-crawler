class Album:
	def __init__(self, title, artist, link):
		self.__title = title
		self.__artist = artist
		self.link = link
		self.songs = []
	
	def title(self):
		return self.__title
	
	def artist(self):
		return self.__artist

	def __repr__(self):
		return f'{self.__title} - {self.__artist}'
