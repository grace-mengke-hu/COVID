import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID/')
import utilFunc


import pickle
import preProcessing

#load time stamp
weeklyBin = utilFunc.utc_weekly_bin()
weeklyLabel = utilFunc.utc_weekly_label()

#load common topic(obtained from annotation) from utilFunc
commonTopic = utilFunc.commonTopic()
topicIDmap = utilFunc.annotateUStopic()#topicID:commonTopic

# document topic Threshold
	#US 15: 0.19881
	#UK 10: 0.24
	#CAN 15:0.15864215
	#AUS 10:0.18434
threshold = 0.19881
numTopic = 15

#load utc of non-empty submissions
prefix = 'C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/COVID'
utcList = pickle.load(open(prefix+"/TopicModeling/UTC_nonEmpty_US.p","rb"))
#load topic vector list of (topicID,probability)correspond to non-empty text
doc2bowVectorList = pickle.load(open(prefix+"/TopicModeling/docTopicList_LDA15_US.p","rb"))
print(len(doc2bowVectorList),len(utcList))
print(doc2bowVectorList[0])
##load submission texts that are non-empty
#textNonEmpty = pickle.load(open("../TopicModeling/Texts_nonEmpty_US.p","rb"))

#find the common topic:utc for post dictionary
commonTopic_UTC = {} #commonTopic:list of utc
for i in range(len(doc2bowVectorList)):
	#check each topic by probability
	for t in doc2bowVectorList[i]:
		if t[1]>threshold and (t[0] in topicIDmap.keys()):#this document can be count as that topic
			if topicIDmap[t[0]] in commonTopic_UTC.keys():
				commonTopic_UTC[topicIDmap[t[0]]].append(utcList[i])
			else:
				commonTopic_UTC[topicIDmap[t[0]]] = []
				commonTopic_UTC[topicIDmap[t[0]]].append(utcList[i])

print(commonTopic_UTC)

#save document UTC stamp for common Topic
pickle.dump(commonTopic_UTC,open('CAN15_commonTopic_UTC.p','wb'))#('CAN15_commonTopic_UTC_july2oct.p','wb'))
