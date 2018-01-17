class StopwordRemover(object):

    @staticmethod
    def remove_stopwords_from_sentence(self, stopwordlist, sentence):
        print("Iterate over sentence and compare tokens with the stopwordlist. "
              "Remove token if it occurs in the stopwordlist")

        return sentence

    def remove_stopwords_from_article(self, stopwordlist, article):
        modified_article = list()
        for sentence in article:
            modified_article.append(self.remove_stopwords_from_sentence(stopwordlist, sentence))
        return modified_article

    @staticmethod
    def remove_stopwords_from_corpus(self, stopwordlist, corpus):
        modified_corpus = list()
        for article in corpus:
            modified_corpus.append(self.remove_stopwords_from_article(stopwordlist, article))
        return modified_corpus
