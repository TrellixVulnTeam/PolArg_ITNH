import IndicatorReader
from Article import Article


class IndicatorAnalyzer(object):

    @staticmethod
    def analyze_argumentation_of_succesive_sentences(premise_list, conjunction_list, article):
        indicator_occurences = 0

        sentences = article.content.split(".")
        lastSentence = ""

        for sentence in sentences:
            sentenceList = IndicatorAnalyzer.cleanListFromUnwantedStrings(sentence.split(" "))
            sentenceList = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(sentenceList)

            premise_list = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(premise_list)
            conjunction_list = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(conjunction_list)

            if lastSentence is not "":
                for word in sentenceList:
                    for conjunction in conjunction_list:
                        if conjunction == word:
                            article._contains_argumentation = True
                            indicator_occurences = indicator_occurences + 1

            for word in sentenceList:
                for premise in premise_list:
                    if premise == word:
                        indicator_occurences = indicator_occurences + 1
                        lastSentence = sentence

                for conjunction in conjunction_list:
                    if conjunction == word:
                        indicator_occurences = indicator_occurences + 1

        return indicator_occurences

    @staticmethod
    def analyze_indicator_occurences(indicator_list_one, indicator_list_two, indicator_threshold, article):
        indicator_occurences = 0

        sentences = article.content.split(".")


        for sentence in sentences:
            sentenceList = IndicatorAnalyzer.cleanListFromUnwantedStrings(sentence.split(" "))
            sentenceList = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(sentenceList)

            indicator_list_one = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(indicator_list_one)
            indicator_list_two = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(indicator_list_two)

            for word in sentenceList:
                for premise in indicator_list_one:
                    if premise == word:
                        indicator_occurences = indicator_occurences + 1
                        lastSentence = sentence

                for conjunction in indicator_list_two:
                    if conjunction == word:
                        indicator_occurences = indicator_occurences + 1

        return indicator_occurences


    def cleanListFromUnwantedStrings(sentence):
        unwanted = list()
        unwanted.append('\n')
        unwanted.append('')

        return [word for word in sentence if word not in unwanted]

    def cleanSentenceListFromWhitespaces(sentence):
        cleanedSentence = list()
        for word in sentence:
            cleanedSentence.append(word.replace(' ', ''))

        return cleanedSentence