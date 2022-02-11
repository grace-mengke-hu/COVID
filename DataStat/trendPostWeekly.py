import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID/')
import utilFunc

import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from collections import Counter


prefixDir = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_merge/'
USjsonList = ['coronavirusus_Feb2Nov_2020_update2.json']
AUSjsonList = ['CoronavirusAustralia_CoronavirusDownunder_Feb2Nov_2020.json']
CANjsonList = ['CoronavirusCanada_CanadaCoronavirus_Feb2Nov_2020.json']
UKjsonList = ['CoronavirusUK_Feb2Nov_2020_update2.json']

dataUS = utilFunc.loadJson(USjsonList,prefixDir)
timeListUS, userListUS = utilFunc.utc_userList(dataUS)
dataCAN = utilFunc.loadJson(CANjsonList,prefixDir)
timeListCAN, userListCAN = utilFunc.utc_userList(dataCAN)
dataAUS = utilFunc.loadJson(AUSjsonList,prefixDir)
timeListAUS, userListAUS = utilFunc.utc_userList(dataAUS)
dataUK = utilFunc.loadJson(UKjsonList,prefixDir)
timeListUK, userListUK = utilFunc.utc_userList(dataUK)

#count the number of submission
submissionUS = utilFunc.submission_utc(dataUS)
submissionUK = utilFunc.submission_utc(dataUK)
submissionAUS = utilFunc.submission_utc(dataAUS)
submissionCAN = utilFunc.submission_utc(dataCAN)
print('num submission US,UK,AUS,CAN',len(submissionUS),len(submissionUK),len(submissionAUS),len(submissionCAN))
print('num post US,UK,AUS,CAN',len(timeListUS),len(timeListUK),len(timeListAUS),len(timeListCAN))
#weekly bin and label
weeklyBin = utilFunc.utc_weekly_bin()
weeklyLabel = utilFunc.utc_weekly_label()

#plot
fig, axs = plt.subplots(2,2)#,figsize=(8,20))
#US
counts, bins, patches = axs[0,0].hist(timeListUS, bins=np.array(weeklyBin),color='skyblue')
axs[0,0].set(xlabel = 'week',ylabel='US Post Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[0,0].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[0,0].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[0,0].set_xticklabels(labels,rotation=45)
axs[0,0].set_yscale('log')

#Can
counts, bins, patches = axs[0,1].hist(timeListCAN, bins=np.array(weeklyBin),color='skyblue')
axs[0,1].set(xlabel = 'week',ylabel='Canada Post Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[0,1].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[0,1].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[0,1].set_xticklabels(labels,rotation=45)
axs[0,1].set_yscale('log')

#UK
counts, bins, patches = axs[1,0].hist(timeListUK, bins=np.array(weeklyBin),color='skyblue')
axs[1,0].set(xlabel = 'week',ylabel='UK Post Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[1,0].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[1,0].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[1,0].set_xticklabels(labels,rotation=45)
axs[1,0].set_yscale('log')

#Australia
counts, bins, patches = axs[1,1].hist(timeListAUS, bins=np.array(weeklyBin),color='skyblue')
axs[1,1].set(xlabel = 'week',ylabel='Australia Post Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[1,1].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[1,1].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[1,1].set_xticklabels(labels,rotation=45)

axs[1,1].set_yscale('log')
plt.show()

