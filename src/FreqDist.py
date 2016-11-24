__author__ = 'gkannappan'

'''
This module ll try to get the review text (imported from the pipe-delimited file) and
ll try to do frequency distribution of unigram and bigram
'''

import re
import pandas

'''
Function to remove punctuation from the text
'''
def rem_punc(text):
    return re.sub("[^a-zA-Z0-9\s]","", text)

'''
Function to create bigram list of list
'''
def bigram(sample):
    o={}
    for z in sample:
        for i in range(1, len(z)):
            g = ' '.join([z[i-1], z[i]])
            o.setdefault(g, 0)
            o[g] += 1
    return o

'''
Function to create list to list of list
'''
def list_to_list_of_list(sample):
    y0 = []
    y = []
    for line in sample:
        y0 = [(rem_punc(words).encode("utf8")) for words in line.split() if words not in stopwords_custom]
        y.append(y0)
    return y

'''
Function to convert word list to dictionary that has word frequency count as value
'''
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

stopwords_custom = ["'s", 'are', 'and', 'it', '!',  'that', 'from', 'in',  'of', 'has', 'a', 'the', 'to', 'is', 'was', 'i', 'for', 'this', 'you', 'as', 'my', 'me', 'they', 'am', 'to', 'an', 'i', 'have', 'having', 'had', 'on', 'all', 'were', 'than', 'with', 'your', 'when']

fo = (r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_DF.txt", 'r+')

ReviewText = pandas.read_csv("/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_DF2.txt", delimiter= '|', index_col=False, header=0, usecols=[3]);
rev_text = ReviewText['ReviewText'].tolist()

l = [sentence.split() for sentence in rev_text]

word_list= [rem_punc(item) for sublist in l for item in sublist]

word_list_no_stopword = [word for word in word_list if word not in stopwords_custom]

word_list_freq = wordListToFreqDict(word_list_no_stopword)

rev_text_no_stopword = list_to_list_of_list(rev_text)

word_list_freq_bigram = bigram(rev_text_no_stopword)

for key, value in sorted(word_list_freq.iteritems(), key=lambda (k,v): (v,k), reverse=True ):
    print "%s: %s" % (key, value)
#for key, value in sorted(word_list_freq_bigram.iteritems(), key=lambda (k,v): (v,k), reverse=True ):
#word_list_freq    print "%s: %s" % (key, value)
