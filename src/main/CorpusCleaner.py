

# Cleans the corpus from empty articles and articles without argumentation
class CorpusCleaner():

    @staticmethod
    def clean_corpus_from_empty_articles(corpus):
        cleaned_corpus = list()

        for article in corpus:
            if article.content is not None:
                cleaned_corpus.append(article)

        return cleaned_corpus


    @staticmethod
    def clean_corpus_from_non_argumentation_articles(corpus):
        cleaned_corpus = list()

        for article in corpus:
            if article._contains_argumentation is True:
                cleaned_corpus.append(article)


        return cleaned_corpus