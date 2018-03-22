from os.path import dirname

from gevent import os

from main import ArticleReader, StopwordRemover, CorpusCleaner

from main.vector import VectorCalculator
from main.vector import VectorFileHandler
import nltk
nltk.download('stopwords')
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

        for article in articles:
            article.content.lower()

        VectorCalculator.VectorCalculator.update_vectors_in_corpus(articles, path_to_premise_file,
                                                                   path_to_conjunction_file,
                                                                   path_to_paratax_file,
                                                                   path_to_hypotax_file,
                                                                   path_to_left_orientation_file,
                                                                   path_to_right_orientation_file,
                                                                   indicator_threshold)
        articles = CorpusCleaner.CorpusCleaner.clean_corpus_from_non_argumentation_articles(articles)

        averageVector = VectorCalculator.VectorCalculator.calculate_min_vector(articles)
        averageVector._orientation = training_file_orientation

        VectorFileHandler.VectorFileHandler.safe_vector_in_file(averageVector, path_to_vector_file)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = ROOT_DIR[:-24]

premise_path = ROOT_DIR + 'resources/premise_file.txt'
conclusion_path = ROOT_DIR + 'resources/conclusion_file.txt'
paratax_path = ROOT_DIR + 'resources/paratax_file.txt'
hypotax_path = ROOT_DIR + 'resources/hypotax_file.txt'
left_orientation_path = ROOT_DIR + 'resources/Linksausgerichtet.txt'
right_orientation_path = ROOT_DIR + 'resources/Rechtsausgerichtet.txt'

left_corpus_path = ROOT_DIR +  "resources/LearnCorpusLeft"
right_corpus_path = ROOT_DIR + "resources/LearnCorpusRight"


TrainingMode.execute_training(
    left_corpus_path,
    100,
    premise_path,
    conclusion_path,
    paratax_path,
    hypotax_path,
    left_orientation_path,
    right_orientation_path,
    1,
    'VectorFileLeft',
    'left')


TrainingMode.execute_training(
    right_corpus_path,
    100,
    premise_path,
    conclusion_path,
    paratax_path,
    hypotax_path,
    left_orientation_path,
    right_orientation_path,
    1,
    'VectorFileRight',
    'right')

