#!../../anaconda2/bin/python
import json
import re


prefixDir = '../../Data_COVID/COVID/'
USjsonList = ['coronavirusus_Jan2Apil_2020.json',
              'coronavirusus_May2June2020.json']
AUSjsonList = ['CovidAustralia_Jan2April2020.json',
	       'CovidAustralia_May2June2020.json']
CANjsonList = ['CovidCanada_Jan2April2020.json',
	       'CovidCanada_May2June2020.json',
	       'CoronavirusCanada_Jan2April2020.json',
	       'CoronavirusCanada_May2June2020.json']
UKjsonList = ['CovidUK_Jan2April2020.json',
	      'CovidUK_May2June2020.json']
OTHERjsonList = ['advice_Jan2Apil_2020.json',
        	 'advice_May2June2020.json',
	         'askreddit_Jan2Apil_2020.json',
		'askreddit_May2June2020.json',           
		'coronavirusNY_Jan2Apil_2020.json',		
		'coronavirusNY_May2June2020.json',
		'China_Flu_Jan2April2020.json',          
		'China_Flu_May2June2020.json',
		'coronavirusCA_Jan2Apil_2020.json',
		'coronavirusCA_May2June2020.json',
		'ncov_Jan2Apil_2020.json',
		'ncov_May2June2020.json',
		'coronavirus_Jan2Apil_2020.json',        
		'coronavirus_May2June2020.json',
	         'relationship_advice_Jan2Apil_2020.json',
		'relationship_advice_May2June2020.json']

def loadJson(jsonList,prefixDir):
	data = []
	for f in jsonList:
		with open(prefixDir+f) as fp:
			data = data+json.load(fp)
	return data
dataUS = loadJson(USjsonList,prefixDir)
dataCAN = loadJson(CANjsonList,prefixDir)
dataAUS = loadJson(AUSjsonList,prefixDir)
dataUK = loadJson(UKjsonList,prefixDir)

def userList(data):
	userList = []
	for d in data:
		userList.append(d['author'])
		if d['comments']:
			for c in d['comments']:
				userList.append(c['data'][0]['author'])
	return list(set(userList))

#covidPattern = "(\W|^)covid(\W|$)|(\W|^)corona(\W|$)"

userUS = userList(dataUS)
userCAN = userList(dataCAN)
userAUS = userList(dataAUS)
userUK = userList(dataUK)

import matplotlib.pyplot as plt
from pyvenn import venn

labels = venn.get_labels([userUS,userCAN,userAUS,userUK], fill=['number'])
venn.venn4(labels, names=['US','Canada','Australia','UK'])
plt.show()

#import matplotlib.pyplot as plt
#from matplotlib_venn import venn3

#from venn import venn 
#%matplotlib inline
#venn({'US':userUS,'Canada':userCAN,'Australia':userAUS,'UK':userUK})
#venn.venn4([userUS,userCAN,userAUS,userUK],set_labels=('US','Canada','Australia','UK'))
#plt.show()









