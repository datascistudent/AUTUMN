__author__ = 'gkannappan'

from textblob import TextBlob
#sample = "can't go wrong with turbo tax software. exactly as ordered"
sample = "another year of doing my personal taxes with this software. another tax year past"


print TextBlob(str(sample.encode('utf-8'))).sentiment.polarity