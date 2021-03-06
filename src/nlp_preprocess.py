# -*- coding: utf-8 -*-
import pandas as pd
import math
import nltk
import re
from nltk.corpus import stopwords as all_stopwords
from nltk import word_tokenize
from nltk.corpus import stopwords
import os
from nltk.util import bigrams
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
from datetime import datetime

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

DATA_PATH = 'src/data/poly-Instagram-2011-2020.csv'

DATA = []
TITRE_DATA = []
DATE_DATA = []


# Lis l'ensemble des données
# paramètre : path pour l'emplacement du .csv
# retourne un dictionnaire composé de listes pour chaque colonne
def read_data(path):
    data_posts = {}
    data = pd.read_csv(path, low_memory=False,
                       dtype={'compte': 'string',
                              'pseudo': 'string',
                              'followers': 'string',
                              'date': 'string',
                              'types': 'string',
                              'likes': int,
                              'commentaires': int,
                              'vues': int,
                              'url': 'string',
                              'lien': 'string',
                              'titre': 'string'})

    data_posts['compte'] = data["compte"].tolist()
    data_posts['pseudo'] = data["pseudo"].tolist()
    data_posts['followers'] = data["followers"].tolist()
    data_posts['date'] = data["date"].tolist()
    data_posts['types'] = data["type"].tolist()
    data_posts['likes'] = data["likes"].tolist()
    data_posts['commentaires'] = data["commentaires"].tolist()
    data_posts['vues'] = data["vues"].tolist()
    data_posts['url'] = data["url"].tolist()
    data_posts['lien'] = data["lien"].tolist()
    data_posts['photo'] = data["photo"].tolist()
    data_posts['titre'] = data["titre"].tolist()

    return data_posts


"""# Prétraitement des titres"""

stopwords = set(stopwords.words("french"))
unwanted_special_char = {".", "«", "»", "“", "|", "[", "]", "–", "&", "”", "’", ",", "!",
                         "?", "*", "'", "\"", "/", "<", ">", ";", ":", "-", "br", ")", "(", "\'\'", "...", "``"}


# prétraite un texte en enlevant les stopwords et les caractères spéciaux non désirés
# paramètre : text en string
# retourne un texte : String
def preprocess_text(text):
    text = text.lower()
    return " ".join([token for token in nltk.word_tokenize(text) if (token not in stopwords and token not in unwanted_special_char)])


# tokenize un titre
# paramètre : titlre [String] pour un titre
# retourne une liste : List[String]
def tokenize(title):
    return re.split("\\s+", title)


# détermine si un titre est 'nan'
# paramètre : titre en string
# retourne : Boolean
def isNotNan(title):
    return not pd.isnull(title)


# retourne la liste des dates sans les heures et 'EDT' : List[String]
def getDates():
    global DATE_DATA
    dates = []
    for date in DATE_DATA:
        d = date.split(" ")
        del d[1:3]
        dates.append(d[0])

    return dates

# Intègre les # au mot associé afin d'éviter d'avoir des # comme token (idem pour le @)
# paramètres : t [string] pour un titre
# retourne le titre : string
def joinSpecialChar(t):
    t = preprocess_text(t).split(" ")
    while '#' in t:
        index_of_hashtag = t.index('#')
        t[index_of_hashtag] = ''.join(
            t[index_of_hashtag] + t[index_of_hashtag+1])
        del t[index_of_hashtag+1]
    while '@' in t:
        index_of_hashtag = t.index('@')
        t[index_of_hashtag] = ''.join(
            t[index_of_hashtag] + t[index_of_hashtag+1])
        del t[index_of_hashtag+1]

    return " ".join(list(t))


# prétraitre un titre
# paramètre : titre [string] pour un titre
# retourne un titre : string
def preprocess(title):
    text = ''
    if isNotNan(title):
        text = joinSpecialChar(title)
    return text


# retourne les ID des publications selon l'année et le mois
# paramètres : y [int] pour l'année, m [int] pour le mois
# retourne une liste d'ID : List[Int]
def getPostIDPerDate(y, m=None):
    dates = getDates()
    posts_id = []
    for i, date in enumerate(dates):
        year, month, day = date.split('-')
        if int(year) == y:
            if m != None and int(month) == m:
                posts_id.append(i)
            elif m == None:
                posts_id.append(i)
    return posts_id


# retire tous les "nan" des données
def removeNan():
    global TITRE_DATA
    for id, title in enumerate(TITRE_DATA):
        if not isNotNan(title):
            TITRE_DATA[id] = ''


"""# Listes de ngram"""

