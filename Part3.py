# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:05:50 2019

@author: M.Hamza Ashraf
"""

#python "E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\IR-Assignment1\Part3.py" 


from nltk.stem import SnowballStemmer
import sys

#arg=sys.argv[2]
arg = "chocolate"

termdict = {}

stemmer = SnowballStemmer('english')

termf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\termids.txt","r")

indexf = open(r"E:\FAST\7th_Semester\Information Retrieval\Assgnments\Assgnment_1\term_index.txt","r")

stemmed_word = (stemmer.stem(arg)) + "\n"
print(stemmed_word)

lines = termf.readlines()

for i in lines:
    thisline = i.split("\t")
    termdict.update({thisline[1]:thisline[0]})

termid = termdict.get(stemmed_word)
print(termid)
# =============================================================================
#     if(thisline[1] == stemmed_word):
#         print("MIL GAYA OYEEEEEEE!!!")
#         print(thisline[1])
#         termid = thisline[0]
#         break
# =============================================================================
 

indexf.close()