import unittest

from main import CorpusCleaner
from main.Article import Article


class CorpusCleanerTest(unittest.TestCase):

    empty_content_no_argumentation_article = Article()
    empty_content_no_argumentation_article.content = None
    empty_content_no_argumentation_article._contains_argumentation = False

    random_content_true_argumentation_article = Article()
    random_content_true_argumentation_article.content = "Random content"
    random_content_true_argumentation_article._contains_argumentation = True

    random_content_false_argumentation_article = Article()
    random_content_false_argumentation_article.content = "Random content"
    random_content_false_argumentation_article._contains_argumentation = False

    corpus_to_clean = [empty_content_no_argumentation_article,random_content_true_argumentation_article,random_content_false_argumentation_article]

    cleaned_from_empty_articles_corpus = [random_content_true_argumentation_article,random_content_false_argumentation_article]
    cleand_from_non_argumentation_articles_corpus = [random_content_true_argumentation_article]

    def test_clean_corpus_from_empty_articles(self):
        cleaned_corpus = CorpusCleaner.CorpusCleaner.clean_corpus_from_empty_articles(self.corpus_to_clean)

        self.assertEqual(self.cleaned_from_empty_articles_corpus,cleaned_corpus)


    def test_clean_corpus_from_non_argumentation_articles(self):
        cleaned_corpus = CorpusCleaner.CorpusCleaner.clean_corpus_from_non_argumentation_articles(self.corpus_to_clean)

        self.assertEqual(self.cleand_from_non_argumentation_articles_corpus,cleaned_corpus)


if __name__ == '__main__':
      unittest.main()