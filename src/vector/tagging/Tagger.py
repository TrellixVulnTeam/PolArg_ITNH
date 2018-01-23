#!/usr/bin/env python
# -- coding: utf-8 --

import codecs
from collections import Counter

from pattern.de import tag
from vector.tagging.TagTuple import TagTuple


class Tagger(object):
	@staticmethod
	def tag_article(article_to_tag):
		new_list = []
		for entry in tag(article_to_tag.content):
			new_list.append(TagTuple(entry[0], entry[1]))
		article_to_tag.tagged_content = new_list
