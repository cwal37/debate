# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import division
import nltk, re, pprint
from nltk import word_tokenize
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

plt.clf()
plt.close()

plt.style.use('bmh')

path = 'data_nospaces.txt'
raw = open(path, 'rU').read()

tokens = nltk.wordpunct_tokenize(raw)

words = [w.lower() for w in tokens]
words = [word for word in words if word not in stopwords.words('english')]
vocab = sorted(set(words))

z= Counter(words)
keys = z.keys()
values = z.values()

df = pd.DataFrame(keys)
df['values'] = values
df.columns = ['word', 'count']

df.sort('count', ascending=False)
problems = ['$', '...', '-', '"', ':', '?', '.', "'", '--', '(', ')', 've', ',', 'll', 're', 'm', 'mr', 'applause']

for val in problems:
    df = df[df['word'] != val]
    
df.to_csv('slightly_clean_yo.csv')


df_15 = df[df['count'] > 15]
df2 = df[df['count'] > 25]

names = ['carson', 'bush', 'trump', 'rubio', 'wallace',  'hillary','huckabee', 
'christie', 'kasich', 'cruz','megyn', 'baier','obama', 'kelly', 'clinton',  
'walker', 'paul']
name_count = []
for name in names:
    count_row = df_15[df_15['word'] == name]
    count  = count_row.iloc[0]['count']
    name_count.append(count)
    

df_names = pd.DataFrame(names)

df_names['c'] = name_count

df_names.columns = ['name', 'count']
    




ind =  range(len(name_count))
#print xlabels
plt.bar(ind, name_count)
plt.title('Names Mentioned at least 15 times')
plt.xticks(ind, names, rotation = 45)
plt.savefig('names.png', dpi=400)
plt.clf()
plt.close()



counts = list(df2['count'])
xlabels = list(df2['word'])
#plt.xlim(0,122)

ind =  range(len(counts))
#print xlabels
plt.figure(figsize=(20,10))
plt.bar(ind, counts)
plt.title('Words Used at Least 25 Times')
plt.xticks(ind, xlabels, rotation = 45)
plt.savefig('words_25.png', dpi=400)
plt.clf()
plt.close()