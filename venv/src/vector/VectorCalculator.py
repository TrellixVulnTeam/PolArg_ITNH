class VectorCalculator:

    def updateVectorsInCorpus(self,corpus,pathToIndicatorFile):
        print("Calculating vectors for corups")

        for article in corpus:
            calculateVector(article,pathToIndicatorFile)

        return articles


    def calculateVector(self,article,pathToIndicatorFile):


        return article