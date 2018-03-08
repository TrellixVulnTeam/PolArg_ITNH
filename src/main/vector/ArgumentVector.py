class ArgumentVector(object):
    def __init__(self):
        self.indicator_count = 0
        self.average_sentence_length = 0
        self.average_number_of_subsentences = 0
        self.token_count = 0
        self.stopword_to_remaining_words_ratio = 0
        self.orientation = ''
        self.left_words_counter = 0
        self.right_words_counter = 0
        self.paratax_hypotax_count = 0
        self.premise_conclusion_count = 0

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

    @left_words_counter.setter
    def left_words_counter(self, val):
        self._left_words_counter = val

    @property
    def right_words_counter(self):
        return self._right_words_counter

    @right_words_counter.setter
    def right_words_counter(self, val):
        self._right_words_counter = val

    @property
    def premise_conclusion_count(self):
        return self._left_words_counter

    @premise_conclusion_count.setter
    def premise_conclusion_count(self, val):
        self._premise_conclusion_count = val

    @property
    def paratax_hypotax_count(self):
        return self._paratax_hypotax_count

    @paratax_hypotax_count.setter
    def paratax_hypotax_count(self, val):
        self._paratax_hypotax_count = val


vector = ArgumentVector()
vector.premise_conclusion_count = 12
print()