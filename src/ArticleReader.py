class ArticleReader(object):
    #Anmerkung C: Pfade beim Methodenaufruf übergeben. Evtl sinnvoll die Artikel in Sätze zu splitten und eine Liste
    #von Sätzen im Article Objekt zu speichern?
    def readArticles(self):
        from glob import glob
        from nltk.corpus import XMLCorpusReader

        texts_online = glob('C:/Users/Paul/Desktop/Vorläufiger Corpus/Online/*')
        texts_magazine = glob('C:/Users/Paul/Desktop/Vorläufiger Corpus/Magazin/*')
        years_online = []
        years_magazine = []
        for text in texts_online:
            if text.endswith('.xml'):
                years_online += glob(text)
        for text in texts_magazine:
            if text.endswith('.xml'):
                years_magazine += glob(text)

        reader_online = XMLCorpusReader('C:/Users/Paul/Desktop/Vorläufiger Corpus', years_online)
        reader_magazine = XMLCorpusReader('C:/Users/Paul/Desktop/Vorläufiger Corpus', years_magazine)

        articles = []

        for fileid in reader_online.fileids():
            words = reader_online.words(fileid)
            string = ' '.join(words)
            article_list = string.split('PMGSPON')
            for article in article_list:
                articles.append(article)
            print(len(article_list))
        # an example for the magazine corpus
        for fileid in reader_magazine.fileids():
            words = reader_magazine.words(fileid)
            string = ' '.join(words)
            article_list = string.split('SP DER SPIEGEL')
            for article in article_list:
                articles.append(article)
            print(len(article_list))

        politic = [article for article in articles if article.__contains__('Politik')]
        print(len(articles))
        print(len(politic))
        return politic


