from gevent import os

from main import ArticleReader, StopwordRemover, CorpusCleaner

from main.vector import VectorCalculator
from main.vector import VectorFileHandler
from main.vector.tagging import Tagger


class TrainingMode(object):

    @staticmethod
    def execute_training(path_to_training_files, minimal_article_length, path_to_premise_file, path_to_conjunction_file,
                         path_to_paratax_file, path_to_hypotax_file, path_to_left_orientation_file,
                         path_to_right_orientation_file,
                         indicator_threshold,
                         path_to_vector_file, training_file_orientation):
        articles = ArticleReader.ArticleReader.read_articles(path_to_training_files, minimal_article_length)
        articles = CorpusCleaner.CorpusCleaner.clean_corpus_from_empty_articles(articles)
        articles = Tagger.Tagger.tag_corpus(articles)
        articles = StopwordRemover.StopwordRemover.remove_stopwrods_from_corpus(articles)

        VectorCalculator.VectorCalculator.update_vectors_in_corpus(articles, path_to_premise_file,
                                                                   path_to_conjunction_file,
                                                                   path_to_paratax_file,
                                                                   path_to_hypotax_file,
                                                                   path_to_left_orientation_file,
                                                                   path_to_right_orientation_file,
                                                                   indicator_threshold)
        articles = CorpusCleaner.CorpusCleaner.clean_corpus_from_non_argumentation_articles(articles)

        averageVector = VectorCalculator.VectorCalculator.calculate_average_vector(articles)
        averageVector._orientation = training_file_orientation

        VectorFileHandler.VectorFileHandler.safe_vector_in_file(averageVector, path_to_vector_file)

premise_path = os.path.join(os.path.dirname(__file__), 'premise_file.txt')
conclusion_path = os.path.join(os.path.dirname(__file__), 'conclusion_file.txt')
paratax_path = os.path.join(os.path.dirname(__file__), 'paratax_file.txt')
hypotax_path = os.path.join(os.path.dirname(__file__), 'hypotax_file.txt')
left_orientation_path = os.path.join(os.path.dirname(__file__), 'Linksausgerichtet.txt')
right_orientation_path = os.path.join(os.path.dirname(__file__), 'Rechtsausgerichtet.txt')



TrainingMode.execute_training(
    '/Users/PaulNikolaus/Desktop/Test Corpus',
    500,
    premise_path,
    conclusion_path,
    paratax_path,
    hypotax_path,
    left_orientation_path,
    right_orientation_path,
    1,
    'VectorFile',
    'generic')
