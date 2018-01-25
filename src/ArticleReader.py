
from nltk.corpus.reader import XMLCorpusReader
from glob import glob
from lxml import etree as ET
from Article import Article

#Anmerkung C: Pfade beim Methodenaufruf übergeben. Evtl sinnvoll die Artikel in Sätze zu splitten und eine Liste
#von Sätzen im Article Objekt zu speichern?


class ArticleReader():
    def read_articles(loc_corpus, article_length):

        texts_online = glob(loc_corpus + '/Online/*')
        texts_magazine = glob(loc_corpus + '/Magazin/*')
        years_online = []
        years_magazine = []
        for text in texts_online:
            if text.endswith('.xml'):
                years_online += glob(text)
        for text in texts_magazine:
            if text.endswith('.xml'):
                years_magazine += glob(text)

        reader_online = XMLCorpusReader(loc_corpus, years_online)
        reader_magazine = XMLCorpusReader(loc_corpus, years_magazine)
        fileid_list = []
        for fileid in reader_magazine.fileids():
            fileid_list.append(fileid)
        for fileid in reader_online.fileids():
            fileid_list.append(fileid)

        articles = []

        for fileid in fileid_list:
            parser = ET.XMLParser(recover=True)
            tree = ET.parse(fileid, parser=parser)
            for elem in tree.iter(tag='artikel'):
                add_article = Article()
                for child in elem.iter(tag='metadaten'):
                    for id in child.iter(tag='artikel-id'):
                        add_article.id = id
                for child in elem.iter(tag='inhalt'):
                    if child.tag is None:
                        break
                    for baby in child.iter(tag='text'):
                        if baby.tag is None:
                            break
                        for titel_liste in baby.iter(tag='titel-liste'):
                            for titel in titel_liste.iter(tag='title'):
                                add_article.titel = titel
                        article_text = ""
                        for text in baby.iter(tag='absatz'):
                            if text.text is None:
                                break
                            if text is not None:
                                article_text += text.text
                        if len(article_text) > article_length:
                            add_article.content = article_text
                articles.append(add_article)
        politic = []
        """
        for article in articles:
            if article.content is not None:
                if article.content.__contains__('Politik'):
                    politic.append(article)
        """
        # print(len(articles))
        print(len(politic))
        return articles
        # return politik

    def read_articles_learn(loc_corpus, article_length):

        texts_online = glob(loc_corpus + '/*')
        texts_magazine = glob(loc_corpus + '/*')
        years_online = []
        years_magazine = []
        for text in texts_online:
            if text.endswith('.xml'):
                years_online += glob(text)
        for text in texts_magazine:
            if text.endswith('.xml'):
                years_magazine += glob(text)

        reader_online = XMLCorpusReader(loc_corpus, years_online)
        reader_magazine = XMLCorpusReader(loc_corpus, years_magazine)
        # reader_corpus = PlaintextCorpusReader(loc_corpus + '/Magazin/Corpus-Magazin', '.*', encoding='utf-16')

        articles = []
        """
        for fileid in reader_online.fileids():
            words = reader_online.words(fileid)
            string = ' '.join(words)
            article_list = string.split('PMGSPON')
            for article in article_list:
                if (len(article.split(' ')) > article_length):
                    add_article = Article()
                    add_article.content = article
                    articles.append(add_article)
            print(len(article_list))
        """
        # an example for the magazine corpus
        for fileid in reader_magazine.fileids():
            words = reader_magazine.words(fileid)
            string = ' '.join(words)
            article_list = string.split('SP DER SPIEGEL')
            for article in article_list:
                if (len(article.split(' ')) > article_length):
                    add_article = Article()
                    add_article.content = article
                    articles.append(add_article)
            print(len(article_list))
        """
        for fileid in reader_corpus.fileids():
            if len(reader_corpus.raw(fileid)) > article_length:
                articles.append(reader_corpus.raw(fileid))
                print(len(reader_corpus.raw(fileid)))
        """
        politic = [article for article in articles if article.content.__contains__('Politik')]
        print(len(articles))
        print(len(politic))
        return politic
