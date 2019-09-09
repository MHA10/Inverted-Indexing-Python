# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 00:15:02 2019

@author: M.Hamza Ashraf
"""
#python Desktop\IR.py "E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\corpus"
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
import sys 
import os
a=0
b=5
c=1
c1=1
results=[]
new_tokens=[]
unique_list = []
final=""
stemmer = SnowballStemmer('english')
tk = RegexpTokenizer("[\w']+") 


arg=sys.argv[1]
#f = open(arg,'r')

docf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\docids.txt","w")
termf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\termids.txt","w",errors='ignore')
files = os.listdir(arg)

for i in files:
    soup = BeautifulSoup(open(arg + "\\" + i, 'rb').read(), "html.parser", from_encoding="iso-8859-1")
    print(i)
    
    docf.write(str(c)+"\t"+i+"\n")
    c=c+1 
    for ext in soup(["script", "style"]):
        ext.extract()
        
    #(ext.extract() for ext in soup(["script", "style"]))            
    
    
    if (soup.find('body')) is not None:
        rows = soup.find('body').text
        #results.append(rows)
        
    else:
        rows=''
    
    final = ''.join(rows)

    tokens = tk.tokenize(final)
    #print(tokens)
    
    tokens=[c.lower() for c in tokens]
    
    StopList = [line.rstrip('\n') for line in open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\stoplist.txt").readlines()]
    s=set(StopList)
    
    for w in tokens: 
        if w not in s: 
            new_tokens.append(w)
    
    stemmed_tokens = [stemmer.stem(x) for x in new_tokens]
    
    
    for j in stemmed_tokens:
        if j not in unique_list: 
                unique_list.append(j)
                termf.write(str(c1)+"\t"+j+"\n")
                c1=c1+1
   
        
      
    
    #a=a+1
    #if a==b:
    #    break
#print(rows)
   


#print(tokens)








#print(new_tokens)
#print('\n')
#print(stemmed_tokens)


docf.close()
termf.close()

#soup = BeautifulSoup(f, 'html.parser')
#soup = BeautifulSoup(open(path + "/" + name, 'rb').read(), "html.parser", from_encoding="iso-8859-1")
#soup = BeautifulSoup(f, "html.parser", from_encoding="iso-8859-1")


#for ext in soup(["script", "style"]):
#    ext.extract()

#rows = soup.find('body').text
#soup.find
#print(arg)
#os.listdir
#gettext
#lltk
#print(rows)