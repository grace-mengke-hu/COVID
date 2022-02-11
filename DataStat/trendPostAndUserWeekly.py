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
weeklyLabel = utilFunc.utc_weekly_tick()
#num user in bin
numUserInBinUS = utilFunc.numUserInBin(weeklyBin, userListUS, timeListUS)
numUserInBinCAN = utilFunc.numUserInBin(weeklyBin, userListCAN, timeListCAN)
numUserInBinUK = utilFunc.numUserInBin(weeklyBin, userListUK, timeListUK)
numUserInBinAUS = utilFunc.numUserInBin(weeklyBin, userListAUS, timeListAUS)

fig, axs = plt.subplots(2,2)#,figsize=(8,20))
counts, bins, patches = axs[0,0].hist(timeListUS, bins=np.array(weeklyBin),color='skyblue',label='post count')#weekly post count
axs[0,0].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinUS),'blue',label='user count')
axs[0,0].set_xlabel('week', size = 16)
axs[0,0].set_ylabel('US Post and User Count', size = 16)
#axs[0,0].set(xlabel = 'week',ylabel='US Post and User Count',size=13)
axs[0,0].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[0,0].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[0,0].set_xticklabels(labels,rotation=45,size=16)
axs[0,0].set_yscale('log')

#axs[0,0].set_yticks(size=13)
#axs[0,0].legend(prop={'size': 16})


#Can
counts, bins, patches = axs[0,1].hist(timeListCAN, bins=np.array(weeklyBin),color='skyblue',label = 'post count')
axs[0,1].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinCAN),'blue',label='user count')
axs[0,1].set_xlabel('week', size = 16)
axs[0,1].set_ylabel('Canada Post and User Count', size = 16)
#axs[0,1].set(xlabel = 'week',ylabel='Canada Post and User Count')
axs[0,1].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[0,1].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[0,1].set_xticklabels(labels,rotation=45,size=16)
axs[0,1].set_yscale('log')
#axs[0,1].legend(prop={'size': 16})

#UK
counts, bins, patches = axs[1,0].hist(timeListUK, bins=np.array(weeklyBin),color='skyblue',label='post count')
axs[1,0].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinUK),'blue',label = 'user count')
axs[1,0].set_xlabel('week', size = 16)
axs[1,0].set_ylabel('UK Post and User Count', size = 16)
#axs[1,0].set(xlabel = 'week',ylabel='UK Post and User Count')
axs[1,0].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[1,0].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[1,0].set_xticklabels(labels,rotation=45,size=16)
axs[1,0].set_yscale('log')
#axs[1,0].legend(prop={'size': 16})

#Australia
counts, bins, patches = axs[1,1].hist(timeListAUS, bins=np.array(weeklyBin),color='skyblue',label='post count')
axs[1,1].plot(np.array(weeklyBin[0:len(weeklyBin)-1]),np.array(numUserInBinAUS),'blue',label='user count')
axs[1,1].set_xlabel('week', size = 16)
axs[1,1].set_ylabel('Australia Post and User Count', size = 16)
#axs[1,1].set(xlabel = 'week',ylabel='Australia Post and User Count')
axs[1,1].set_xticks(np.array(weeklyBin))
labels = [item.get_text() for item in axs[1,1].get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[1,1].set_xticklabels(labels,rotation=45,size=16)
axs[1,1].set_yscale('log')
#axs[1,1].legend(prop={'size': 16})

#fig.tight_layout()


plt.subplots_adjust(left=0.05,
                    bottom=0.1, 
                    right=0.97, 
                    top=0.92, 
                    wspace=0.2, 
                    hspace=0.4)


# plt.legend(bbox_to_anchor=(1,0), loc="lower left",prop={'size': 14})#, mode="expand", ncol=2)
# fig.legend(handles, ['post count', 'user count'], bbox_to_anchor=(2, 0),loc = 'lower right')
axs[0,0].legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left",mode="expand", ncol=2, prop={'size': 16})


plt.show()