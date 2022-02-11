import json
import nltk;nltk.download('stopwords')
from nltk.corpus import stopwords

def loadJson(jsonList,prefixDir):
	data = []
	for f in jsonList:
		with open(prefixDir+f) as fp:
			data = data+json.load(fp)
	return data



def userList(data):
	userList = []
	for d in data:
		userList.append(d['author'])
		if d['comments']:
			for c in d['comments']:
				userList.append(c['data'][0]['author'])
	return list(set(userList))

#initiating posts
def textData(data):
	textList = []
	for d in data:
		outText = d['title']+' '
		if 'selftext' in d.keys():
			outText = outText+d['selftext']
		textList.append(outText)
	return textList

#submission utc
def submission_utc(data):
	utcList = []
	for d in data:
		utcList.append(d['created_utc'])
	return utcList


#utc of post and user name including comments
def utc_userList(data):
	timeList = []
	userList = []
	for d in data:
		timeList.append(d['created_utc'])
		userList.append(d['author'])
		if d['comments']:
			for c in d['comments']:
				timeList.append(c['data'][0]['created_utc'])
				userList.append(c['data'][0]['author'])
	return timeList, userList


def utc_weekly_bin():
	weekBin = [1581206400,
		1581811200,
		1582416000,
		1583020800,
		1583625600,
		1584230400,
		1584835200,
		1585440000,
		1586044800,
		1586649600,
		1587254400,	
		1587859200,
		1588464000,
		1589068800,
		1589673600,
		1590278400,
		1590883200,
		1591488000,
		1592092800,
		1592697600,
		1593302400,
		1593907200,
		1594512000,
		1595116800,
		1595721600,
		1596326400,
		1596931200,
		1597536000,
		1598140800,
		1598745600,
		1599350400,
		1599955200,
		1600560000,
		1601164800,
		1601769600,
		1602374400,
		1602979200,
		1603584000,
		1604188800,
		1604793600,
		1605398400,
		1606003200,
		1606608000
	]
	return weekBin

#weekly label monthly tick
def utc_weekly_tick():
	weekLabel = ['02-09',
		'',
		'',
		'03-01',
		'',
		'',
		'03-22',
		'',
		'',
		'04-12',
		'',
		'',
		'05-03',
		'',
		'',
		'05-24',
		'',
		'',
		'06-14',
		'',
		'',
		'07-05',
		'',
		'',
		'07-26',
		'',
		'',
		'08-16',
		'',
		'',
		'09-06',
		'',
		'',
		'09-27',
		'',
		'',
		'10-18',
		'',
		'',
		'11-08',
		'',
		'',
		'11-29'
	]
	return weekLabel

def utc_weekly_label():
	weekLabel = ['02-09',
		'02-16',
		'02-23',
		'03-01',
		'03-08',
		'03-15',
		'03-22',
		'03-29',
		'04-05',
		'04-12',
		'04-19',
		'04-26',
		'05-03',
		'05-10',
		'05-17',
		'05-24',
		'05-31',
		'06-07',
		'06-14',
		'06-21',
		'06-28',
		'07-05',
		'07-12',
		'07-19',
		'07-26',
		'08-02',
		'08-09',
		'08-16',
		'08-23',
		'08-30',
		'09-06',
		'09-13',
		'09-20',
		'09-27',
		'10-04',
		'10-11',
		'10-18',
		'10-25',
		'11-01',
		'11-08',
		'11-15',
		'11-22',
		'11-29'
	]
	return weekLabel

def numUserInBin(weekBin, userList, timeList):
	numUserInBinList = []
	for i in range(len(weekBin)-1):
		currentBinUser = set()
		for j in range(len(timeList)):
			if timeList[j]>=weekBin[i] and timeList[j]<=weekBin[i+1]:
				currentBinUser.add(userList[j])
	
		numUserInBinList.append(len(currentBinUser))
	return numUserInBinList


def stopwords(d): #d is element in data from json pulled from pushshiftio
	#stop words
	stop_words = stopwords.words('english')
	stop_words.extend(['hi','www','com','s','http','https','amp','ampersand','from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come',
#extend function words to be removed https://www.edu.uwo.ca/faculty-profiles/docs/other/webb/essential-word-list.pdf
'the','which','still','although','forty','and','up','last','past','nobody','of','out','being','himself','unless','to','would','must','seven','mine','a','when','another','eight','anybody','I','your','between','along','till','in','will','might','round','herself','you','their','both','several','twelve','that','who','five','someone','fifteen','it','some','four','whatever','beyond','for','two','around','among','whom','he','because','while','across','below','on','how','each','behind','none','we','other','under','million','nor','they','could','away','outside','more','be','our','every','nine','most','with','into','next','thousand','this','these','anything','shall','have','than','few','myself','but','any','though','themselves','as','where','since','itself','not','over','against','somebody','at','back','second','upon','what','first','nothing','thirty','so','much','without','third','there','down','during','above','or','its','six','therefore','one','should','enough','everybody','by','after','once','towards','from','those','however','thus','all','may','half','everyone','she','something','yet','near','no','three','whether','inside','his','little','everything','nineteen','do','many','until','yourself','can','why','hundred','fifty','if','before','within','whose','about','such','ten','anyone','my','off','twenty','per','her','through','either','except' ])

	return stop_words	


def commonTopic():
	"""
	return list of common Topics
	"""
	return ['Case Report',#'Case report&interaction with medical system',
'Prevention',#'prevention/Social distancing/Transmission risk/vaccine',
'COVID impact',#'Work/Finance/Education/Children/feeling',
'Policy&News'#'Policy/QA&News/Travel restriction/testing'
]

def annotateUStopic():
	"""
	return a dictionary: {LDA topic ID: annotated topic}
	"""
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
	return UStopicMap 

def annotateUKtopic():
	"""
	return a dictionary: {LDA topic ID: annotated topic}
	"""
	UKtopicMap = {
    0:'Case Report',
    1:'COVID impact',
    2:'COVID impact',
    3:'Policy&News',
    5:'Policy&News',
    6:'COVID impact',
    7:'Policy&News',
    8:'Prevention',
    9:'Case Report'}
	return UKtopicMap

def annotateAUStopic():
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
	return AUStopicMap

def annotateCANtopic():
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
	return CANtopicMap


















