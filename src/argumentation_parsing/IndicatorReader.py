class IndicatorReader(object):

    @staticmethod
    def read_indicator_file(path_to_indicator_file):
        return open(path_to_indicator_file).split("-")
