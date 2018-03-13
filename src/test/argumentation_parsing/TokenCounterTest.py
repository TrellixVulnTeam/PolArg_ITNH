import unittest

from main.argumentation_parsing import TokenCounter
from main.Article import Article


class IndicatorAnalyzerTest(unittest.TestCase):

    article = Article();
    article.content = "Das ist der erste Satz indem kein Indicator vorkommt. Das ist der zweite Satz in dem der Indicator da vorkommt." \
                      " Das ist der dritte Satz indem der Indicator also vorkommt."

    expected_token_count = 30
    expected_average_sentence_length = 10
    expected_number_of_sub_sentences = 0;

    def test_count_article_tokens(self):
        article_token_count = TokenCounter.TokenCounter.count_article_tokens(self.article)

        self.assertEqual(self.expected_token_count,article_token_count)

    def test_count_average_sentence_length(self):
        average_sentence_length = TokenCounter.TokenCounter.count_average_sentence_length(self.article)

        self.assertEqual(self.expected_average_sentence_length,average_sentence_length)

    def test_count_number_of_sub_sentences(self):
        number_of_subsentences = TokenCounter.TokenCounter.count_number_of_sub_sentences(self.article)

        self.assertEqual(self.expected_number_of_sub_sentences,number_of_subsentences)


    if __name__ == '__main__':
        unittest.main()