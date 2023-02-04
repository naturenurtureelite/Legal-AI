from summ_eval.meteor_metric import MeteorMetric
rouge = MeteorMetric()
import os
import csv
from collections import defaultdict, Counter
from multiprocessing import Pool
from time import time
from rouge import Rouge
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def remove_stopwords(sent):
    word_tokens = word_tokenize(sent)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    filtered_sentence.append(' ')
    return " ".join(filtered_sentence)

def getRouge(hyp, ref):
    ROUGE = Rouge()
    #hyp = preprocess(hyp)
    #ref = preprocess(ref)

    if len(hyp) == 0 or len(ref) == 0: return {}

    return ROUGE.get_scores(hyp, ref, avg = True)

def dict_sum(cnt, d):
        for key, val in d.items():
                cnt[key].update(val)
import os

#summaries = ["This is one summary", "This is another summary"]
#references = ["This is one reference", "This is another"]
diri=os.listdir(sys.argv[1]+"/")
diri_expert1=os.listdir("Expert-Summaries/India/A1_processed/")
diri_expert2=os.listdir("Expert-Summaries/India/A2_processed/")
l=[]
ll=[]
for i in range(0,len(diri)):
    fi1=open(sys.argv[1]+"/"+diri[i],"r+")
    read1=remove_stopwords(fi1.read().replace('\n', ' '))
    fi2=open("Expert-Summaries/India/A1_processed/"+diri_expert1[i],"r+")
    read2=remove_stopwords(fi2.read().replace('\n', ' '))
    read1=[read1]
    read2=[read2]
    rouge_dict = rouge.evaluate_batch(read1, read2)
    l.append(rouge_dict['meteor'])
    print(rouge_dict['meteor'])
for i in range(0,len(diri)):
    fi1=open(sys.argv[1]+"/"+diri[i],"r+")
    read1=remove_stopwords(fi1.read().replace('\n', ' '))
    fi2=open("Expert-Summaries/India/A2_processed/"+diri_expert2[i],"r+")
    read2=remove_stopwords(fi2.read().replace('\n', ' '))
    read1=[read1]
    read2=[read2]
    rouge_dict = rouge.evaluate_batch(read1, read2)
    l.append(rouge_dict['meteor'])
    print(rouge_dict['meteor'])
print("------------------------------")


for i in range(0,50):
    print((l[i]+l[50+i])/2.0)

a=0.0
print("------------------------------")
for i in range(0,100):
    a=a+l[i]

print("Meteor",(a/100.0))

