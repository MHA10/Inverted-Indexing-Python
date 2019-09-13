# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 00:15:02 2019

@author: M.Hamza Ashraf
"""
#python "E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\IR-Assignment1\IR.py" "E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\corpus"
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
import sys 
import os
a=0
b=5
DocId=1
TermId=1

inverteddict={}
uniquedict={}

new_tokens=[]
unique_list = []
final=""
stemmer = SnowballStemmer('english')
tk = RegexpTokenizer("[\w']+") 

arg=r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\corpus"
#arg=sys.argv[1]


docf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\docids.txt","w")
termf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\termids.txt","w",errors='ignore')
#indexf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\term_index.txt","w")
StopList = [line.rstrip('\n') for line in open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\stoplist.txt").readlines()]
s=set(StopList)
files = os.listdir(arg)

for i in files:
    soup = BeautifulSoup(open(arg + "\\" + i, 'rb').read(), "html.parser", from_encoding="iso-8859-1")
    print(i)
    
    
    for ext in soup(["script", "style"]):
        ext.extract()
    
    
    if (soup.find('body')) is not None:
        rows = soup.find('body').text
        docf.write(str(DocId)+"\t"+i+"\n")
        
        
    else:
        rows=''
    
    final = ''.join(rows)

    tokens = tk.tokenize(final)
    #print(tokens)
    
    tokens=[DocId.lower() for DocId in tokens]
    
    
    
    for w in list(tokens): 
        if w not in s: 
            new_tokens.append(w)
    
    stemmed_tokens = [stemmer.stem(x) for x in new_tokens]
    
    
    for j in stemmed_tokens:
        if j not in uniquedict.keys():
            uniquedict.update({j:TermId})
            termf.write(str(TermId)+"\t"+j+"\n")
            inverteddict.update({TermId:[DocId]})
            TermId=TermId+1
                
        else:
            #print("repeat!!")
            key = uniquedict.get(j)
            inverteddict[key].append(DocId)
            
        
    
    DocId=DocId+1  
    tokens.clear()
    new_tokens.clear()
    stemmed_tokens.clear()
    
    a=a+1
    if a==b:
        break
    
print(inverteddict)
   

docf.close()
termf.close()
