import pickle

class VectorFileHandler:

    @staticmethod
    def read_vector_from_file(path_to_vector_file):
        pickle_in = open(path_to_vector_file,"rb")
        vector_from_file = pickle.load(pickle_in)

        return vector_from_file

    @staticmethod
    def safe_vector_in_file(vector, path_to_vector_file):
        pickle_out = open(path_to_vector_file,"wb")
        pickle.dump(vector,pickle_out)
        pickle_out.close()
        print("Vector safed in File!")
