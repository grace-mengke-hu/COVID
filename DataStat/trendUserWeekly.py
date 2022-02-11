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

#weekly bin and label
weeklyBin = utilFunc.utc_weekly_bin()
weeklyLabel = utilFunc.utc_weekly_label()

#num user in bin
numUserInBinUS = utilFunc.numUserInBin(weeklyBin, userListUS, timeListUS)
numUserInBinCAN = utilFunc.numUserInBin(weeklyBin, userListCAN, timeListCAN)
numUserInBinUK = utilFunc.numUserInBin(weeklyBin, userListUK, timeListUK)
numUserInBinAUS = utilFunc.numUserInBin(weeklyBin, userListAUS, timeListAUS)
#plot
fig, axs = plt.subplots(2,2)
#US
axs[0,0].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinUS),'blue')
axs[0,0].set(xlabel = 'week',ylabel='US User Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[0,0].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[0,0].get_xticklabels()]
for i in range(len(weeklyLabel)):
        labels[i] = weeklyLabel[i]
axs[0,0].set_xticklabels(labels,rotation=45)
axs[0,0].set_yscale('log')

#CAN
axs[0,1].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinCAN),'blue')
axs[0,1].set(xlabel = 'week',ylabel='Canada User Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[0,1].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[0,1].get_xticklabels()]
for i in range(len(weeklyLabel)):
        labels[i] = weeklyLabel[i]
axs[0,1].set_xticklabels(labels,rotation=45)
axs[0,1].set_yscale('log')

#UK
axs[1,0].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinUK),'blue')
axs[1,0].set(xlabel = 'week',ylabel='UK User Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[1,0].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[1,0].get_xticklabels()]
for i in range(len(weeklyLabel)):
        labels[i] = weeklyLabel[i]
axs[1,0].set_xticklabels(labels,rotation=45)
axs[1,0].set_yscale('log')

#AUS
axs[1,1].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinAUS),'blue')
axs[1,1].set(xlabel = 'week',ylabel='Australia User Count')
#axs[0,0].set_xlim([1356998401,1546300798])
axs[1,1].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[1,1].get_xticklabels()]
for i in range(len(weeklyLabel)):
        labels[i] = weeklyLabel[i]
axs[1,1].set_xticklabels(labels,rotation=45)
axs[1,1].set_yscale('log')

plt.show()

