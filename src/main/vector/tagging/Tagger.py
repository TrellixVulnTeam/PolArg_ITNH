#!/usr/bin/env python
# -- coding: utf-8 --


from pattern.de import tag
from main.vector.tagging import TagTuple
from pattern.vector import Document


class Tagger(object):

    @staticmethod
    def tag_article(article_to_tag):
        new_list = []
        for entry in tag(article_to_tag.content):
            new_list.append(TagTuple.TagTuple(entry[0], entry[1]))
        article_to_tag.tagged_content = new_list

    def tag_corpus(corpus):
        for article in corpus:
            Tagger.tag_article(article)

        return corpus

    def get_keywords_article(article):
        tagged_content_words = ([i.Word for i in article.tagged_content if i.Tag.startswith('NN')])
        d = Document(tagged_content_words)
        k = d.keywords(top=5)
        article.keywords = k

    def get_keyword_corpus(corpus):
        for article in corpus:
            Tagger.get_keywords_article(article)

        return corpus