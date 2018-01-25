class IndicatorAnalyzer(object):

    @staticmethod
    def analyze_indicator_occurences(premise_list,conjunction_list,article):
        indicator_occurences = 0

        sentences = article.content.split(".")
        lastSentence = ""

        for sentence in sentences:
            if lastSentence is not "":
                for word in sentence.split(" "):
                    if conjunction_list.contains(word):
                        article._contains_argumentation = True
                        indicator_occurences = indicator_occurences + 1

            for word in sentence.split(" "):
                if premise_list.contains(word):
                    indicator_occurences = indicator_occurences + 1
                    lastSentence = sentence

                if conjunction_list.contains(word):
                    indicator_occurences = indicator_occurences + 1

        return indicator_occurences
