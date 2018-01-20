class ArgumentVector(object):
    def __init__(self):
        self._indicator_count = 0
        self._average_sentence_length = 0
        self._average_number_of_subsentences = 0
        self._tokencount = 0;
        self._stopword_to_remaining_words_ratio = 0;
        self._orientation = none

    @property
    def indicator_count(self):
        return self._indicator_count

    @indicator_count.setter
    def indicator_count(self, val):
        self._indicator_count = val

    @property
    def average_sentence_length(self):
        return self._average_sentence_length

    @average_sentence_length.setter
    def average_sentence_length(self, val):
        self._average_sentence_length = val

    @property
    def average_number_of_subsentences(self):
        return self._average_number_of_subsentences

    @average_number_of_subsentences.setter
    def average_number_of_subsentences(self, val):
        self._average_number_of_subsentences = val

    @property
    def token_count(self):
        return self._tokencount

    @token_count.setter
    def token_count(self, val):
        self._tokencount = val

    @property
    def _stopword_to_remaining_words_ratio(self):
        return self._tokencount

    @_stopword_to_remaining_words_ratio.setter
    def _stopword_to_remaining_words_ratio(self, val):
        self._stopword_to_remaining_words_ratio = val

    @property
    def _orientation(self):
        return self._orientation

    @_orientation.setter
    def _orientation(self, val):
        self._orientation = val