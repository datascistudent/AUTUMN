__author__ = 'gkannappan'


'''
**********************************************************************************
"Supervised" classification of Amazon Customer Reviews on TurboTax Desktop Product

Broad steps:
    01. Connector to get the customer reviews from Amazon Product Page
        a. CustomerID
        b. Review Date
        c. Rating
        d. Review Title & Text
        e. Usefulness Vote (found this helpful)^
        f. Response Text^
        g. Comments^
    02. Classification of the customer review data
        a. n-grams
        b. frequency distribution
        c. auto-classification and dendogram^
        d. manual classification
    03. Sentiment Analytics on the data
    04. Visualizing results
        a.
        b.
        c.

**********************************************************************************
TurboTax Deluxe 2015 Federal + State Taxes + Fed Efile Tax Preparation Software - PC/Mac Disc
http://www.amazon.com/TurboTax-Deluxe-Federal-Preparation-Software/dp/B01617VPUY/ref=cm_cr_arp_d_product_top?ie=UTF8
2,083 customer reviews
http://www.amazon.com/TurboTax-Deluxe-Federal-Preparation-Software/product-reviews/B01617VPUY/ref=cm_cr_getr_d_paging_btm_2?ie=UTF8&showViewpoints=1&sortBy=helpful&pageNumber=2
http://www.amazon.com/TurboTax-Deluxe-Federal-Preparation-Software/product-reviews/B01617VPUY/ref=cm_cr_getr_d_paging_btm_210?ie=UTF8&showViewpoints=1&sortBy=recent&pageNumber=210
----------------------------------------------------------------------
TurboTax Deluxe 2015 Federal + State Taxes + Fed Efile Tax Preparation Software - PC Download
http://www.amazon.com/TurboTax-Deluxe-Federal-Preparation-Software/dp/B01637RFR4/ref=cm_cr_arp_d_product_top?ie=UTF8
1,641 customer reviews

####################################################################################
Sequence of .py files to be executed

Scrape.py       -   This ll scrape the URL and get the contents and dump it to a file
Clean.py        -   Clean up the file to handle extraneous/incomplete tags
Test.py         -   Remove additional unwanted tags to get the right ones for the rating
WriteToFile.py  -   Write the features to a pipe delimited file
FreqDist.py     -   Unigram and Bigram frequency distribution
Sentiment.py    -   Outputs sentiment polarity of the review text



####################################################################################
'''


import sys
import urllib2
from bs4 import BeautifulSoup
from pprint import pprint
import re
import pandas
from textblob import TextBlob
from nltk.tokenize import TabTokenizer
import nltk

#url = ['http://www.amazon.com/product-reviews/B01617VPUY']
fw = open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_One.txt", 'a+')
fr = open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc.txt", 'r')
ft = open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_Text.txt", 'w+')
fo = open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_DF.txt", 'w+')

stopwords_custom = ["'s", 'are', 'and', 'it', '!',  'that', 'from', 'in',  'of', 'has', 'a', 'the', 'to', 'is', 'was', 'i', 'for', 'this', 'you', 'as', 'my', 'me', 'they', 'am', 'to', 'an', 'i', 'have', 'having', 'had', 'on', 'all', 'were', 'than', 'with', 'your', 'when']

'''
Function to convert word list to dictionary that has word frequency count as value
'''
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    #print dict(zip(wordlist, wordfreq))
    return dict(zip(wordlist,wordfreq))

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

#The below chunk of code scrapes through *all* the pages of particular product
'''
for u in range(1,215):

    try:
        url = "http://www.amazon.com/TurboTax-Deluxe-Federal-Preparation-Software/product-reviews/B01617VPUY/ref=cm_cr_getr_d_paging_btm_{}?ie=UTF8&showViewpoints=1&sortBy=recent&pageNumber={}".format(u,u)
        url2 = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
        pprint(url)
        f = urllib2.urlopen(url2)
        #f = urllib2.urlopen('http://www.amazon.com/product-reviews/B01617VPUY')
        page=f.read().lower()#; print '%s'%(page.count('product-reviews'))
        soup = BeautifulSoup(page, "lxml")
        id1 = soup.find('div', {'class' : 'a-column a-span6 view-point-review positive-review'})
        id1.extract()
        id2 = soup.find('div', {'class' : 'a-column a-span6 view-point-review critical-review a-span-last'})
        id2.extract()
        #id3 = soup.find('i', {'class' : 'a-icon a-icon-text-separator'})
        #id3.extract()
        print  >> fw, soup.prettify().encode('utf-8')
    except AttributeError:
        break
    #print soup.prettify()
    #pprint(soup)
    #page=f.read().lower(); print '%s'%(page.count('member-review'))
    #pprint(soup.find_all('a')) # find all a tag
    #print '+'*40
    ####spans = soup.find_all('span', {'class' : 'a-size-base review-text'})
    ####print(spans)
    #print soup.select(".review-date") #Review Date but this brings in Extra Two (top Positive & Critical)
    ####rev_date = soup.select(".review-date")
    ####pprint(rev_date)
    ####print '*'*50
    #print rev_date[0].string
    ####pprint([s.string.replace('on ', '') for s in rev_date])
print '-'*40
'''

