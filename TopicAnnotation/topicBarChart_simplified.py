import pickle
from collections import Counter

# document topic Threshold
	#US 15: 0.19881
	#UK 10: 0.24
	#CAN 15:0.15864215
	#AUS 10:0.18434

#load topic according to best number of topics
prefix = 'C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID'
#US10
topicsUS = pickle.load(open(prefix+"/TopicModeling/topics_LDA15_US.p","rb"))
docTopicListUS = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA15_US.p","rb")) 
#UK10
topicsUK = pickle.load(open(prefix+"/TopicModeling/topics_LDA10_UK.p","rb"))
docTopicListUK = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA10_UK.p","rb"))
#Canada 15
topicsCAN = pickle.load(open(prefix+"/TopicModeling/topics_LDA15_CAN.p","rb"))
docTopicListCAN = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA15_CAN.p","rb"))
#Australia 10
topicsAUS = pickle.load(open(prefix+"/TopicModeling/topics_LDA10_AUS.p","rb"))
docTopicListAUS = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA10_AUS.p","rb"))
print(docTopicListUS[0])#list of (topicID, probability)


commonTopics = ['Case Report',#'Case report&interaction with medical system',
'Prevention',#'prevention/Social distancing/Transmission risk/vaccine',
'COVID impact',#'Work/Finance/Education/Children/feeling',
'Policy&News'#'Policy/QA&News/Travel restriction/testing'
]

#US 15 non-zero topicsID:commonTopic
UStopicMap = {
    0:'Policy&News',
    1:'Prevention',
    2:'COVID impact',
    4:'Policy&News',
    5:'COVID impact', 
    6:'Case Report',
    7:'COVID impact',
    8:'COVID impact',
    9:'COVID impact',
    11:'Policy&News',
    12:'Prevention',
    13:'Case Report',
    14:'Prevention',
    }
USthreshold = 0.19881

#UK 10
UKtopicMap = {
    0:'Case Report',
    1:'COVID impact',
    2:'COVID impact',
    3:'Policy&News',
    5:'Policy&News',
    6:'COVID impact',
    7:'Policy&News',
    8:'Prevention',
    9:'Case Report'
}
UKthreshold = 0.24

#CAN 15
CANtopicMap = {
0:'Case Report',
1:'Case Report',
2:'Policy&News',
3:'COVID impact',
4:'COVID impact',
5:'COVID impact',
6:'Case Report',
7:'COVID impact',
8:'Policy&News',
9:'Case Report',
10:'Case Report',
11:'COVID impact',
12:'COVID impact',
13:'Prevention',
14:'COVID impact'
}
CANthreshold = 0.15864215

#AUS 10
AUStopicMap = {
0:'COVID impact',
1:'COVID impact',
2:'Case Report',
3:'COVID impact',
4:'Prevention',
5:'Policy&News',
6:'Policy&News',
7:'COVID impact',
8:'Policy&News',
9:'Policy&News'
}
AUSthreshold = 0.18434

#US doc topic
commonTopRateDicUS = {}#common topic :rate
#for t in commonTopics:#go through common topic;t is topic string
for doc in docTopicListUS:#go through doc which is a list of (topic, probability)
    for t in doc:#go through each topic for that document
        if t[1]>USthreshold and (t[0] in UStopicMap.keys()): #topic probability above threshold and the toipc has commonTopic labeled
            if UStopicMap[t[0]] in commonTopRateDicUS.keys():#add to dictionary
                commonTopRateDicUS[UStopicMap[t[0]]] =commonTopRateDicUS[UStopicMap[t[0]]]+1 #one more document belong to this common topic
            else:
                commonTopRateDicUS[UStopicMap[t[0]]] = 1
#dictionary to rate
USsum = sum(commonTopRateDicUS.values())
for t in commonTopRateDicUS.keys():
    commonTopRateDicUS[t] = commonTopRateDicUS[t]/float(USsum)

#AUS doc topic
commonTopRateDicAUS = {}#common topic :rate
#for t in commonTopics:#go through common topic;t is topic string
for doc in docTopicListAUS:#go through doc which is a list of (topic, probability)
    for t in doc:#go through each topic for that document
        if t[1]>AUSthreshold and (t[0] in AUStopicMap.keys()): #topic probability above threshold and the toipc has commonTopic labeled
            if AUStopicMap[t[0]] in commonTopRateDicAUS.keys():#add to dictionary
                commonTopRateDicAUS[AUStopicMap[t[0]]] =commonTopRateDicAUS[AUStopicMap[t[0]]]+1 #one more document belong to this common topic
            else:
                commonTopRateDicAUS[AUStopicMap[t[0]]] = 1
