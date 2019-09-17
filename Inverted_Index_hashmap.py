# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 00:15:02 2019

@author: M.Hamza Ashraf
"""
#python "E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\IR-Assignment1\Inverted_Index_hashmap.py" "E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\corpus"
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
import sys
import os

# =============================================================================
# a=0
# b=5
# 
# =============================================================================
DocId=1
prev_DocId = 0
prev_Position = 0
TermId=1
position=0

inverteddict={}
uniquedict={}

edict = {}

new_tokens=[]
unique_list = []
final=""
stemmer = SnowballStemmer('english')
tk = RegexpTokenizer("[\w']+") 

#arg=r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\corpus"
arg=sys.argv[1]


#docf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\docids.txt","w")
#termf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\termids.txt","w",errors='ignore')
indexf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\term_index.txt","w")
StopList = [line.rstrip('\n') for line in open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\stoplist.txt").readlines()]
s=set(StopList)
files = os.listdir(arg)

for i in files:
    path = arg + "\\" + i
    p = os.path.splitext(path)
    
    if(p[1]!=".txt"):
        soup = BeautifulSoup(open(arg + "\\" + i, 'rb').read(), "html.parser", from_encoding="iso-8859-1")
        print(i)
    
        for ext in soup(["script", "style"]):
            ext.extract()
  
        if (soup.find('body')) is not None:
            rows = soup.find('body').text
            #docf.write(str(DocId)+"\t"+i+"\n")
            DocId=DocId+1

            
        else:
            rows=''
        
        final = ''.join(rows)
        final = final.encode("utf-8").decode()
        tokens = tk.tokenize(final)
        
        tokens=[tok.lower() for tok in tokens if tok.isalpha()]
        
        for w in list(tokens): 
            if w not in s: 
                new_tokens.append(w)
        
        stemmed_tokens = [stemmer.stem(x) for x in new_tokens]
                
        for j in stemmed_tokens:
            position = position + 1
            
            if j not in uniquedict.keys():
     
                uniquedict.update({j:TermId})
                #termf.write(str(TermId)+"\t"+j+"\n")
                
                inverteddict.update({TermId:[str(DocId-1) + "," + str(position)]})               
                TermId=TermId+1
                    
            else:
                key = uniquedict.get(j)
                inverteddict[key].append(str(DocId-1) + "," + str(position))

    tokens.clear()
    new_tokens.clear()
    stemmed_tokens.clear()
    position=0
    
# =============================================================================
#     a=a+1
#     if a==b:
#         break
# =============================================================================

ulist = []
tlist = []     
a=1;

curr_DocId = 0;
curr_Position = 0;
doc_occ = []

for k, v in inverteddict.items():

    prev_DocId = (inverteddict[k][0]).split(',')[0]
    prev_Position = (inverteddict[k][0]).split(',')[1]
    
    
    for x in v:
        if (x.split(',')[0]) not in ulist:
            ulist.append(x.split(',')[0])
            
        if(a == 1):
            tlist.append(str(prev_DocId) + "," + str(prev_Position))
            a = 0;
        
        else:
           curr_DocId = x.split(',')[0]
           curr_Position = x.split(',')[1]
        
           if((int(curr_DocId) - int(prev_DocId)) == 0): 
               tlist.append(str(int(curr_DocId) - int(prev_DocId)) + "," + str(int(curr_Position) - int(prev_Position)))
               
           else:
               tlist.append(str(int(curr_DocId) - int(prev_DocId)) + "," + str(curr_Position))
               prev_DocId = curr_DocId
               prev_Position = curr_Position
    doc_occ.append(len(ulist))
    ulist.clear()     
    a = 1;
    edict.update({k:tlist})
    tlist = []       

c=1
for k, v in edict.items():
    vv = ' '.join(v)
        
    indexf.write(str(k) + " ")
    indexf.write(str(len(v)) + " ")
    indexf.write(str(doc_occ[c-1]) + " ")
    
    for i in vv:
        indexf.write(i)
        
    indexf.write("\n")    
    ulist.clear()

    c=c+1
#docf.close()
#termf.close()
indexf.close()
