import pickle

topics = pickle.load(open("../TopicModeling/topics_LDA20_CAN.p","rb"))
docTopicList = pickle.load(open("../TopicModeling/docTopicList_LDA20_CAN.p","rb"))#each element in the list represent a document. Each element is a list of tuples (TopicID, probability)
textList = pickle.load(open("../TopicModeling/Texts_nonEmpty_CAN.p","rb"))
numTopic = 20

#from topics, generate topicID:wordList dictionary
topicDic = {} #ID:topic word list
for t in topics:
	wordList = []
	for word in t[1]:
		wordList.append(word[0])#.encode("ascii"))
	topicDic[t[0]] = wordList	


threshold = 0.13445035


docTopic = []#list of topic ID that each document deem as main topic(above threshold)
topTextDic = {}
for doc in docTopicList:
	ind = docTopicList.index(doc)
	for t in doc: # each doc is a list of (topID,proba) tuples
		if t[1]>threshold: # topic probability
			docTopic.append(t[0]) #topic ID
			#print(t[0])
			if t[0] in topTextDic.keys():
				topTextDic[t[0]] = topTextDic[t[0]]+'\n++++++++++\n '+textList[ind]
			else:
				topTextDic[t[0]] = textList[ind]
	

print('total number of doc topic:',len(docTopic))
print("total number of posts:",len(docTopicList))

	
topicID = range(numTopic)

def numDocTopic(docTopic,num):
	n=0
	for t in docTopic:
		if t==num:
			n = n+1
	return n 

for tID in topicID:
	nDoc = numDocTopic(docTopic,tID)
	ratio = nDoc/float(len(docTopicList))
	print('{0:.16f}'.format(ratio))	


pickle.dump(docTopic,open("docTopicWithThreshold_LDA20_CAN.p","wb"))
pickle.dump(topTextDic,open("topTextDic_LDA20_CAN.p","wb"))


