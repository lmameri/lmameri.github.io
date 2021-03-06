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

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

DATA_PATH = "./poly-Instagram-2011-2020.csv"

DATA = []
TITRE_DATA = []
DATE_DATA = []


# Lis l'ensemble des données
# paramètre : path pour l'emplacement du .csv
# retourne un dictionnaire composé de listes pour chaque colonne
def read_data(path) :
  data_posts = {}
  data = pd.read_csv(path, low_memory=False,
  dtype={'compte':'string', 
  'pseudo':'string',
  'followers':'string', 
  'date':'string', 
  'types':'string', 
  'likes':'string', 
  'commentaires':'string', 
  'vues':'string', 
  'url':'string', 
  'lien':'string', 
  'titre':'string' })

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
unwanted_special_char = {".", "«", "»", "“", "|", "[", "]", "–", "&", "”", "’", ",", "!", "?", "*", "'", "\"", "/", "<", ">", ";", ":", "-", "br", ")", "(", "\'\'", "...", "``"}

# prétraite un texte en enlevant les stopwords et les caractères spéciaux non désirés
# paramètre : text en string
# retourne un texte : String
def preprocess_text(text):
    text = text.lower()
    return " ".join([token for token in nltk.word_tokenize(text) if (token not in stopwords and token not in unwanted_special_char)])

# tokenize un titre
# paramètre : titlre [String] pour un titre
# retourne une liste : List[String]
def tokenize(title) :
  return re.split("\\s+", title)

# détermine si un titre est 'nan'
# paramètre : titre en string
# retourne : Boolean
def isNotNan(title) :
  return not pd.isnull(title)

# Construit dictionnaire de vocabulaire avec pour chaque ngram le nombre d'occurences et la liste des id où le ngram apparaît
# paramètres : corpus comme ensemble de titres List[String], n = 1 pour unigram et n = 2 pour bigram
# retourne un dictionnaire : {'score' : Int, 'id' : List[Int]}
def build_voc(corpus, n = 1):
  vocab = {}
  for id, text in enumerate(corpus):
    if n == 1 :
      for word in text.split(" "):
        if word != '' :
            if word not in vocab:
                vocab[word] = {'score' : 1}
                vocab[word]['id'] = []
            else:
                vocab[word]['score'] += 1
            vocab[word]['id'].append(id)
    elif n == 2 :
      for bigram in text :
        if bigram not in vocab :
          vocab[bigram] = {"score" : 1}
          vocab[bigram]['id'] = []
        else :
          vocab[bigram]['score'] += 1
        vocab[bigram]['id'].append(id)

  return vocab

# retourne la liste des dates sans les heures et 'EDT' : List[String]
def getDates() : 
  global DATE_DATA
  dates = []
  for date in DATE_DATA :
    d = date.split(" ")
    del d[1:3]
    dates.append(d[0])

  return dates

# Intègre les # au mot associé afin d'éviter d'avoir des # comme token (idem pour le @)
# paramètres : t [string] pour un titre
# retourne le titre : string
def joinHashtag(t) :
  t = preprocess_text(t).split(" ")
  while '#' in t :
    index_of_hashtag = t.index('#')
    t[index_of_hashtag] = ''.join(t[index_of_hashtag] + t[index_of_hashtag+1])
    del t[index_of_hashtag+1]
  while '@' in t :
    index_of_hashtag = t.index('@')
    t[index_of_hashtag] = ''.join(t[index_of_hashtag] + t[index_of_hashtag+1])
    del t[index_of_hashtag+1]

  return " ".join(list(t))

# prétraitre un titre
# paramètre : titre [string] pour un titre
# retourne un titre : string
def preprocess(title) :
  text = ''
  if isNotNan(title) :
    text = joinHashtag(title)
  return text

# retourne les ID des publications selon l'année et le mois
# paramètres : y [int] pour l'année, m [int] pour le mois
# retourne une liste d'ID : List[Int]
def getPostIDPerDate(y, m=None) :
  dates = getDates()
  posts_id = []
  for i, date in enumerate(dates) :
    year, month, day = date.split('-')
    if int(year) == y :
      if m != None and int(month) == m :
        posts_id.append(i)
      elif m == None :
        posts_id.append(i)
  return posts_id

# retire tous les "nan" des données
def removeNan() :
  global TITRE_DATA
  for id, title in enumerate(TITRE_DATA) :
    if not isNotNan(title) :
      TITRE_DATA[id] = ''