#This step would read the file and remove certain lines to make the input file look like one big html instead of
#multiple pages stiched together
'''
rem_words = ['</html>', '<!DOCTYPE html>', '<html class="a-no-js" data-19ax5a9jf="dingo">']

with open('/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_One.txt') as oldfile, open('/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_Ref.txt', 'a+') as newfile:
    print >> newfile, '<!DOCTYPE html>'
    print >> newfile, '<html class="a-no-js" data-19ax5a9jf="dingo">'
    for line in oldfile:
        if not any(rem_word in line for rem_word in rem_words):
            newfile.write(line)
    print >> newfile, '</html>'
'''

soup = BeautifulSoup(open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_new.txt", 'r+'))
#rev_id = soup.find_all('div', {'class' : 'a-section review'})
#print len(rev_id)
#print rev_id[0]
#print rev_id[9]
#print rev_id[99]
#print rev_id[999]
#print '*'*50

rev_date = [element.get_text() for element in soup.select(".review-date")]
rev_date = map(lambda s: s.strip(), rev_date)

#rev_date = soup.select(".review-date")
#print len(rev_date)
#print rev_date[0]
#print rev_date[9]
#print rev_date[99]
#print rev_date[999]
#print '*'*50

#a class="a-link-normal" href="/gp/customer-

#rev_rate = soup.find_all('a', {'class' : "a-link-normal"})
rev_rate = [element.get_text() for element in soup.find_all('span', {'class' : "a-icon-alt"})]
rev_rate = map(lambda s: s.strip(), rev_rate)
rev_rate = [x for x in rev_rate if 'stars' in x]
#print len(rev_rate)
#print rev_rate[0]
#print rev_rate[9]
#print rev_rate[99]
#print rev_rate[999]
#print '-+-+-+-+-+'*20

rev_title = [element.get_text() for element in soup.find_all('a', {'class': 'a-size-base a-link-normal review-title a-color-base a-text-bold'})]
rev_title = map(lambda s: s.strip(), rev_title)
#rev_title = soup.find_all('a', {'class': 'a-size-base a-link-normal review-title a-color-base a-text-bold'})
#print len(rev_title)
#print rev_title[0]
#print rev_title[9]
#print rev_title[99]
#print rev_title[999]
#print '*'*50

rev_text = [element.get_text() for element in soup.find_all('span', {'class' : 'a-size-base review-text'})]
rev_text = map(lambda s: s.strip(), rev_text)

#print len(rev_text)
#print rev_text[0]
#print rev_text[9]
#print rev_text[99]
#print rev_text[999]
#print '*'*50

ReviewDF = pandas.DataFrame({'ReviewDate' : rev_date, 'ReviewRating' : rev_rate, 'ReviewText':rev_text, 'ReviewTitle':rev_title})

#print ReviewDF.head(10)

print 'Number of rows {}'.format(ReviewDF['ReviewText'].shape)
print 'Number of text {}'.format(len(rev_text))


ReviewDF.to_csv(fo, sep='|', encoding='utf-8')

#tok = TextBlob(str(ReviewDF['ReviewText']))
#print type(tok)

#print type(tok.words)
#print len(tok.words)
#print tok.words

#wordListToFreqDict(rev_text)

#print [s for s in rev_text]

#print [w for s in rev_text for w in s.strip()]

#sys.exit()

l = [sentence.split() for sentence in rev_text]

word_list= [rem_punc(item) for sublist in l for item in sublist]

word_list_no_stopword = [word for word in word_list if word not in stopwords_custom]

word_list_freq = wordListToFreqDict(word_list_no_stopword)
#print rev_title

###rev_text_no_punc= [rem_punc(item) for sublist in rev_text for item in sublist]
#rev_text_no_stopword = [word for word in rev_text if word not in stopwords_custom]

rev_text_no_stopword = list_to_list_of_list(rev_text)
#print 'Rev Text No StopWord\n', rev_text_no_stopword

print 'print is done!'

#sys.exit()

#word_list_freq_bigram = []
word_list_freq_bigram = bigram(rev_text_no_stopword)
#change this to process rev_text after removal of stopwords

#for z in rev_text:
#    blob = TextBlob(z.encode("utf8"))
#    print blob.ngrams(n=3)

####word_list_no_stopword_bigram = []

####def bigram_split(words):
    #return dict([(' '.join(word), True) for word in nltk.bigrams(words.split())])
    ####return [(' '.join(word), True) for word in nltk.bigrams(words.split())]


####for line in word_list_no_stopword:
####    word_list_no_stopword_bigram.append(bigram_split(line))

####print word_list_no_stopword_bigram

#word_list_freq_bigram = wordListToFreqDict(word_list_no_stopword_bigram)

#print sortFreqDict(word_list_freq)

#print sorted(word_list_freq, key=word_list_freq.get)

#pprint(word_list_freq)

#print ReviewDF.ReviewText[0:15]

#pprint(rev_text[0:150])

#for i in range(0,len(rev_text)-1):
    #print >> ft, unicode(rev_text[i]).replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
#    print >> ft, rev_text[i].encode("utf8")

#print word_list_freq_bigram

#for key, value in sorted(word_list_freq_bigram.iteritems(), key=lambda (k,v): (v,k), reverse=True ):
#    print "%s: %s" % (key, value)

for key, value in sorted(word_list_freq_bigram.iteritems(), key=lambda (k,v): (v,k), reverse=True ):
    print >> ft, "%s: %s" % (key, value)

