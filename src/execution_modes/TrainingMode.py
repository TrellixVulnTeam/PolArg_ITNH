import ArticleReader
import StopwordFileReader
import StopwordRemover
import VectorCalculator
import VectorFileHandler


class TrainingMode:

    def executeTraining(self, pathToTrainingFiles, pathToStopwordFile, pathToIndicatorFile,trainingdataname,article_length,pathToVectorFile):
        articles = ArticleReader.read_articles(pathToTrainingFiles, article_length)

        stopwordlist = StopwordFileReader.readStopwordFile(pathToStopwordFile)
        articles = StopwordRemover.removeStopwordsFromCorpus(stopwordlist,articles)

        articles = VectorCalculator.updateVectorsInCorpus(articles,pathToIndicatorFile)

        VectorFileHandler.safeVectorInFile(pathToVectorFile)