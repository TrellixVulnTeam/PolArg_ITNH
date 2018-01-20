import ArgumentVector
import IndicatorReader
import IndicatorAnalyzer


class VectorCalculator:

    def update_vectors_in_corpus(self, corpus, path_to_indicator_file):
        print("Calculating vectors for corpus")

        for article in corpus:
            self.calculate_vector(article, path_to_indicator_file)

        return corpus

    @staticmethod
    def calculate_vector(article, path_to_indicator_file):
        indicator_list = IndicatorReader.read_indicator_file(path_to_indicator_file)
        indicator_count = IndicatorAnalyzer.analyze_indicator_occurences(indicator_list, article)

        return article

    @staticmethod
    def calculate_average_vector(articles):

        sum_indicator_count = 0
        sum_average_sentence_length = 0
        sum_average_number_of_subsentences = 0
        sum_token_count = 0
        sum_stopword_to_remaining_words_ratio = 0

        for article in articles:
            sum_indicator_count = sum_indicator_count + article.vector.indicator_count
            sum_average_sentence_length = sum_average_sentence_length + article.vector.average_sentence_length
            sum_average_number_of_subsentences = sum_average_number_of_subsentences + article.vector.average_number_of_subsentences
            sum_token_count = sum_token_count + article.vector.token_count
            sum_stopword_to_remaining_words_ratio = sum_stopword_to_remaining_words_ratio + article.vector.stopword_to_remaining_words_ratio
        average_vector = ArgumentVector.init()
        average_vector.token_count(sum_token_count / articles.size)
        average_vector.indicator_count(sum_indicator_count / articles.size)
        average_vector.average_number_of_subsentences(sum_average_number_of_subsentences / articles.size)
        average_vector.average_sentence_length(sum_average_sentence_length / articles.size)
        return average_vector
