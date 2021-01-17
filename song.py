class Song:
	def __init__(self, title, link):
		self._title = title
		self.link = link
		self.lyrics = ''

	def __repr__(self):
		return self._title
