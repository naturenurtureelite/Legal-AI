import string
import sys
import os
#variable initialization
import spacy

from stellargraph.data import BiasedRandomWalk
from stellargraph import StellarGraph

avg=0
nlp = spacy.load("en_core_web_sm")
avg_length=[1700, 1822, 1230, 1190, 1771, 1470, 1423, 3565, 1817, 1666, 1903, 1960, 2884, 1477, 1984, 1964, 2180, 1401, 4610, 1742, 2155, 1298, 1734, 1856, 1300, 1164, 1406, 1487, 1151, 5392, 1270, 1258, 1419, 1254, 1176, 1518, 1332, 2011, 1950, 1430, 1697, 979, 2130, 1568, 2224, 1439, 2322, 1608, 1498, 1030]

#avg_length=[1588,1034,1490,5705,1594,1669,1182,1631,2157,2179,2578,1906,1592,1172,1988,1731,1726,1678,1761,2246,1562,1814,1534,2044,1701,1350,3278,1413,1840,2428,1238,1399,1508,2030,934,1339,1792,2200,1389,1967,2766,2090,1492,2392,1425,1676,1420,1396,1566,1783]
for i in range(0,len(avg_length)):
	avg=avg+avg_length[i]
print(avg/50.0)
# Python program to print connected
# components in an undirected graph
 
 
class Graph:
 
    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
 
    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp
 
    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
 
    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
    def finddegree(self,v):
    	return len(self.adj[v])
    	
 
uu=0
v4=[]
v5=[]
v6=[]
v7=[]
count=0
countf=0
counta=0
countr=0
countp=0
countr1=0
countr2=0
counti=0
counts=0
first=0
last=0
first1=0
last1=0
k1=0.0
k2=0.0
k3=0.0
k4=0.0
k5=0.0
k6=0.0
k7=0.0
k8=0.0
first1=0.0
last1=0.0
first2=0.0
last2=0.0
total_length=0.0
import networkx as nx
#list of all possible summarization algorithms
#a=["ChineseGist"]
if sys.argv[1]=="unsupervised_domain_independent":
	a=["LexRankSummarizer","LuhnSummarizer","LsaSummarizer","ReductionSummarizer","DSDR"]
elif sys.argv[1]=="unsupervised_domain_specific":
	a=["LetSum","KMM","CaseSummarizer","MMR","DELSumm"]
elif sys.argv[1]=="supervised":
	a=["SummaRuNNer/AttnRNN_F7_avr","SummaRuNNer/RNN_RNN_F7_avr","SummaRuNNer/CNN_RNN_F7_avr","ChineseGist","BERT"]
elif sys.argv[1]=="unsupervised":
	a=["LexRankSummarizer","LuhnSummarizer","LsaSummarizer","ReductionSummarizer","DSDR","LetSum","KMM","CaseSummarizer","MMR","DELSumm"]
elif sys.argv[1]=="all_methods":
	a=["BERT","CaseSummarizer","ChineseGist","DELSumm","DSDR","KMM","LetSum","LexRankSummarizer","LsaSummarizer","LuhnSummarizer","MMR","ReductionSummarizer","SummaRuNNer/AttnRNN_F7_avr","SummaRuNNer/RNN_RNN_F7_avr","SummaRuNNer/CNN_RNN_F7_avr"]
elif sys.argv[1]=="top_4":
	a=["SummaRuNNer/RNN_RNN_F7_avr","SummaRuNNer/AttnRNN_F7_avr","BERT","DELSumm"]

#a=["BERT","SummaRuNNer/AttnRNN_F7_avr","DELSumm","SummaRuNNer/RNN_RNN_F7_avr"]
#a=["DELSumm","MMR","CaseSummarizer","LetSum","KMM"]
#a=["DELSumm","MMR","CaseSummarizer","LetSum","KMM","LexRankSummarizer","LuhnSummarizer","LsaSummarizer","ReductionSummarizer","DSDR"]
#a=["SummaRuNNer/AttnRNN_F7_avr","SummaRuNNer/RNN_RNN_F7_avr","BERT","DELSumm"]
#a=["LexRankSummarizer","LuhnSummarizer","LsaSummarizer","ReductionSummarizer","DSDR"]
#rouge_score=[0.5355,0.5473,0.5397,0.53745,0.5712]
#a=["BERT","CaseSummarizer","ChineseGist","DELSumm","DSDR","KMM","LetSum","LexRankSummarizer","LsaSummarizer","LuhnSummarizer","MMR","ReductionSummarizer","SummaRuNNer/AttnRNN_F7_avr","SummaRuNNer/RNN_RNN_F7_avr","SummaRuNNer/CNN_RNN_F7_avr"]
#a=["SummaRuNNer/AttnRNN_F7_avr","SummaRuNNer/RNN_RNN_F7_avr","SummaRuNNer/CNN_RNN_F7_avr","BERT","ChineseGist"]
t=os.listdir("Full-Text-segments/India/")
print(t)
#loop over all summarization algorithms
def sortSecond(val):
    return val[1] 
