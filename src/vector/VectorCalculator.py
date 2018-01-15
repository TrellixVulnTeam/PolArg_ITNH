import ArgumentVector
import IndicatorReader
import IndicatorAnalyzer


class VectorCalculator:

    def updateVectorsInCorpus(self,corpus,pathToIndicatorFile):
        print("Calculating vectors for corups")

        for article in corpus:
            self.calculateVector(article, pathToIndicatorFile)

        return corpus


    def calculateVector(self,article,pathToIndicatorFile):
        indicatorList = IndicatorReader.readIndicatorFile(pathToIndicatorFile)
        indicatorCount = IndicatorAnalyzer.analyzeIndicatorOccurences(indicatorList,article)

        return article


    def calculateAverageVector(self,articles):
        sumTokenCount = 0
        sumIndicatorCount = 0
        sumAverageSentenceLength = 0
        sumAverageNumberOfSubsentences = 0

        for article in articles:
            sumTokenCount = sumTokenCount + article.vector.tokenCount
            sumIndicatorCount = sumIndicatorCount + article.vector.indicatorCount

        averageVector = ArgumentVector.init()
        averageVector.TokenCount(sumTokenCount / articles.size)
        averageVector.IndicatorCount(sumIndicatorCount / articles.size)
        averageVector.AverageNumberOfSubsentences(sumAverageNumberOfSubsentences / articles.size)
        averageVector.AverageSentenceLength(sumAverageSentenceLength / articles.size)
        return averageVector