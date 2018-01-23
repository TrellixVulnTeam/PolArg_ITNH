from ArgumentVector import ArgumentVector


class Article(object):
    def __init__(self):
        self._id = ""
        self._author = ""
        self._content = None
        self._vector = ArgumentVector()
        self._vector.__init__()
        self._tagged_content = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
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

    @property
    def tagged_content(self):
        return self._tagged_content

    @tagged_content.setter
    def tagged_content(self, val):
        self._tagged_content = val