def cosinesimilarity(l1,l2):
	c=0.0
	d=0.0
	e=0.0
	cosine=0.0
	for i in range(0,len(l1)):
		c+=l1[i]*l2[i]
	for i in range(0,len(l1)):
		d+=l1[i]**2
		e+=l2[i]**2
	cosine=c/(d*e)
	return cosine

for i in range(0,50):
	no_of_words=0
	v1=[]
	v4=[]
	v5=[]
	v7=[]
	pair=[]
		#loop over all 50 files
	file1 = open("Full-Text-segments/India/"+t[i], 'r')
	Lines = file1.readlines()
 
	#count = 0
			
			#read a line from a file in the full text segments
	for line in Lines:
		p=line.strip()
		if p[-1]==".":
			v1.append(p[:-1])
		else:
			v1.append(p)
			


			#separate a line into sentence and label
	for l in range(0,len(v1)):
		u=v1[l]
		u=u.split("-->")
		u[0]=u[0].strip()
		if u[0][-1]==".":
			v4.append(u[0][:-1])
		else:
			v4.append(u[0])
				
		v5.append(u[1])
			#v4 contains sentence
			#v5 contains label
	for x2 in range(0,len(v4)):
		a_string=v4[x2]
		alphanumeric=""
		for character in a_string:
			if character.isalnum():
				alphanumeric+=character
		v7.append(alphanumeric)
	
	
	v6=[]
	v10=[]
	for j in range(0,len(a)):

			#open a particular file and read
			file1 = open("Algo-Summaries/India/"+a[j]+'/'+t[i], 'r')
			Lines = file1.readlines()

			v=[]
			#v6=[]
			#v1=[]
			#p=""
			#count = 0

			# read a line from a summarized document where the summarized text is generated by a algorithm 
			for line in Lines:
				p=line.strip()
				if p[-1]==".":
					v.append(p[:-1])
					v10.append(p[:-1])
				else:
					v.append(p)
					v10.append(p)
			

			#read a line from a file in the full text segments		
			
			
			
			#remove the punctuation characters and only store only alphanumeric characters
			for x1 in range(0,len(v)):
				a_string=v[x1]
				alphanumeric=""
				for character in a_string:
					if character.isalnum():
						alphanumeric+=character
				v6.append(alphanumeric)

			#remove the punctuation characters and only store only alphanumeric characters
			

			#check whether the line present in the summary file is present in the first half or the second half of the text file
	count=[]
	counter=[]
	v10=sorted(list(set(v10)))
	for j in range(0,len(v10)):
		for jj in range(0,len(a)):
			counter.append(0)
		count.append(counter)
		counter=[]
	

	#print(count[0])
	v=[]
	v8=[]
	for j in range(0,len(a)):

			#open a particular file and read
			file1 = open("Algo-Summaries/India/"+a[j]+'/'+t[i], 'r')
			Lines = file1.readlines()

			v=[]
			v8=[]
			#v1=[]
			#p=""
			#count = 0

			# read a line from a summarized document where the summarized text is generated by a algorithm 
			for line in Lines:
				p=line.strip()
				if p[-1]==".":
					v.append(p[:-1])
					v8.append(p[:-1])
				else:
					v.append(p)
					v8.append(p)
			

			#read a line from a file in the full text segments		
			
			
			
			#remove the punctuation characters and only store only alphanumeric characters
			for x1 in range(0,len(v)):
				a_string=v[x1]
				alphanumeric=""
				for character in a_string:
					if character.isalnum():
						alphanumeric+=character
				#v8.append(alphanumeric)
			for x1 in range(0,len(v10)):
				for x2 in range(0,len(v8)):
					if v10[x1]==v8[x2]:
						count[x1][j]=1
			#v8=[]

	g = nx.Graph()
	g1 = nx.Graph()

	
	for j in range(0,len(count)):
		for k in range(0,len(count)):
			value=0
			if j!=k:
				for l in range(0,len(count[k])):
					if count[j][l]==1 and count[k][l]==1:
						value=value+1
			#if float(value)>=((len(a)/2)+1):
			#	g.addEdge(j, k)
			g.add_edge(j,k,weight=value)
	
	square=StellarGraph.from_networkx(g)

	from stellargraph.data import BiasedRandomWalk

	rw = BiasedRandomWalk(square)


	walks = rw.run(
    nodes=list(square.nodes()),  # root nodes
    length=100,  # maximum length of a random walk
    n=10,  # number of random walks per root node
    p=0.5,  # Defines (unormalised) probability, 1/p, of returning to source node
    q=2.0,  # Defines (unormalised) probability, 1/q, for moving away from source node
	)
	from gensim.models import Word2Vec

	str_walks = [[str(n) for n in walk] for walk in walks]
	model = Word2Vec(str_walks, window=5, min_count=0, sg=1, workers=1)
	for j in range(0,len(v10)):
		for k in range(0,len(v10)):
			if j!=k:
				stri1=str(j)
				stri2=str(k)
				emb1=list(model.wv[stri1])
				emb2=list(model.wv[stri2])
				value=cosinesimilarity(emb1,emb2)
				#print(value)
				if value>=0.0:
					g1.add_edge(j,k,weight=value)
				#print(type(emb1),type(emb2))
				#cosine=
		#stri1=str(j)
		#print(model.wv[stri])
	ll=nx.pagerank(g1)
	#print(g1)
	v_new=[]
	#file5 = open("Method1/"+str(t[i]), 'a+')
	#for j in range(0,len(ll)):
	#	v_new.append([j,ll[j]])
	#v_new.sort(key=sortSecond,reverse=True)
	#print(len(v_new),len(v10))
		
