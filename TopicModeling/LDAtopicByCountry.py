import json
import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID/')
import utilFunc
import preProcessing
import pandas as pd

#import numpy as np

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

#spacy for lemmatization
import spacy
import string
import nltk;nltk.download('stopwords')
from nltk.corpus import stopwords
import pickle


prefixDir = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_merge/'
USjsonList = ['coronavirusus_Feb2Nov_2020_update2.json']
AUSjsonList = ['CoronavirusAustralia_CoronavirusDownunder_Feb2Nov_2020.json']
CANjsonList = ['CoronavirusCanada_CanadaCoronavirus_Feb2Nov_2020.json']
UKjsonList = ['CoronavirusUK_Feb2Nov_2020_update2.json']

#load raw data
data = utilFunc.loadJson(AUSjsonList,prefixDir)
#dataUS = utilFunc.loadJson(USjsonList,prefixDir)
#dataCAN = utilFunc.loadJson(CANjsonList,prefixDir)
#dataAUS = utilFunc.loadJson(AUSjsonList,prefixDir)
#dataUK = utilFunc.loadJson(UKjsonList,prefixDir)

#extract text from submissions
text = utilFunc.textData(data)


#extract utc for submissions
utc = utilFunc.submission_utc(data)

#put extracted data into dataframe
countryList = []
for t in text:
	countryList.append('AUS')
print(len(text),len(utc))
X = pd.DataFrame(data={"country":countryList,"Texts":text,"UTC":utc})
print(X.head())

#stop words
stop_words = stopwords.words('english')
stop_words.extend(['hi','www','com','s','http','https','amp','ampersand','from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come'])
#extend function words to be removed https://www.edu.uwo.ca/faculty-profiles/docs/other/webb/essential-word-list.pdf
stop_words.extend(['the','which','still','although','forty','and','up','last','past','nobody','of','out','being','himself','unless','to','would','must','seven','mine','a','when','another','eight','anybody','I','your','between','along','till','in','will','might','round','herself','you','their','both','several','twelve','that','who','five','someone','fifteen','it','some','four','whatever','beyond','for','two','around','among','whom','he','because','while','across','below','on','how','each','behind','none','we','other','under','million','nor','they','could','away','outside','more','be','our','every','nine','most','with','into','next','thousand','this','these','anything','shall','have','than','few','myself','but','any','though','themselves','as','where','since','itself','not','over','against','somebody','at','back','second','upon','what','first','nothing','thirty','so','much','without','third','there','down','during','above','or','its','six','therefore','one','should','enough','everybody','by','after','once','towards','from','those','however','thus','all','may','half','everyone','she','something','yet','near','no','three','whether','inside','his','little','everything','nineteen','do','many','until','yourself','can','why','hundred','fifty','if','before','within','whose','about','such','ten','anyone','my','off','twenty','per','her','through','either','except' ])

#pipline: remove emails, newline character and distracting single quotes, remove unicode like \u2062
textList_clean = []
for text in X['Texts']: #each text is a post
    textList_clean.append(preProcessing.removeSingleQuotes(preProcessing.removeNewline(preProcessing.removeEmail( preProcessing.removeURL(text)))))
    #text.encode('ascii','ignore')
print('===remove quotes, email ===')
print(textList_clean[0:5])

#Tokenize
printable = set(string.printable)
tokenizedList = [preProcessing.tokenizer(''.join(filter(lambda x: x in printable,t)) ) for t in textList_clean]
print('===tokenizer===')
print(tokenizedList[0:3])

# Build the bigram and trigram models OBJECT
bigram = gensim.models.Phrases(tokenizedList, min_count=5, threshold=100)
# higher threshold fewer phrases.OBJECT
trigram = gensim.models.Phrases(bigram[tokenizedList], threshold=100)
# OBJECT: Faster way to get a sentence clubbed as a trigram/bigram
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
tokenizedList_noPNG = preProcessing.remove_pngWords(tokenizedList)#remove a_b word(png file name)
cleanList_nostops = preProcessing.remove_stopwords(tokenizedList_noPNG,stop_words)
#make bigram
cleanList_bigram = make_bigrams(cleanList_nostops)
print('===bigrams===')
print(cleanList_bigram[0:2])

#lemmentation
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

#after preprocessing, remove empty post
cleanList_nonEmpty = []
country_nonEmpty = []
text_nonEmpty = []
utc_nonEmpty = []
for i in range(len(cleanList_bigram)):
    if cleanList_bigram[i]:
        cleanList_nonEmpty.append(cleanList_bigram[i])
        country_nonEmpty.append(X["country"][i])
        text_nonEmpty.append(X["Texts"][i])	
        utc_nonEmpty.append(X["UTC"][i])

cleanList_lemmatized = lemmatization(cleanList_nonEmpty, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
print(cleanList_lemmatized[0:2])

# Create Dictionary
id2word = corpora.Dictionary(cleanList_lemmatized)
# Create Corpus
texts = cleanList_lemmatized
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
print('===corpus example===')
print(corpus[:1])

#build topic model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
id2word=id2word,
num_topics=20,
random_state=100,
update_every=1,
chunksize=100,
passes=10,
alpha='auto',
per_word_topics=True)

print("ok")

topics = lda_model.show_topics(num_topics=20, num_words=40,formatted=False)
for t in topics:
    print('======TOPIC:',t[0])
    words = []
    for wordProba in t[1]:
        words.append(wordProba[0])
    print(', '.join(words))
#print(topics)

#document topics:doc:(topic,probability)
docTopicList = []
for c in corpus:
    docTopicList.append(lda_model.get_document_topics(c))

print(len(corpus),len(country_nonEmpty),len(docTopicList))

# Compute Perplexity
print('\nPerplexity: ', lda_model.log_perplexity(corpus))  # a measure of how good the model is. lower the better.

# Compute Coherence Score
coherence_model_lda = CoherenceModel(model=lda_model, texts=texts, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)

#save LDA model
lda_model.save("LDA_AUS_20")
#save dictionary
id2word.save_as_text("dictionary20_AUS")
#loaded_dct = Dictionary.load_from_text(tmp_fname)
#save corpus doc frequency map
pickle.dump(corpus,open("corpus_docFreq20_AUS.p","wb"))
## Load a potentially pretrained model from disk.
#lda = LdaModel.load(temp_file)

#NOTE do not remove empty text easily we cannot count utc later
#pickle.dump(country_nonEmpty,open("countryList20_UK.p","wb"))
pickle.dump(docTopicList,open("docTopicList_LDA20_AUS.p","wb"))
pickle.dump(topics,open("topics_LDA20_AUS.p","wb"))
pickle.dump(text_nonEmpty,open("Texts_nonEmpty_AUS.p","wb"))
pickle.dump(utc_nonEmpty,open("UTC_nonEmpty_AUS.p","wb"))
