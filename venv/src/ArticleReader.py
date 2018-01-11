class ArticleReader:
    def readArticles(self):
        from glob import glob
        from nltk.corpus import XMLCorpusReader

        textsOnline = glob('C:/Users/Paul/Desktop/Spiegel-Corpus/Online/*')
        textsMagazin = glob('C:/Users/Paul/Desktop/Spiegel-Corpus/Magazin/*')
        articles = []
        for text in textsOnline:
            if text.endswith('.xml'):
                articles += glob(text)
        for text in textsMagazin:
            if text.endswith('.xml'):
                articles += glob(text)
        reader = XMLCorpusReader('C:/Users/Paul/Desktop/Spiegel-Corpus', articles)
        print(len(reader.fileids()))
        # An example for the online corpus
        """""
        words = reader.words(reader.fileids()[0])
        string = ' '.join(words)
        list1 = string.split('PMGSPON')
        politik = [article for article in list1 if article.__contains__('Politik')]
        print(len(list1))
        print(len(politik))
        """""
        # an example for the magazin corpus
        words2 = reader.words(reader.fileids()[17])
        string2 = ' '.join(words2)
        list2 = string2.split('SP DER SPIEGEL')
        politik2 = [article for article in list2 if article.__contains__('Politik')]
        print(len(list2))
        print(len(politik2))
