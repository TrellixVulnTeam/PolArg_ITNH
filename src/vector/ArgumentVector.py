class ArgumentVector(object):
    def __init__(self):
        self._indicatorCount = 0
        self._average_sentence_length = 0
        self._average_number_of_subsentences = 0
        self._tokencount = 0;

    @property
    def IndicatorCount(self):
        return self._indicatorCount

    @IndicatorCount.setter
    def IndicatorCount(self, val):
        self._indicatorCount = val

    @property
    def AverageSentenceLength(self):
        return self._average_sentence_length

    @AverageSentenceLength.setter
    def AverageSentenceLength(self, val):
        self._average_sentence_length = val

    @property
    def AverageNumberOfSubsentences(self):
        return self._average_number_of_subsentences

    @AverageNumberOfSubsentences.setter
    def AverageNumberOfSubsentences(self, val):
        self._average_number_of_subsentences = val

    @property
    def TokenCount(self):
        return self._tokencount

    @TokenCount.setter
    def TokenCount(self, val):
        self._tokencount = val