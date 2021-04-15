import time
import csv
import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 

from numpy import dot
from numpy.linalg import norm
import numpy as np


def preprocess_doc(document):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    output=''
    for char in document:
        if char.isdigit() or char in punctuations:
            output=output+''
        else:
            output=output+char.lower()
    return output

# On initialise TFIDF, il faut séparer cette étape du reste car elle prend quelques secondes et c'est couteux lors de Q5
def initilialize_tfidf(documents,ids):
    time1=time.time()
    stop_words = set(stopwords.words('english')) # Les abstracts sont à grande majorité en anglais
    cv = CountVectorizer(stop_words=stop_words)
    data = cv.fit_transform(documents).toarray()
    vocab = cv.get_feature_names()
    doc_term_matrix = pd.DataFrame(data=data,columns=vocab).transpose()
    doc_term_matrix.columns=ids
    
    #                                             IDF transformer
 
    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True) 
    tfidf_transformer.fit(data)

    # matrice terme-document 
    df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])  

    count_vector=cv.transform(documents) 
 
    # tf-idf scores 
    tf_idf_vector=tfidf_transformer.transform(count_vector) 
    feature_names = cv.get_feature_names() 
    time4=time.time()
    df_tfidf=tf_idf_vector.T.todense()
    df_tfidf = pd.DataFrame(df_tfidf, index=feature_names, columns=ids)
    return df_tfidf

start=time.time()
with open('abstracts.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
documents=[]
ids=[]

for i in range(len(data)):
    abstract=data[i][4]
    #abstract = preprocess(abstract)
    documents.append(abstract)
    ids.append(data[i][1])

vect=initilialize_tfidf(documents,ids)
print(vect)
print('Execution time :'+str(time.time()-start))




