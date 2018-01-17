#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import ArticleReader
from pattern.de import tag
from collections import Counter
import codecs

class Tagger(object):
    def tag_article(self, article_to_tag):
        #test code
        file = codecs.open("C:/text.txt", "r", "utf-8")
        text = file.read()
        file.close()

        print("Tagging article...")
        tagged_file = tag(text)
        return tagged_file

    def get_tag_distribution(self, article_to_tag):
        #test code
        file = codecs.open("C:/text.txt", "r", "utf-8")
        text = file.read()
        file.close()

        print("Tagging article...")
        tagged_file = tag(text)

        counts = Counter(tag for word, tag in tagged_file)
        total = sum(counts.values())
        normal = dict((word, float(count) / total) for word, count in counts.items())
        #print(normal)
        return normal
    #def get_pos_distribution(self, pos):