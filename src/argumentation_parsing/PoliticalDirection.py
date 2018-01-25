import IndicatorReader


class PoliticalDirection(object):
    def compare_with_indicator_words(path_to_left_file, path_to_right_file, corpus):
        left_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_left_file)
        right_list = IndicatorReader.IndicatorReader.read_indicator_file(path_to_right_file)

