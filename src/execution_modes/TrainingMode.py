import ArticleReader
import CorpusCleaner

import VectorCalculator
import VectorFileHandler
from StopwordRemover import StopwordRemover
from tagging.Tagger import Tagger


class TrainingMode(object):

    @staticmethod
    def execute_training(path_to_training_files,minimal_article_length, path_to_premise_file, path_to_conjunction_file
                         , path_to_vector_file, training_file_orientation):
        articles = ArticleReader.ArticleReader.read_articles(path_to_training_files, minimal_article_length)
        articles = CorpusCleaner.ArgumentVector.cleanCorpusFromEmptyArticles(articles)
        articles = Tagger.tag_corpus(articles)
        articles = StopwordRemover.StopwordRemover.remove_stopwrods_from_corpus(articles)

        VectorCalculator.VectorCalculator.update_vectors_in_corpus(articles, path_to_premise_file, path_to_conjunction_file)
        articles = CorpusCleaner.ArgumentVector.cleanCorpusFromNonArgumentationArticles(articles)

        averageVector = VectorCalculator.VectorCalculator.calculate_average_vector(articles)
        averageVector._orientation = training_file_orientation

        VectorFileHandler.VectorFileHandler.safe_vector_in_file(averageVector,path_to_vector_file)


TrainingMode.execute_training('/Users/christophmaier/Documents/Uni Passau/Text Mining Project/files/Spiegel-Corpus Modified',500,"/Users/christophmaier/PycharmProjects/PolArg/premise_file.txt","/Users/christophmaier/PycharmProjects/PolArg/conclusion_file.txt","VectorFile","generic")



