import ArgumentVector
import IndicatorReader
import IndicatorAnalyzer
from StopwordRemover import StopwordRemover
from TokenCounter import TokenCounter


class VectorCalculator:

    def update_vectors_in_corpus(corpus, path_to_premise_file, path_to_conjunction_file, path_to_paratax_file, path_to_hypotax_file, indicator_threshold):
        print("Calculating vectors for corpus")

        premise_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_premise_file)
        conjunction_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_conjunction_file)

        paratax_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_premise_file)
        hypotax_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_premise_file)

        for article in corpus:
            VectorCalculator.calculate_vector(article, premise_list, conjunction_list, paratax_list, hypotax_list, indicator_threshold)

        return corpus

    @staticmethod
    def calculate_vector(article, premise_list, conjunction_list, paratax_list, hypotax_list, indicator_threshold):

        premise_conclusion_count = IndicatorAnalyzer.IndicatorAnalyzer.analyze_argumentation_of_succesive_sentences(premise_list,conjunction_list, article)
        paratax_hypotax_count = IndicatorAnalyzer.IndicatorAnalyzer.analyze_argumentation_of_succesive_sentences(paratax_list,hypotax_list, article)


        if premise_conclusion_count + paratax_hypotax_count < indicator_threshold:
            return

        article._contains_argumentation = True

        vector = ArgumentVector.ArgumentVector()

        vector.token_count = TokenCounter.count_article_tokens(article)
        vector.average_sentence_length = TokenCounter.count_average_sentence_length(article)
        vector.average_number_of_subsentences = TokenCounter.count_number_of_sub_sentences(article)
        #vector.stopword_to_remaining_words_ratio = StopwordRemover.stopword_to_remaining_words_ratio(article)

        article.vector = vector
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
        average_vector = ArgumentVector.ArgumentVector()
        average_vector._token_count = sum_token_count / len(articles)
        average_vector._indicator_count = sum_indicator_count / len(articles)
        average_vector._average_number_of_subsentences = sum_average_number_of_subsentences / len(articles)
        average_vector._average_sentence_length = sum_average_sentence_length / len(articles)
        return average_vector
