class IndicatorAnalyzer(object):

    # Iterates over all sentences in an article. If a token in a sentence is contained in the premise list, the following
    # sentences are checked for the occurence of an token of the conjunction list.
    #
    # Returns the number subsequent occurences
    @staticmethod
    def analyze_argumentation_of_succesive_sentences(premise_list, conjunction_list, article):
        succesive_occurences = 0

        sentences = article.content.split(".")
        lastSentence = ""

        for sentence in sentences:
            sentenceList = IndicatorAnalyzer.cleanListFromUnwantedStrings(sentence.split(" "))
            sentenceList = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(sentenceList)

            if lastSentence is not "":
                for word in sentenceList:
                    for conjunction in conjunction_list:
                        if conjunction == word:
                            article._contains_argumentation = True
                            succesive_occurences = succesive_occurences + 1

            for word in sentenceList:
                for premise in premise_list:
                    if premise == word:
                        lastSentence = sentence

        return succesive_occurences

    # Iterates over all sentences in an article and returns the number of occurences of the tokens from indicator list
    # one and indicator list two
    @staticmethod
    def analyze_indicator_occurences_of_two_lists(indicator_list_one, indicator_list_two, article):
        indicator_occurences = 0

        sentences = article.content.split(".")


        for sentence in sentences:
            sentenceList = IndicatorAnalyzer.cleanListFromUnwantedStrings(sentence.split(" "))
            sentenceList = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(sentenceList)

            for word in sentenceList:
                for premise in indicator_list_one:
                    if premise == word:
                        indicator_occurences = indicator_occurences + 1
                        lastSentence = sentence

                for conjunction in indicator_list_two:
                    if conjunction == word:
                        indicator_occurences = indicator_occurences + 1

        return indicator_occurences

    # Iterates over all sentences in an article and returns the number of occurences of the tokens from indicator list
    @staticmethod
    def analyze_indicator_occurences_of_single_list(indicator_list_one, article):
        indicator_occurences = 0

        sentences = article.content.split(".")

        for sentence in sentences:
            sentenceList = IndicatorAnalyzer.cleanListFromUnwantedStrings(sentence.split(" "))
            sentenceList = IndicatorAnalyzer.cleanSentenceListFromWhitespaces(sentenceList)

            for word in sentenceList:
                for premise in indicator_list_one:
                    if premise == word:
                        indicator_occurences = indicator_occurences + 1


        return indicator_occurences

    # Removes line breaks and empty spaces from a list of strings
    @staticmethod
    def cleanListFromUnwantedStrings(sentence):
        unwanted = list()
        unwanted.append('\n')
        unwanted.append('')

        return [word for word in sentence if word not in unwanted]

    # Removes whitespaces from a list of strings
    @staticmethod
    def cleanSentenceListFromWhitespaces(sentence):
        cleanedSentence = list()
        for word in sentence:
            if word != ' ':
                cleanedSentence.append(word)

        return cleanedSentence