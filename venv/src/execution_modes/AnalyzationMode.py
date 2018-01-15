class AnalyzationMode:

    def execute(self, pathToTrainingFiles, pathToStopwordFile, pathToIndicatorFile):
        print("Start Analyzation")
        print("Read analyzation files...")
        corpus = getattr(ArticleReader(), 'readArticles')(pathToTrainingFiles)

        stopwordlist = getattr(StopwordFileReader(), 'readStopwordFile')(pathToStopwordFile)
        corpusWithoutStopwords = getattr(StopwordRemover(), 'removeStopwordsFromCorpus')(stopwordlist, corpus)

        corpusWithVectors = getattr(VectorCalculator(), 'updateVectorsInCorpus')(corpusWithoutStopwords, pathToIndicatorFile)

        comparisonResults = getattr(VectorComparator(),'compareAnalyzationVectorsToTrainingVectors')(corpusWithVectors,pathToTrainingVectors)

        for result in comparisonResults:
            print(getattr(result,'toString'))

        return