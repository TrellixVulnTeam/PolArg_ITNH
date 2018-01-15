class VectorCalculator:

    def updateVectorsInCorpus(self,corpus,pathToIndicatorFile):
        print("Calculating vectors for corups")

        for article in corpus:
            calculateVector(article,pathToIndicatorFile)

        return articles


    def calculateVector(self,article,pathToIndicatorFile):
        indicatorList = getattr(IndicatorReader(),'readIndicatorFile')(pathToIndicatorFile)
        indicatorCount = getattr(IndicatorAnalyzer,'getIndicato')

        return article


    def calculateAverageVector(self,articles):
        averageTokenCount
        averageIndicatorCount

        sumTokenCount
        sumIndicatorCount

        for article in articles:
            sumTokenCount = sumTokenCount + article.vector.tokenCount
            sumIndicatorCount = sumIndicatorCount + article.vector.indicatorCount


        averageTokenCount = sumTokenCount / articles.size
        avergeIndicatorCount = sumIndicatorCount / articles.size

        averageVector = ArgumentVector.init(averageTokenCount,avergeIndicatorCount)
        return averageVector