class Album:
	def __init__(self, title, artist, link):
		self._title = title
		self._artist = artist
		self.link = link
		self.songs = []
	
	def __repr__(self):
		return f'{self._title} - {self._artist}'
