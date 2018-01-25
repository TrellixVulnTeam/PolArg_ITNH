class ArgumentVector(object):
    def __init__(self):
        self._indicator_count = 0
        self._average_sentence_length = 0
        self._average_number_of_subsentences = 0
        self._token_count = 0
        self._stopword_to_remaining_words_ratio = 0
        self._orientation = ''
        self._left_words_counter = 0
        self._right_words_counter = 0

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
        return self._token_count

    @token_count.setter
    def token_count(self, val):
        self._token_count = val

    @property
    def stopword_to_remaining_words_ratio(self):
        return self._token_count

    @stopword_to_remaining_words_ratio.setter
    def stopword_to_remaining_words_ratio(self, val):
        self._stopword_to_remaining_words_ratio = val

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, val):
        self._orientation = val

    @property
    def left_words_counter(self):
        return self.left_words_counter

    @left_words_counter
    def left_words_counter(self, val):
        self._left_words_counter = val

    @property
    def right_words_counter(self):
        return self.right_words_counter

    @right_words_counter
    def right_words_counter(self, val):
        self._right_words_counter = val