class TrainingMode:

    def executeTraining(self, pathToTrainingFiles, pathToStopwordFile, pathToIndicatorFile,trainingdataname):
        print("Start training")
        print("Read training files...")
        articles = getattr(ArticleReader(), 'readArticles')(pathToTrainingFiles)

        stopwordlist = getattr(StopwordFileReader,'readStopwordFile')(pathToStopwordFile)
        articles = getattr(StopwordRemover,'removeStopwordsFromCorpus')(stopwordlist,articles)

        articles = getattr(VectorCalculator,'updateVectorsInCorpus')(articles,pathToIndicatorFile)

        getattr(VectorFileHandler,'saveAverageVector')(articles,trainingdataname)

        return