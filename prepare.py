import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import acquire

import pandas as pd

#exercise 1
def lower_case(string):
    '''
    function takes in string and cleans it
    '''
    lower = string.lower()
    lower = re.sub(r"[^a-z0-9'\s]", '', lower)
    lower = lower.replace('\n', ' ')
    
    return lower


# exercise 2
def tokenize(string):
    '''
    function tokenizes text
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string, return_str = True)

# exercise 3
def stem(string):
    '''
    stemms string
    '''
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    article_stemmed = ' '.join(stems)
    return article_stemmed


# exercise 4
def lemmatize(string):
    '''
    lemmatizes string
    '''
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    article_lemmatized = ' '.join(lemmas)
    return article_lemmatized

# exercise 5
def remove_stopwords(string):
    stopword_list = stopwords.words('english')
    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]
    article_without_stopwords = ' '.join(filtered_words)

    return article_without_stopwords


'''
exercise 9

a. lemmatize because it is a small dataset
b. stemming or lematizing because it is in between a large and small corpus
c. stemming because it is a large dataset and it is quicker

'''