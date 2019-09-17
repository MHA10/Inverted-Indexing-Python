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
a=0
b=3
DocId=1
TermId=1
position=0


doc_term_list = []
inverted_list = []
ulist = []

invertedtuple=()
uniquedict={}


new_tokens=[]
unique_list = []
final=""
stemmer = SnowballStemmer('english')
tk = RegexpTokenizer("[\w']+") 

arg=r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\corpus"
#arg=sys.argv[1]


#docf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\docids.txt","w")
#termf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\termids.txt","w",errors='ignore')
indexf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\term_index.txt","w")
StopList = [line.rstrip('\n') for line in open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\stoplist.txt").readlines()]
s=set(StopList)
files = os.listdir(arg)

def takeSecond(elem):
    #print (elem[1])
    return elem[0] 

for i in files:
    path = arg + "\\" + i
    p = os.path.splitext(path)
    
    if(p[1]!=".txt"):
        soup = BeautifulSoup(open(arg + "\\" + i, 'rb').read(), "html.parser", from_encoding="iso-8859-1")
        print(i)
    
        
        for ext in soup(["script", "style"]):
            ext.extract()
        
        
        if (soup.find('body')) is not None:
            if(p[1]!=".txt"):
                rows = soup.find('body').text
                #docf.write(str(DocId)+"\t"+i+"\n")
                DocId = DocId + 1
            
        else:
            rows=''
        
        final = ''.join(rows)
        final = final.encode("utf-8").decode()
        tokens = tk.tokenize(final)
        #print(tokens)
        
        tokens=[tok.lower() for tok in tokens if tok.isalpha()]
        
        
        
        for w in list(tokens): 
            if w not in s: 
                new_tokens.append(w)
        
        stemmed_tokens = [stemmer.stem(x) for x in new_tokens]
        
        
        for j in stemmed_tokens:
            position = position + 1
            
            if j not in ulist:
                ulist.append(j)
                doc_term_list.append([TermId,str(DocId-1) + "," + str(position)])
                TermId=TermId+1
                #inverted_list.append(j)
              
            else:
                key = (ulist.index(j)) + 1
                doc_term_list.append([key,str(DocId-1) + "," + str(position)])
                #inverted_list[takeSecond(j)-1].append(j[1])
            
            
    tokens.clear()
    new_tokens.clear()
    stemmed_tokens.clear()
    position=0
    
    a=a+1
    if a==b:
        break

doc_term_list.sort(key=takeSecond) 

prev = 1

for j in doc_term_list:
            if (j[0] == prev):
                     
                     inverted_list.append(j)
                     prev = prev + 1
            else:
            
                inverted_list[takeSecond(j)-1].append(j[1])   
  
 
tlist = []
a=1

for k in inverted_list:
    c=1
    for x in k:

        if(a == 1):
            indexf.write(str(x) + " ")
            indexf.write(str(len(k)-1) + " ")
            
        
        else:
            print(x)
           
            if ((str(x).split(',')[0]) not in tlist):
                tlist.append(str(x).split(',')[0])  
            
            #indexf.write(str(len(tlist)) + " ")
            indexf.write(x + " ")
       
            c = c + 1   
            
            tlist.clear()                       
        a = 0
    indexf.write("\n")             
    a=1       
    
   

indexf.close()
