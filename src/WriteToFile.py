__author__ = 'gkannappan'

from bs4 import BeautifulSoup
import pandas

fo = open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_DF2.txt", 'w+')
#soup = BeautifulSoup(open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_new.txt", 'r+'))
soup = BeautifulSoup(open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_new2.txt", 'r+'))

rev_date = [element.get_text() for element in soup.select(".review-date")]
rev_date = map(lambda s: s.strip(), rev_date)

rev_rate = [element.get_text() for element in soup.find_all('span', {'class' : "a-icon-alt"})]
rev_rate = map(lambda s: s.strip(), rev_rate)
rev_rate = [x for x in rev_rate if 'stars' in x]

rev_title = [element.get_text() for element in soup.find_all('a', {'class': 'a-size-base a-link-normal review-title a-color-base a-text-bold'})]
rev_title = map(lambda s: s.strip(), rev_title)

rev_text = [element.get_text() for element in soup.find_all('span', {'class' : 'a-size-base review-text'})]
rev_text = map(lambda s: s.strip().replace("\n", ""), rev_text)

ReviewDF = pandas.DataFrame({'ReviewDate' : rev_date, 'ReviewRating' : rev_rate, 'ReviewText':rev_text, 'ReviewTitle':rev_title})
print 'Number of rows {}'.format(ReviewDF['ReviewText'].shape)
print 'Number of text {}'.format(len(rev_text))

ReviewDF.to_csv(fo, sep='|', encoding='utf-8')