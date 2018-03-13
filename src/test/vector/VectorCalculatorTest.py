import unittest

import VectorCalculator
from ArgumentVector import ArgumentVector
from main.Article import Article


class VectorCalculatorTest(unittest.TestCase):
    vector_1 = ArgumentVector()
    vector_1.token_count = 1
    vector_1.premise_conclusion_count = 1
    vector_1.paratax_hypotax_count = 1
    vector_1.right_words_counter = 1
    vector_1.left_words_counter = 1
    vector_1.indicator_count = 1
    vector_1.stopword_to_remaining_words_ratio = 1
    vector_1.average_number_of_subsentences = 1
    vector_1.average_sentence_length = 1

    vector_2 = ArgumentVector()
    vector_2.token_count = 2
    vector_2.premise_conclusion_count = 2
    vector_2.paratax_hypotax_count = 2
    vector_2.right_words_counter = 2
    vector_2.left_words_counter = 2
    vector_2.indicator_count = 2
    vector_2.stopword_to_remaining_words_ratio = 2
    vector_2.average_number_of_subsentences = 2
    vector_2.average_sentence_length = 2

    vector_3 = ArgumentVector()
    vector_3.token_count = 3
    vector_3.premise_conclusion_count = 3
    vector_3.paratax_hypotax_count = 3
    vector_3.right_words_counter = 3
    vector_3.left_words_counter = 3
    vector_3.indicator_count = 3
    vector_3.stopword_to_remaining_words_ratio = 3
    vector_3.average_number_of_subsentences = 3
    vector_3.average_sentence_length = 3

    article_1 = Article()
    article_1.vector = vector_1

    article_2 = Article()
    article_2.vector = vector_2

    article_3 = Article()
    article_3.vector = vector_3

    corpus_for_average_vector_calculation = [article_1,article_2,article_3]

    expected_average_vector = ArgumentVector()
    expected_average_vector.token_count = 2
    expected_average_vector.premise_conclusion_count = 2
    expected_average_vector.paratax_hypotax_count = 2
    expected_average_vector.right_words_counter = 2
    expected_average_vector.left_words_counter = 2
    expected_average_vector.indicator_count = 2
    expected_average_vector.stopword_to_remaining_words_ratio = 2
    expected_average_vector.average_number_of_subsentences = 2
    expected_average_vector.average_sentence_length = 2

    def test_calculate_average_vector(self):
        calculated_average_vector = VectorCalculator.VectorCalculator.calculate_average_vector(self.corpus_for_average_vector_calculation)

        self.assertTrue(self.expected_average_vector.equals(calculated_average_vector))

    if __name__ == '__main__':
        unittest.main()