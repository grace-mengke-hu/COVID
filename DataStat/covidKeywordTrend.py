import json
import re


#Cigarettes_JanToApril20_2020.json            marijuana_JanToApril20_2020.json
#Coronavirus.json                             stopsmoking_JanToApril20_2020.json
#CoronavirusMemes.json                        trees_JanToApril20_2020.json
#CoronavirusUS.json                           Vaping101_JanToApril20_2020.json
#electronic_cigarette_JanToApril20_2020.json  vaping_JanToApril20_2020.json
#marijuanaenthusiasts_JanToApril20_2020.json  weed_JanToApril20_2020.json

with open('../Data_COVID/Cigarettes_JanToApril20_2020.json') as fp:
        data1 = json.load(fp)
with open('../Data_COVID/electronic_cigarette_JanToApril20_2020.json') as fp:
        data2 = json.load(fp)
with open('../Data_COVID/marijuanaenthusiasts_JanToApril20_2020.json') as fp:
        data3 = json.load(fp)
with open('../Data_COVID/marijuana_JanToApril20_2020.json') as fp:
        data4 = json.load(fp)
with open('../Data_COVID/stopsmoking_JanToApril20_2020.json') as fp:
        data5 = json.load(fp)
with open('../Data_COVID/trees_JanToApril20_2020.json') as fp:
        data6 = json.load(fp)
with open('../Data_COVID/Vaping101_JanToApril20_2020.json') as fp:
        data7 = json.load(fp)
with open('../Data_COVID/vaping_JanToApril20_2020.json') as fp:
        data8 = json.load(fp)
with open('../Data_COVID/weed_JanToApril20_2020.json') as fp:
        data9 = json.load(fp)
data = data1+data2+data3+data4+data5+data6+data7+data8+data9

print(data[0])

covidPattern = "(\W|^)covid(\W|$)|(\W|^)corona(\W|$)"


textList = []
utcList = []
for sub in data:
	if 'selftext' in sub.keys():
		if re.search(covidPattern, sub['title']+'\n\n'+sub['selftext'], re.IGNORECASE):
			textList.append(sub['title']+'\n\n'+sub['selftext'])
			utcList.append(sub['created_utc'])
	else:
		if re.search(covidPattern,sub['title'],re.IGNORECASE):
			textList.append(sub['title'])
			utcList.append(sub['created_utc'])

	if sub['comments']:
		for c in sub['comments']:
			if re.search(covidPattern,c['data'][0]['body'],re.IGNORECASE):
				#print(c['data'][0]['body'])
				textList.append(c['data'][0]['body'])
				utcList.append(c['data'][0]['created_utc'])	
#print(textList[0])


UnixTimeEpoch = [1577836800, 1580515200,1583020800,1585699200,1587427199]
Xaxis = ['Jan 1','Feb. 1','March. 1','April 1','April 20']
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
fig, ax = plt.subplots()
counts, bins, patches = ax.hist(utcList, bins=UnixTimeEpoch,color=['bisque'])
ax.set_xticks(bins)
labels = [item.get_text() for item in ax.get_xticklabels()]

for i in range(len(labels)):
        labels[i] = Xaxis[i]

ax.set_xticklabels(labels)
plt.ylabel('Post Counts')
plt.title('Trend of COVID mentions from Jan 1 2020 to April 20 2020')
plt.show()