#dictionary to rate
AUSsum = sum(commonTopRateDicAUS.values())
for t in commonTopRateDicAUS.keys():
    commonTopRateDicAUS[t] = commonTopRateDicAUS[t]/float(AUSsum)

#UK doc topic
commonTopRateDicUK = {}#common topic :rate
#for t in commonTopics:#go through common topic;t is topic string
for doc in docTopicListUK:#go through doc which is a list of (topic, probability)
    for t in doc:#go through each topic for that document
        if t[1]>UKthreshold and (t[0] in UKtopicMap.keys()): #topic probability above threshold and the toipc has commonTopic labeled
            if UKtopicMap[t[0]] in commonTopRateDicUK.keys():#add to dictionary
                commonTopRateDicUK[UKtopicMap[t[0]]] =commonTopRateDicUK[UKtopicMap[t[0]]]+1 #one more document belong to this common topic
            else:
                commonTopRateDicUK[UKtopicMap[t[0]]] = 1
#dictionary to rate
UKsum = sum(commonTopRateDicUK.values())
for t in commonTopRateDicUK.keys():
    commonTopRateDicUK[t] = commonTopRateDicUK[t]/float(UKsum)

#CAN doc topic
commonTopRateDicCAN = {}#common topic :rate
#for t in commonTopics:#go through common topic;t is topic string
for doc in docTopicListCAN:#go through doc which is a list of (topic, probability)
    for t in doc:#go through each topic for that document
        if t[1]>CANthreshold and (t[0] in CANtopicMap.keys()): #topic probability above threshold and the toipc has commonTopic labeled
            if CANtopicMap[t[0]] in commonTopRateDicCAN.keys():#add to dictionary
                commonTopRateDicCAN[CANtopicMap[t[0]]] =commonTopRateDicCAN[CANtopicMap[t[0]]]+1 #one more document belong to this common topic
            else:
                commonTopRateDicCAN[CANtopicMap[t[0]]] = 1
#dictionary to rate
CANsum = sum(commonTopRateDicCAN.values())
for t in commonTopRateDicCAN.keys():
    commonTopRateDicCAN[t] = commonTopRateDicCAN[t]/float(CANsum)

import pandas as pd
rateData = {}#country:topic rate

#lable name column
rateData['topic label'] = commonTopics

#US
rateData['US'] = []
for t in commonTopics:
	if t in commonTopRateDicUS.keys(): 
		rateData['US'].append(commonTopRateDicUS[t])
	else:
		rateData['US'].append(0)

#UK
rateData['UK'] = []
for t in commonTopics:
        if t in commonTopRateDicUK.keys():
                rateData['UK'].append(commonTopRateDicUK[t])
        else:
                rateData['UK'].append(0)

#CAN
rateData['CAN'] = []
for t in commonTopics:
        if t in commonTopRateDicCAN.keys():
                rateData['CAN'].append(commonTopRateDicCAN[t])
        else:
                rateData['CAN'].append(0)

#AUS
rateData['AUS'] = []
for t in commonTopics:
        if t in commonTopRateDicAUS.keys():
                rateData['AUS'].append(commonTopRateDicAUS[t])
        else:
                rateData['AUS'].append(0)

#form dataframe
df1 = pd.DataFrame(rateData)

#transpose plot
rateDataT = {}
rateDataT['Country'] = ['US','UK','CAN','AUS']
for i in range(len(commonTopics)):
        rateDataT[commonTopics[i]] = []
        rateDataT[commonTopics[i]].append(rateData['US'][i])
        rateDataT[commonTopics[i]].append(rateData['UK'][i])
        rateDataT[commonTopics[i]].append(rateData['CAN'][i])
        rateDataT[commonTopics[i]].append(rateData['AUS'][i])


df2 = pd.DataFrame(rateDataT)
import matplotlib.pyplot as plt


# plot a Stacked Bar Chart using matplotlib 
df2.plot(
    x = 'Country', 
    kind = 'barh', 
    stacked = True, 
    title = 'Stacked Bar Graph',
    colormap='Paired',
    mark_right = True) 
plt.rc('font', size=18)
plt.show()
