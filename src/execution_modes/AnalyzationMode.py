import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorComparator


class AnalyzationMode:

    def execute(self, pathToTrainingFiles, pathToStopwordFile, pathToIndicatorFile):
        print("Start Analyzation")
        print("Read analyzation files...")
        corpus = ArticleReader.read_articles(pathToTrainingFiles)

        stopwordlist = StopwordFileReader.readStopwordFile(pathToStopwordFile)
        corpusWithoutStopwords = StopwordRemover.removeStopwordsFromCorpus(stopwordlist, corpus)

        corpusWithVectors = VectorCalculator.updateVectorsInCorpus(corpusWithoutStopwords, pathToIndicatorFile)

        comparisonResults = VectorComparator.compareCorpusVectorsToTrainingVectors(corpusWithVectors,pathToTrainingFiles)

        for result in comparisonResults:
            print(result.showResult)

        return