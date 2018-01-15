# -*- coding: utf-8 -*-

import Article
import ArticleReader

from pattern.de import gender, MALE, FEMALE, NEUTRAL, parse, split
print ("Gender Katze="+gender('Katze'))

s = parse('Die Katze liegt auf der Matte.')
print(s)
for sentence in split(s):
	print (sentence)

for word in sentence.words:
	print (word.part_of_speech+" : "+word.string)
