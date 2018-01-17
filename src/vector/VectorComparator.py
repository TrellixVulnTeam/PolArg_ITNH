import math


class VectorComparator:

    @staticmethod
    def compare_corpus_vectors_to_training_vectors(self, corpus, path_to_training_files):
        comparison_results = list()

        return comparison_results

    def compare_vectors(self, vector1, vector2):
        similarity = 0.0
        print("Compare vectors...")

        inner_product = vector1.indicator_count * vector2.indicator_count
        inner_product += vector1.average_sentence_length * vector2.average_sentence_length
        inner_product += vector1.average_number_of_subsentences * vector2.average_number_of_subsentences
        inner_product += vector1.token_count * vector2.token_count

        length_vector1 = self.calculate_vector_length(vector1)
        length_vector2 = self.calculate_vector_length(vector2)

        return math.acos(inner_product / (length_vector1 * length_vector2))

    @staticmethod
    def calculate_vector_length(self, vector):
        return (vector.indicator_count * vector.indicator_count + vector.average_sentence_length *
                vector.average_sentence_length + vector.average_number_of_subsentences *
                vector.average_number_of_subsentences + vector.token_count * vector.token_count) ^ 0.5
