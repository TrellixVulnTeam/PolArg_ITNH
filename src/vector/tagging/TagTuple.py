# -- coding: utf-8 --

class TagTuple(object):
	def __init__(self, Word, Tag):
		self.__word = Word
		self.__tag = Tag

	@property
	def Word(self):
		return self.__word

	@property
	def Tag(self):
		return self.__tag
