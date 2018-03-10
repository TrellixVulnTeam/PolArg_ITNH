import unittest
from gevent import os

from ArgumentVector import ArgumentVector
from VectorFileHandler import VectorFileHandler


class VectorFileHandlerTest(unittest.TestCase):

    vector = ArgumentVector()
    vector.token_count = 3
    vector.premise_conclusion_count = 5
    vector.paratax_hypotax_count = 512
    vector.right_words_counter = 10
    vector.left_words_counter = 23
    vector.indicator_count = 2
    vector.stopword_to_remaining_words_ratio = 6
    vector.average_number_of_subsentences = 1
    vector.average_sentence_length = 15

    filehandler = VectorFileHandler()
    path_to_vector = "UnitTestingVector"

    def test_read_write(self):
        self.filehandler.safe_vector_in_file(self.vector,self.path_to_vector)
        read_vector = self.filehandler.read_vector_from_file(self.path_to_vector)

        self.remove_created_test_files()
        self.assertTrue(self.vector.equals(read_vector))


    def remove_created_test_files(self):
        os.remove(self.path_to_vector)


if __name__ == '__main__':
    unittest.main()