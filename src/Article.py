class Article(object):
    def __init__(self):
        self._id = ""
        self._author = ""
        self._content = ""
        self._vector = none

    @property
    def _id(self):
        return self._id

    @_id.setter
    def _id(self, val):
        self._id = val

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, val):
        self._vector = val

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, val):
        self._author = val

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, val):
        self._content = val
