import codecs
from nltk.corpus import stopwords


# Removes the stopwords form the articles
# Necessary for further analyse
class StopwordRemover(object):

    # Calls the the function which removes the stopwords
    def remove_stopwrods_from_corpus(corpus):
        for article in corpus:
            StopwordRemover.remove_stopwords_from_article(article)

        return corpus

    # Removes the stopwords from the articles
    def remove_stopwords_from_article(article):
        stop_words = set(stopwords.words('german'))
        stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{','}'])
        removed_stopword_list = [i for i in article.tagged_content if i.Word not in stop_words]
        article.tagged_content = removed_stopword_list

    # Returns the ratio between the stopwords and the remaining wors in an article
    def stopword_to_remaining_words_ratio(article):
        return len(article.tagged_content) / len(article.content)
