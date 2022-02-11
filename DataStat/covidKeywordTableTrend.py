#!../anaconda2/bin/python
import json
import re


with open('../Data_COVID/cripplingalcoholism_JanToApril20_2020.json') as fp:
        data = json.load(fp)

print(data[0])

covidPattern = "(\W|^)covid(\W|$)|(\W|^)corona(\W|$)"


textList = []
utcList = []
noKeywordUTC = []
for sub in data:
	if 'selftext' in sub.keys():
		if re.search(covidPattern, sub['title']+'\n\n'+sub['selftext'], re.IGNORECASE):
			textList.append(sub['title']+'\n\n'+sub['selftext'])
			utcList.append(sub['created_utc'])
		else:
			noKeywordUTC.append(sub['created_utc'])
	else:
		if re.search(covidPattern,sub['title'],re.IGNORECASE):
			textList.append(sub['title'])
			utcList.append(sub['created_utc'])
		else:
			noKeywordUTC.append(sub['created_utc'])

	if sub['comments']:
		for c in sub['comments']:
			if re.search(covidPattern,c['data'][0]['body'],re.IGNORECASE):
				#print(c['data'][0]['body'])
				textList.append(c['data'][0]['body'])
				utcList.append(c['data'][0]['created_utc'])	
			else:
				noKeywordUTC.append(sub['created_utc'])
#print(textList[0])

print('keyword', len(utcList),'no keyword',len(noKeywordUTC))
UnixTimeEpoch = [1577836800, 1580515200,1583020800,1585699200,1587427199]
Xaxis = ['Jan 1','Feb. 1','March. 1','April 1','April 20']
import numpy as np

Jan = 0
Feb = 0
March = 0
April = 0
for i in utcList:
	if i>=1577836800 and i <1580515200:
		Jan = Jan+1
	elif i>=1580515200 and i <1583020800:
		Feb = Feb+1
	elif i>=1583020800 and i <1585699200:
		March = March+1
	elif i>=1585699200 and i<=1587427199:
		April = April+1 
	else:
		print(i)
jan = 0
feb = 0
march = 0
april = 0
for i in noKeywordUTC:
	if i>=1577836800 and i <1580515200:
		jan = jan+1
	if i>=1580515200 and i <1583020800:
		feb = feb+1
	if i>=1583020800 and i <1585699200:
		march = march+1
	if i>=1585699200 and i<=1587427199:
		april = april+1 

print('jan keyword:',Jan, 'jan no keyword:',jan)
print('feb keyword:',Feb, 'feb no keyword:',feb)
print('march keyword:',March, 'march no keyword:',march)
print('april keyword:',April, 'april no keyword:',april)
