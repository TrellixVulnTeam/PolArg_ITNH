
from nltk.corpus.reader import XMLCorpusReader
from glob import glob
from lxml import etree as ET
from main.Article import Article


# Parses the given Files to objects
class ArticleReader():

    # Iterates through the XML tree of the files and extracts the relevant information
    # SAves the information in article objects
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
                for metadaten in elem.iter(tag='metadaten'):
                    for id in metadaten.iter(tag='artikel-id'):
                        add_article.id = id.text
                for metadaten in elem.iter(tag='inhalt'):
                    if metadaten.tag is None:
                        break
                    for child in metadaten.iter(tag='text'):
                        if child.tag is None:
                            break
                        for titel_liste in child.iter(tag='titel-liste'):
                            for title in titel_liste.iter(tag='titel'):
                                add_article.title = title.text
                        article_text = ""
                        for text in child.iter(tag='absatz'):
                            if text.text is None:
                                break
                            if text is not None:
                                article_text += text.text
                        if len(article_text) > article_length:
                            add_article.content = article_text
                articles.append(add_article)
       
        return articles
