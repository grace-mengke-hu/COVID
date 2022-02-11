# This Python file uses the following encoding: utf-8

import nltk;nltk.download('stopwords')
from nltk.corpus import stopwords

import re
import numpy as np
import pandas as pd

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

#spacy for lemmatization
import spacy

import string


def removeEmail(text):
    """
    Return a string of text without any emails.
    @type text: string
    @param text: one paragraph of text (maybe one post from one user).
    @rtype: string
    @return: clean text without any emails.
    """
    return re.sub('\S*@\S*\s?', '', text)

 
def removeNewline(text):
    """
    Remove newline character
    @type text: string
    @rtype: string
    """
    return re.sub('\s+', ' ', text)

def removeURL(text):
    return re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)

def removeSingleQuotes(text):
    """
    Remove single quotes
    @type text: string
    @rtype: string
    """
    return re.sub("\'", "", text)

def tokenizer(text):
    """
    Gensim tokenizer
    @type text: string
    @rtype: list of tokens
    """
    return gensim.utils.simple_preprocess(str(text), deacc=True)# deacc=True removes punctuations
    
def remove_pngWords(texts):
    """
    remove a_b words png name
    @type texts: list of list of tokenized words
    """
    return [[word for word in simple_preprocess(str(doc)) if not('_' in word)] for doc in texts]

def remove_stopwords(texts,stop_words):
    """
    remove stop words and words like 'a_b'
    @type texts: list of list of tokenized words
    @type stop_words: list of words
    @rtype: list of token list
    """
    return [[word for word in simple_preprocess(str(doc)) if (word not in stop_words)] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    """https://spacy.io/api/annotation"""
    nlp = spacy.load('en', disable=['parser', 'ner'])    
    texts_out = []
    for sent in texts:
            #print(sent)
        if sent: #not empty
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out
    
def preprocessing(textList):
    """
    return list of lis of one-two gram	
    """
    #stop words
    stop_words = stopwords.words('english')
    stop_words.extend(['from','subject','re','edu','use','hi','www','com','s','http','https','amp','ampersand','from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come',
#extend function words to be removed https://www.edu.uwo.ca/faculty-profiles/docs/other/webb/essential-word-list.pdf
'the','which','still','although','forty','and','up','last','past','nobody','of','out','being','himself','unless','to','would','must','seven','mine','a','when','another','eight','anybody','I','your','between','along','till','in','will','might','round','herself','you','their','both','several','twelve','that','who','five','someone','fifteen','it','some','four','whatever','beyond','for','two','around','among','whom','he','because','while','across','below','on','how','each','behind','none','we','other','under','million','nor','they','could','away','outside','more','be','our','every','nine','most','with','into','next','thousand','this','these','anything','shall','have','than','few','myself','but','any','though','themselves','as','where','since','itself','not','over','against','somebody','at','back','second','upon','what','first','nothing','thirty','so','much','without','third','there','down','during','above','or','its','six','therefore','one','should','enough','everybody','by','after','once','towards','from','those','however','thus','all','may','half','everyone','she','something','yet','near','no','three','whether','inside','his','little','everything','nineteen','do','many','until','yourself','can','why','hundred','fifty','if','before','within','whose','about','such','ten','anyone','my','off','twenty','per','her','through','either','except' ])

    #pipline: remove emails, newline character and distracting single quotes
    textList_clean = []
    for text in textList: #each text is a post
        textList_clean.append(removeSingleQuotes(removeNewline(removeEmail(removeURL(text.encode('ascii','ignore'))))))

    #Tokenize
    printable = set(string.printable)
    tokenizedList = [tokenizer(''.join(filter(lambda x: x in printable,t)) ) for t in textList_clean]

    # Build the bigram and trigram models
    bigram = gensim.models.Phrases(tokenizedList, min_count=5, threshold=100)
    # higher threshold fewer phrases.
    trigram = gensim.models.Phrases(bigram[tokenizedList], threshold=100)
    # Faster way to get a sentence clubbed as a trigram/bigram
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    def make_bigrams(texts):
        return [bigram_mod[doc] for doc in texts]

    def make_trigrams(texts):
        return [trigram_mod[bigram_mod[doc]] for doc in texts]

    def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        texts_out = []
        for sent in texts:
            if sent: #not empty
            	doc = nlp(" ".join(sent))
            	texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out
    
    #remove stopwords
    tokenizedList_noPNG = remove_pngWords(tokenizedList)#remove a_b word(png file name)
    cleanList_nostops = remove_stopwords(tokenizedList_noPNG,stop_words)
    #make bigram
    cleanList_bigram = make_bigrams(cleanList_nostops)
   
    #lammentation
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    cleanList_lemmatized = lemmatization(cleanList_bigram, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']) 
    return cleanList_lemmatized
#cleanList_bigram
