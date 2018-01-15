import math


class VectorComparator:

    def compareCorpusVectorsToTrainingVectors(self,corpus,pathToTrainingFiles):
        comparisonResults = list()

        return comparisonResults

    def compareVectors(self, vector1, vector2):
        similarity = 0.0
        print("Compare vectors...")

        innerProduct = vector1.IndicatorCount * vector2.IndicatorCount
        innerProduct = innerProduct + vector1.AverageSentenceLength * vector2.AverageSentenceLength
        innerProduct = innerProduct + vector1.AverageNumberOfSubsentences * vector2.AverageNumberOfSubsentences
        innerProduct = innerProduct + vector1.TokenCount * vector2.TokenCount

        lengthVector1 = self.calculateVectorLength(vector1)
        lengthVector2 = self.calculateVectorLength(vector2)

        return math.acos(innerProduct / (lengthVector1 * lengthVector2))

    def calculateVectorLength(self, vector):
        return (vector.IndicatorCount * vector.IndicatorCount + vector.AverageSentenceLength * vector.AverageSentenceLength + vector.AverageNumberOfSubsentences * vector.AverageNumberOfSubsentences + vector.TokenCount * vector.TokenCount) ^ 0.5