#print("Number of random walks: {}".format(len(walks)))
	v_new=[]
	file5 = open("unordered/"+str(t[i]), 'a+')
	for j in range(0,len(ll)):
		v_new.append([j,ll[j]])
	v_new.sort(key=sortSecond,reverse=True)
	print(len(v_new),len(v10))
	no_of_words=0
	for j in range(0,len(v_new)):
		parsed = nlp(v10[v_new[j][0]])
		no_of_words =no_of_words+len(parsed)
		#print(no_of_words,avg_length[i])
		if no_of_words<=avg_length[i]:
				file5.write(v10[v_new[j][0]]+"."+"\n")
		else:
				no_of_words=no_of_words-len(parsed)
	print(no_of_words,avg_length[i])

	#v_new=[]
	#for i in range(0,len()):
	'''
	tempo=""
	pos=-1
	maxi=-1.0
	#components=g.connectedComponents()
	
	connect=g.connectedComponents()
	
	
	#print(connect)
	ttt=[]
	for j in range(0,len(connect)):
		ttt.append([connect[j],len(connect[j])])
	ttt.sort(key=sortSecond,reverse=True)
	connect=[]
	for j in range(0,len(ttt)):
		connect.append(ttt[j][0])
	
	components=connect
	#print(connect)
	no_of_words=0
	ttt=[]
	file5 = open("Method1/"+str(t[i]), 'a+')
	for l in range(0,len(components)):
		for k in range(0,len(components[l])):
			parsed = nlp(v10[components[l][k]])
			
			ttt.append([v10[components[l][k]],g.finddegree(components[l][k]),len(parsed)])
			#print(g.finddegree(components[l][k]))
			#file5.write(vline[components[l][k]]+"."+"\t"+vrhetoric[components[l][k]]+"\n")
		ttt.sort(key = sortSecond,reverse=True)
		

		
		for k in range(0,len(ttt)):
			no_of_words =no_of_words+ttt[k][2]
			if no_of_words<=avg_length[i]:
				file5.write(ttt[k][0]+"."+"\n")
			else:
				no_of_words =no_of_words-ttt[k][2]

			#file5.write(pair[l][0]+"."+"\n")
			#file5.write(vline[pos]+"."+"\n")
		#else:
			#break
		#	no_of_words=no_of_words-len(parsed)

		#for k in range(0,len(ttt)):
		#	file5.write(ttt[k][0]+"."+"\n")
		ttt=[]
	print(no_of_words,avg_length[i])
		#no_of_words=0
	#for m in range(0,len(count)):
	#	print(count[m])	
'''
'''
	for m in range(0,len(count)):		
		pair.append([v4[m],count[m]])	
	pair.sort(key = sortSecond,reverse=True)
	#print(pair)
	no_of_words=0
	file5 = open("Method4/"+str(t[i]), 'a+')

	for l in range(0,len(pair)):
		pair[l][0]=pair[l][0].translate(str.maketrans('', '', string.punctuation))  # remove punctuation from a line
		parsed = nlp(pair[l][0])
		no_of_words =no_of_words+len(parsed)
		if no_of_words<=avg_length[i]:
			file5.write(pair[l][0]+"."+"\n")
		else:
			no_of_words=no_of_words-len(parsed)
			break
	total_length=total_length+no_of_words
	print(avg_length[i],no_of_words,t[i])
	print(no_of_words)
	#print(avg_length[i])
	#print(leng)
	#pair=[]
	#print(t[i])
	
	#for m in range(0,int(leng)):
		
	pair=[]
	#for i in range(0,len(pair)):
	#	print(pair[0],"---->",pair[1])
	#pair=[] 	
	#print("---------------------------")
print(total_length/50)
'''
