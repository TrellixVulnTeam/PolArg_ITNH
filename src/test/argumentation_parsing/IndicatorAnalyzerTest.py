import unittest

from IndicatorAnalyzer import IndicatorAnalyzer
from main.Article import Article

class IndicatorAnalyzerTest(unittest.TestCase):

    expected_indicator_occurences = 1
    expected_indicator_occurences_of_two_list_analyzation = 2

    analyzer = IndicatorAnalyzer()
    premise_list = ["weil","da","denn","als","ja","doch"];
    conjunction_list = ["folglich", "deshalb", "also","ergo","infolgedessen","daher","eben","und so","natürlich"];
    article = Article();
    article.content = "Das ist der erste Satz indem kein Indicator vorkommt. Das ist der zweite Satz in dem der Indicator da vorkommt." \
                      "Das ist der dritte Satz indem der Indicator also vorkommt."

    sentence_to_clean_from_whitespaces = ["Das","ist","ein","Beispielsatz"," "," ","mit","zu","vielen","Leerzeichen."]
    expected_cleaned_sentence_from_whitespaces = ["Das","ist","ein","Beispielsatz","mit","zu","vielen","Leerzeichen."]

    sentence_to_clean_from_unwanted_strings = ["Das","ist","ein","Beispielsatz","\n","\n","mit","ungewollten","Zeichen."]
    expected_cleaned_sentence_from_unwanted_strings = ["Das","ist","ein","Beispielsatz","mit","ungewollten","Zeichen."]

    def test_analyze_argumentation_of_succesive_sentences(self):
        indicatorOccurences = self.analyzer.analyze_argumentation_of_succesive_sentences(self.premise_list,self.conjunction_list,self.article)

        self.assertEqual(self.expected_indicator_occurences,indicatorOccurences)

    def test_analyze_indicator_occurences_of_two_lists(self):
        indicator_occurences = self.analyzer.analyze_indicator_occurences_of_two_lists(self.premise_list,self.conjunction_list,self.article)

        self.assertEqual(self.expected_indicator_occurences_of_two_list_analyzation,indicator_occurences)

    def test_analyze_indicator_occurences_of_single_list(self):
        indicator_occurences = self.analyzer.analyze_indicator_occurences_of_single_list(self.premise_list,self.article)

        self.assertEqual(self.expected_indicator_occurences, indicator_occurences)

    def test_cleanListFromUnwantedStrings(self):
        cleaned_sentence = self.analyzer.cleanSentenceListFromWhitespaces(self.sentence_to_clean_from_whitespaces)

        self.assertEqual(self.expected_cleaned_sentence_from_whitespaces,cleaned_sentence)

    def test_cleanListFromWhitespaces(self):
        cleaned_sentence = self.analyzer.cleanListFromUnwantedStrings(self.expected_cleaned_sentence_from_unwanted_strings)

        self.assertEqual(self.expected_cleaned_sentence_from_unwanted_strings,cleaned_sentence)

if __name__ == '__main__':
    unittest.main()