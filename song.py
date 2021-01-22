class Song:
	def __init__(self, album, artist, title, link):
		self._album = album
		self._artist = artist
		self._title = title
		self.link = link
		self.lyrics = ''
	
	def info(self):
		return {'album':	self._album,
				'artist':	self._artist,
				'title':	self._title,}
	
	def __repr__(self):
		return self._title
