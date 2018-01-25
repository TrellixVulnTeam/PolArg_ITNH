import IndicatorReader


class PoliticalDirection(object):
    def compare_with_left_words(path_to_left_file, corpus):
        left_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_left_file)
        for article in corpus:
            counter = 0
            for word in article.content:
                for left in left_list:
                    if word is left:
                        counter += 1

            article.vector.left_words_counter = counter

    def compare_with_right_words(path_to_right_file, corpus):
        right_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_right_file)
        for article in corpus:
            counter = 0
            for word in article.content:
                for right in right_list:
                    if word is right:
                        counter += 1

            article.vector.right_words_counter = counter

