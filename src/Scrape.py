__author__ = 'gkannappan'

import urllib2
import pprint
from bs4 import BeautifulSoup

fw = open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_One.txt", 'a+')

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