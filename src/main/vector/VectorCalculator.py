from main.vector import ArgumentVector
from main.argumentation_parsing import IndicatorReader
from main.argumentation_parsing import IndicatorAnalyzer
from main.StopwordRemover import StopwordRemover
from main.argumentation_parsing.TokenCounter import TokenCounter


class VectorCalculator:

    def update_vectors_in_corpus(corpus, path_to_premise_file, path_to_conjunction_file, path_to_paratax_file,
                                 path_to_hypotax_file, path_to_left_orientation_file, path_to_right_orientation_file,
                                 indicator_threshold):
        print("Calculating vectors for corpus")

        premise_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_premise_file)
        conjunction_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_conjunction_file)

        paratax_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_paratax_file)
        hypotax_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_hypotax_file)

        left_orientation_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_left_orientation_file)
        right_orientation_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_right_orientation_file)

        for article in corpus:
            VectorCalculator.calculate_vector(article, premise_list, conjunction_list, paratax_list, hypotax_list,
                                              left_orientation_list, right_orientation_list, indicator_threshold)

        return corpus

    @staticmethod
    def calculate_vector(article, premise_list, conjunction_list, paratax_list, hypotax_list,
                         left_orientation_indicators, right_orientation_indicators, indicator_threshold):

        premise_conclusion_count = IndicatorAnalyzer.IndicatorAnalyzer.analyze_argumentation_of_succesive_sentences(
            premise_list, conjunction_list, article)
        paratax_hypotax_count = IndicatorAnalyzer.IndicatorAnalyzer.analyze_argumentation_of_succesive_sentences(
            paratax_list, hypotax_list, article)

        if premise_conclusion_count + paratax_hypotax_count < indicator_threshold and article._contains_argumentation is False:
            return

        article._contains_argumentation = True

        vector = ArgumentVector.ArgumentVector()

        vector.token_count = TokenCounter.count_article_tokens(article)
        vector.average_sentence_length = TokenCounter.count_average_sentence_length(article)
        vector.average_number_of_subsentences = TokenCounter.count_number_of_sub_sentences(article)
        vector.stopword_to_remaining_words_ratio = StopwordRemover.stopword_to_remaining_words_ratio(article)
        vector.premise_conclusion_count = premise_conclusion_count
        vector.paratax_hypotax_count = paratax_hypotax_count
        vector.left_words_counter = IndicatorAnalyzer.IndicatorAnalyzer.analyze_indicator_occurences_of_single_list(
            left_orientation_indicators, article)
        vector.right_words_counter = IndicatorAnalyzer.IndicatorAnalyzer.analyze_indicator_occurences_of_single_list(
            right_orientation_indicators, article)

        article.vector = vector
        return article

    @staticmethod
    def calculate_average_vector(articles):

        sum_indicator_count = 0
        sum_average_sentence_length = 0
        sum_average_number_of_subsentences = 0
        sum_token_count = 0
        sum_stopword_to_remaining_words_ratio = 0
        sum_left_words_counter = 0
        sum_right_words_counter = 0
        sum_paratax_hypotax_counter = 0

        for article in articles:
            sum_indicator_count = sum_indicator_count + article.vector.indicator_count
            sum_average_sentence_length = sum_average_sentence_length + article.vector.average_sentence_length
            sum_average_number_of_subsentences = sum_average_number_of_subsentences + article.vector.average_number_of_subsentences
            sum_token_count = sum_token_count + article.vector.token_count
            sum_stopword_to_remaining_words_ratio = sum_stopword_to_remaining_words_ratio + article.vector.stopword_to_remaining_words_ratio
            sum_left_words_counter = sum_left_words_counter  + article.vector.left_words_counter
            sum_right_words_counter = sum_right_words_counter + article.vector.right_words_counter
            sum_paratax_hypotax_counter = sum_paratax_hypotax_counter + article.vector.paratax_hypotax_count

        average_vector = ArgumentVector.ArgumentVector()
        average_vector._token_count = sum_token_count / len(articles)
        average_vector._indicator_count = sum_indicator_count / len(articles)
        average_vector._average_number_of_subsentences = sum_average_number_of_subsentences / len(articles)
        average_vector._average_sentence_length = sum_average_sentence_length / len(articles)
        average_vector.left_words_counter = sum_left_words_counter / len(articles)
        average_vector.right_words_counter = sum_right_words_counter / len(articles)
        average_vector.paratax_hypotax_count = sum_paratax_hypotax_counter / len(articles)

        return average_vector


    @staticmethod
    def calculate_max_vector(articles):

        max_indicator_count = 0
        max_average_sentence_length = 0
        max_average_number_of_subsentences = 0
        max_token_count = 0
        max_stopword_to_remaining_words_ratio = 0
        max_left_words_counter = 0
        max_right_words_counter = 0
        max_paratax_hypotax_counter = 0


        for article in articles:
            if article.vector.indicator_count > max_indicator_count:
                max_indicator_count = article.vector.indicator_count

            if article.vector.average_sentence_length > max_average_sentence_length:
                max_average_sentence_length = article.vector.average_sentence_length

            if article.vector.average_number_of_subsentences > max_average_number_of_subsentences:
                max_average_number_of_subsentences = article.vector.average_number_of_subsentences

            if article.vector.token_count > max_token_count:
                max_token_count = article.vector.token_count

            if article.vector.stopword_to_remaining_words_ratio > max_stopword_to_remaining_words_ratio:
                max_stopword_to_remaining_words_ratio = article.vector.stopword_to_remaining_words_ratio

            if article.vector.left_words_counter > max_left_words_counter:
                max_left_words_counter = article.vector.left_words_counter

            if article.vector.right_words_counter > max_right_words_counter:
                max_right_words_counter = article.vector.right_words_counter

            if article.vector.paratax_hypotax_count > max_paratax_hypotax_counter:
                max_paratax_hypotax_counter = article.vector.paratax_hypotax_count

        max_vector = ArgumentVector.ArgumentVector()
        max_vector._token_count = max_token_count
        max_vector._indicator_count = max_indicator_count
        max_vector._average_number_of_subsentences = max_average_number_of_subsentences
        max_vector._average_sentence_length = max_average_sentence_length
        max_vector.left_words_counter = max_left_words_counter
        max_vector.right_words_counter = max_right_words_counter
        max_vector.paratax_hypotax_count = max_paratax_hypotax_counter


        return max_vector

    @staticmethod
    def calculate_min_vector(articles):

        first_article = next(iter(articles or []), None)

        min_indicator_count = first_article.vector.indicator_count
        min_average_sentence_length = first_article.vector.average_sentence_length
        min_average_number_of_subsentences = first_article.vector.average_number_of_subsentences
        min_token_count = first_article.vector.token_count
        min_stopword_to_remaining_words_ratio = first_article.vector.stopword_to_remaining_words_ratio
        min_left_words_counter = first_article.vector.left_words_counter
        min_right_words_counter = first_article.vector.right_words_counter
        min_paratax_hypotax_counter = first_article.vector.paratax_hypotax_count

        for article in articles:
            if article.vector.indicator_count < min_indicator_count:
                min_indicator_count = article.vector.indicator_count

            if article.vector.average_sentence_length < min_average_sentence_length:
                min_average_sentence_length = article.vector.average_sentence_length

            if article.vector.average_number_of_subsentences < min_average_number_of_subsentences:
                min_average_number_of_subsentences = article.vector.average_number_of_subsentences

            if article.vector.token_count < min_token_count:
                min_token_count = article.vector.token_count

            if article.vector.stopword_to_remaining_words_ratio < min_stopword_to_remaining_words_ratio:
                min_stopword_to_remaining_words_ratio = article.vector.stopword_to_remaining_words_ratio

            if article.vector.left_words_counter < min_left_words_counter:
                min_left_words_counter = article.vector.left_words_counter

            if article.vector.right_words_counter < min_right_words_counter:
                min_right_words_counter = article.vector.right_words_counter

            if article.vector.paratax_hypotax_count < min_paratax_hypotax_counter:
                min_paratax_hypotax_counter = article.vector.paratax_hypotax_count

        min_vector = ArgumentVector.ArgumentVector()
        min_vector._token_count = min_token_count
        min_vector._indicator_count = min_indicator_count
        min_vector._average_number_of_subsentences = min_average_number_of_subsentences
        min_vector._average_sentence_length = min_average_sentence_length
        min_vector.left_words_counter = min_left_words_counter
        min_vector.right_words_counter = min_right_words_counter
        min_vector.paratax_hypotax_count = min_paratax_hypotax_counter

        return min_vector