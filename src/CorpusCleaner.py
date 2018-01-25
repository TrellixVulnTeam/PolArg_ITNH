class ArgumentVector(object):

    def cleanCorpus(corpus):
        for article in corpus:
            if article.content is None:
                corpus.remove(article)

        return corpus