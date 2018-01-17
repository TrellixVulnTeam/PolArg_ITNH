import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorFileHandler


class TrainingMode:

    @staticmethod
    def execute_training(self, path_to_training_files, path_to_stopword_file, path_to_indicator_file, training_data_name,
                         minimal_article_length, path_to_vector_file):
        articles = ArticleReader.read_articles(path_to_training_files, minimal_article_length)

        articles = StopwordRemover.remove_stopwords_from_corpus(StopwordFileReader.read_stopwordfile(path_to_stopword_file), articles)

        #articles = #
        VectorCalculator.update_vectors_in_corpus(articles, path_to_indicator_file)

        VectorFileHandler.safe_vector_in_file(path_to_vector_file)
