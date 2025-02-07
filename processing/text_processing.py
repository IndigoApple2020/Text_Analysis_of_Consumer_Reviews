"""
Package for text processing. 

This package performs generic text preprocessing operations like tokenization,
clean text from numbers, stopwords
"""

import string
import nltk
from typing import List
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer, PorterStemmer

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

punct_ls = list(string.punctuation)
punct_ls.extend([2*x for x in list(string.punctuation)])
punct_ls.extend([3*x for x in list(string.punctuation)])


def remove_stopwords(text: List['str'],
                     stpwds_ls: List['str']) -> List['str']:
    return [token for token in text if token not in stpwds_ls]


def remove_punctuation(text: List['str'],
                       punct_ls: List['str']) -> List['str']:
    return [token for token in text if token not in punct_ls]


def remove_numbers(text: List['str']) -> List['str']:
    return [token for token in text if not token.isdigit()]


def tokenize_and_clean(text: str,
                       stopwords_ls: List[str],
                       stopwords=True,
                       punct=True,
                       numerics=True) -> List[str]:
    """
    Performs tokenizations and cleaning processes given a document/text.
    The function will always tokenize the given text but the cleaning tasks
    are optional.
    
    Parameters
    ----------
    text: 
        A document, which can be a word or sentence of arbitrary length.
    stopwords: default True
        Indicator of removing tokens that are stopwords.
    punct: 
        Indicator of removing tokens that are punctuation marks.
    numerics: 
        Indicator of removing tokens that correspond to numbers.

    Returns
    --------
         A tokenized version of 'text' with the necessary updates depending on
         the cleanup steps performed.
    """
    tokenized = nltk.word_tokenize(text, language='english')
    
    tokenized = [token.lower() for token in tokenized]

    if punct:
        tokenized = remove_punctuation(tokenized, punct_ls=punct_ls)
        
    if numerics:
        tokenized = remove_numbers(tokenized)
        
    if stopwords:
        tokenized = remove_stopwords(tokenized, stpwds_ls=stopwords_ls)

    return tokenized


def lemmatize(text: List['str'],
              pos_type = 'a') -> List['str']:
    return [lemmatizer.lemmatize(token, pos=pos_type) for token in text]


def stem(text: List['str']) -> List['str']:
    return [stemmer.stem(token) for token in text]


def sentence_to_ngram_tokens(text: str, ngram_size=2) -> List[str]:
    """
    Given a sentence as tokens, return the n-gram combinations joined by an
    underscore.
    """
    return ["_".join(w) for w in ngrams(text, ngram_size)]
    
