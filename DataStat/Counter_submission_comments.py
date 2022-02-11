import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID/')
import utilFunc

import json
import numpy as np
prefixDir = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_merge/'
USjsonList = ['coronavirusus_Feb2Nov_2020_update2.json']
AUSjsonList = ['CoronavirusAustralia_CoronavirusDownunder_Feb2Nov_2020.json']
CANjsonList = ['CoronavirusCanada_CanadaCoronavirus_Feb2Nov_2020.json']
UKjsonList = ['CoronavirusUK_Feb2Nov_2020_update2.json']

USsubreddit = 'coronavirusus'
dataUS = utilFunc.loadJson(USjsonList,prefixDir)
UKsubreddit = 'CoronavirusUK'
dataUK = utilFunc.loadJson(UKjsonList,prefixDir)
CANsubreddit1 = 'CoronavirusCanada'
CANsubreddit2 = 'CanadaCoronavirus'
dataCAN = utilFunc.loadJson(CANjsonList,prefixDir)
AUSsubreddit1 = 'CoronavirusAustralia'
AUSsubreddit2 = 'CoronavirusDownunder'
dataAUS = utilFunc.loadJson(AUSjsonList,prefixDir)

numSubmission = 0
numComments = 0
authors = []
for d in dataAUS:
    
    if d['subreddit'].lower() == AUSsubreddit2.lower():
        authors.append(d['author'])
        numSubmission =numSubmission +1
        if d['comments']:
            for c in d['comments']:
                numComments = numComments +1
                authors.append(c['data'][0]['author'])
print(numSubmission, numComments)
print(len(list(set(authors))))

