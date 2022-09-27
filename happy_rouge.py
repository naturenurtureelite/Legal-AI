from rouge_metric import RougeMetric
rouge = RougeMetric()
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:23:38 2021

@author: Paheli
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:56:20 2020

@author: Paheli
"""
import os
from tqdm import tqdm
import json
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
diri=os.listdir("/home/aniket/Aniket-India/vecsim_greedylength_allmethods")
diri_expert1=os.listdir("/home/aniket/Aniket-India/Expert-Summaries/India/A1_processed/")
diri_expert2=os.listdir("/home/aniket/Aniket-India/Expert-Summaries/India/A2_processed/")
l_p=[]
l_r=[]
l_f1=[]
ll_p=[]
ll_r=[]
ll_f1=[]
for i in range(0,len(diri)):
    fi1=open("/home/aniket/Aniket-India/vecsim_greedylength_allmethods/"+diri[i],"r+")
    read1=remove_stopwords(fi1.read().replace('\n', ' '))
    print(read1)
    fi2=open("/home/aniket/Aniket-India/Expert-Summaries/India/A1_processed/"+diri_expert1[i],"r+")
    read2=remove_stopwords(fi2.read().replace('\n', ' '))
    read1=[read1]
    read2=[read2]
    rouge_dict = rouge.evaluate_batch(read1, read2)
    #print(rouge_dict)
    l_p.append(rouge_dict["rouge"]["rouge_2_precision"])
    l_r.append(rouge_dict["rouge"]['rouge_2_recall'])
    l_f1.append(rouge_dict["rouge"]['rouge_2_f_score'])
    ll_p.append(rouge_dict["rouge"]["rouge_l_precision"])
    ll_r.append(rouge_dict["rouge"]['rouge_l_recall'])
    ll_f1.append(rouge_dict["rouge"]['rouge_l_f_score'])
    print(rouge_dict["rouge"])
for i in range(0,len(diri)):
    fi1=open("/home/aniket/Aniket-India/vecsim_greedylength_allmethods/"+diri[i],"r+")
    read1=remove_stopwords(fi1.read().replace('\n', ' '))
    fi2=open("/home/aniket/Aniket-India/Expert-Summaries/India/A2_processed/"+diri_expert2[i],"r+")
    read2=remove_stopwords(fi2.read().replace('\n', ' '))
    read1=[read1]
    read2=[read2]
    rouge_dict = rouge.evaluate_batch(read1, read2)
    #ll=ll+rouge_dict['meteor']
    l_p.append(rouge_dict["rouge"]["rouge_2_precision"])
    l_r.append(rouge_dict["rouge"]['rouge_2_recall'])
    l_f1.append(rouge_dict["rouge"]['rouge_2_f_score'])
    ll_p.append(rouge_dict["rouge"]["rouge_l_precision"])
    ll_r.append(rouge_dict["rouge"]['rouge_l_recall'])
    ll_f1.append(rouge_dict["rouge"]['rouge_l_f_score'])
    #print(rouge_dict["rouge"]['rouge_2_precision'])
    print(rouge_dict["rouge"]['rouge_l_precision'])
print("------------------------------------------")
#print("Rouge-2 precision"+str((l_p)/100.0))
#print("Rouge-2 recall"+str((l_r)/100.0))
#print("Rouge-2 f1 score"+str((l_f1)/100.0))
#print("Rouge-l precision"+str((ll_p)/100.0))
#print("Rouge-l recall"+str((ll_r)/100.0))
#print("Rouge-l f1 score"+str((ll_f1)/100.0)):
print("------------------------------------------")
for i in range(0,50):
    print((l_p[i]+l_p[50+i])/2.0)
print("------------------------------------------")

for i in range(0,50):
    print((l_r[i]+l_r[50+i])/2.0)
print("------------------------------------------")

for i in range(0,50):
    print((l_f1[i]+l_f1[50+i])/2.0)
print("------------------------------------------")

for i in range(0,50):
    print((ll_p[i]+ll_p[50+i])/2.0)
print("------------------------------------------")

for i in range(0,50):
    print((ll_r[i]+ll_r[50+i])/2.0)
print("------------------------------------------")

for i in range(0,50):
    print((ll_f1[i]+ll_f1[50+i])/2.0)
print("------------------------------------------")
a=0.0
b=0.0
c=0.0
d=0.0
e=0.0
f=0.0
#print("Rouge-2 precision"+str((l_p)/100.0))
#print("Rouge-2 recall"+str((l_r)/100.0))
#print("Rouge-2 f1 score"+str((l_f1)/100.0))
#print("Rouge-l precision"+str((ll_p)/100.0))
#print("Rouge-l recall"+str((ll_r)/100.0))
#print("Rouge-l f1 score"+str((ll_f1)/100.0))
for i in range(0,100):
    a=a+l_p[i]
print("------------------------------------------")

for i in range(0,100):
    b=b+l_r[i]
print("------------------------------------------")

for i in range(0,100):
    c=c+l_f1[i]
print("------------------------------------------")

for i in range(0,100):
    d=d+ll_p[i]
print("------------------------------------------")

for i in range(0,100):
    e=e+ll_r[i]
print("------------------------------------------")

for i in range(0,100):
    f=f+ll_f1[i]
print("------------------------------------------")
print("Rouge-2 precision"+str((a)/100.0))
print("Rouge-2 recall"+str((b)/100.0))
print("Rouge-2 f1 score"+str((c)/100.0))
print("Rouge-l precision"+str((d)/100.0))
print("Rouge-l recall"+str((e)/100.0))
print("Rouge-l f1 score"+str((f)/100.0))

