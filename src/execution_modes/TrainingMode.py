import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorFileHandler
from tagging.Tagger import Tagger


class TrainingMode(object):

    @staticmethod
    def execute_training(path_to_training_files,minimal_article_length, path_to_stopword_file, path_to_premise_file, path_to_conjunction_file
                         , path_to_vector_file, training_file_orientation):
        articles = ArticleReader.ArticleReader.read_articles(path_to_training_files, minimal_article_length)
        articles = Tagger.tag_corpus(articles)
        articles = StopwordRemover.StopwordRemover.remove_stopwrods_from_corpus(articles)

        VectorCalculator.VectorCalculator.update_vectors_in_corpus(articles, path_to_premise_file, path_to_conjunction_file)

        averageVector = VectorCalculator.VectorCalculator.calculate_average_vector(articles)
        averageVector._orientation = training_file_orientation

        VectorFileHandler.VectorFileHandler.safe_vector_in_file(averageVector,path_to_vector_file)


TrainingMode.execute_training('/Users/christophmaier/Documents/Uni Passau/Text Mining Project/Spiegel-Corpus Modified',500,0,0,"VectorFile","generic")



