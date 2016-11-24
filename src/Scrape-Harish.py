__author__ = 'gkannappan'

from bs4 import BeautifulSoup
import csv
import codecs
import cStringIO
class DictUnicodeWriter(object):
    def __init__(self, f, fieldnames, encoding="utf-8"):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.DictWriter(self.queue, fieldnames, lineterminator = '\n')
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, D):
        self.writer.writerow({k:v.encode("utf-8") for k,v in D.items()})
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    def writerows(self, rows):
        for D in rows:
            self.writerow(D)
    def writeheader(self):
        self.writer.writeheader()

rev_date_header = 'Date'
rev_title_header = 'Title'
rev_rate_header = 'Rate'
rev_text_header = 'Text'
rev_vote_header = 'Votes'
csvfile = open("C:/Harish/out.csv", "w")
csvfile.truncate()
csvwriter = DictUnicodeWriter(csvfile,[rev_date_header, rev_title_header, rev_rate_header, rev_text_header, rev_vote_header])
# csvWriter = UnicodeWriter(csvfile, fieldnames=fieldnames, delimiter =' ',quotechar =',',quoting=csv.QUOTE_MINIMAL)
csvwriter.writeheader()
fullHTML = BeautifulSoup(open("C:/Harish/Process.html"),'html.parser')
for reviewList in fullHTML.find_all('div', {'id' : 'cm_cr-review_list'}):
    for review in reviewList.find_all('div', {'class' : 'review'}):
        rev_date_element = review.find('span',{'class' : 'review-date'})
        rev_date = '' if (rev_date_element is None or rev_date_element.text is None) else rev_date_element.text.strip().replace(',','')
        rev_title_element = review.find('a',{'class' : 'review-title'})
        rev_title = '' if (rev_title_element is None or rev_title_element.text is None) else rev_title_element.text.strip().replace(',','')
        rev_rate_element = review.find('i',{'class' : 'review-rating'})
        rev_rate = '' if (rev_rate_element is None) else '' if rev_rate_element.find('span') is None or rev_rate_element.find('span').text is None else rev_rate_element.find('span').text.strip().replace(',','')
        rev_text_element = review.find('span', {'class' : 'review-text'})
        rev_text =  '' if (rev_text_element is None or rev_text_element.text is None) else rev_text_element.text.strip().replace(',','')
        rev_vote_element = review.find('span', {'class' : 'review-votes'})
        rev_vote =  '' if (rev_vote_element is None or rev_vote_element.text is None) else rev_vote_element.text.strip().replace(',','')
        csvwriter.writerow({rev_date_header:rev_date, rev_title_header:rev_title, rev_rate_header:rev_rate, rev_text_header:rev_text, rev_vote_header:rev_vote})
csvfile.close()