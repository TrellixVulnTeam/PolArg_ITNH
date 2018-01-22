import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorFileHandler


class TrainingMode(object):

    @staticmethod
    def execute_training(path_to_training_files,minimal_article_length, path_to_stopword_file, path_to_indicator_file
                         , path_to_vector_file, training_file_orientation):
        articles = ArticleReader.ArticleReader.read_articles(path_to_training_files, minimal_article_length)

       # articles = StopwordRemover.remove_stopwords_from_corpus(StopwordFileReader.read_stopwordfile(path_to_stopword_file), articles)

        VectorCalculator.VectorCalculator.update_vectors_in_corpus(articles, path_to_indicator_file)

        averageVector = VectorCalculator.VectorCalculator.calculate_average_vector(articles)
        averageVector._orientation = training_file_orientation

        VectorFileHandler.safe_vector_in_file(averageVector,path_to_vector_file)


TrainingMode.execute_training('C:/Users/Paul/Desktop/Vorläufiger Corpus',500,0,0,"C:/Users/Paul/Desktop/VectorFile","generic")



