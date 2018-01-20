class ComparisonResult(object):

    def __init__(self):
        self._article_reference = none
        self._orientation_one_name = none
        self._orientation_one_similarity = 0
        self._orientation_two_name = none
        self._orientation_two_similarity = 0

    @property
    def _article_reference(self):
        return self._article_reference

    @_article_reference.setter
    def _article_reference(self, val):
        self._article_reference = val

    @property
    def _orientation_one_name(self):
        return self._orientation_one_name

    @_orientation_one_name.setter
    def _orientation_one_name(self, val):
        self._orientation_one_name = val

    @property
    def _orientation_one_similarity(self):
        return self._orientation_one_similarity

    @_orientation_one_similarity.setter
    def _orientation_one_similarity(self, val):
        self._orientation_one_similarity = val

    @property
    def _orientation_two_name(self):
        return self._orientation_two_name

    @_orientation_two_name.setter
    def _orientation_two_name(self, val):
        self._orientation_two_name = val

    @property
    def _orientation_two_similarity(self):
        return self._orientation_two_similarity

    @_orientation_two_similarity.setter
    def _orientation_two_similarity(self, val):
        self._orientation_two_similarity = val

    @staticmethod
    def show_result():
        print("Analyzation results of the article with the id: " + ComparisonResult._article_reference)
        print("The similarity to the policitcal orientation " + ComparisonResult._orientation_one_name + " is " + ComparisonResult._orientation_one_similarity + ".")
        print("The similarity to the policitcal orientation " + ComparisonResult._orientation_two_name + " is " + ComparisonResult._orientation_two_similarity + ".")
