import pickle
import re
import random


topTextDic = pickle.load(open("topTextDic_LDA20_UK.p","rb"))



textDic = {}
for t in topTextDic.keys():
	text = topTextDic[t]#all text for this topic
	textNoURL = re.sub(r"http\S+", "", text)#remove url

	parseList = textNoURL.split('\n++++++++++\n ')#return list of posts
	for post in parseList:
		parse = post.split(' ')
		if len(parse)>10 and len(parse)<1000:#words count
			if t in textDic.keys():
				textDic[t].append(post)
			else:
				textDic[t] = []
				textDic[t].append(post)
		

for t in textDic.keys():
	postList = textDic[t]
	num = 100
	if len(postList)<num:
		num=len(postList)
	randomText = random.sample(postList,num)
	print(num)
	outText = ''
	for post in randomText:
		outText = outText+'\n++++++++++\n '+post

	f = open('UK20/'+str(t)+'_100sample.txt', 'w',encoding="utf-8")
	f.write(outText)#.encode("utf-8",'ignore').decode("utf-8",'ignore'))
	f.close()
