import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorComparator

class AnalyzationMode:

    @staticmethod
    def execute(path_to_training_files, path_to_stopword_file, path_to_indicator_file):
        print("Start Analyzation")
        corpus = ArticleReader.ArticleReader.read_articles(path_to_training_files)

        stopwordlist = StopwordFileReader.StopwordFileReader.read_stopword_file(path_to_stopword_file)
        corpus_without_stopwords = StopwordRemover.StopwordRemover.remove_stopwords_from_corpus(stopwordlist, corpus)

        corpus_with_vectors = VectorCalculator.VectorCalculator.update_vectors_in_corpus(corpus_without_stopwords, path_to_indicator_file)

        comparison_results = VectorComparator.VectorComparator.compare_corpus_vectors_to_training_vectors(corpus_with_vectors,
                                                                                         path_to_training_files)

        for result in comparison_results:
            print(result.show_result)
