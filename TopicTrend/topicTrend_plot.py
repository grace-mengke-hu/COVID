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
commonTopic_UTC = pickle.load(open('AUS10_commonTopic_UTC.p','rb'))
print(commonTopic_UTC.keys())

#histogram on different topics for one country
fig, axs = plt.subplots()
y1,binEdges1=np.histogram(np.array(commonTopic_UTC[commonTopic[0]]),bins=weeklyBin)
bincenters1 = 0.5*(binEdges1[1:]+binEdges1[:-1])
plt.plot(bincenters1,y1,'-',color='skyblue',label = commonTopic[0])
y2,binEdges2=np.histogram(np.array(commonTopic_UTC[commonTopic[1]]),bins=weeklyBin)
bincenters2 = 0.5*(binEdges2[1:]+binEdges2[:-1])
plt.plot(bincenters2,y2,'-',color='orange',label = commonTopic[1])
y3,binEdges3=np.histogram(np.array(commonTopic_UTC[commonTopic[2]]),bins=weeklyBin)
bincenters3 = 0.5*(binEdges3[1:]+binEdges3[:-1])
plt.plot(bincenters3,y3,'-',color='salmon',label = commonTopic[2])
y4,binEdges4=np.histogram(np.array(commonTopic_UTC[commonTopic[3]]),bins=weeklyBin)
bincenters4 = 0.5*(binEdges4[1:]+binEdges4[:-1])
plt.plot(bincenters4,y4,'-',color='olive',label = commonTopic[3])

##setting
axs.set_xlabel('week', size = 13)
axs.set_ylabel('Australia Post Count for the 4 Topics', size = 13)
#axs.set(xlabel = 'week',ylabel='US Post Count for the 4 Topics')

axs.set_xticks(np.array(bincenters4))#bin center changed not weeklyBin
labels = [item.get_text() for item in axs.get_xticklabels()]
for i in range(len(labels)):
        labels[i] = weeklyLabel[i]
axs.set_xticklabels(labels,rotation=45,size=13)

plt.legend(loc="upper right",prop={'size': 13})
plt.show()
