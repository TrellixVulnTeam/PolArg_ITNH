import codecs
from nltk.corpus import stopwords


class StopwordRemover(object):
    def remove_stopwords_from_article(self, article):
        stop_words = set(stopwords.words('german'))
        # stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{','}'])
        removed_stopword_list = [i for i in article.tagged_content if i.Word not in stop_words]
        article.tagged_content = removed_stopword_list

    def stopword_to_remaining_words_ratio(self, article):
        return len(article.tagged_content) / len(article.content)

    # @staticmethod
    # def remove_stopwords_from_sentence(self, stopwordlist, sentence):
    #     print("Iterate over sentence and compare tokens with the stopwordlist. "
    #           "Remove token if it occurs in the stopwordlist")
    #
    #     return sentence
    #
    # def remove_stopwords_from_article(self, stopwordlist, article):
    #     modified_article = list()
    #     for sentence in article:
    #         modified_article.append(self.remove_stopwords_from_sentence(stopwordlist, sentence))
    #     return modified_article
    #
    # @staticmethod
    # def remove_stopwords_from_corpus(self, stopwordlist, corpus):
    #     modified_corpus = list()
    #     for article in corpus:
    #         modified_corpus.append(self.remove_stopwords_from_article(stopwordlist, article))
    #     return modified_corpus
