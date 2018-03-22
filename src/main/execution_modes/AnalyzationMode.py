from gevent import os

from main import ArticleReader, StopwordRemover, StopwordFileReader, CorpusCleaner
import VectorCalculator
import VectorComparator
import nltk
nltk.download('stopwords')
from tagging import Tagger


class AnalyzationMode(object):

    @staticmethod
    def execute(path_to_analyzation_files, minimal_article_length, path_to_premise_file,
                path_to_conjunction_file,
                path_to_paratax_file, path_to_hypotax_file, path_to_left_orientation_file,
                path_to_right_orientation_file,
                indicator_threshold,
                path_to_training_file_one,
                training_file_one_orientation,
                path_to_training_file_two,
                training_file_two_orientation):
        corpus = ArticleReader.ArticleReader.read_articles(path_to_analyzation_files, minimal_article_length)

        corpus = CorpusCleaner.CorpusCleaner.clean_corpus_from_empty_articles(corpus)
        corpus = Tagger.Tagger.tag_corpus(corpus)
        corpus = StopwordRemover.StopwordRemover.remove_stopwrods_from_corpus(corpus)

        corpus = VectorCalculator.VectorCalculator.update_vectors_in_corpus(corpus, path_to_premise_file,
                                                                   path_to_conjunction_file,
                                                                   path_to_paratax_file,
                                                                   path_to_hypotax_file,
                                                                   path_to_left_orientation_file,
                                                                   path_to_right_orientation_file,
                                                                   indicator_threshold)

        corpus = CorpusCleaner.CorpusCleaner.clean_corpus_from_non_argumentation_articles(corpus)

        comparison_results = VectorComparator.VectorComparator.compare_corpus_vectors_to_training_vectors(
            corpus,
            path_to_training_file_one,
            path_to_training_file_two)

        for result in comparison_results:
            result.show_result(result)


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = ROOT_DIR[:-24]

premise_path = ROOT_DIR + 'resources/premise_file.txt'
conclusion_path = ROOT_DIR + 'resources/conclusion_file.txt'
paratax_path = ROOT_DIR + 'resources/paratax_file.txt'
hypotax_path = ROOT_DIR + 'resources/hypotax_file.txt'
left_orientation_path = ROOT_DIR + 'resources/Linksausgerichtet.txt'
right_orientation_path = ROOT_DIR + 'resources/Rechtsausgerichtet.txt'

test_corpus_path = ROOT_DIR + "resources/LearnCorpusRight"

AnalyzationMode.execute(
    test_corpus_path,
    100,
    premise_path,
    conclusion_path,
    paratax_path,
    hypotax_path,
    left_orientation_path,
    right_orientation_path,
    2,
    "VectorFileLeft",
    "Links",
    "VectorFileRight",
    "Rechts")
