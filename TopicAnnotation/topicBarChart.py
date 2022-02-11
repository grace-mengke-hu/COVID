import pickle
from collections import Counter

#load topic according to best number of topics
prefix = 'C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID'
#US10
topicsUS = pickle.load(open(prefix+"/TopicModeling/topics_LDA10_US.p","rb"))
docTopicListUS = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA10_US.p","rb")) 
#UK10
topicsUK = pickle.load(open(prefix+"/TopicModeling/topics_LDA10_UK.p","rb"))
docTopicListUK = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA10_UK.p","rb"))
#Canada 15
topicsCAN = pickle.load(open(prefix+"/TopicModeling/topics_LDA10_CAN.p","rb"))
docTopicListCAN = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA10_CAN.p","rb"))
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
USdocTopic = []
for doc in docTopicListUS:
    for t in doc:#go through each topic for that document
        if t[1]>USthreshold: #topic probability
            USdocTopic.append(t[0])	#append all the main topics			
UStopicCounter = dict(Counter(USdocTopic))#topic :frequency
commonTopRateDicUS = {}#common topic :rate
for t in commonTopics:#go through common topic;t is topic string
    for tID in UStopicCounter.keys():#tID is topic ID
        if tID in UStopicMap.keys() and UStopicMap[tID]==t:#not all topic has been annotated and find the same topic string
            #different topic ID may belong to same topic, the document frequency should be added up
            if t in commonTopRateDicUS.keys():
                commonTopRateDicUS[t] =commonTopRateDicUS[t]+UStopicCounter[tID] #add up the posts on the same topic
            else:
                commonTopRateDicUS[t]=UStopicCounter[tID]
#dictionary to rate
USsum = sum(commonTopRateDicUS.values())
for t in commonTopRateDicUS.keys():
    commonTopRateDicUS[t] = commonTopRateDicUS[t]/float(USsum)


#CAN doc topic
CANdocTopic = []
for doc in docTopicListCAN:
    for t in doc:
        if t[1]>CANthreshold: #topic probability
            CANdocTopic.append(t[0])
CANtopicCounter = dict(Counter(CANdocTopic))#topic :frequency
commonTopRateDicCAN = {}#common topic :rate
for t in commonTopics:#go through common topic;t is topic string
    for tID in CANtopicCounter.keys():#tID is topic ID
        if tID in CANtopicMap.keys() and CANtopicMap[tID]==t:#not all topic has been annotated and find the same topic string
            if t in commonTopRateDicCAN.keys():
                commonTopRateDicCAN[t] =commonTopRateDicCAN[t]+CANtopicCounter[tID] #add up the posts on the same topic
            else:
                commonTopRateDicCAN[t]=CANtopicCounter[tID]

                	
#dictionary to rate
CANsum = sum(commonTopRateDicCAN.values())
for t in commonTopRateDicCAN.keys():
    commonTopRateDicCAN[t] = commonTopRateDicCAN[t]/float(CANsum)

#UK doc topic
UKdocTopic = []
for doc in docTopicListUK:
    for t in doc:
        if t[1]>UKthreshold: #topic probability
            UKdocTopic.append(t[0])
UKtopicCounter = dict(Counter(UKdocTopic))#topic :frequency
commonTopRateDicUK = {}#common topic :rate
for t in commonTopics:#go through common topic;t is topic string
    for tID in UKtopicCounter.keys():#tID is topic ID
        if tID in UKtopicMap.keys() and UKtopicMap[tID]==t:#not all topic has been annotated and find the same topic string
            if t in commonTopRateDicUK.keys():
                commonTopRateDicUK[t] =commonTopRateDicUK[t]+UKtopicCounter[tID]#add up the posts on the same topic
            else:
                commonTopRateDicUK[t]=UKtopicCounter[tID]
#dictionary to rate
UKsum = sum(commonTopRateDicUK.values())
for t in commonTopRateDicUK.keys():
	commonTopRateDicUK[t] = commonTopRateDicUK[t]/float(UKsum)
print(commonTopRateDicUK)
print(UKtopicCounter)

#AUS doc topic
AUSdocTopic = []
for doc in docTopicListAUS:
    for t in doc:
        if t[1]>AUSthreshold: #topic probability
            AUSdocTopic.append(t[0])
AUStopicCounter = dict(Counter(AUSdocTopic))#topic :frequency
commonTopRateDicAUS = {}#common topic :total post->rate
for t in commonTopics:#go through common topic;t is topic string
    for tID in AUStopicCounter.keys():#tID is topic ID
        if tID in AUStopicMap.keys() and AUStopicMap[tID]==t:#not all topic has been annotated and find the same topic string
            if t in commonTopRateDicAUS.keys():
                commonTopRateDicAUS[t] =commonTopRateDicAUS[t]+AUStopicCounter[tID] #add up the posts on the same topic
            else:
                commonTopRateDicAUS[t]=AUStopicCounter[tID]

#dictionary to rate
AUSsum = sum(commonTopRateDicAUS.values())
for t in commonTopRateDicAUS.keys():
    commonTopRateDicAUS[t] = commonTopRateDicAUS[t]/float(AUSsum)

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
parameters = {'axes.labelsize': 18,
          'axes.titlesize': 24,
          'xtick.labelsize':18,
          'ytick.labelsize':18}
plt.rcParams.update(parameters)
df2.plot(
    x = 'Country', 
    kind = 'barh', 
    stacked = True, 
    #title = 'Stacked Bar Graph',
    colormap='Paired',
    mark_right = True) 



# plt.rc('axes', titlesize=24)     # fontsize of the axes title
# plt.rc('xtick', labelsize=18)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=18)    # fontsize of the tick labels
plt.legend(bbox_to_anchor=(0, 1, 1, 0), loc="lower left", ncol=2,prop={'size': 18})


#df1.plot(
#    x = 'topic label', 
#    kind = 'barh', 
#    stacked = True, 
#    title = 'Stacked Bar Graph',
#    colormap='Paired',
#    mark_right = True) 

plt.show()

