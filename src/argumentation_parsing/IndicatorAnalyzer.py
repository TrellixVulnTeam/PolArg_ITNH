class IndicatorAnalyzer(object):

    @staticmethod
    def analyze_succesive_indicator_occurences(premise_list, conjunction_list, article):
        indicator_occurences = 0

        sentences = article.content.split(".")
        lastSentence = ""

        for sentence in sentences:
            sentenceList = IndicatorAnalyzer.cleanListFromUnwantedStrings(sentence.split(" "))
            sentenceList = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(sentenceList)

            if lastSentence is not "":
                for word in sentenceList:
                    for conjunction in conjunction_list:
                        if conjunction is word:
                            article._contains_argumentation = True
                            indicator_occurences = indicator_occurences + 1

            for word in sentenceList:
                for premise in premise_list:
                    if premise is word:
                        indicator_occurences = indicator_occurences + 1
                        lastSentence = sentence

                for conjunction in conjunction_list:
                    if conjunction is word:
                        indicator_occurences = indicator_occurences + 1

        return indicator_occurences

    @staticmethod
    def analyze_indicator_occurences(indicator_list_one, indicator_list_two, indicator_threshold, article):
        indicator_occurences = 0

        sentences = article.content.split(".")


        for sentence in sentences:
            sentenceList = IndicatorAnalyzer.cleanListFromUnwantedStrings(sentence.split(" "))
            sentenceList = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(sentenceList)

            for word in sentenceList:
                for premise in indicator_list_one:
                    if premise is word:
                        indicator_occurences = indicator_occurences + 1
                        lastSentence = sentence

                for conjunction in indicator_list_two:
                    if conjunction is word:
                        indicator_occurences = indicator_occurences + 1

        return indicator_occurences


    def cleanListFromUnwantedStrings(sentence):
        unwanted = list()
        unwanted.append('\n')
        unwanted.append('')

        return [word for word in sentence if word not in unwanted]

    def cleanSentenceListFromWhitespaces(sentence):
        for word in sentence:
            word.replace(' ', '')

        return sentence