#!../../anaconda2/bin/python
import json
import re


with open('../../Data_COVID/cripplingalcoholism_JanToApril20_2020.json') as fp:
        data = json.load(fp)

#print(data[0])

covidPattern = "(\W|^)covid(\W|$)|(\W|^)corona(\W|$)"


textList = []
for sub in data:
	if 'selftext' in sub.keys():
		if re.search(covidPattern, sub['title']+'\n\n'+sub['selftext'], re.IGNORECASE):
			textList.append(sub['title']+'\n\n'+sub['selftext'])
	else:
		if re.search(covidPattern,sub['title'],re.IGNORECASE):
			textList.append(sub['title'])

	if sub['comments']:
		for c in sub['comments']:
			if re.search(covidPattern,c['data'][0]['body'],re.IGNORECASE):
				textList.append(c['data'][0]['body'])

fp = open("cripplingalcoholism.txt", "w")
for line in textList:
	fp.write(line.encode('UTF8'))
	fp.write("\n\n")
fp.close()

