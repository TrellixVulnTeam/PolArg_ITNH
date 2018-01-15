class Article(object):
	def __init__(self):
		self._author = ""
		self._content = ""
		self._vector = none

	@property
	def Vector(self):
		return self._vector

	@Vector.setter
	def Vector(self, val):
		self._vector = val

	@property
	def Author(self):
		return self._author

	@Author.setter
	def Author(self, val):
		self._author = val

	@property
	def Content(self):
		return self._content

	@Content.setter
	def Content(self, val):
		self._content = val
