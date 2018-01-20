class TagTuple(object):
	def __init__(self, POS, Tag):
		self.__pos = POS
		self.__tag = Tag

	@property
	def POS(self):
		return self.__pos

	@property
	def Tag(self):
		return self.__tag
