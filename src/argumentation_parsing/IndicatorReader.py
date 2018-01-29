class IndicatorReader(object):

    @staticmethod
    def read_indicator_file(path_to_indicator_file):
        return IndicatorReader.cleanSentenceListFromWhitespaces(open(path_to_indicator_file,"r").read().split("-"))


    def cleanSentenceListFromWhitespaces(sentence):
        cleanedSentence = list()
        for word in sentence:
            cleanedSentence.append(word.replace(' ', ''))

        return cleanedSentence