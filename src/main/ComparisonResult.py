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

    @staticmethod
    def show_result(self):
        print("Analyzation results of the article with the id: " + self._article_reference)
        print("The similarity to the policitcal orientation " + self._orientation_one_name + " is " + "%.9f" % self._orientation_one_similarity + ".")
        print("The similarity to the policitcal orientation " + self._orientation_two_name + " is " + "%.9f" % self._orientation_two_similarity + ".")

        if (self._orientation_one_similarity > self._orientation_two_similarity):
            print(self._orientation_one_name)
        else:
            print(self._orientation_two_name)