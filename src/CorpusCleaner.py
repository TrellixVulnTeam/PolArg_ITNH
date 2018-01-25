class ArgumentVector():

    def cleanCorpusFromEmptyArticles(corpus):
        cleaned_corpus = list()

        for article in corpus:
            if article.content is not None:
                cleaned_corpus.append(article)

        return cleaned_corpus


    def cleanCorpusFromNonArgumentationArticles(corpus):
        cleaned_corpus = list()

        for article in corpus:
            if article._contains_argumentation is True:
                cleaned_corpus.append(article)


        return cleaned_corpus