"""# Listes de ngram"""

# retourne le topN des ngram selon l'année et le mois
# paramètres : y [int] pour l'année, m [int] pour le mois, n [int] pour le topN, ngram [int] pour la taille des ngram voulue
# intervalle [(2020,1), (2020,3)] pour de janvier 2020 à mars 2020
# retourne la liste de topN : List[String]
def getTopNgram(y=None, m=None, n = 100, ngram = 2, intervalle = None) :
    global TITRE_DATA
    data = []
    posts_id = []
    if y != None :
      posts_id = getPostIDPerDate(y, m)
    elif y == None and m == None and intervalle != None :
        beg_year = intervalle[0][0]
        beg_month = intervalle[0][1]
        end_year = intervalle[1][0]
        end_month = intervalle[1][1]

        while beg_year <= end_year and beg_month <= end_month :
          posts_id += getPostIDPerDate(beg_year, beg_month)
          if beg_month == 12 :
            beg_month = 1
            beg_year += 1
          else :
            beg_month += 1

    for id in posts_id :
        data.append(TITRE_DATA[id])

    if data == [] : 
      return data

    vocab_1gram = build_voc(data)
    vocab_2gram = build_voc(data, n=2)

    vectorizer = CountVectorizer(ngram_range = (1, ngram), tokenizer=tokenize, preprocessor=preprocess)
    X1 = vectorizer.fit_transform(data) 
    features = (vectorizer.get_feature_names())
      
    vectorizer = TfidfVectorizer(ngram_range = (1, ngram), tokenizer=tokenize, preprocessor = preprocess)
    X2 = vectorizer.fit_transform(data)
    scores = (X2.toarray())

    sums = X2.sum(axis = 0)

    data1 = []
    for col, term in enumerate(features):
        data1.append( (term, sums[0, col] ))
    ranking = pd.DataFrame(data1, columns = ['term', 'rank'])
    words = (ranking.sort_values('rank', ascending = False))
    # print ("\n\nWords : \n", words.head(50)) #uncomment to show scores to each term
    topN = words["term"].tolist()[:n]
    if '' in topN :
      topN = words["term"].tolist()[:n+1]
      del topN[topN.index('')]
    return topN, vocab_1gram, vocab_2gram


# vocab_1gram['coronavirus']

# Récupérer la liste des ID (des publications) où un mot apparaît
# vocab_1gram['TERM']['ID']

# Récupérer par exemple le nombre de likes d'un post 
# DATA['likes'][id]
# ou la date : 
# DATA['dates'][id]

def main():
  global DATA
  global TITRE_DATA 
  global DATE_DATA 

  DATA = read_data(DATA_PATH)
  TITRE_DATA = DATA['titre']
  DATE_DATA = DATA['date']
  removeNan()
  for i, title in enumerate(TITRE_DATA) :
    TITRE_DATA[i] = preprocess(title)
  topN, vocab_1gram, vocab_2gram = getTopNgram(2020, m=8, n=20, ngram=1)

  print(topN)

if __name__ == "__main__":
    main()

"""# Unigrammes des NOUN (part of speech)"""

# import os.path
# from os import path

# if not path.exists("/content/stanford-corenlp-full-2018-02-27/stanford-french-corenlp-2018-02-27-models.jar") :
#   !wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip
#   !unzip stanford-corenlp-full-2018-02-27.zip
#   !wget https://raw.githubusercontent.com/stanfordnlp/CoreNLP/master/src/edu/stanford/nlp/pipeline/StanfordCoreNLP-french.properties 
#   !wget https://nlp.stanford.edu/software/stanford-french-corenlp-2018-02-27-models.jar
#   os.rename('/content/stanford-french-corenlp-2018-02-27-models.jar', '/content/stanford-corenlp-full-2018-02-27/stanford-french-corenlp-2018-02-27-models.jar')
#   !pip install stanfordcorenlp

# # Extraire tous les NOUN des titres
# from stanfordcorenlp import StanfordCoreNLP
# titles_NOUN = []
# with StanfordCoreNLP('stanford-corenlp-full-2018-02-27', lang='fr') as nlp:
#   for title in titre_data :
#     if not isinstance(title, float) or not math.isnan(title) :
#       titles_NOUN.append(" ".join([word for word, tag in nlp.pos_tag((preprocess_text(title))) if tag == 'NOUN']))
#     else :
#       titles_NOUN.append('')

# build_voc(titles_NOUN)
# get_n_top_occurences(vocab, 50)