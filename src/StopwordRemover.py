class StopwordRemover(object):

    def removeStopwordsFromSentence(self, stopwordlist, sentence):
        print("Iterate over sentence and compare tokens with the stopwordlist. "
              "Remove token if it occurs in the stopwordlist")

        return sentence

    def removeStopwordsFromArticle(self, stopwordlist, article):
        modifiedArticle = list()
        for sentence in article:
            modifiedArticle.append(self.removeStopwordsFromSentence(stopwordlist,sentence))
        return modifiedArticle


    def removeStopwordsFromCorpus(self, stopwordlist, corpus):
        modifiedCorpus = list()
        for article in corpus:
            modifiedCorpus.append(self.removeStopwordsFromArticle(stopwordlist,article))
        return modifiedCorpus