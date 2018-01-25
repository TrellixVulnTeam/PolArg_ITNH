import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorComparator
from ComparisonResult import ComparisonResult


class AnalyzationMode(object):

    @staticmethod
    def execute(path_to_analyzation_files, minimal_article_length, path_to_stopword_file, path_to_premise_file, path_to_conjunction_file, path_to_training_file_one,
                path_to_training_file_two):
        corpus = ArticleReader.ArticleReader.read_articles(path_to_analyzation_files, minimal_article_length)

        stopwordlist = StopwordFileReader.StopwordFileReader.read_stopword_file(path_to_stopword_file)
        #corpus_without_stopwords = StopwordRemover.StopwordRemover.remove_stopwords_from_corpus(stopwordlist, corpus)

        corpus = VectorCalculator.VectorCalculator.update_vectors_in_corpus(corpus,path_to_premise_file, path_to_conjunction_file)

        comparison_results = VectorComparator.VectorComparator.compare_corpus_vectors_to_training_vectors(
            corpus,
            path_to_training_file_one,
            path_to_training_file_two)

        for result in comparison_results:
            result.show_result(result)

AnalyzationMode.execute('/Users/christophmaier/Documents/Uni Passau/Text Mining Project/Spiegel-Corpus Modified',500,0,0,"VectorFile","VectorFile")