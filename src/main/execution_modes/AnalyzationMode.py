from gevent import os

from main import ArticleReader, StopwordRemover, StopwordFileReader, CorpusCleaner
import VectorCalculator
import VectorComparator
import nltk

from main.result_handling import ResultFileWriter

nltk.download('stopwords')
from tagging import Tagger


class AnalyzationMode(object):

    # Analyzes each article in a given corpus and calculates vectors representing the argumentation and its complexity.
    # Compares the calculated vectors to the vectors inserted in the method and returns to which of the given
    # vectors the similarity is the best. The results are safed in the analyzation_results directory.
    #
    # path_to_analyzation_files: directory where the corpus of articles is located
    # minimal_article_length: length an article has to have to be analyzed
    # path_to_premise_file: directory where the text file with the premise indicators is located
    # path_to_conjunction_file: directory where the text file with the conjunction indicators is located
    # path_to_paratax_file: directory where the text file with the paratax indicators is located
    # path_to_hypotax_file: directory where the text file with the hypotax indicators is located
    # path_to_left_orientation_file: directory where the text file with the left wing indicators is located
    # path_to_right_orientation_file: directory where the text file with the right wing indicators is located
    # indicator_threshold: number of argumentation structures with claim/premise that is required for a text to be
    #                       recognized as argumentation
    # path_to_training_file_one: path to the training vector one
    # training_file_one_orientation: political orientation of the training vector one
    # path_to_training_file_two: path to the training vector two
    # training_file_two_orientation: political orientation of the training vector two
    # comparison_result_destination: directory where the results are safed
    # analyzation_run_name: name of the current analyzation name. The result file is named accordingly + the current date and time
    @staticmethod
    def execute(path_to_analyzation_files, minimal_article_length, path_to_premise_file,
                path_to_conjunction_file,
                path_to_paratax_file, path_to_hypotax_file, path_to_left_orientation_file,
                path_to_right_orientation_file,
                indicator_threshold,
                path_to_training_file_one,
                training_file_one_orientation,
                path_to_training_file_two,
                training_file_two_orientation,
                comparison_result_destination,
                analyzation_run_name):
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

        ResultFileWriter.ResultFileWriter.write_analyzation_results_for_whole_corpus(comparison_results,comparison_result_destination,analyzation_run_name)


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = ROOT_DIR[:-24]

premise_path = ROOT_DIR + 'resources/premise_file.txt'
conclusion_path = ROOT_DIR + 'resources/conclusion_file.txt'
paratax_path = ROOT_DIR + 'resources/paratax_file.txt'
hypotax_path = ROOT_DIR + 'resources/hypotax_file.txt'
left_orientation_path = ROOT_DIR + 'resources/Linksausgerichtet.txt'
right_orientation_path = ROOT_DIR + 'resources/Rechtsausgerichtet.txt'

comparison_result_path = ROOT_DIR + 'analyzation_results/'
test_run_name = "ResultFile"
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
    "Rechts",
    comparison_result_path,
    test_run_name)