# retourne le topN des ngram selon l'année et le mois
# paramètres : y [int] pour l'année, m [int] pour le mois, n [int] pour le topN, ngram [int] pour la taille des ngram voulue
# intervalle [(2020,1), (2020,3)] pour de janvier 2020 à mars 2020
# retourne la liste de topN : List[String]
def getTopNgram(y=None, m=None, n=100, ngram=1, intervalle=None):
    global TITRE_DATA
    data = []
    posts_id = []
    vocab_1gram = {}
    vocab_2gram = {}
    if y != None:
        posts_id = getPostIDPerDate(y, m)
    elif y == None and m == None and intervalle != None:
        beg_year = intervalle[0][0]
        beg_month = intervalle[0][1]
        end_year = intervalle[1][0]
        end_month = intervalle[1][1]
        beginning_date = datetime(beg_year, beg_month, 1)
        end_date = datetime(end_year, end_month, 1)
        while beginning_date <= end_date:
            posts_id += getPostIDPerDate(beg_year, beg_month)
            if beg_month == 12:
                beg_month = 1
                beg_year += 1
            else:
                beg_month += 1
            beginning_date = datetime(beg_year, beg_month, 1)

    for id in posts_id:
        data.append(TITRE_DATA[id])
    if data == []:
        return data

    for id in posts_id:
        title_split = TITRE_DATA[id].split(" ")
        for term in title_split:
            if term not in vocab_1gram:
                vocab_1gram[term] = {'id': []}
            vocab_1gram[term]['id'].append(id)

        if ngram == 2:
            for bigram in list(bigrams(title_split)):
                b = " ".join(bigram)
                if b not in vocab_2gram:
                    vocab_2gram[b] = {'id': []}
                vocab_2gram[b]['id'].append(id)

    vectorizer = CountVectorizer(ngram_range=(
        1, ngram), tokenizer=tokenize, preprocessor=preprocess)
    X1 = vectorizer.fit_transform(data)
    features = (vectorizer.get_feature_names())

    vectorizer = TfidfVectorizer(ngram_range=(
        1, ngram), tokenizer=tokenize, preprocessor=preprocess)
    X2 = vectorizer.fit_transform(data)
    scores = (X2.toarray())

    sums = X2.sum(axis=0)

    data1 = []
    for col, term in enumerate(features):
        data1.append((term, sums[0, col]))
    ranking = pd.DataFrame(data1, columns=['term', 'rank'])
    words = (ranking.sort_values('rank', ascending=False))
    # print ("\n\nWords : \n", words.head(50)) #uncomment to show scores to each term
    topN = words["term"].tolist()[:n]
    if '' in topN:
        topN = words["term"].tolist()[:n+1]
        del topN[topN.index('')]
    return topN, vocab_1gram, vocab_2gram


# converti les date de 'string' a date
# paramètres : dataframe
def convert_dates(df):
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df


# recupere les donnees necessaires pour la heatmap des mots clés
# paramètres : la liste des topN mots, unigramme et les données globales (DATA)
def get_data_heatmap(topwords, unigram, bigram, data):
    df = pd.DataFrame(columns=['id', 'mot', 'date', 'nb_likes',
                      'nb_vues', 'nb_commentaires', 'nb_occurences'])
    for i, word in enumerate(topwords):
        if (len(word.split(' ')) == 1):
            for publication in unigram[word]['id']:
                info = {'id': i, 'mot': word, 'date': data['date'][publication], 'nb_likes': data['likes'][publication], 'nb_vues': data['vues']
                        [publication], 'nb_commentaires': data['commentaires'][publication], 'nb_occurences': len(unigram[word]['id'])}
                df = df.append(info, ignore_index=True)
        if(len(word.split(' ')) == 2):
            for publication in bigram[word]['id']:
                info = {'id': i, 'mot': word, 'date': data['date'][publication], 'nb_likes': data['likes'][publication], 'nb_vues': data['vues']
                        [publication], 'nb_commentaires': data['commentaires'][publication], 'nb_occurences': len(bigram[word]['id'])}
                df = df.append(info, ignore_index=True)
    convert_dates(df)
    df = df.sort_values(by=['id'], ascending=False)
    return(df)

# recupere les donnees necessaires pour le barchart
# paramètres : dataframe
def get_data_barchart(df):
    df = df.groupby(['mot', 'id'])['nb_occurences'].count().reset_index()
    df = df.sort_values(by=['id'], ascending=True)
    return(df)


# execute les differentes etapes afin de recuperer les donnees necessaires pour la heatmap et le barchart
# paramètres : n le nombre n de mots cles qu on souhaite recuperer, la date de debut et le fin pour l intervalle de temps
def execute_preprocess(n, beg_year, beg_month, end_year, end_month):
    global DATA
    global TITRE_DATA
    global DATE_DATA

    DATA = read_data(DATA_PATH)
    TITRE_DATA = DATA['titre']
    DATE_DATA = DATA['date']
    removeNan()
    for i, title in enumerate(TITRE_DATA):
        TITRE_DATA[i] = preprocess(title)
    topN, vocab_1gram, vocab_2gram = getTopNgram(
        n=n, ngram=2, intervalle=((beg_year, beg_month), (end_year, end_month)))

    data_heatmap_by_keywords = get_data_heatmap(
        topN, vocab_1gram, vocab_2gram, DATA)
    data_heatmap_by_keywords_by_date = data_heatmap_by_keywords.copy()
    data_heatmap_by_keywords_by_date = data_heatmap_by_keywords_by_date.groupby('mot')[
        'date'].min().reset_index()
    data_heatmap_by_keywords_by_date = data_heatmap_by_keywords_by_date.sort_values(
        by=['date'], ascending=False)
    data_heatmap_by_keywords_by_date.insert(
        loc=0, column='order_by_date', value=np.arange(len(data_heatmap_by_keywords_by_date)))
    data_heatmap_by_date = data_heatmap_by_keywords.copy()

    for i in data_heatmap_by_date.index:
        for j in data_heatmap_by_keywords_by_date.index:
            if data_heatmap_by_date['mot'][i] == data_heatmap_by_keywords_by_date['mot'][j]:
                data_heatmap_by_date['id'][i] = data_heatmap_by_keywords_by_date['order_by_date'][j]
    data_heatmap_by_date = data_heatmap_by_date.sort_values(
        by=['id'], ascending=True)

    data_barchart_by_keywords = get_data_barchart(data_heatmap_by_keywords)
    data_barchart_by_keywords = data_barchart_by_keywords.sort_values(
        by=['id'], ascending=False)
    data_barchart_by_date = get_data_barchart(data_heatmap_by_date)

    return data_heatmap_by_keywords, data_heatmap_by_date, data_barchart_by_keywords, data_barchart_by_date
