# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:05:50 2019

@author: M.Hamza Ashraf
"""

#python "E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\IR-Assignment1\Part3.py" 


from nltk.stem import SnowballStemmer
import sys

arg=sys.argv[2]

termdict = {}

stemmer = SnowballStemmer('english')

termf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\termids.txt","r")

indexf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\term_index.txt","r")

stemmed_word = (stemmer.stem(arg)) + "\n"

lines = termf.readlines()

for i in lines:
    thisline = i.split("\t")
    termdict.update({thisline[1]:thisline[0]})

termid = termdict.get(stemmed_word)

lines1 = indexf.readlines()
thisline = ""

if(termid != None):
    i=1;

    for line in lines1:
        
        if(i == int(termid)):
            thisline = line.split(" ")
            break
        i = i + 1
     
    print("\nListing for term: " + arg + "\n")
    print("TERMID: " + termid + "\n")
    print("Number of documents containing term: " + thisline[2] + "\n")
    print("Term frequency in corpus: " + thisline[1] + "\n")

else:
    print("\nTerm not found\n")

termf.close()
indexf.close()