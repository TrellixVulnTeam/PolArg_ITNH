import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorFileHandler


class TrainingMode:

    @staticmethod
    def execute_training(path_to_training_files,minimal_article_length, path_to_stopword_file, path_to_indicator_file
                         , path_to_vector_file, training_file_orientation):
        articles = ArticleReader.read_articles(path_to_training_files, minimal_article_length)

        articles = StopwordRemover.remove_stopwords_from_corpus(StopwordFileReader.read_stopwordfile(path_to_stopword_file), articles)

        VectorCalculator.update_vectors_in_corpus(articles, path_to_indicator_file)

        averageVector = VectorCalculator.calculate_average_vector(articles)
        averageVector._orientation = training_file_orientation

        VectorFileHandler.safe_vector_in_file(averageVector,path_to_vector_file)



