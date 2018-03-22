class ComparisonResult(object):

    def __init__(self):
        self.article_reference = ""
        self.orientation_one_name = ""
        self.orientation_one_similarity = 0
        self.orientation_two_name = ""
        self.orientation_two_similarity = 0

    @property
    def article_reference(self):
        return self._article_reference

    @article_reference.setter
    def article_reference(self, val):
        self._article_reference = val

    @property
    def orientation_one_name(self):
        return self._orientation_one_name

    @orientation_one_name.setter
    def orientation_one_name(self, val):
        self._orientation_one_name = val

    @property
    def orientation_one_similarity(self):
        return self._orientation_one_similarity

    @orientation_one_similarity.setter
    def orientation_one_similarity(self, val):
        self._orientation_one_similarity = val

    @property
    def orientation_two_name(self):
        return self._orientation_two_name

    @orientation_two_name.setter
    def orientation_two_name(self, val):
        self._orientation_two_name = val

    @property
    def orientation_two_similarity(self):
        return self._orientation_two_similarity

    @orientation_two_similarity.setter
    def orientation_two_similarity(self, val):
        self._orientation_two_similarity = val


    def get_result(self):
        return_string = "Analyzation results of the article with the id: " + self._article_reference + "\n"
        return_string += "The similarity to the policitcal orientation " + self._orientation_one_name + " is " + "%.9f" % self._orientation_one_similarity + "."+ "\n"


        return_string += "The similarity to the policitcal orientation " + self._orientation_two_name + " is " + "%.9f" % self._orientation_two_similarity + "." + "\n"

        if (self._orientation_one_similarity > self._orientation_two_similarity):
            return_string += self._orientation_one_name + "\n"
        else:
            return_string += self._orientation_two_name + "\n"

        return return_string