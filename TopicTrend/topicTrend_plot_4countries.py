import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID/')
import utilFunc

import pickle
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

#load bin
weeklyBin = utilFunc.utc_weekly_bin()
weeklyLabel = utilFunc.utc_weekly_tick()

#load commonTopic
commonTopic = utilFunc.commonTopic()

#load commonTopic:UTC dictionary (commonTopic:utc list)
commonTopic_UTC_AUS = pickle.load(open('AUS10_commonTopic_UTC.p','rb'))
commonTopic_UTC_US = pickle.load(open('US15_commonTopic_UTC.p','rb'))
commonTopic_UTC_UK = pickle.load(open('UK10_commonTopic_UTC.p','rb'))
commonTopic_UTC_CAN = pickle.load(open('CAN15_commonTopic_UTC.p','rb'))

#initiate 4 subplots
fig, axs = plt.subplots(2,2)

#US
y1,binEdges1=np.histogram(np.array(commonTopic_UTC_US[commonTopic[0]]),bins=weeklyBin)
bincenters1 = 0.5*(binEdges1[1:]+binEdges1[:-1])
axs[0,0].plot(bincenters1,y1,'-',color='skyblue',label = commonTopic[0])
y2,binEdges2=np.histogram(np.array(commonTopic_UTC_US[commonTopic[1]]),bins=weeklyBin)
bincenters2 = 0.5*(binEdges2[1:]+binEdges2[:-1])
axs[0,0].plot(bincenters2,y2,'-',color='orange',label = commonTopic[1])
y3,binEdges3=np.histogram(np.array(commonTopic_UTC_US[commonTopic[2]]),bins=weeklyBin)
bincenters3 = 0.5*(binEdges3[1:]+binEdges3[:-1])
axs[0,0].plot(bincenters3,y3,'-',color='salmon',label = commonTopic[2])
y4,binEdges4=np.histogram(np.array(commonTopic_UTC_US[commonTopic[3]]),bins=weeklyBin)
bincenters4 = 0.5*(binEdges4[1:]+binEdges4[:-1])
axs[0,0].plot(bincenters4,y4,'-',color='olive',label = commonTopic[3])
##setting
axs[0,0].set_xlabel('week', size = 16)
axs[0,0].set_ylabel('US Post Count for the 4 Topics', size = 16)
axs[0,0].set_xticks(np.array(bincenters4))#bin center changed not weeklyBin
labels = [item.get_text() for item in axs.get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[0,0].set_xticklabels(labels,rotation=45,size=16)
axs[0,0].legend(loc="upper right",prop={'size': 16})



#UK
y1,binEdges1=np.histogram(np.array(commonTopic_UTC_UK[commonTopic[0]]),bins=weeklyBin)
bincenters1 = 0.5*(binEdges1[1:]+binEdges1[:-1])
axs[0,1].plot(bincenters1,y1,'-',color='skyblue',label = commonTopic[0])
y2,binEdges2=np.histogram(np.array(commonTopic_UTC_UK[commonTopic[1]]),bins=weeklyBin)
bincenters2 = 0.5*(binEdges2[1:]+binEdges2[:-1])
axs[0,1].plot(bincenters2,y2,'-',color='orange',label = commonTopic[1])
y3,binEdges3=np.histogram(np.array(commonTopic_UTC_UK[commonTopic[2]]),bins=weeklyBin)
bincenters3 = 0.5*(binEdges3[1:]+binEdges3[:-1])
axs[0,1].plot(bincenters3,y3,'-',color='salmon',label = commonTopic[2])
y4,binEdges4=np.histogram(np.array(commonTopic_UTC_UK[commonTopic[3]]),bins=weeklyBin)
bincenters4 = 0.5*(binEdges4[1:]+binEdges4[:-1])
axs[0,1].plot(bincenters4,y4,'-',color='olive',label = commonTopic[3])
##setting
axs[0,1].set_xlabel('week', size = 16)
axs[0,1].set_ylabel('UK Post Count for the 4 Topics', size = 16)
axs[0,1].set_xticks(np.array(bincenters4))#bin center changed not weeklyBin
labels = [item.get_text() for item in axs.get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[0,1].set_xticklabels(labels,rotation=45,size=16)
axs[0,1].legend(loc="upper right",prop={'size': 16})


#CAN
y1,binEdges1=np.histogram(np.array(commonTopic_UTC_CAN[commonTopic[0]]),bins=weeklyBin)
bincenters1 = 0.5*(binEdges1[1:]+binEdges1[:-1])
axs[1,0].plot(bincenters1,y1,'-',color='skyblue',label = commonTopic[0])
y2,binEdges2=np.histogram(np.array(commonTopic_UTC_CAN[commonTopic[1]]),bins=weeklyBin)
bincenters2 = 0.5*(binEdges2[1:]+binEdges2[:-1])
axs[1,0].plot(bincenters2,y2,'-',color='orange',label = commonTopic[1])
y3,binEdges3=np.histogram(np.array(commonTopic_UTC_CAN[commonTopic[2]]),bins=weeklyBin)
bincenters3 = 0.5*(binEdges3[1:]+binEdges3[:-1])
axs[1,0].plot(bincenters3,y3,'-',color='salmon',label = commonTopic[2])
y4,binEdges4=np.histogram(np.array(commonTopic_UTC_CAN[commonTopic[3]]),bins=weeklyBin)
bincenters4 = 0.5*(binEdges4[1:]+binEdges4[:-1])
axs[1,0].plot(bincenters4,y4,'-',color='olive',label = commonTopic[3])
##setting
axs[1,0].set_xlabel('week', size = 16)
axs[1,0].set_ylabel('Canada Post Count for the 4 Topics', size = 16)
axs[1,0].set_xticks(np.array(bincenters4))#bin center changed not weeklyBin
labels = [item.get_text() for item in axs.get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[1,0].set_xticklabels(labels,rotation=45,size=16)
axs[1,0].legend(loc="upper right",prop={'size': 16})




#Aus
y1,binEdges1=np.histogram(np.array(commonTopic_UTC_AUS[commonTopic[0]]),bins=weeklyBin)
bincenters1 = 0.5*(binEdges1[1:]+binEdges1[:-1])
axs[1,1].plot(bincenters1,y1,'-',color='skyblue',label = commonTopic[0])
y2,binEdges2=np.histogram(np.array(commonTopic_UTC_AUS[commonTopic[1]]),bins=weeklyBin)
bincenters2 = 0.5*(binEdges2[1:]+binEdges2[:-1])
axs[1,1].plot(bincenters2,y2,'-',color='orange',label = commonTopic[1])
y3,binEdges3=np.histogram(np.array(commonTopic_UTC_AUS[commonTopic[2]]),bins=weeklyBin)
bincenters3 = 0.5*(binEdges3[1:]+binEdges3[:-1])
axs[1,1].plot(bincenters3,y3,'-',color='salmon',label = commonTopic[2])
y4,binEdges4=np.histogram(np.array(commonTopic_UTC_AUS[commonTopic[3]]),bins=weeklyBin)
bincenters4 = 0.5*(binEdges4[1:]+binEdges4[:-1])
axs[1,1].plot(bincenters4,y4,'-',color='olive',label = commonTopic[3])
##setting
axs[1,1].set_xlabel('week', size = 16)
axs[1,1].set_ylabel('US Post Count for the 4 Topics', size = 16)
axs[1,1].set_xticks(np.array(bincenters4))#bin center changed not weeklyBin
labels = [item.get_text() for item in axs.get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs[1,1].set_xticklabels(labels,rotation=45,size=16)
axs[1,1].legend(loc="upper right",prop={'size': 16})


plt.subplots_adjust(left=0.05,
                    bottom=0.1, 
                    right=0.98, 
                    top=0.98, 
                    wspace=0.2, 
                    hspace=0.4)

plt.show()
